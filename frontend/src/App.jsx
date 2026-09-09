import { useState, useRef, useEffect } from "react";
import Sidebar from "./components/Sidebar";
import Message from "./components/Message";
import WelcomeScreen from "./components/WelcomeScreen";
import InputArea from "./components/InputArea";

const API_BASE = import.meta.env.VITE_API_URL || "";

// Custom hook for mobile detection
const useIsMobile = () => {
  const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);
  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth <= 768);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);
  return isMobile;
};

export default function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [conversations, setConversations] = useState([]);
  const [currentConvId, setCurrentConvId] = useState(null);
  const [token, setToken] = useState("");

  // Sidebar state
  const isMobile = useIsMobile();
  const [sidebarOpen, setSidebarOpen] = useState(!isMobile); // Desktop'ta açık başla, mobilde kapalı

  const messagesEndRef = useRef(null);

  // Mobil değişikliğinde sidebar durumunu güncelle
  useEffect(() => {
    if (isMobile) {
      setSidebarOpen(false);
    } else {
      setSidebarOpen(true);
    }
  }, [isMobile]);

  // Headers helper
  const getHeaders = (json = false) => {
    const headers = {};
    if (json) headers["Content-Type"] = "application/json";
    if (token.trim()) headers["Authorization"] = `Bearer ${token.trim()}`;
    return headers;
  };

  const loadConversations = async () => {
    try {
      const res = await fetch(`${API_BASE}/conversations`, { headers: getHeaders() });
      if (res.ok) setConversations(await res.json());
    } catch { }
  };

  const loadConversation = async (convId) => {
    try {
      const res = await fetch(`${API_BASE}/conversations/${convId}`, { headers: getHeaders() });
      if (!res.ok) return;
      const data = await res.json();
      const msgs = [];
      data.forEach((m) => {
        msgs.push({ role: "user", content: m.prompt });
        msgs.push({ role: "ai", content: m.response });
      });
      setMessages(msgs);
      setCurrentConvId(convId);
      if (isMobile) setSidebarOpen(false);
    } catch { }
  };

  const sendMessage = async (text) => {
    const prompt = text || input.trim();
    if (!prompt || loading) return;

    setInput("");
    setMessages((prev) => [...prev, { role: "user", content: prompt }]);
    setLoading(true);

    try {
      const body = { prompt };
      if (currentConvId) body.conversation_id = currentConvId;

      const res = await fetch(`${API_BASE}/chat`, {
        method: "POST",
        headers: getHeaders(true),
        body: JSON.stringify(body),
      });

      if (!res.ok) {
        const err = await res.json();
        setMessages((prev) => [...prev, { role: "ai", content: `❌ Hata: ${err.detail || "Bir şeyler yanlış gitti"}` }]);
        return;
      }

      const data = await res.json();
      setMessages((prev) => [...prev, { role: "ai", content: data.response }]);
      setCurrentConvId(data.conversation_id);
      loadConversations();
    } catch (err) {
      setMessages((prev) => [...prev, { role: "ai", content: `❌ Bağlantı hatası: ${err.message}` }]);
    } finally {
      setLoading(false);
    }
  };

  const newChat = () => {
    setMessages([]);
    setCurrentConvId(null);
    if (isMobile) setSidebarOpen(false);
  };

  // Scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  useEffect(() => { loadConversations(); }, [token]);

  const toggleSidebar = () => setSidebarOpen(!sidebarOpen);

  return (
    <div className="app-container">
      <Sidebar
        isOpen={sidebarOpen}
        toggle={toggleSidebar}
        conversations={conversations}
        currentConvId={currentConvId}
        onLoadConversation={loadConversation}
        onNewChat={newChat}
        token={token}
        setToken={setToken}
        isMobile={isMobile}
      />

      <main className="main-area">
        <header className="chat-header">
          <div className="chat-header-left">
            <button className="menu-btn" onClick={toggleSidebar}>
              {/* İkon duruma göre değişebilir */}
              {isMobile || !sidebarOpen ? "☰" : "✖"}
            </button>
            <span style={{ fontWeight: 600, fontSize: 15 }}>AI Asistan</span>
            <span className="model-badge">OpenAI GPT-4o-mini</span>
          </div>
        </header>

        <div className="messages-container">
          {messages.length === 0 ? (
            <WelcomeScreen onSuggestionClick={sendMessage} />
          ) : (
            <>
              {messages.map((msg, i) => (
                <Message key={i} role={msg.role} content={msg.content} />
              ))}
              {loading && (
                <div className="message ai">
                  <div className="message-avatar">🤖</div>
                  <div className="message-bubble">
                    <div className="typing-dots"><span></span><span></span><span></span></div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </>
          )}
        </div>

        <InputArea
          input={input}
          setInput={setInput}
          onSend={() => sendMessage()}
          loading={loading}
        />
      </main>
    </div>
  );
}

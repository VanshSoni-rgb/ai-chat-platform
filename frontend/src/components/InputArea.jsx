import React, { useRef, useEffect } from 'react';

export default function InputArea({ input, setInput, onSend, loading }) {
    const textareaRef = useRef(null);

    const handleKeyDown = (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            onSend();
        }
    };

    useEffect(() => {
        if (textareaRef.current) {
            textareaRef.current.style.height = "auto";
            textareaRef.current.style.height = Math.min(textareaRef.current.scrollHeight, 120) + "px";
        }
    }, [input]);

    return (
        <div className="input-area">
            <div className="input-wrapper">
                <textarea
                    ref={textareaRef}
                    rows="1"
                    placeholder="Mesajınızı yazın..."
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={handleKeyDown}
                    disabled={loading}
                />
                <button
                    className="send-btn"
                    disabled={!input.trim() || loading}
                    onClick={() => onSend()}
                >
                    {loading ? "⏳" : "➤"}
                </button>
            </div>
            <div className="input-hint">Enter ile gönder · Shift+Enter ile satır atla</div>
        </div>
    );
}

import React from 'react';
import ReactMarkdown from 'react-markdown';

export default function Message({ role, content }) {
    const isUser = role === 'user';

    return (
        <div className={`message ${isUser ? 'user' : 'ai'}`}>
            <div className="message-avatar">
                {isUser ? "👤" : "🤖"}
            </div>
            <div className="message-bubble">
                {isUser ? (
                    content
                ) : (
                    <ReactMarkdown>{content}</ReactMarkdown>
                )}
            </div>
        </div>
    );
}

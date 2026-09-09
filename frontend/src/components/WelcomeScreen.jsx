import React from 'react';

export default function WelcomeScreen({ onSuggestionClick }) {
    return (
        <div className="welcome">
            <div className="welcome-icon">🤖</div>
            <h2>Merhaba!</h2>
            <p>Ben FastAPI ile çalışan AI asistanınım. Size nasıl yardımcı olabilirim?</p>
            <div className="suggestions">
                <button className="suggestion-btn" onClick={() => onSuggestionClick("Python ile neler yapabilirim?")}>
                    💡 Python ile neler yapabilirim?
                </button>
                <button className="suggestion-btn" onClick={() => onSuggestionClick("FastAPI nedir ve neden kullanılır?")}>
                    🚀 FastAPI nedir?
                </button>
                <button className="suggestion-btn" onClick={() => onSuggestionClick("Bana bir günlük motivasyon ver")}>
                    ✨ Günlük motivasyon
                </button>
            </div>
        </div>
    );
}

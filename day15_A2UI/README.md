## day15

Today I learned that chat-only interfaces are limited when collecting structured data or showing complex choices.
I learned about A2UI, which lets agents send structured JSON streams instead of plain text. The client listens and renders native UI components like buttons and forms.

Key points:

UI definition is separate from rendering.
It works across frameworks (React, Angular, Flutter, Android).
It is transport agnostic (HTTP, WebSockets, etc.).
It is secure (no remote code execution).
It is still early stage (v0.8, public preview).

git clone https://github.com/google/a2ui.git
cd a2ui
export GEMINI_API_KEY="your_gemini_api_key_here"
cd samples/client/lit
npm install
npm run demo:all

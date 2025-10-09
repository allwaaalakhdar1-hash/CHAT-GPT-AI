style
  #chat-toggle-btn {
    position fixed;
    bottom 20px;
    right 20px;
    background-color #0073aa;
    color white;
    border none;
    padding 12px 16px;
    border-radius 50%;
    cursor pointer;
    font-size 20px;
    z-index 10000;
    box-shadow 0 4px 10px rgba(0,0,0,0.3);
  }

  #chat-widget {
    position fixed;
    bottom 80px;
    right 20px;
    width 320px;
    display none;
    background-color #f9f9f9;
    border-radius 16px;
    box-shadow 0 4px 16px rgba(0, 0, 0, 0.2);
    font-family 'Segoe UI', sans-serif;
    overflow hidden;
    z-index 9999;
  }

  #chat-header {
    background-color #0073aa;
    color white;
    padding 10px;
    font-weight bold;
    text-align center;
  }

  #chat-messages {
    height 240px;
    overflow-y auto;
    padding 10px;
    background white;
  }

  #chat-input-area {
    display flex;
    border-top 1px solid #ddd;
    background #f0f0f0;
  }

  #user-input {
    flex 1;
    border none;
    padding 10px;
    font-size 14px;
    outline none;
  }

  .quick-replies {
    display flex;
    flex-wrap wrap;
    gap 5px;
    padding 10px;
    background #fff;
  }

  .quick-reply {
    background #0073aa;
    color white;
    padding 6px 10px;
    border-radius 12px;
    cursor pointer;
    font-size 13px;
  }

  .message {
    margin-bottom 8px;
  }

  .user {
    color #333;
  }

  .bot {
    color #0073aa;
  }
style

button id=chat-toggle-btn💬button

div id=chat-widget
  div id=chat-headerمساعد المتجرdiv
  div id=chat-messagesdiv
  div class=quick-replies
    div class=quick-reply🔍 ابحث عن منتجdiv
    div class=quick-reply🆕 ما الجديد؟div
    div class=quick-reply💰 أرني العروضdiv
  div
  div id=chat-input-area
    input type=text id=user-input placeholder=اكتب سؤالك هنا... 
  div
div

script
  const endpoint = httpsYOUR-RENDER-URL.onrender.comchat;  استبدله برابط API الخاص بك

  const toggleBtn = document.getElementById(chat-toggle-btn);
  const chatBox = document.getElementById(chat-widget);
  const input = document.getElementById(user-input);
  const messages = document.getElementById(chat-messages);

  toggleBtn.addEventListener(click, () = {
    chatBox.style.display = chatBox.style.display === none  block  none;
  });

  function sendMessage(msg) {
    if (!msg) return;
    addMessage(🧑‍💼, msg, user);
    saveMessage(🧑‍💼, msg, user);

    fetch(endpoint, {
      method POST,
      headers { Content-Type applicationjson },
      body JSON.stringify({ message msg })
    })
    .then(res = res.json())
    .then(data = {
      addMessage(🤖, data.reply, bot);
      saveMessage(🤖, data.reply, bot);
    })
    .catch(() = {
      addMessage(⚠️, تعذر الاتصال بالخادم., bot);
    });
  }

  function addMessage(sender, text, cls) {
    const div = document.createElement(div);
    div.className = `message ${cls}`;
    div.textContent = `${sender} ${text}`;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function saveMessage(sender, text, cls) {
    const chatLog = JSON.parse(localStorage.getItem(chatLog)  []);
    chatLog.push({ sender, text, cls });
    localStorage.setItem(chatLog, JSON.stringify(chatLog));
  }

  function restoreChat() {
    const chatLog = JSON.parse(localStorage.getItem(chatLog)  []);
    chatLog.forEach(msg = addMessage(msg.sender, msg.text, msg.cls));
  }

  input.addEventListener(keypress, function (e) {
    if (e.key === Enter) {
      const msg = input.value.trim();
      input.value = ;
      sendMessage(msg);
    }
  });

  document.querySelectorAll(.quick-reply).forEach(btn = {
    btn.addEventListener(click, () = {
      const msg = btn.textContent;
      sendMessage(msg);
    });
  });

  restoreChat();
script

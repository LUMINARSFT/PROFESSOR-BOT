class script(object):  
    START_TXT = """<b>✨ ආයුබෝවන් {user}.

මම සිංහල මූවී බොට් කෙනෙක්.
මගෙ නම​ {bot}.

මට පුලුවන් ඔයා ඉල්ලන සිංහල හඩකැවූ මූවීස් දෙන්න​</b>

මූවීස් ඉල්ලන්න නම් මේ 👉 https://t.me/sinhalamoviesearch group එකට join වෙන්න​"""
    
    HELP_TXT = "Settings and Actions"

    ABOUT_TXT = """<b>✯ Mʏ ɴᴀᴍᴇ: {}
✯ Redesigned: <a herf=https://t.me/sinhalafilmsgo>InFine Devs</a>
✯ Cᴏᴅᴇᴅ Oɴ: ᴩʏᴛʜᴏɴ/ᴩʏʀᴏɢʀᴀᴍ 🐍
✯ Mʏ DᴀᴛᴀBᴀꜱᴇ: ᴍᴏɴɢᴏ-ᴅʙ ☘️
✯ Mʏ Sᴇʀᴠᴇʀ: At home 😜
✯ Mʏ Vᴇʀꜱɪᴏɴ: SLMN M BOT Revision 1.0</b>"""
   
    SOURCE_TXT = """<b>NOTE:</b>
- Main Group ◉› :<a href=https://t.me/sinhalafilmsgo>SLMN MBot</a>

<b>Redesigned: <a herf=https://t.me/sinhalafilmsgo>InFine Devs</a></b>"""

    FILE_TXT = """<b>Disabled By Admins</b>"""
  
    FILTER_TXT = "Warning : Dont touch this​...✨"
    
    GLOBALFILTER_TXT = """<b>Disabled By Admins</b>"""

    MANUELFILTER_TXT = """<b>Disabled By Admins</b>"""

    BUTTON_TXT = """<b>Disabled By Admins</b>"""

    AUTOFILTER_TXT = """<b>Disabled By Admins</b>"""

    CONNECTION_TXT = """<b>Disabled By Admins</b>"""

    ADMIN_TXT = """<b>Hᴇʟᴩ Fᴏʀ Aᴅᴍɪɴꜱ</b>
    
<i>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ</b>
• /logs - Tᴏ Gᴇᴛ Tʜᴇ Rᴇᴄᴇɴᴛ Eʀʀᴏʀꜱ
• /delete - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪꜰɪᴄ Fɪʟᴇ Fʀᴏᴍ DB
• /deleteall - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Fɪʟᴇs Fʀᴏᴍ DB
• /users - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Uꜱᴇʀꜱ Aɴᴅ Iᴅꜱ
• /chats - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Cʜᴀᴛꜱ Aɴᴅ Iᴅꜱ
• /channel - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟꜱ
• /broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀꜱᴛ A Mᴇꜱꜱᴀɢᴇ Tᴏ Aʟʟ Uꜱᴇʀꜱ
• /group_broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs
• /leave  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ
• /disable  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Dɪꜱᴀʙʟᴇ A Cʜᴀᴛ
• /invite - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Gᴇᴛ Tʜᴇ Iɴᴠɪᴛᴇ Lɪɴᴋ Oғ Aɴʏ Cʜᴀᴛ Wʜᴇʀᴇ Tʜᴇ Bᴏᴛ Is Aᴅᴍɪɴ
• /ban_user  - Wɪᴛʜ Iᴅ Tᴏ Bᴀɴ A Uꜱᴇʀ
• /unban_user  - Wɪᴛʜ Iᴅ Tᴏ Uɴʙᴀɴ A Uꜱᴇʀ
• /restart - Tᴏ Rᴇsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
• /clear_junk - Cʟᴇᴀʀ Aʟʟ Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ & Bʟᴏᴄᴋᴇᴅ Aᴄᴄᴏᴜɴᴛ Iɴ Dᴀᴛᴀʙᴀsᴇ
• /clear_junk_group - Cʟᴇᴀʀ Aᴅᴅ Rᴇᴍᴏᴠᴇᴅ Gʀᴏᴜᴘ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Gʀᴏᴜᴘs Oɴ Dʙ"""


    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>  
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
◉ ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
◉ ꜰᴇᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {a}
◉ ɢ-ɪᴅ: <code>{b}</code>
◉ ʟɪɴᴋ: @{c}
◉ ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
◉ ᴀᴅᴅᴇᴅ ʙʏ: {e}

◉ ʙʏ: @{f}</b>"""
  
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{}

◉ ʙʏ: @{}</b>"""
  
    GROUPMANAGER_TXT = """<b>Hᴇʟᴩ Fᴏʀ GʀᴏᴜᴩMᴀɴᴀɢᴇʀ</b>

<i>Tʜɪꜱ Iꜱ Hᴇʟᴩ Oꜰ Yᴏᴜʀ Gʀᴏᴜᴩ Mᴀɴᴀɢɪɴɢ. Tʜɪꜱ Wɪʟʟ Wᴏʀᴋ Oɴʟʏ Fᴏʀ Gʀᴏᴜᴩ aᴅᴍɪɴꜱ</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
• /inkick - Cᴏᴍᴍᴀɴᴅ Wɪᴛʜ Rᴇǫᴜɪʀᴇᴅ Aʀɢᴜᴍᴇɴᴛs Aɴᴅ I Wɪʟʟ Kɪᴄᴋ Mᴇᴍʙᴇʀs Fʀᴏᴍ Gʀᴏᴜᴘ.
• /instatus - Tᴏ Cʜᴇᴄᴋ Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs Oғ Cʜᴀᴛ Mᴇᴍʙᴇʀ Fʀᴏᴍ Gʀᴏᴜᴘ.
• /dkick - Tᴏ Kɪᴄᴋ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛs
• /ban - To Bᴀɴ A Uꜱᴇʀ Fᴏʀᴍ Tʜᴇ Gʀᴏᴜᴩ
• /unban - Uɴʙᴀɴ Tʜᴇ Bᴀɴɴᴇᴅ Uꜱᴇʀ
• /tban - Tᴇᴍᴩᴏʀᴀʀʏ Bᴀɴ A Uꜱᴇʀ
• /mute - To Mᴜᴛᴇ A Uꜱᴇʀ
• /unmute - To Uɴᴍᴜᴛᴇ Tʜᴇ Mᴜᴛᴇᴅ Uꜱᴇʀ
• /tmute - Wɪᴛʜ Vᴀʟᴜᴇ To Mᴜᴛᴇ Uᴩ To Pᴀʀᴛɪᴄᴜʟᴀʀ Tɪᴍᴇ Eɢ: <code>/tmute 2h</code> To Mᴜᴛᴇ 2Hᴏᴜʀ Vᴀʟᴜᴇꜱ Iꜱ (m/h/d)
• /pin - Tᴏ Pɪɴ A Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ
• /unpin - Tᴏ Uɴᴩɪɴ Tʜᴇ Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ
• /purge - Dᴇʟᴇᴛᴇ Aʟʟ Mᴇssᴀɢᴇs Fʀᴏᴍ Tʜᴇ Rᴇᴘʟɪᴇᴅ Tᴏ Mᴇssᴀɢᴇ, Tᴏ Tʜᴇ Cᴜʀʀᴇɴᴛ Mᴇssᴀɢᴇ """

    EXTRAMOD_TXT = """<b>Disabled By Admins</b>"""    
    
    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"
      
    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**"
      
    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"
      
    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"
      
    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"
      
    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"
      
    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"
   
    SERVER_STATS = """Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
Uᴩᴛɪᴍᴇ: {}
CPU Uꜱᴀɢᴇ: {}%
RAM Uꜱᴀɢᴇ: {}%
Tᴏᴛᴀʟ Dɪꜱᴋ: {}
Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
Fʀᴇᴇ Dɪꜱᴋ: {}"""
    
    BUTTON_LOCK_TEXT = "Hᴇʏ {query}\nTʜɪꜱ Iꜱ Nᴏᴛ Fᴏʀ Yᴏᴜ. Sᴇᴀʀᴄʜ Yᴏᴜʀ Sᴇʟꜰ"
   
    FORCE_SUB_TEXT = "Sᴏʀʀʏ Bʀᴏ Yᴏᴜʀ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Sᴏ Pʟᴇᴀsᴇ Cʟɪᴄᴋ Jᴏɪɴ Bᴜᴛᴛᴏɴ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Aɴᴅ Tʀʏ Aɢᴀɪɴ"
   
    WELCOM_TEXT = """Hᴇʏ {user} 💞

සාදරයෙන් පිළිගන්නවා {chat} group එකට​."""
  
    IMDB_TEMPLATE = """<b>ඔබගේ ඉල්ලීමට අදාළ පිළිතුර​ 👇 </b>"""

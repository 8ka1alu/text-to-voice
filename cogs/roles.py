from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import random
import datetime

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class roles(commands.Cog):
    # rolesクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    # メインとなるroleコマンド
    @commands.group(aliases=['rl'])
    @commands.has_permissions(manage_guild=True)
    async def role(self, ctx):
        """役職関連(管理者用)"""
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['ad'])
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        """付与(管理者用)"""
        await member.add_roles(role)
        await ctx.send('付与しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command(aliases=['rm'])
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        """剥奪(管理者用)"""
        await member.remove_roles(role)
        await ctx.send('剥奪しました。')

    # roleコマンドのサブコマンド
    # 指定した役職を削除する。
    @role.command(aliases=['dl'])
    async def delete(self, ctx, role: discord.Role=None):
        """削除(管理者用)"""
        if role == None:
            await ctx.send('役職名を指定して下さい。')
            return
        #role = discord.utils.get(ctx.guild.roles, name=role_name)
        await role.delete()
        await ctx.send('削除しました。')

    # roleコマンドのサブコマンド
    # 役職を作成する。
    @role.command(aliases=['cr'])
    async def create(self, ctx, what= None):
        """作成(管理者用)"""
        if what == None:
            what = "new role"
        rote = 0
        #システム
        hoist = False
        mentionable = False
        #基本権限
        administrator = False
        view_audit_log = False
        manage_guild = False
        manage_roles = False
        manage_channels = False
        kick_members = False
        ban_members = False
        create_instant_invite = False
        change_nicknames = False
        manage_nicknames = False
        manage_emojis = False
        manage_webhooks = False
        read_messages = False
        #テキスト権限
        send_messages = False
        send_tts_messages = False
        manage_messages = False
        embed_links = False
        attach_files = False
        read_message_history = False
        mention_everyone = False
        external_emojis = False
        add_reactions = False
        #ボイス権限
        connect = False
        speak = False
        mute_members = False
        deafen_members = False
        move_members = False
        use_voice_activation = False
        while rote < 2:
            if rote == 1:
                await msg.delete()
                if read_messages == True:
                    await msgf.delete()
                rote=0
            roleedit = discord.Embed(title="権限設定",description=f"番号・記号を入力して下さい。")
            roleedit.add_field(name=f"**オンラインメンバーとは別にロールメンバーを表示する({hoist})**",value='`a`')
            roleedit.add_field(name=f"**このロールに対して@mentionを許可する({mentionable})**",value='`b`')
            roleedit.add_field(name=f"**管理者({administrator})**",value='`1`')
            roleedit.add_field(name=f"**監査ログを表示({view_audit_log})**",value='`2`')
            roleedit.add_field(name=f"**サーバーの管理({manage_guild})**",value='`3`')
            roleedit.add_field(name=f"**ロールの管理({manage_roles})**",value='`4`')
            roleedit.add_field(name=f"**チャンネルの管理({manage_channels})**",value='`5`')
            roleedit.add_field(name=f"**メンバーをKICK({kick_members})**",value='`6`')
            roleedit.add_field(name=f"**メンバーをBAN({ban_members})**",value='`7`')
            roleedit.add_field(name=f"**招待を作成({create_instant_invite})**",value='`8`')
            roleedit.add_field(name=f"**ニックネームの変更({change_nicknames})**",value='`9`')
            roleedit.add_field(name=f"**ニックネームの管理({manage_nicknames})**",value='`10`')
            roleedit.add_field(name=f"**絵文字の管理({manage_emojis})**",value='`11`')
            roleedit.add_field(name=f"**ウェブフックの管理({manage_webhooks})**",value='`12`')
            roleedit.add_field(name=f"**テキストチャンネルの閲覧&ボイスチャンネルの表示({read_messages})**",value='`13`')
            roleedit.add_field(name="－－－－－－－－－－",value='－－－－－－－－－－')
            roleedit.add_field(name="**無付与・設定完了**",value='`0`')
            msg = await ctx.send(embed=roleedit) 
            if read_messages == True:
                await asyncio.sleep(0.1)
                roletxt = discord.Embed(title="テキストの権限",description=f"番号を入力して下さい。")
                roletxt.add_field(name=f"**メッセージを送信({send_messages})**",value='`14`')
                roletxt.add_field(name=f"**TTSメッセージを送信({send_tts_messages})**",value='`15`')
                roletxt.add_field(name=f"**メッセージの管理({manage_messages})**",value='`16`')
                roletxt.add_field(name=f"**埋め込みリンク({embed_links})**",value='`17`')
                roletxt.add_field(name=f"**ファイルの添付({attach_files})**",value='`18`')
                roletxt.add_field(name=f"**メッセージ履歴を読む({read_message_history})**",value='`19`')
                roletxt.add_field(name=f"**@everyone,@here,すべてのロールにメンション({mention_everyone})**",value='`20`')
                roletxt.add_field(name=f"**外部の絵文字の使用({external_emojis})**",value='`21`')
                roletxt.add_field(name=f"**リアクションの追加({add_reactions})**",value='`22`')
                roletxt.add_field(name="－－－－－－－－－－",value='－－－－－－－－－－')
                roletxt.add_field(name="**無付与・設定完了**",value='`0`')
                await ctx.channel.send(embed=roletxt) 
                await asyncio.sleep(0.1)
                rolevoc = discord.Embed(title="音声の権限",description=f"番号を入力して下さい。")
                rolevoc.add_field(name=f"**接続({connect})**",value='`23`')
                rolevoc.add_field(name=f"**発言({speak})**",value='`24`')
                rolevoc.add_field(name=f"**メンバーをミュート({mute_members})**",value='`25`')
                rolevoc.add_field(name=f"**メンバーのスピーカーをミュート({deafen_members})**",value='`26`')
                rolevoc.add_field(name=f"**メンバーを移動({move_members})**",value='`27`')
                rolevoc.add_field(name=f"**音声検出を使用({use_voice_activation})**",value='`28`')
                rolevoc.add_field(name="－－－－－－－－－－",value='－－－－－－－－－－')
                rolevoc.add_field(name="**無付与・設定完了**",value='`0`')
                msgf = await ctx.send(embed=rolevoc) 
            def  rotetime(m):
                return m.content == "a" or "b" or "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14" or "15" or "16" or "17" or "18" "19" or "20" or "21" or "22" or "23" or "24" or "25" or "26" or "27" or "28" and m.author == ctx.author
            try:
                reply = await self.bot.wait_for( "message" , check = rotetime , timeout = 300.0 )
            except asyncio.TimeoutError:
                await ctx.channel.send( "設定を中止します。(type:time over)" )
                return
            else:
                if reply.content == "0":
                    rote = 2
                elif reply.content == "a":
                    if hoist == False:
                        hoist = True
                    elif hoist == True:
                        hoist = False
                    rote = 1
                elif reply.content == "b":
                    if mentionable == False:
                        mentionable = True
                    elif mentionable == True:
                        mentionable = False
                    rote = 1
                elif reply.content == "1":
                    if administrator == False:
                        administrator = True
                    elif administrator == True:
                        administrator = False
                    rote = 1
                elif reply.content == "2":
                    if view_audit_log == False:
                        view_audit_log = True
                    elif view_audit_log == True:
                        view_audit_log = False
                    rote = 1
                elif reply.content == "3":
                    if manage_guild == False:
                        manage_guild = True
                    elif manage_guild == True:
                        manage_guild = False
                    rote = 1
                elif reply.content == "4":
                    if manage_roles == False:
                        manage_roles = True
                    elif manage_roles == True:
                        manage_roles = False
                    rote = 1
                elif reply.content == "5":
                    if manage_channels == False:
                        manage_channels = True
                    elif manage_channels == True:
                        manage_channels = False
                    rote = 1
                elif reply.content == "6":
                    if kick_members == False:
                        kick_members = True
                    elif kick_members == True:
                        kick_members = False
                    rote = 1
                elif reply.content == "7":
                    if ban_members == False:
                        ban_members = True
                    elif ban_members == True:
                        ban_members = False
                    rote = 1
                elif reply.content == "8":
                    if create_instant_invite == False:
                        create_instant_invite = True
                    elif create_instant_invite == True:
                        create_instant_invite = False
                    rote = 1
                elif reply.content == "9":
                    if change_nicknames == False:
                        change_nicknames = True
                    elif change_nicknames == True:
                        change_nicknames = False
                    rote = 1
                elif reply.content == "10":
                    if manage_nicknames == False:
                        manage_nicknames = True
                    elif manage_nicknames == True:
                        manage_nicknames = False
                    rote = 1
                elif reply.content == "11":
                    if manage_emojis == False:
                        manage_emojis = True
                    elif manage_emojis == True:
                        manage_emojis = False
                    rote = 1
                elif reply.content == "12":
                    if manage_webhooks == False:
                        manage_webhooks = True
                    elif manage_webhooks == True:
                        manage_webhooks = False
                    rote = 1
                elif reply.content == "13":
                    if read_messages == False:
                        read_messages = True
                        msgf = await ctx.send("○")
                    elif read_messages == True:
                        read_messages = False
                        send_messages = False
                        send_tts_messages = False
                        manage_messages = False
                        embed_links = False
                        attach_files = False
                        read_message_history = False
                        mention_everyone = False
                        external_emojis = False
                        add_reactions = False
                        connect = False
                        speak = False
                        mute_members = False
                        deafen_members = False
                        move_members = False
                        use_voice_activation = False
                        await msgf.delete()
                    rote = 1
                elif reply.content == "14":
                    if send_messages == False:
                        send_messages = True
                    elif send_messages == True:
                        send_messages = False
                    rote = 1
                elif reply.content == "15":
                    if send_tts_messages == False:
                        send_tts_messages = True
                    elif send_tts_messages == True:
                        send_tts_messages = False
                    rote = 1
                elif reply.content == "16":
                    if manage_messages == False:
                        manage_messages = True
                    elif manage_messages == True:
                        manage_messages = False
                    rote = 1
                elif reply.content == "17":
                    if embed_links == False:
                        embed_links = True
                    elif embed_links == True:
                        embed_links = False
                    rote = 1
                elif reply.content == "18":
                    if attach_files == False:
                        attach_files = True
                    elif attach_files == True:
                        attach_files = False
                    rote = 1
                elif reply.content == "19":
                    if read_message_history == False:
                        read_message_history = True
                    elif read_message_history == True:
                        read_message_history = False
                    rote = 1
                elif reply.content == "20":
                    if mention_everyone == False:
                        mention_everyone = True
                    elif mention_everyone == True:
                        mention_everyone = False
                    rote = 1
                elif reply.content == "21":
                    if external_emojis == False:
                        external_emojis = True
                    elif external_emojis == True:
                        external_emojis = False
                    rote = 1
                elif reply.content == "22":
                    if add_reactions == False:
                        add_reactions = True
                    elif add_reactions == True:
                        add_reactions = False
                    rote = 1
                elif reply.content == "23":
                    if connect == False:
                        connect = True
                    elif connect == True:
                        connect = False
                    rote = 1
                elif reply.content == "24":
                    if speak == False:
                        speak = True
                    elif speak == True:
                        speak = False
                    rote = 1
                elif reply.content == "25":
                    if mute_members == False:
                        mute_members = True
                    elif mute_members == True:
                        mute_members = False
                    rote = 1
                elif reply.content == "26":
                    if deafen_members == False:
                        deafen_members = True
                    elif deafen_members == True:
                        deafen_members = False
                    rote = 1
                elif reply.content == "27":
                    if move_members == False:
                        move_members = True
                    elif move_members == True:
                        move_members = False
                    rote = 1
                elif reply.content == "28":
                    if use_voice_activation == False:
                        use_voice_activation = True
                    elif use_voice_activation == True:
                        use_voice_activation = False
                    rote = 1
                
        pre = discord.Permissions(administrator=administrator,view_audit_log=view_audit_log,manage_guild=manage_guild,manage_roles=manage_roles,manage_channels=manage_channels,kick_members=kick_members,ban_members=ban_members,create_instant_invite=create_instant_invite,change_nickname=change_nicknames,manage_nicknames=manage_nicknames,manage_emojis=manage_emojis,manage_webhooks=manage_webhooks,read_messages=read_messages,send_messages=send_messages,
                                  send_tts_messages=send_tts_messages,manage_messages=manage_messages,embed_links=embed_links,attach_files=attach_files,read_message_history=read_message_history,mention_everyone=mention_everyone,external_emojis=external_emojis,add_reactions=add_reactions,
                                  connect=connect,speak=speak,mute_members=mute_members,deafen_members=deafen_members,move_members=move_members,use_voice_activation=use_voice_activation)       
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2,hoist=hoist,mentionable=mentionable,permissions=pre)
        await ctx.send(f'作成しました。@' + set_name2)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(roles(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。

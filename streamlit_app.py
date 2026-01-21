import streamlit as st
import random
import datetime

# ページ設定
st.set_page_config(page_title="ヒソカの運勢鑑定", page_icon="♣️")

def hisoka_suffix():
    return random.choice(["♣︎", "♦︎", "♥︎", "♠︎"])

st.title("♣︎ ヒソカの運勢鑑定所 ♦︎")
st.write(f"ボクを退屈させないでよ…？ {hisoka_suffix()}")

with st.form("fortune_form"):
    birthday = st.date_input("キミの誕生日を教えてよ…♠︎")
    submitted = st.form_submit_button("占う")

if submitted:
    # シード値を固定（誕生日＋今日の日付）
    seed_value = int(birthday.strftime("%Y%m%d")) + int(datetime.date.today().strftime("%Y%m%d"))
    random.seed(seed_value)

    # 運勢データ
    fortunes = [
        "絶好調じゃないか…！キミはまさにダイヤの原石だね♣︎", 
        "悪くないね、ボク好みだ❤︎", 
        "ボクが壊したくなっちゃうよ…♦︎", 
        "少し期待外れかな…今はまだ食べ頃じゃない♠︎"
    ]
    love_luck = [
        "ボクからの熱い愛を受け取れるかもね❤︎", 
        "今はまだ、キミはただの『石ころ』だ。磨きなよ♦︎", 
        "いい刺激が待っているよ、フフフ……♣︎", 
        "ボクと戦うかい？それともデートかな？♠︎"
    ]
    # 用意しやすいアイテムに限定
    items = [
        "コンビニで買えるガム（伸縮自在なら最高だね）", 
        "トランプのカード（ジョーカーなら吉だよ）", 
        "清潔なハンカチ（ドッキリには欠かせないからね）", 
        "小銭（弾いて遊ぶのにちょうどいい♠︎）", 
        "ヘアワックス（キミも髪を立ててみたらどうだい？）",
        "スマホの充電器（ボクとの連絡が途切れないようにね❤︎）"
    ]

    res_overall = random.choice(fortunes)
    res_love = random.choice(love_luck)
    res_item = random.choice(items)

    st.divider()

    st.subheader(f"フフフ…鑑定結果だよ {hisoka_suffix()}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**全体運**\n\n{res_overall}")
    with col2:
        st.warning(f"**恋愛運**\n\n{res_love}")

    st.success(f"**ラッキーアイテム**： {res_item} {hisoka_suffix()}")

    st.write(f"次は実戦で会おう。それまで死なないでよ…？ {hisoka_suffix()}")

st.sidebar.markdown("ボクを満足させてくれるかな…？♠︎")

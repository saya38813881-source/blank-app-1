import streamlit as st
import random
import datetime

# ページ設定
st.set_page_config(page_title="ヒソカの運勢鑑定", page_icon="♣️")

def hisoka_suffix():
    return random.choice(["♣︎", "♦︎", "♥︎", "♠︎"])

st.title("♣︎ ヒソカの運勢鑑定所 ♦︎")
st.write(f"ボクを退屈させないでよ…？ {hisoka_suffix()}")

# 日付範囲の定義
min_date = datetime.date(1900, 1, 1)
max_date = datetime.date(2100, 12, 31)

with st.form("fortune_form"):
    birthday = st.date_input(
        "キミの誕生日を教えてよ…♠︎",
        value=datetime.date(2000, 1, 1),
        min_value=min_date,
        max_value=max_date
    )
    submitted = st.form_submit_button("ボクの資質を占って…♥︎")

if submitted:
    # シード値を固定
    seed_value = int(birthday.strftime("%Y%m%d")) + int(datetime.date.today().strftime("%Y%m%d"))
    random.seed(seed_value)

    # 1. 念系統の判定（誕生日の数字を元に固定）
    nen_types = ["強化系", "変化系", "放出系", "操作系", "具現化系", "特質系"]
    # 誕生日の数字だけでシードを再設定（系統は毎日変わらないように）
    random.seed(int(birthday.strftime("%Y%m%d")))
    my_nen = random.choice(nen_types)
    
    # 運勢用にシードを戻す
    random.seed(seed_value)

    # 運勢データ
    fortunes = ["絶好調じゃないか…！", "悪くないね、ボク好みだ❤︎", "ボクが壊したくなっちゃうよ…♦︎", "少し期待外れかな…♠︎"]
    love_luck = ["ボクからの愛を受け取れるかもね❤︎", "今はまだ、キミはただの『石ころ』だ♦︎", "いい刺激が待っているよ♣︎", "ボクと戦うかい？♠︎"]
    items = ["コンビニのガム", "トランプのカード", "清潔なハンカチ", "小銭", "ヘアワックス", "スマホの充電器"]

    res_overall = random.choice(fortunes)
    res_love = random.choice(love_luck)
    res_item = random.choice(items)

    st.divider()

    # ヒソカの鑑定結果
    st.subheader(f"フフフ…ボクが見立ててあげたよ {hisoka_suffix()}")

    # 念系統の表示を強調
    st.markdown(f"### 念系統： **{my_nen}**")
    
    # 系統ごとのヒソカ流コメント
    nen_comments = {
        "強化系": "単純で一途なキミは、壊しがいがありそうだ…♣︎",
        "変化系": "ボクと同じだね…嘘つきで気まぐれ。気が合いそうだよ♦︎",
        "放出系": "短気で大雑把かな？ 飛ばしすぎないように注意しなよ♠︎",
        "操作系": "理屈屋でマイペース。ボクの嫌いなタイプだけど、面白いね♥︎",
        "具現化系": "神経質で慎重。キミが何を作り出すのか、見てみたいよ♣︎",
        "特質系": "カリスマ性があるのかい？ ボクを飽きさせないでくれよ♦︎"
    }
    st.write(nen_comments[my_nen])

    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**全体運**\n\n{res_overall}")
    with col2:
        st.warning(f"**恋愛運**\n\n{res_love}")

    st.success(f"**ラッキーアイテム**： {res_item} {hisoka_suffix()}")

    st.write(f"早くボクのレベルまで上がっておいで。待っているよ…… {hisoka_suffix()}")

st.sidebar.image("https://www.google.com/s2/favicons?domain=streamlit.io&sz=64") # アイコン代わり
st.sidebar.markdown("キミのオーラ、ボクが美味しく判定してあげる♠︎")

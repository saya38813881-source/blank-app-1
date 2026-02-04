treamlit と Supabase を用いて作成した、ヒソカ風の口調で占いを行う Web アプリです。
ユーザーが誕生日を入力すると、念系統・全体運・恋愛運・ラッキーアイテムをヒソカが判定し、その結果をデータベースに保存します。

📌 アプリの機能

誕生日を入力すると占い結果を表示

念系統（強化系・変化系など）をランダムに判定

全体運・恋愛運・ラッキーアイテムを表示

占い結果を Supabase（PostgreSQL）に保存し、アプリ再起動後もデータが残る

ヒソカの口調・世界観を意識した UI / メッセージ表示

🚀 アプリのURL
https://blank-app-xe276otmsek.streamlit.app/

👉 アプリはこちらから試せます

🛠 使用技術

Python

Streamlit

Supabase（PostgreSQL）

GitHub

📂 Supabase について

占い結果は hisoka_fortunes テーブルに保存

Row Level Security（RLS）はオフに設定

st.secrets を利用して API キーを安全に管理

保存される主なデータ：

誕生日

占った日付

念系統

全体運・恋愛運・ラッキーアイテム

💡 開発時に工夫した点・大変だった点

st.secrets の設定方法が分からず、Supabase 接続時にエラーが多発した

URL や API Key を直接コードに書いてしまい、KeyError が発生

nano エディタの操作に慣れておらず、ターミナル操作に戸惑った

解決方法

secrets.toml を正しい場所（.streamlit/secrets.toml）に作成

キー名（SUPABASE_URL, SUPABASE_KEY）をコードと一致させる

Supabase の Table Editor でデータ保存を確認

🤖 生成AIの活用について

Streamlit と Supabase の接続コード生成

エラー内容の解釈と修正案の提示

README.md の構成や文章の作成

生成AIを活用することで、エラー解決のスピードが大幅に向上し、実装の理解も深まった。

📎 補足

このアプリは授業課題（タスク11改良）として作成しましたが、キャラクター性を持たせることで、学習用アプリとしての楽しさも意識しています。

import streamlit as st
import retriever_chain as rc

# 此python檔為chat bot執行檔

chain = rc.chain()

def clear_chat_history():
    st.session_state.update(messages=[{"role": "assistant", "content": "請輸入想查詢化學物質"}])

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.update(messages=[{"role": "assistant", "content": "請輸入想查詢化學物質"}])

def display_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

def get_response(query):
    try:
        # 使用 retriever chain 來處理查詢
        response = chain.invoke(query)
        return response, None
    except Exception as e:
        return None, str(e)

def handle_user_input(prompt):
    # 將用戶消息添加到會話狀態中
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # 構建查詢
    query = " ".join([msg["content"] for msg in st.session_state.messages if msg["role"] == "user"])

    with st.spinner("Thinking..."):
        response, error = get_response(query)
        
        if error:
            st.error(f"Error: {error}")
        else:
            # 將模型生成的回應添加到會話狀態中並顯示
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

# Sidebar
with st.sidebar:
    st.title('💬 SAS Chatbot')
    st.caption("🦙 A SAS chatbot powered by Llama3 and NeMo-Guardrails")
    st.button('清除歷史資料', on_click=clear_chat_history)
    st.markdown("[回到SAS平台](https://www.cmdm.tw)")

# 初始化會話狀態
init_session_state()

# 顯示會話狀態中的所有消息
display_messages()

# 接收用戶輸入的消息
if prompt := st.chat_input("請輸入想查詢化學物質"):
    handle_user_input(prompt)
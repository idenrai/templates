import streamlit as st
import requests

# Flask API 서버의 URL
API_URL = "http://127.0.0.1:5000/items"


# 아이템 리스트를 새로고침하는 함수
def refresh_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch items.")
        return {}


st.title("Item Management Interface")

if st.button("Add a new item"):
    st.session_state.open_add_page = True
    st.rerun()


# 아이템 등록 섹션
if "open_add_page" in st.session_state:
    st.header("Add a New Item")
    name = st.text_input("Item Name", value="")
    description = st.text_area("Item Description", value="")

    if st.button("Add Item"):
        if name:
            response = requests.post(API_URL, json={"name": name, "description": description})
            if response.status_code == 201:
                del st.session_state.open_add_page
                st.rerun()
            else:
                st.error("Failed to add item.")
        else:
            st.error("Item name is required.")


# 전체 아이템 조회 섹션
st.header("All Items")
items = refresh_items()
if items:
    for item_id, item in items.items():
        with st.expander(item['name']):
            st.write(item['description'])

            if st.button(f"Update (ID: {item_id})"):
                st.session_state.update_item_id = item_id
                st.session_state.update_name = item['name']
                st.session_state.update_description = item['description']
                st.rerun()  # 수정 페이지로 이동

            if st.button(f"Delete (ID: {item_id})"):
                delete_url = f"{API_URL}/{item_id}"
                del_response = requests.delete(delete_url)
                if del_response.status_code == 200:
                    st.rerun()
                else:
                    st.error(f"Failed to delete item ID '{item_id}'.")


# 아이템 수정 섹션
if "update_item_id" in st.session_state:
    st.header(f"Update Item ID {st.session_state.update_item_id}")
    update_name = st.text_input("Updated Name", value=st.session_state.update_name)
    update_description = st.text_area("Updated Description", value=st.session_state.update_description)

    if st.button("Update Item"):
        update_url = f"{API_URL}/{st.session_state.update_item_id}"
        update_response = requests.put(update_url, json={"name": update_name, "description": update_description})
        if update_response.status_code == 200:
            st.success(f"Item ID '{st.session_state.update_item_id}' updated successfully!")
            del st.session_state.update_item_id
            del st.session_state.update_name
            del st.session_state.update_description
            st.rerun()
        else:
            st.error("Failed to update item.")

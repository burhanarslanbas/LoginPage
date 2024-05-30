//write a python script to publish the index.html file located in the Login_v2 folder in streamlit sharing//write a python script to publish the index.html file located in the Login_v2 folder in streamlit sharing.

//Login_v2/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>


//streamlit_login.py
import streamlit as st

st.set_page_config(page_title="Login", page_icon=":shark:", layout="centered", initial_sidebar_state="expanded")

def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Login</h1>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.button("Login")
    if submit_button:
        if username == "admin" and password == "1234":
            st.success("Login Successful")
        else:
            st.error("Invalid Username or Password")

if __name__ == "__main__":
    main()

//run the python script using the following command:
//streamlit run streamlit_login.py

//output
//Login
//Username
//Password
//Login

//The output will be displayed in the web browser.


//write a python script to publish the index.html file located in the Login_v2 folder in streamlit sharing.

//Login_v2/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="/login" method="post">
        <label for="username
#streamlit run Login_v2/index.html

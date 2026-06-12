
import streamlit as st
from utils.auth import register_user, login_user
from modules import login

def show():

    st.title("🏥 AI Healthcare System")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # ---------------- LOGIN ----------------

    with tab1:

        st.subheader("Login")

        login_email = st.text_input(
            "Email",
            key="login_email"
        )

        login_password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login"):

            user = login_user(
                login_email,
                login_password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.user = user[1]
                st.session_state.role = user[4]

                st.success(
                    f"Welcome {user[1]}"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Email or Password"
                )

    # ---------------- REGISTER ----------------

    with tab2:

        st.subheader("Create Account")

        name = st.text_input(
            "Name",
            key="reg_name"
        )

        email = st.text_input(
            "Email",
            key="reg_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="reg_password"
        )

        role = st.selectbox(
            "Role",
            [
                "Admin",
                "Doctor",
                "Patient"
            ]
        )

        if st.button("Register"):

            success = register_user(
                name,
                email,
                password,
                role
            )

            if success:

                st.success(
                    "Registration Successful! Now Login."
                )

            else:

                st.error(
                    "User already exists"
                )


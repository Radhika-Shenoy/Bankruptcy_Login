import streamlit as st 
#st.set_page_config(layout="wide")
image1_url = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1538356343135-65849f66b4a1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcxMzEzODQ3OA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080');
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>
    '''
st.markdown(image1_url, unsafe_allow_html=True)

st.markdown('<h1 style="color:black;font-size:35px;text-align:left;margin-left:20px;">Finance Radar</h1>', unsafe_allow_html=True)




    #st.markdown('<p style="color:black; font-weight:bold;">Manager Login</p>', unsafe_allow_html=True)
#Login form for initial login page
#with st.sidebar:
with st.form(key='login_form1'):
    st.subheader('Login Credentials')
    username = st.text_input('**Enter your userID:**',help=' Hint: CompanyNameuser')       
    password = st.text_input('**Enter your password:**', type='password',help='Default password: CompanyNamepassword')
    
    st.markdown('<p style="color:black; font-weight:bold;">Disclaimer!</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:black; font-weight:bold;">Certain sections of the web app contain sensitive company financial record data. Kindly refrain from accessing this information if you are not an authorized team member. Unauthorized access will be subject to penalties.</p>', unsafe_allow_html=True)
    checkbox_val = st.checkbox("**I am an employed company member**") 
    login_button = st.form_submit_button('Login')
    if login_button:
        if not username or not password:
            st.error("Please enter the credentials to login")
    if login_button:
        if username and password:
            # Based on the credentials login is redirected
            if (username == 'C1user' and password == 'C1password'):
                if not checkbox_val:
                    st.error('Please accept that you are an authorized member')
                if checkbox_val:
                    if login_button:
                        st.success('Login Successful!')
                        st.session_state['userID'] = username
                        st.markdown(f'<a href="https://cmseproject-3pttvdumrkrn8bxu2szg7a.streamlit.app"><button>Go to the Authorised Manager website</button></a>', unsafe_allow_html=True)    
            
            elif (username == 'C2user' and password == 'C2password'):
                if not checkbox_val:
                    st.error('Please accept that you are an authorized member')
                if checkbox_val:
                    if login_button:
                        st.success('Login Successful!')
                        st.session_state['userID'] = username
                        st.markdown(f'<a href="https://cmseproject-3pttvdumrkrn8bxu2szg7a.streamlit.app"><button>Go to the Authorised Manager website</button></a>', unsafe_allow_html=True)          


    

                
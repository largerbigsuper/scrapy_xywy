from fake_useragent import UserAgent


# ua.safari
# ua.ie
# ua.opera
# ua.chrome
# ua.firefox

def gen_user_agent():
    path = 'user_agent.json'
    ua = UserAgent(path=path)
    ua.random

if __name__ == "__main__":
    gen_user_agent()
import time

URL = "YOUR_WEBSITE_URL"
EMAIL_SELECTOR = 'CSS_SELECTOR_1'
CONTINUE_SELECTOR = 'CSS_SELECTOR_2'
PASSWORD_SELECTOR = 'CSS_SELECTOR_3'
SIGNIN_SELECTOR = 'CSS_SELECTOR_4'
"""
2段階認証があるウェブサイトではこの部分のコメントアウトを解除して使用してください
IDLE = 'networkidle'
TWO_FACTOR_WAIT_MS = 45000
"""  
LOAD_TIMEOUT = 30000  

def perform_login(page, email, password):
    # ログイン処理
    page.goto(URL, timeout=LOAD_TIMEOUT)
    page.fill(EMAIL_SELECTOR, email)
    page.click(CONTINUE_SELECTOR)
    page.wait_for_selector(PASSWORD_SELECTOR, timeout=10000)
    page.fill(PASSWORD_SELECTOR, password)
    page.click(SIGNIN_SELECTOR)
    
    """
    
    print('ログインのために2段階認証コードを入力してください。45秒待機します。')
    page.wait_for_timeout(TWO_FACTOR_WAIT_MS)
    page.wait_for_load_state(IDLE)
    """

    if not page.url.startswith(URL):
        raise Exception("YOUR_WEBSITE_URLへのログインに失敗しました。URLが想定と異なります。")
    
    print("YOUR_WEBSITE_URLへのログインに成功しました。")
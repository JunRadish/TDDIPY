from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase): #1 - unittest.TestCase를 상속해서 테스트를 클래스 형태로 만든다!
    def setUp(self): #2 테스트 시작! 메소드
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): #3 테스트 종료! 메소드 에러가 발생해도 실행됨!
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #4 테스트 메인 코드.

        # browser = webdriver.Firefox()
        # # Edith는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다.
        self.browser.get('http://127.0.0.1:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다.
        self.assertIn('To-Do',self.browser.title) #5 테스트 assertion method 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # 그녀는 바로 작업을 추가하기로 한다.
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'), 
            '작업 아이템 입력'
        )

        # "공작깃털 사기"라고 텍스트 상자에 입력한다.
        # Edith의 취미는 날치 잡이용 그물을 만드는 것이다.
        input_box.send_keys('공작깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고, 작업록록에 "1: 공작깃털 사기" 아이템이 추가된다.
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: 공작깃털 사기' for row in rows),
            "신규 작업이 테이블에 표시되지 않는다."
        )
        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다.(Edith는 매우 체계적인 사람이다.)
        self.fail("Finish the test!")
        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다.
        # Edith는 사이트가 입력한 목록을 저장하고 있는지 궁금하다.

        # 사이트는 그녀를 위한 특정 URL을 생성해준다.
        # 이때 URL에 대한 설명도 함께 제공된다.

        # 해당 URL에 접속하면 그녀가 만든 작업목록이 그대로 있는 것을 확인할 수 있다.

        # 만족하고 잠자리에 든다.

if __name__ == '__main__': #7
    unittest.main(warnings='ignore') #8
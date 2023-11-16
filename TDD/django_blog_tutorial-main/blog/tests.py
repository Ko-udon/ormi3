from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from accounts.models import User

class Test(TestCase):
    def setUp(self):
        print('-- blog app 테스트 시작 --')
        self.client = Client()
        self.user_hojun = User.objects.create_user(
            username='hojun',
            password='nopassword'
        )

    def test_connection(self):
        
        # 접속확인
        print('# 접속확인 테스트')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)


    def test_tag(self):
        print('# 상속 확인')

        ## ./
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertEqual(None, headbar)

        ## /about/
        response = self.client.get('/about/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertIn('Document', headbar.text)

        bodybar = soup.body
        self.assertIn('about', bodybar.text)

        # footer는 없음,,
        # footer = soup.footer
        # self.assertIn(None, footer)


        ## /contact/
        response = self.client.get('/contact/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertIn('Document', headbar.text)

        bodybar = soup.body
        self.assertIn('contact', bodybar.text)

        # footer = soup.footer
        # self.assertIn(None, footer)
        
        ## /blog/
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        headbar = soup.head
        self.assertIn('Blog', headbar.text)

        bodybar = soup.body
        self.assertIn('blog', bodybar.text)

        # footer = soup.footer
        # self.assertIn(None, footer)




    def test_post_list(self):
        print('# 게시물 리스트 확인')
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')

        if Post.objects.count() == 0:
            print('게시물이 없는 경우')
            self.assertIn('아직 게시물이 없습니다.', soup.body.text)
        else:
            print('게시물이 있는 경우')
            print(Post.objects.count())
            print(len(soup.body.select('h2')))
            self.assertGreater(len(soup.body.select('h2')), 1) # h2태그가 1개 이상


    def test_post_detail(self):
        print('게시물 상세페이지 확인')
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World.',
            author = self.user_hojun
        )

        # 상세페이지 정상적으로 불러오는지 확인
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        detail = soup.body.main.text
        detail_content = detail.split('\n')

        # 제목 자리에 제목이 들어있는지
        self.assertEqual(detail_content[1], '첫 번째 포스트입니다.')
        
        # 내용 자리에 내용이 들어있는지
        self.assertEqual(detail_content[2], 'Hello World.')

        # 최종 수정 날짜에 수정날짜가 들어가 있는지
        self.assertIn(detail_content[3][:-8], post_001.updated_at.strftime('%Y년 %m월 %d일'))
        
        # 상속이 제대로 이뤄져 있는지
        navbar = soup.nav
        self.assertIn('Home', navbar.text)
        self.assertIn('About', navbar.text)
        self.assertIn('Blog', navbar.text)

        # footer는 없음,,
        # footer = soup.footer
        # self.assertIn(None, footer)


        # print('-- 상속 확인 --')
        # # 2. 상속
        # # 2.1 페이지 상속이 제대로 되었다면 nav태그가 있고, footer태그가 있어야 합니다.
        # # 2.2 nav태그 내부에는 Home, About, Blog라는 문구(메뉴)가 있어야 합니다.
        # navbar = soup.nav
        # self.assertIn('Home', navbar.text)
        # self.assertIn('About', navbar.text)
        # self.assertIn('Blog', navbar.text)

        # # 3. 포스트 내용
        # # 3.1 포스트가 1개 있다면 해당 포스트의 제목(title)이 포스트 영역에 있어야 합니다.
        # self.assertIn(post_001.title, soup.body.text)
        # # 3.2 포스트가 1개 있다면 해당 포스트의 내용(content)이 포스트 영역에 있어야 합니다.
        # self.assertIn(post_001.content, soup.body.text)
        # # 3.3 포스트가 1개 있다면 해당 포스트의 작성자(author)가 포스트 영역에 있어야 합니다.
        # self.assertIn(post_001.author.username, soup.body.text)

    
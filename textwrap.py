import textwrap3

txt = '최근 일부 프로젝트가 프론트 엔드에서 파이썬을 자바스크립트로 트랜스파일하거나 웹어셈블리를 통해 프런트엔드에서 파이썬을 실행하는 방법을 시도했지만, 현재 구현되는 방식은 투박하고 원시적이다. 개발자에게 지금 바로 더 좋은 선택지는 없을까? 물론 있다. 새로운 파이썬 웹 프레임워크 제품군을 사용하면 백엔드에서 프로그래밍 방식으로 프런트 엔드 코드를 생성하는 선언적인 파이썬 코드를 작성할 수 있다. 파이썬 객체를 사용해 HTML 엔티티와 해당 자바스크립트 기반 동작을 기술한 다음, 클라이언트에 제공될 때 프레임워크가 이러한 객체를 자동으로 생성하도록 할 수 있다.'
print(txt)

print(textwrap3.shorten(txt, width=200))
print(textwrap3.shorten(txt, width=100, placeholder='...[중략]'))

wrapped_txt = textwrap3.wrap(txt, width=40)
print(wrapped_txt)
print('\n'.join(wrapped_txt))
filled_txt = textwrap3.fill(txt, width=40)
print(filled_txt)
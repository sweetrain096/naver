from matplotlib import font_manager, rc #한글이 나오게
import matplotlib.pyplot as plt
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.figure(figsize=(14,8))
plt.plot([1,2,3],[1,2,3],'g^') #각각의 값과 점의 모양설정
plt.text(1,1,'사과') #텍스트 찍기
plt.text(2,2,'바나나')
plt.text(3,3,'포도')
#각 축의 크기 설정
plt.axis([0,6,0,6]) # 그래프의 x축,y축 크기설정
plt.show()

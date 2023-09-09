import streamlit as st

st.title('RIOT GAMES 소개')
image_path= 'rgg.PNG'
st.image(image_path)

st.title('RIOT GAMES 인트로')
st.video("https://i.namu.wiki/i/WQ4_DwaJxVLMK3EqyZV45nYa7BvzdkzDD7VMlShzWCOC9SLwxiSS4or9L_jsgQsX47cUE8mCiX0EVmw6giGI_A.mp4")

st.title("'RIOT GAMES'의 게임들")
st.write("League Of Legend")
image_path1="롤.jfif"
st.image(image_path1)
st.write("VALORANT")
image_path2="발로.jfif"
st.image(image_path2)
st.write("League Of Legend Wild Rift")
image_path3='와일드 리프트.jfif'
st.image(image_path3)

st.title('게임 알아보기')
Games = st.radio(
    'RIOT GAMES가 개발하는 게임 소개',
    ('League Of Legend', 'VALORANT', 'League Of Legend Wild Rift')
)

if Games == 'League Of Legend':
    image_path5='f리그 오브.jfif'
    st.image(image_path5)
    st.write('개인의 숙련도와 팀 시너지를 조합하는 5대5 MOBA, 리그 오브 레전드에서 플레이어님의 실력을 선보이세요. 포지션을 선택하고, 아이템 빌드를 완성하고, 맵에서 치열한 전투를 펼쳐 적의 넥서스를 파괴하세요. 무한한 플레이 방식을 가진 150명 이상의 챔피언 중 자신만의 챔피언을 찾아 승리를 쟁취하세요.')
elif Games == 'VALORANT':
    image_path6='발로.jfif'
    st.image(image_path6)
    st.write('정밀한 실력 자랑, 굉장한 전리품, 숨 막히는 게임플레이와 짜릿한 경험까지. 모두 발로란트에서 무료로 즐길 수 있습니다. 발로란트에서는 각각 다섯 명으로 이루어진 공격팀과 수비팀이 25라운드 13선승제로 총격전을 벌입니다. 무엇보다 투명하고 공정한 게임플레이가 중요한 게임이기 때문에, 라이엇 게임즈에서는 발로란트를 위해 투자를 아끼지 않고 전례 없이 뛰어난 백엔드 시스템을 구축했습니다. 이 시스템은 전용 128틱 서버, 맞춤 제작 넷코드, 서버 권한 게임 아키텍처, 특유의 부정행위 방지 기능 등을 자랑합니다.')
else:
    image_path7='와맆.jfif'
    st.image(image_path7)
    st.write('와일드 리프트의 세계에 빠져보세요. 실력과 전략으로 승부하는 리그 오브 레전드의 5대5 MOBA 게임이 모바일과 콘솔에 맞춰 새롭게 탄생합니다. 새로운 조작법이 적용된 박진감 넘치는 게임에서 친구와 팀을 구성하고, 챔피언을 정하고, 짜릿한 승부를 겨뤄 보세요.')

st.title("라이엇 스토어")
st.write('스태츄, 피규어부터 옷까지 게임 속에만 있던 캐릭터들이 현실로')
image_path4=('라이엇 스토어.jfif')
st.image(image_path4)

Store = st.radio(
    '라이엇 스토어가 판매하는 굿즈',
    ('아리 망토 후드', '팝스타 아리 장패드', '아리 워치 스트랩', '그웬 인형', '스태츄')
)
if Store == '아리 망토 후드':
    image_path8='후드 망토.PNG'
    st.image(image_path8)
    st.write('자신의 동족과 기원을 찾아 나서는 아리의 망토는 어디에서나 감싸줍니다. 폭신한 아리의 망토를 지금 만나보세요. ')

elif Store == '팝스타 아리 장패드':
    image_path9='장패드.PNG'
    st.image(image_path9)
    st.write('음악계를 휩쓴 팝스타 아리가 장패드로 돌아왔습니다 !')

elif Store == '아리 워치 스트랩':
    image_path10='워치 스트립.PNG'
    st.image(image_path10)
    st.write('영혼과 감정을 다루는게 좋다면 이 스트랩이 여러분에게 딱 맞을지도 모릅니다.')

elif Store == '그웬 인형':
    image_path11='그웬.PNG'
    st.image(image_path11)
    st.write('게임에서만 보던 그웬을 인형으로 만나보세요.')

elif Store == '스태츄':
    image_path12='스태츄.PNG'
    st.image(image_path12)
    st.write('게임에서 본 캐릭터를 스태츄로 만나보세요.')

button = st.button('구입하기')
if button:
    st.write('상품 문의는 02-2039-9583으로 연락해 주세요.')

st.title('e스포츠를 빛낸 RIOT GAMES')
st.write('지난 9월에 열린 "롤드컵"에서 많은 유저들이 관심을 가져다 주었습니다.')
st.write('롤드컵이란 리그 오브 레전드의 국제 대회로, 롤 + 월드컵을 합친 말인데 라이엇이 주최하는 대회 중 가장 큰 대회입니다.')
image_path13='롤드컵.PNG'
st.image(image_path13)
st.write('2022년 롤드컵 결승의 모습')

image_path14='우승.PNG'
st.image('우승.PNG')
st.write('2대2 접전끝에 2022 롤드컵의 챔피언은 DRX가 가져가게 되었습니다. 저들은 모두 리그 오브 레전드를 플레이하며 꿈을 이루기 위해 노력하였고, 결국 우승이라는 꿈을 이루게 되었습니다.')

st.title('여러분도 꿈을 이루고 싶나요 ? 여러분의 꿈을 이루기 위해 RIOT GAMES가 함께하겠습니다 !')
st.write('라이엇 계정 회원가입 하기')
st.write('https://www.riotgames.com/ko ')



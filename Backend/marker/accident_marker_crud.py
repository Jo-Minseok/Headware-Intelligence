from db.models import Accident, AccidentProcessing
from sqlalchemy.orm import Session
from db.db_connection import db_session
from datetime import datetime, timedelta
import numpy as np

# 사고 발생 데이터 조회
def get_accidents(db: Session):
    return db.query(Accident).all()

# 사고처리 데이터 조회
def get_accident_processing(db: Session, no: int):
    return db.query(AccidentProcessing).filter(AccidentProcessing.no == no).first()

# 사고 발생 데이터 삽입(테스트 용도)
def insert_accident(start=datetime(2023, 1, 1), end=datetime(2024, 6, 30), size=400, K=3):
    # db 세션 연결
    db = db_session()
    
    # 데이터 생성 전 데이터 삭제
    db.query(Accident).delete()
    db.commit()
    
    # 부산광역시 남구 유엔로157번길 75 기준 위도, 경도 값
    base_latitude = 35.1336437235
    base_longitude = 129.09320833287

    # 1도의 위도와 경도가 약 111km를 나타내므로, K km는 대략 K/111도임
    # 반경을 K km로 설정하여 주변에 데이터를 생성
    radius_km = K / 111

    # 무작위로 size개의 좌표 생성
    np.random.seed(42) # 재현성을 위해 시드 설정
    latitude = np.random.uniform(low=base_latitude - radius_km, high=base_latitude + radius_km, size=size)
    longitude = np.random.uniform(low=base_longitude - radius_km, high=base_longitude + radius_km, size=size)
    
    # 시작 날짜와 끝 날짜 설정
    start_date = start
    end_date = end

    # size개의 무작위 정수 생성 (날짜 차이를 일 단위로 나타내는 정수)
    random_days = np.random.randint(0, (end_date - start_date).days + 1, size=size)

    # 시작 날짜에 무작위로 생성된 날짜 차이를 더하여 날짜 생성
    random_dates = [start_date + timedelta(days=int(random_day)) for random_day in random_days]
    
    for lat, lon, day in zip(latitude, longitude, random_dates):
        accident = Accident(date=day.strftime('%Y-%m-%d'), 
                            time=datetime.now().strftime('%H:%M:%S'), 
                            latitude=lat, 
                            longitude=lon, 
                            victim_id='test', 
                            category='test')
        db.add(accident)

    db.commit()
    
    # 사고 처리 데이터의 번호 값을 지정하기 위해 Accident 테이블의 모든 데이터를 질의
    accidents = db.query(Accident).all()
    
    # 데이터 생성 전 데이터 삭제
    db.query(AccidentProcessing).delete()
    db.commit()
    
    # 상황 데이터는 아래 세 가지 데이터를 랜덤하게 사용
    situation = ['처리 완료', '119 신고중', '처리중']
    
    for accident in accidents:
        processing = AccidentProcessing(no=accident.no, 
                                        situation=situation[np.random.randint(0, 3)], 
                                        date=day.strftime('%Y-%m-%d'), 
                                        time=datetime.now().strftime('%H:%M:%S'), 
                                        detail='')
        db.add(processing)
    
    db.commit()
    db.close()
    
# insert_accident()
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mv: target '동향_20200331.csv' is not a directory\r\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[0m\u001b[01;32m'전국 신규 민간 아파트 분양가격 동향_20200331.csv'\u001b[0m*\r\n"
     ]
    }
   ],
   "source": [
    "%ls data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[0m\u001b[01;32m'전국 신규 민간 아파트 분양가격 동향_20200331.csv'\u001b[0m*\r\n",
      "\u001b[01;32m'주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv'\u001b[0m\u001b[K*\r\n"
     ]
    }
   ],
   "source": [
    "%ls data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4675, 5)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_last = pd.read_csv(\"data/주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv\", encoding=\"cp949\")\n",
    "df_last.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>지역명</th>\n",
       "      <th>규모구분</th>\n",
       "      <th>연도</th>\n",
       "      <th>월</th>\n",
       "      <th>분양가격(㎡)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>서울</td>\n",
       "      <td>전체</td>\n",
       "      <td>2015</td>\n",
       "      <td>10</td>\n",
       "      <td>5841</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>서울</td>\n",
       "      <td>전용면적 60㎡이하</td>\n",
       "      <td>2015</td>\n",
       "      <td>10</td>\n",
       "      <td>5652</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>서울</td>\n",
       "      <td>전용면적 60㎡초과 85㎡이하</td>\n",
       "      <td>2015</td>\n",
       "      <td>10</td>\n",
       "      <td>5882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>서울</td>\n",
       "      <td>전용면적 85㎡초과 102㎡이하</td>\n",
       "      <td>2015</td>\n",
       "      <td>10</td>\n",
       "      <td>5721</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>서울</td>\n",
       "      <td>전용면적 102㎡초과</td>\n",
       "      <td>2015</td>\n",
       "      <td>10</td>\n",
       "      <td>5879</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  지역명               규모구분    연도   월 분양가격(㎡)\n",
       "0  서울                 전체  2015  10    5841\n",
       "1  서울         전용면적 60㎡이하  2015  10    5652\n",
       "2  서울   전용면적 60㎡초과 85㎡이하  2015  10    5882\n",
       "3  서울  전용면적 85㎡초과 102㎡이하  2015  10    5721\n",
       "4  서울        전용면적 102㎡초과  2015  10    5879"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_last.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>지역명</th>\n",
       "      <th>규모구분</th>\n",
       "      <th>연도</th>\n",
       "      <th>월</th>\n",
       "      <th>분양가격(㎡)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>4670</th>\n",
       "      <td>제주</td>\n",
       "      <td>전체</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "      <td>4085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4671</th>\n",
       "      <td>제주</td>\n",
       "      <td>전용면적 60㎡이하</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "      <td>4039</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4672</th>\n",
       "      <td>제주</td>\n",
       "      <td>전용면적 60㎡초과 85㎡이하</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "      <td>4091</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4673</th>\n",
       "      <td>제주</td>\n",
       "      <td>전용면적 85㎡초과 102㎡이하</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4674</th>\n",
       "      <td>제주</td>\n",
       "      <td>전용면적 102㎡초과</td>\n",
       "      <td>2020</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     지역명               규모구분    연도  월 분양가격(㎡)\n",
       "4670  제주                 전체  2020  4    4085\n",
       "4671  제주         전용면적 60㎡이하  2020  4    4039\n",
       "4672  제주   전용면적 60㎡초과 85㎡이하  2020  4    4091\n",
       "4673  제주  전용면적 85㎡초과 102㎡이하  2020  4     NaN\n",
       "4674  제주        전용면적 102㎡초과  2020  4     NaN"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_last.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.15+"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

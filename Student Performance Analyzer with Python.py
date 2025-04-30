import pandas as pd
import streamlit as st
# dataset
file = st.file_uploader('drop file here')
if file:
       df = pd.read_csv(file)

       # sep women and men with their score
       women_score = df.loc[df['gender'] =='female',['gender','math score','reading score','writing score']]
       men_score = df.loc[df['gender'] =='male',['gender','math score','reading score','writing score']]
       #woman scores
       st.markdown('# Women score')
       st.dataframe(women_score)
       # men scores
       st.markdown('# Men score')
       st.dataframe(men_score)
       #avg men and women scores
       st.markdown('# Average women score')
       st.write(f'##### Math score: {df.loc[(df['gender']=='female'),'math score'].mean()}')
       st.write(f'##### reading score: {df.loc[(df['gender']=='female'),'reading score'].mean()}')
       st.write(f'##### writing score: {df.loc[(df['gender']=='female'),'writing score'].mean()}')
       st.markdown('# Average men score')
       st.write(f'##### Math score: {df.loc[(df['gender']=='male'),'math score'].mean()}')
       st.write(f'##### reading score: {df.loc[(df['gender']=='male'),'reading score'].mean()}')
       st.write(f'##### writing score: {df.loc[(df['gender']=='male'),'writing score'].mean()}')
       #compare two gender
       st.markdown('# compare men and women')
       comp_w_m = {'Male':...,'Female':...}

       man_math_avg = df.loc[(df['gender']=='male'),'math score'].mean()
       women_math_avg = df.loc[(df['gender']=='female'),'math score'].mean()
       man_read_avg = df.loc[(df['gender']=='male'),'reading score'].mean()
       women_read_avg = df.loc[(df['gender']=='female'),'reading score'].mean()
       man_write_avg = df.loc[(df['gender']=='male'),'writing score'].mean()
       women_write_avg = df.loc[(df['gender']=='female'),'writing score'].mean()
       st.write('### MATH')
       if man_math_avg > women_math_avg:
              st.write(f'##### Male  {man_math_avg}')
       else:
              st.write(f'##### Female  {women_math_avg}')
       st.write('### Reading')
       if man_read_avg > women_read_avg:
              st.write(f'##### Male  {man_read_avg}')
       else:
              st.write(f'##### Female  {women_read_avg}')
       st.markdown('### Writing')
       if man_write_avg > women_write_avg:
              st.write(f'##### Male  {man_write_avg}')
       else:
              st.write(f'##### Female  {women_write_avg}')
       st.write('# Chart')
       # CHART
       """#### Female math score chart"""
       st.line_chart(df.loc[df['gender']=='female','math score'])
       """#### Male math score chart"""
       st.line_chart(df.loc[df['gender']=='male','math score'])
       """#### Female reading score chart"""
       st.line_chart(df.loc[df['gender']=='female','reading score'])
       """#### Male reading score chart"""
       st.line_chart(df.loc[df['gender']=='male','reading score'])
       """#### Female writing score chart"""
       st.line_chart(df.loc[df['gender']=='female','writing score'])
       """#### Male writing score chart"""
       st.line_chart(df.loc[df['gender']=='female','writing score'])

       men_score_pass = men_score.loc[(df['math score'] >= 50) & (df['reading score']>=50) & (df['writing score']>=50),['gender','math score','reading score','writing score']]
       women_score_pass = women_score.loc[(df['math score'] >= 50) & (df['reading score']>=50) & (df['writing score']>=50),['gender','math score','reading score','writing score']]
       men_score_fail = men_score.loc[(df['math score'] < 50) & (df['reading score']<50) & (df['writing score']<50),['gender','math score','reading score','writing score']]
       women_score_fail = women_score.loc[(df['math score'] < 50) & (df['reading score']<50) & (df['writing score']<50),['gender','math score','reading score','writing score']]











       # low and high score all
       score_read =df['math score'].tolist()
       score_write = df['math score'].tolist()
       score_math = df['math score'].tolist()
       scores = []
       scores.extend(score_read)
       scores.extend(score_math)
       scores.extend(score_write)
       #Grade Categories
       '''# Female'''
       df_female_grade_cat = df.loc[df['gender']=='female',['math score','reading score','writing score']]
       grade_Fe_categories = df_female_grade_cat.applymap(lambda x: 'A' if x >= 80 else ('B' if x >= 60 else ('C' if x >= 50 else 'F')))
       st.write(grade_Fe_categories)
       '''# Male'''
       df_female_grade_cat = df.loc[df['gender']=='male',['math score','reading score','writing score']]
       grade_Fe_categories = df_female_grade_cat.applymap(lambda x: 'A' if x >= 80 else ('B' if x >= 60 else ('C' if x >= 50 else 'F')))
       st.write(grade_Fe_categories)

       st.write()



       #scores classification
       # st.write("# Grade Categories")
       # grade_categories = list(map(lambda x:'A' if x>=80 else ('B' if x >= 60 else 'C') , scores))
       # st.write(grade_categories)

       # low_scores = list(filter(lambda x:x<50,scores))
       # high_scores =  list(filter(lambda x:x>=50,scores))
       # st.write("# LOW SCORES")
       # st.write(low_scores)
       # st.write("# HIGH SCORES")
       # st.write(high_scores)

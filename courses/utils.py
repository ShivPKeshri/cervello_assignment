from .models import *

import os
import pandas as pd
from sqlalchemy import create_engine


def upload_excel_util(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    df_dict = pd.read_excel(path,sheet_name=None)

    engine = create_engine('sqlite:///db.sqlite3')

    df_courses = df_dict['Course'].reset_index()
    df_courses.rename(columns={"index":"id"}, inplace=True)

    df_courses.to_sql("courses_courses", if_exists='replace', con=engine, index=False)
        
    df_sections = df_dict['Section'].reset_index()
    df_sections.rename(columns={"index":"id"}, inplace=True)

    courses_qs = Courses.objects.all()

    for index, section in df_sections.iterrows():
        section['course'] = [course.pk for course in courses_qs if course.title==section['course']][0]

    df_sections.to_sql("courses_sections", if_exists='replace', con=engine, index=False)

    sections_qs = Sections.objects.all()

    df_lectures = df_dict['Lectures'].reset_index()
    df_lectures.rename(columns={"index":"id"}, inplace=True)

    for index, lecture in df_lectures.iterrows():
        lecture['section'] = [section.pk for section in sections_qs if section.title==section['section']][0]

    df_lectures.to_sql("courses_lectures", if_exists='replace', con=engine, index=False)

  

    # cources = Courses.objects.all()
    # print(cources)
    # if cources:
    #     print('deleting objects')
    #     cources.delete()


    # print(df_dict['Course'])

    # courses_dict = df_dict['Course'].to_dict('records')
    
    # courses_instances = [Courses(
    #     title=record['title']  
    #     ) for record in courses_dict]

    # print(courses_instances)
    # Courses.objects.bulk_create(courses_instances)

    # cource = [course for course in courses_instances if course.title=='Flask']
    # print(cource)

    # sections_dict = df_dict['Section'].to_dict('records')
    
    # sections_instances = [Sections(
    #     title=record['title'] ,
    #     courses=[course for course in courses_instances if course.title==record['course']][0]
    #     ) for record in sections_dict]

    # for section in sections_instances:
    #     print(section.title,'-->', section.courses)

    # Sections.objects.bulk_create(sections_instances)

    # for ss in sections_instances:
    #     tt = Sections.objects.create(ss)
    #     tt.save()

import pandas as pd
import datetime as dt
df = pd.read_csv('be.csv')
df2 = df
name = df['Vac_name']
new_name = []
"""Разбиение на группы по вакансиям"""
for i in name:
    if (i.lower().find('рекрутер')!=-1 or i.lower().find('recruiter')!=-1):
        new_name.append('IT-рекрутер')
    elif ((i.lower().find('проект')!=-1 or i.lower().find('project')!=-1) and 
         (i.lower().find('менеджер')!=-1 or i.lower().find('manager')!=-1)
         or i.lower().find('руководитель')!=-1 or
         i.lower().find('админ')!=-1 or i.lower().find('admin')!=-1 ):
        new_name.append('Project manager')
    elif (i.lower().find('ресечер')!=-1 or i.lower().find('ресёчер')!=-1
        or i.lower().find('researcher')!=-1 or i.lower().find('ресерчер')!=-1):
        new_name.append('Ресечер')
    elif ((i.lower().find('админ')!=-1 or i.lower().find('administrator')!=-1)
        and (i.lower().find('системный')!=-1 or i.lower().find('system')!=-1)
        or (i.find('Cистемный')!=-1)):
        new_name.append('Системный администратор')
    elif i.lower().find('frontend')!=-1 or i.lower().find('front-end')!=-1:
        new_name.append('Frontend - developer')
    elif i.lower().find('backend')!=-1 or i.lower().find('back-end')!=-1:
        new_name.append('Backend - developer')
    elif ((i.lower().find('продукт')!=-1 or
           i.lower().find('product')!=-1 or i.lower().find('продакт')!=-1) and 
         (i.lower().find('менеджер')!=-1 or i.lower().find('manager')!=-1)):
        new_name.append('Product manager')
    elif ((i.lower().find('продаж')!=-1 or i.lower().find('sale')!=-1) and 
         (i.lower().find('менеджер')!=-1 or i.lower().find('manager')!=-1
          or i.lower().find('специалист')!=-1 or
          i.lower().find('specialist')!=-1 or 
          i.lower().find('консультант')!=-1 or
          i.lower().find('consultant')!=-1)):
        new_name.append('Sales manager')
    elif i.lower().find('юрис')!=-1:
        new_name.append('IT Юрист')
    elif i.lower().find('аналитик')!=-1 or i.lower().find('analyst')!=-1:
        new_name.append('IT Аналитик')
    elif i.lower().find('hr')!=-1 or i.lower().find('персонал')!=-1:
        new_name.append('HR manager')
    elif i.lower().find('developer')!=-1 or i.lower().find('разработчик')!=-1:
        if (i.lower().find('java')!=-1):
            new_name.append('Java developer')
        elif (i.lower().find('react')!=-1):
            new_name.append('React developer')
        elif ((i.lower().find('.net')!=-1) or (i.lower().find('c#')!=-1)):
            new_name.append('C# developer')
        else:
            new_name.append('IT Developer')
    elif i.lower().find('консультант')!=-1 or i.lower().find('consultant')!=-1:
        new_name.append('IT консультант')
    elif (i.lower().find('маркетолог')!=-1 or i.lower().find('smm')!=-1
                        or i.lower().find('маркетинг')!=-1):
        new_name.append('SMM')
    elif i.lower().find('директор')!=-1 or i.lower().find('director')!=-1:
        new_name.append('IT Директор')
    elif i.lower().find('инженер')!=-1 or i.lower().find('engineer')!=-1:
        new_name.append('IT Инженер')
    elif i.lower().find('специалист')!=-1 or i.lower().find('specialist')!=-1 :
        new_name.append('IT Специалист')
    elif i.lower().find('програм')!=-1:
        new_name.append('Программист')
    elif i.lower().find('manager')!=-1 or i.lower().find('менеджер')!=-1:
        new_name.append('IT manager')
    else:
        new_name.append(i)
print(f'Было уникальных вакансий {len(set(name))} стало {len(set(new_name))}')
df2['Vac_name'] = new_name
df2['Day_from_pars'] = [None]*len(df2)

""" Добавление ЗП вместо пустых и новый признак кол-во дней с парсинга """
for idx,row in df2.iterrows():
    if pd.isna(row['From_salary']):
        fr_salary = df2.loc[(df2['Vac_name'] == row['Vac_name']) & 
                            (df2['City'] == row['City'])]['From_salary'].mean()
        if not pd.isna(fr_salary):
            fr_salary = int(fr_salary)
        df2.at[idx, 'From_salary'] = fr_salary
    if pd.isna(row['To_salary']):
        to_salary = df2.loc[(df2['Vac_name'] == row['Vac_name']) & 
                            (df2['City'] == row['City'])]['To_salary'].mean()
        if not pd.isna(to_salary):
            to_salary = int(to_salary)
        df2.at[idx,'To_salary'] = to_salary
    delta = dt.date.today() - dt.datetime.strptime(row['Date'].split('T')[0],
                                                   "%Y-%m-%d").date()
    df2.at[idx,'Day_from_pars'] = int(str(delta).split()[0])

df2['Expirience'] = df2['Expirience'].fillna('Нет опыта')
df2['Employment'] = df2['Employment'].fillna('Любой тип')

df2.to_csv('after.csv')
# #列表增加单个元素
# a = [1,2,3]
# a.append(4)
# print(a)
#
# a = []
# for x in range(10):
#     if x % 2 == 0:
#         for y in range(10):
#             if y % 3 == 0:
#                 a.append([x,y])
# print(a)
#
# for each in "fishc":
#         print(each)
#
# sum = 0
# for i in range(1,11):#起始
#         print(i)
#         sum += i
#         i += 1
# print(sum)


# import pandas as pd
# import numpy as np
# import torch
# from torch.utils.data import DataLoader, TensorDataset
#
# def read_chord(chordDataPath, chord2play):
#     chord8BarData = []
#     chord4BarData = []
#     genre4BarData = []
#     genre8BarData = []
#     chordFile = pd.read_csv(chordDataPath)
#     for num, i in enumerate(chordFile.chord):
#         i = i.split(' ')
#         if len(i) == 4:
#             chord4BarData.append(i)
#             genre4BarData.append(chordFile.name[num][:2])
#         elif len(i) == 8:
#             i.insert(0, 'sos')
#             i.append('eos')
#             genre8BarData.append(chordFile.name[num][:2])
#             chord8BarData.append(i)
#     return chord4BarData, genre4BarData, chord8BarData, genre8BarData
# from music21 import*
# file = converter.parse("b97c529ab9ef783a849b896816001748.mid")
# components = []
# for element in file.recurse():
#     components.append(element)
#     song = {}
#     song['note'] = []
#     song['chord'] = []
#     song['key_sig'] = []
#     song['time_sig'] = []
# if isinstance(, note.Note):
#
# print(components)


# import os
# from music21 import*
# def get_notes():
#     filepath = 'data/lpd_5_cleansed'
#     files = os.listdir(filepath)



#
# from music21 import*
# def get_nodes():
#     stream = converter.parse('b97c529ab9ef783a849b896816001748.mid')
#
#     # 获取乐器
#     print('parts:')
#     parts = instrument.partitionByInstrument(stream)
#     # 输出所有乐器
#     for i in parts:
#         print(i)
#
#     # 音调信息
#     print('notes:')
#     note_list = []
#     notes = parts.parts[0].recurse()
#     for i in notes:
#         print(i)
#         if isinstance(i, note.Note):
#             # 音调
#             print(i.pitch)
#             note_list.append(str(i.pitch))
#         elif isinstance(i, chord.Chord):
#             print(i.normalOrder)
#             note_list.append('.'.join(
#                 map(str,
#                     i.normalOrder)
#             ))
#         print('---\n')
#
#     for i in note_list:
#         print(i)
#     return note_list
#
#
# def create_music(prediction):
#     # 音符之间是有间距的,每次加上一个值，表示间隔时间
#     # 间隔越小，节奏越快
#     offset = 0
#     output_notes = []
#
#     # 生成Note和Chord
#     for data in prediction:
#         if '.' in data or str(data).isdigit():
#             # 和弦
#             note_list = []
#             for i in data.split('.'):
#                 new_note = note.Note(int(i))
#                 new_note.storedInstrument = instrument.Piano()
#                 # new_note.storedInstrument = instrument.Guitar()
#                 note_list.append(new_note)
#             new_chord = chord.Chord(note_list)
#             new_chord.offset = offset
#             output_notes.append(new_chord)
#         else:
#             print('d:', data)
#             new_note = note.Note(data)
#             new_note.offset = offset
#             new_note.storedInstrument = instrument.Piano()
#             # new_note.storedInstrument = instrument.Guitar()
#             output_notes.append(new_note)
#             # 每次 迭代增加偏移，这样不会覆盖和迭代
#
#         offset += .5
#     # 创建流写入文件
#     mini_stream = stream.Stream(output_notes)
#     mini_stream.write('midi', fp='out4.mid')
#
#
# note_list = get_nodes()
# create_music(note_list)

#
# from music21 import*
# import music21 as ms21
# s=ms21.converter.parse('b97c529ab9ef783a849b896816001748.mid')
# C = []
# for note in s.flat.notesAndRests:
#     if isinstance(note, ms21.note.Rest):
#         note = "rest"
#         print(note)
#     elif isinstance(note,ms21.note.Note):
#         # note = note.pitch
#         # print(note)
#         print(note.pitch,note.pitch.midi,note.duration.quarterLength)
#     C.append(note)
# print(C)
#
# #
#
# def read_chord(chordDataPath, chord2play):
#     chord8BarData = []
#
#     genre8BarData = []
#     chordFile = pd.read_csv(chordDataPath)
#     for num, i in enumerate(chordFile.chord):
#         i = i.split(' ')
#          if len(i) == 8:
#             i.insert(0, 'CLS')
#             i.append('')
#             genre8BarData.append(chordFile.name[num][:2])
#             chord8BarData.append(i)
#     return chord8BarData, genre8BarData


#
# import os
# from music21 import converter, instrument, note, chord, stream
#
#
# # 读取训练数据的Notes
# #
# Notes = []
# stream = converter.parse('b97c529ab9ef783a849b896816001748.mid')
# instru = instrument.partitionByInstrument(stream)
# if instru:  # 如果有乐器部分，取第一个乐器部分
#     notes = instru.parts[0].recurse()
# else:  # 如果没有乐器部分，直接取note
#     notes = stream.flat.notes
# for element in notes:
#     # 如果是 Note 类型，取音调
#     # 如果是 Chord 类型，取音调的序号,存int类型比较容易处理
#     if isinstance(element, note.Note):
#         Notes.append(str(element.pitch))
#     elif isinstance(element, chord.Chord):
#         Notes.append('.'.join(str(n) for n in element.normalOrder))
#     with open('Note', 'a+') as f:
#         f.write(str(Notes))
# print(Notes)
# #

#
# from music21 import*
# Notes=[]
# stream = converter.parse('b97c529ab9ef783a849b896816001748.mid')
# notes = stream.flat.notes
# for element in notes:
#     # 如果是 Note 类型，取音调
#     # 如果是 Chord 类型，取音调的序号,存int类型比较容易处理
#     if isinstance(element, note.Note):
#         Notes.append(str(element.pitch))
#     elif isinstance(element, chord.Chord):
#         Notes.append('.'.join(str(n) for n in element.normalOrder))
# print(Notes)


# import music21 as ms21
# s=ms21.converter.parse("b97c529ab9ef783a849b896816001748.mid")
# NoteRest = []
# for note in s.flat.notesAndRests:
#     if isinstance(note, ms21.note.Rest):
#         # print(note.name)
#         NoteRest.append(note.name)
#     elif isinstance(note,ms21.note.Note):
#         # note = note.pitch
#         # print(note)
#         # print(note.pitch,note.pitch.midi,note.duration.quarterLength)
#         NoteRest.append(note.name)
# print(NoteRest)

# import music21 as ms21
# s=ms21.converter.parse("b97c529ab9ef783a849b896816001748.mid")
# Notes = []
# for note in s.flat.notesAndRests:
#     if isinstance(note, ms21.note.Rest):
#         Notes.append(note.name+'_'+str(note.duration.quarterLength))
#     elif isinstance(note,ms21.note.Note):
#         Notes.append(str(note.pitch)+"_"+str(note.duration.quarterLength))
# print(Notes)



# import music21 as ms21
# def get_notes:
#     s=ms21.converter.parse("b97c529ab9ef783a849b896816001748.mid")
#     Notes = []
#     for note in s.flat.notesAndRests:
#         if isinstance(note, ms21.note.Rest):
#             Notes.append(note.name+'_'+str(note.duration.quarterLength))
#         elif isinstance(note,ms21.note.Note):
#             Notes.append(str(note.pitch)+"_"+str(note.duration.quarterLength))
#     print(Notes)


# import os
# # 递归遍历目录
# def getAlldirInDiGui(path):
#     filesList = os.listdir(path)
#     print(filesList)
#     for fileName in filesList:
#         fileAbpath = os.path.join(path, fileName)
#         if os.path.isdir(fileAbpath):
#             print("目录：", fileName)
#             getAlldirInDiGui(fileAbpath)
#         else:
#             print("普通文件", fileName)
# # 传递参数的时候，注意需要写上（r）表明传递的是路径
# getAlldirInDiGui(r"C:\Users\Jiang\PycharmProjects\MIDI note\data")
#
import os
# 递归遍历目录
# def getAlldirInDiGui(path):
#     filesList = os.listdir(path)#os.listdir(path)中有一个参数，就是传入相应的路径，将会返回那个目录下的所有文件名。这个函数在遍历文件操作时很常用
#     print(filesList)
#     for fileName in filesList:
#         fileAbpath = os.path.join(path, fileName)#拼接所有的文，看他是文件还是文件夹
#         if os.path.isdir(fileAbpath):            #文件夹    判断是否是文件夹isdir，判断是否是文件就写isfles
#             print("目录：", fileName)
#             getAlldirInDiGui(fileAbpath)        #再次递归看看是不是下面还有其他路径
#         else:                                    #文件
#             print("普通文件", fileName)
# # 传递参数的时候，注意需要写上（r）表明传递的是路径
# getAlldirInDiGui(r"C:\Users\Jiang\PycharmProjects\MIDI note\data") #插入自己的路径

import music21 as ms21
import os
def ReadData(path):
    paths = os.listdir(path)
    for fileName in paths:
        Joint = os.path.join(path, fileName)#文件名和目录合成一个路径
        if os.path.isdir(Joint):
            ReadData(Joint)#进行第二次递归，读取目录下面的目录
        if os.path.isfile(Joint):
            if 'mid' in Joint:
                s=ms21.converter.parse(Joint)
                Notes = []
                for note in s.flat.notesAndRests:
                    if isinstance(note, ms21.note.Rest):
                        Notes.append(note.name+'_'+str(note.duration.quarterLength))
                    elif isinstance(note,ms21.note.Note):
                        Notes.append(str(note.pitch)+"_"+str(note.duration.quarterLength))
                #print(Notes)
ReadData(r"./data") #插入自己的路径
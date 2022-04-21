import glob
import nltk
import re
from nltk.corpus import wordnet
import os
import sys

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

###READ DATA###

def textdata(docs):
    data = []
    #txtfile = glob.glob(docs)
    #print(glob.glob(docs))
    #print(docs)
    for file in docs:
        #txtfile = glob.glob(file)
        op = open(file, 'r')
        temp = op.read()
        data.append(temp)
    return data

###REDACTING NAMES###

def redact_name(data):

    x=[]
    names1 = []
    names = []
    for i in nltk.sent_tokenize(data):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(i))):
            if hasattr(chunk, 'label'):
                   x.append((chunk.label(), ' '.join(c[0] for c in chunk)))
    for i in x:
        if i[0] == 'PERSON':
            red = '█' * len(i[1])
            names1.append(i[1])
            data = data.replace(i[1], red)
    for l in names1:
        if l not in names:
            names.append(l)
    return data,names

###REDACTING GENDER REVEALING WORDS###

def redact_gender(data):
    gender = ['him', 'her', 'father', 'mother', 'woman', 'man','men','women', 'boy', 'girl','he', 'she' , 'his', 'hers', 'male', 'female', 'Him', 'Her', 'Father', 'Mother', 'Woman', 'Man','Men','Women', 'Boy', 'Girl','He', 'She', 'His', 'Hers', 'Male', 'Female','HIM', 'HER', 'FATHER', 'MOTHER', 'MAN', 'WOMAN', 'MEN', 'WOMEN', 'FATHER', 'MOTHER','BOY', 'GIRL', 'HE', 'SHE','HIS', 'HERS', 'MALE', 'FEMALE','uncle','Uncle','UNCLE','aunt','Aunt','AUNT','husband','Husband','HUSBAND','wife','Wife','WIFE','boyfriend','Boyfriend','BOYFRIEND','girlfriend','Girlfriend','GIRLFRIEND','actor','actress','Actor','Actress','ACTOR','ACTRESS','waiter','waitress','Waiter','Waitress','WAITER','WAITRESS','brother','Brother','BROTHER','sister','Sister','SISTER','Gentleman','Lady','gentleman','lady','GENTLEMAN','LADY','Nephew','Niece','nephew','niece','NEPHEW','NIECE','grandfather','grandmother','Grandfather','Grandmother','GRANDFATHER','GRANDMOTHER','son','daughter','Son','Daughter','SON','DAUGHTER','sir','madam','Sir','Madam','SIR','MADAM','policeman','policewoman','salesman','saleswoman','Policeman','Policewoman','Salesman','Saleswoman','businessman','businesswoman','Englishman','Englishwoman','chairman','chairwoman','postman','postwoman','foreman','forewoman','businessman','businesswoman','Englishman','Englishwoman','chairman','chairwoman','postman','postwoman','foreman','forewoman','Businessman','Businesswoman','englishman','englishwoman','Chairman','Chairwoman','Postman','Postwoman','Foreman','Forewoman','Businessman','Businesswoman','englishman','englishwoman','Chairman','Chairwoman','Postman','Postwoman','Foreman','Forewoman','grandson','grandaughter','Grandson','Grandaughter',]
    token = nltk.word_tokenize(data)
    gender_words1 = []
    gender_words = []
    for i in token:
        for j in gender:
            if i == j:
                #red = '█' * len(i)
                gender_words1.append(i)
                data = data.replace(i, '█' * len(i))
    for l in gender_words1:
        if l not in gender_words:
            gender_words.append(l)
    return data,gender_words

###REDACTING DATES###

def redact_date(data):
    pattern='(\d{1,2}[\/|\-]\d{1,2}[\/|\-]\d{2,4})|(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|january|february|march|april|may|june|july|august|september|november|december|jan|feb|mar|apr|may|jun|jul|aug|sept|sep|nov|dec)[\s]((\d{1,2}[\,]\s\d{2,4})|(\d{1,2}\s\d{2,4}))|((?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|january|february|march|april|may|june|july|august|september|november|december|jan|feb|mar|apr|may|jun|jul|aug|sept|sep|nov|dec)[\s]((\d{1,2}(?:st|nd|rd|th)[\,]\s\d{2,4})|(\d{1,2}(?:st|nd|rd|th)\s\d{2,4}))|(\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|january|february|march|april|may|june|july|august|september|november|december|jan|feb|mar|apr|may|jun|jul|aug|sept|sep|nov|dec)\s\d{2,4}))'
    match = re.findall(pattern, data)
    date1 = []
    date = []
    for j in match:
        for k in j:
            red = '█' * len(k)
            date1.append(k)
            data = data.replace(k,red)
    for l in date1:
        if l not in date:
            date.append(l)
    return data,date

###REDACTING PHONE NUMBERS###

def redact_phnum(data):
    pattern=('((\+\d{0,2}\s)?\(?\d{3}\)?[\-|\s]?\(?\d{3}\)?[\-|\s]\(?\d{4}\)?)')
    match = re.findall(pattern, data)
    phone = []
    phone1 = []
    for j in match:
        for k in j:
            phone1.append(k)
            red = '█' * len(k)
            data = data.replace(k,red)
    for l in phone1:
        if l not in phone:
            phone.append(l)
    #print(phone)
    return data,phone

###REDACTING ADDRESSES###

def redact_address(data):
    pattern='(\d{1,4} [\w\s]{1,20}(?:Apartment|Apt|Avenue|Ave|Boulevard|Blvd|Building|Bldg|Center|Ctr|Circle|Cir|Court|Ct|Drive|Dr|East|E|Expressway|Expy|Extension|Ext|Fort|Ft|Freeway|Fwy|Height|Hts|Highway|Hwy|Island|Is|Junction|Jct|Lane|LnMount(ain)|MtNorth|N|Northeast|NE|Northwest|NW|Parkway|Pky|Place|Pl|Post Office|PO|Road|Rd|Rural Delivery|RD|Rural Route|RR|Saint|St|South|S|Southeast|SE|Southwest|SW|Spring|Spg|Springs|Spgs|Square(s)|Sq|Street|St|Suite|Ste|Terrace|Ter|Turnpike|Tpke|West|W))'
    match = re.findall(pattern, data)
    address = []
    address1 = []
    for j in match:
        for k in j:
            address1.append(k)
            red = '█' * len(k)
            data = data.replace(k, red)
    for l in address1:
        if l not in address:
            address.append(l)
    #print(address)
    return data,address

###CONCEPT###

def concept(word,data):
    synonyms = []
    synsentences1 = []
    synsentences = []
    #print(word)
    for x in word:
        for syn in wordnet.synsets(x):
            for l in syn.lemmas():
                synonyms.append(l.name())
        for i in nltk.sent_tokenize(data):
            for j in synonyms:
                #print(i,j)
                if j.lower() in i.lower():
                    data = data.replace(i,'█' * len(i))
                    synsentences1.append(i)
        for l in synsentences1:
            if l not in synsentences:
                synsentences.append(l)
    #print(synsentences)
    return data,synsentences

###STATS###

def stats(filePath,args,name,gender_words,date,phone,address,synsentences):
    name_count=0
    gender_count=0
    date_count=0
    phone_count=0
    address_count=0
    synsentence_count=0
    for i in name:
        if i != '':
            name_count+=1
    for i in gender_words:
        if i != '':
            gender_count+=1
    for i in date:
        if i != '':
            date_count+=1
    for i in phone:
        if i != '':
            phone_count+=1
    for i in address:
        if i != '':
            address_count+=1
    for i in synsentences:
        if i != '':
            synsentence_count+=1
    sp = filePath.split("\\")
    temp = sp[-1].split(".")
    temp[0] += '.redacted'
    if(args.stats == 'stderr'):
        file = open("stderr",mode="a")
        file.write("%s\nName_Count:%d\nGender_Word Count:%d\nDate Count:%d\nPhone Number Count:%d\nAddress Count:%d\nSentence Count:%d\n\n" % (temp[0], name_count, gender_count, date_count, phone_count, address_count, synsentence_count))
        #file.close()
        stderr_file = sys.stderr
        stderr_file.write('%s\nName_Count:%d\nGender_Word Count:%d\nDate Count:%d\nPhone Number Count:%d\nAddress Count:%d\nSentence Count:%d\n\n' % (temp[0], name_count, gender_count, date_count, phone_count, address_count, synsentence_count))
    elif(args.stats == 'stdout'):
        file = open("stdout", mode="a")
        file.write("%s\nName_Count:%d\nGender_Word Count:%d\nDate Count:%d\nPhone Number Count:%d\nAddress Count:%d\nSentence Count:%d\n\n" % (temp[0], name_count, gender_count, date_count, phone_count, address_count, synsentence_count))
        stdout_file = sys.stdout
        stdout_file.write('%s\nName_Count:%d\nGender_Word Count:%d\nDate Count:%d\nPhone Number Count:%d\nAddress Count:%d\nSentence Count:%d\n\n'%(temp[0],name_count,gender_count,date_count,phone_count,address_count,synsentence_count))



###OUTPUT FILES###
def output(filePath, data, outputPath):
    #print(len(file))
    #print(file)
    sp = filePath.split("\\")
    temp = sp[-1].split(".")
    temp[0] += '.redacted'
    #print(temp[0])
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    with open(os.path.join(outputPath,temp[0]),'w',encoding= 'utf-8') as file1:
        file1.write(data)
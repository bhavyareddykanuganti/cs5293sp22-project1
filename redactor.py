import argparse
from project1 import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, action='append', help="Path.", nargs='*')
    parser.add_argument("--names", required=False, action='store_true', help="Redact Names")
    parser.add_argument("--genders", required=False, action='store_true', help="Redact Gender")
    parser.add_argument("--dates", required=False, action='store_true', help="Redact Dates")
    parser.add_argument("--phones", required=False, action='store_true', help="Redact Phone number")
    parser.add_argument("--addresses", required=False, action='store_true', help="Redact Addresses")
    parser.add_argument("--concept", type=str, required=False, action='append', help="Redact Concept")
    parser.add_argument("--stats", type=str,required=True, help="stats")
    parser.add_argument("--output", type=str, required=True, help="stats")
    args = parser.parse_args()
    listData = []
    j=0
    # print(args.input[0])
    listData = main.textdata(args.input[0])
    #print(listData)
    #print(listData)
    for data in listData:
        if args.names:
            data,name=main.redact_name(data)
        if args.genders:
            data,gender_words=main.redact_gender(data)
        if args.dates:
            data,date=main.redact_date(data)
        if args.phones:
            data,phone=main.redact_phnum(data)
        if args.addresses:
            data,address=main.redact_address(data)
        if args.concept:
            for i in args.concept:
                data,synsentences = main.concept(i,data)
        if args.stats:
            main.stats(args,name,gender_words,date,phone,address,synsentences)

        if args.output:
            main.output(args.input[0][j], data, args.output)
            j+=1
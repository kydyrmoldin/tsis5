import re
def converted_date(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "1864-09-25"
print("YYY-MM-DD Format: ",dt1)
print("DD-MM-YYYY Format: ",converted_date(dt1))

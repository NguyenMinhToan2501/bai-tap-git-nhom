def tinh_thue_thu_nhap(thu_nhap):
    if thu_nhap <= 5000000:
        thue = thu_nhap * 0.05
    elif thu_nhap <= 10000000:
        thue = thu_nhap * 0.10
    elif thu_nhap <= 18000000:
        thue = thu_nhap * 0.15
    else:
        thue = thu_nhap * 0.20

    return thue

print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(10000000))

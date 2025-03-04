Dưới đây là một số ví dụ cụ thể để minh họa cách hoạt động của thuật toán:

### **Ví dụ 1: n = 12**
Ta kiểm tra xem **12 có thể được biểu diễn dưới dạng tổng của các lũy thừa của 3 không**.

#### **Bước 1: Chuyển 12 sang hệ cơ số 3**
- 12 chia 3 được 4, dư **0** → chữ số hàng đơn vị là **0**
- 4 chia 3 được 1, dư **1** → chữ số hàng tiếp theo là **1**
- 1 chia 3 được 0, dư **1** → chữ số hàng tiếp theo là **1**

**Kết quả trong hệ cơ số 3**: \( 12_{10} = 110_3 \)

- Chỉ chứa các chữ số **0** và **1** → **Thoả mãn điều kiện**.
- **Kết luận: 12 có thể được biểu diễn dưới dạng tổng của các lũy thừa của 3**.

✅ **Output: `True`**
---
### **Ví dụ 2: n = 91**
#### **Bước 1: Chuyển 91 sang hệ cơ số 3**
- 91 chia 3 được 30, dư **1**
- 30 chia 3 được 10, dư **0**
- 10 chia 3 được 3, dư **1**
- 3 chia 3 được 1, dư **0**
- 1 chia 3 được 0, dư **1**\
90  = 30.3 + 1.3<sup>0</sup> (n=30) \
    = 3<sup>1</sup>(3.10 + 0) + 1.3<sup>0</sup>                     (n=10) \
    = 3<sup>2</sup>(3.3 + 1) + 0.3<sup>1</sup> + 1.3<sup>0</sup>    (n=3) \
    = 3<sup>3</sup>(3.1 + 0) + 1.3<sup>2</sup> + 0.3<sup>2</sup> + 1.3<sup>0</sup> (n=1) \
    = 3<sup>4</sup> + 0.3<sup>3</sup> + 1.3<sup>2</sup> + 0.3<sup>2</sup> + 1.3<sup>0</sup> (n =0)

**Kết quả trong hệ cơ số 3**: \( 91_{10} = 10101_3 \)

- Chỉ chứa **0** và **1** → **Thoả mãn điều kiện**.
- **Kết luận: 91 có thể được biểu diễn dưới dạng tổng của các lũy thừa của 3**.

✅ **Output: `True`**
---
### **Ví dụ 3: n = 21**
#### **Bước 1: Chuyển 21 sang hệ cơ số 3**
- 21 chia 3 được 7, dư **0**
- 7 chia 3 được 2, dư **1**
- 2 chia 3 được 0, dư **2** ❌ (có số 2, không hợp lệ)

**Kết quả trong hệ cơ số 3**: \( 21_{10} = 210_3 \)

- Có chữ số **2**, nên **không thể biểu diễn dưới dạng tổng của các lũy thừa của 3**.

❌ **Output: `False`**
---

### **Tóm tắt kết quả**
| **n**  | **Biểu diễn hệ cơ số 3** | **Hợp lệ?** | **Output** |
|--------|------------------|---------|---------|
| 12     | 110            | ✅       | True    |
| 91     | 10101          | ✅       | True    |
| 21     | 210            | ❌       | False   |

Bạn có thể thử chạy code để kiểm tra với các số khác! 🚀

### **Tại sao sau khi chia lại lấy kết quả ngược từ dưới lên trong hệ cơ số? Có công thức nào không?**
---
### **1. Quy trình chuyển đổi số từ hệ thập phân (cơ số 10) sang hệ cơ số b (cơ số bất kỳ)**
Khi chuyển đổi một số từ hệ thập phân sang hệ cơ số **b**, chúng ta sử dụng **phép chia liên tiếp**:

#### **Quy tắc**
1. Chia số \( n \) cho cơ số \( b \) (ở đây là 3).
2. Lưu lại **phần dư** sau mỗi lần chia.
3. Lấy **phần nguyên** của phép chia để tiếp tục chia cho \( b \).
4. Lặp lại bước 1 - 3 cho đến khi phần nguyên bằng 0.
5. Đọc kết quả **ngược từ dưới lên**.

---
### **2. Tại sao phải lấy kết quả ngược lại từ dưới lên?**
Hãy xem xét cách biểu diễn một số trong hệ cơ số **b**:

- Một số \( n \) trong hệ cơ số \( b \) có thể được viết dưới dạng:
\[
n = d_k \cdot b^k + d_{k-1} \cdot b^{k-1} + ... + d_1 \cdot b^1 + d_0 \cdot b^0
\]
  - \( d_0 \) là phần dư đầu tiên (hàng đơn vị).
  - \( d_1 \) là phần dư thứ hai (hàng chục).
  - \( d_2 \) là phần dư thứ ba (hàng trăm), v.v.

💡 **Khi chúng ta thực hiện phép chia liên tiếp, phần dư đầu tiên chính là chữ số có trọng số thấp nhất (hàng đơn vị), phần dư thứ hai là hàng chục, và cứ thế. Vì vậy, để có số đúng, chúng ta phải đọc phần dư từ dưới lên!**

---
### **3. Ví dụ minh họa với n = 12 trong hệ cơ số 3**
Chuyển đổi \( 12 \) từ hệ thập phân sang hệ cơ số 3:

| Phép chia | Phần nguyên | Phần dư |
|-----------|------------|---------|
| \( 12 \div 3 \) | 4 | **0** |
| \( 4 \div 3 \)  | 1 | **1** |
| \( 1 \div 3 \)  | 0 | **1** |

**Kết quả đọc ngược lại từ dưới lên:**
\[
12_{10} = 110_3
\]
💡 Nếu đọc từ trên xuống, ta sẽ có **011**, nhưng điều này không đúng vì chữ số đầu tiên không còn giữ đúng trọng số.

---
### **4. Công thức tổng quát để chuyển số từ hệ 10 sang hệ b**
Nếu bạn muốn biểu diễn một số **n** trong hệ cơ số \( b \), ta có thể dùng công thức sau:

\[
n = d_0 + d_1 \cdot b + d_2 \cdot b^2 + d_3 \cdot b^3 + ... + d_k \cdot b^k
\]

Trong đó:
- **\( d_i = n \mod b \)** (phần dư khi chia cho \( b \)).
- **\( n = n // b \)** (lấy phần nguyên để tiếp tục chia).
- **Lặp lại cho đến khi \( n = 0 \)**.
- **Đọc dãy số từ dưới lên để có kết quả chính xác**.

---
### **5. Code Python để chuyển đổi số từ hệ 10 sang hệ b**
Dưới đây là đoạn code Python giúp bạn chuyển đổi một số từ hệ thập phân sang một hệ cơ số bất kỳ \( b \):

```python
def decimal_to_base(n, b):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        remainder = n % b  # Lấy phần dư
        result = str(remainder) + result  # Thêm phần dư vào đầu chuỗi
        n //= b  # Chia lấy phần nguyên
    
    return result

# Ví dụ
print(decimal_to_base(12, 3))  # Output: 110
print(decimal_to_base(91, 3))  # Output: 10101
print(decimal_to_base(21, 3))  # Output: 210
```

---
### **6. Kết luận**
- Khi chuyển từ hệ thập phân sang hệ **b**, ta chia số đó nhiều lần cho **b** và lấy phần dư.
- Phần dư đầu tiên chính là **chữ số cuối cùng** trong hệ cơ số mới, vì vậy phải đọc **ngược lại từ dưới lên**.
- Công thức tổng quát:
  \[
  n = d_k \cdot b^k + d_{k-1} \cdot b^{k-1} + ... + d_1 \cdot b^1 + d_0 \cdot b^0
  \]
- Cách thực hiện trong Python có thể dùng vòng lặp chia liên tiếp.

📌 **Hy vọng bạn đã hiểu rõ hơn về cách hoạt động của phép chuyển đổi hệ cơ số!** 🚀
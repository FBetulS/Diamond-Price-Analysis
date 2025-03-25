# Diamond Price Analysis

## 🔗 Kaynaklar
- Örnek Çözüm ve Veri Seti: [Diamond Price Prediction with Machine Learning](https://thecleverprogrammer.com/2021/01/20/diamond-price-prediction-with-machine-learning/#google_vignette)
- Hugging Face : [Diamond Price Prediction Space](https://huggingface.co/spaces/btulftma/diamond-price)

## 📖 Giriş
Bu projenin hedefi, elmasların fiyatlarını tahmin etmek için veri bilimi ve analitik yöntemler kullanarak, elmasların çeşitli özelliklerine dayalı bir analiz yapmaktır. Kullanıcıların elmas fiyatlarını tahmin etmelerine yardımcı olacak bir model geliştirilmiştir.

## 📊 Veri Seti
Proje, 53,940 pırlanta hakkında bilgi içeren bir veri seti kullanmaktadır. Bu veri seti, 11 özellikten oluşmaktadır:
- **carat**: Pırlantanın ağırlığı, karat cinsinden.
- **cut**: Kesim kalitesi (örn. Ideal, Premium, Good).
- **color**: Pırlanta rengi (örn. D, E, J).
- **clarity**: Pırlantanın berraklık derecesi (örn. SI1, VS2).
- **depth**: Pırlantanın toplam derinlik yüzdesi.
- **table**: Pırlantanın masa yüzdesi.
- **price**: Pırlantanın fiyatı (ABD doları cinsinden).
- **x, y, z**: Pırlantanın boyutları (milimetre cinsinden).

### Berraklık Dereceleri Özeti
- **IF**: İçsel kusursuz; en yüksek berraklık.
- **VVS1**: Çok çok hafif dahil; zor görünür.
- **VS1**: Çok hafif dahil; zor görünür.
- **SI1**: Hafifçe dahil; zor görünür.
- **I1**: Gözle görülebilen büyük kusurlar; en düşük berraklık.

### Kesim Kalitesi Özeti
- **Ideal**: En yüksek kesim kalitesi.
- **Premium**: Yüksek kesim kalitesi.
- **Very Good**: İyi kesim kalitesi.
- **Good**: Orta düzey kesim kalitesi.
- **Fair**: En düşük kesim kalitesi.

## 🔍 Veri Analizi
Veri analizi aşamasında, pırlanta fiyatları ile diğer özellikler arasındaki korelasyon incelenmiştir. Örneğin, pırlanta ağırlığı ve hacmi fiyat ile güçlü bir korelasyon göstermektedir.

## 📈 Model Geliştirme
Farklı regresyon modelleri kullanılarak elmas fiyatlarının tahmin edilmesi amaçlanmıştır. Kullanılan başlıca modeller:
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **XGB Regressor**

Sonuçlar, XGB Regressor modelinin en yüksek doğruluk oranına sahip olduğunu göstermiştir.

### Sonuçlar
Model performansına bakıldığında, XGB Regressor (R-Squared = 0.981, RMSE = 549.17, MAE = 278.02) fiyat tahmini konusunda en güçlü model olarak öne çıkmaktadır.

## 💾 Model Kaydetme
En iyi model, `joblib` kullanılarak kaydedilmiştir.

## 📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

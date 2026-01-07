#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_expected_loss(probability, loss_amount):
    """
    Olasılık ve hasar miktarını alıp beklenen hasarı (risk primini) hesaplar.
    """
    expected_loss = probability * loss_amount
    return expected_loss

# Test edelim
olasilik = 0.10
hasar = 50000

sonuc = calculate_expected_loss(olasilik, hasar)
print(f"Beklenen Hasar (Risk): {sonuc} TL")


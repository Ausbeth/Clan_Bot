import discord
import os
from PIL import Image
from io import BytesIO
 

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


# Define the array of characters with assigned images
characters = {
    "Naruto": "GWbfLO5.png",
    "Sakura": "RhRtWaN.png",
    "Sasuke": "rWFqUwo.png",
    "Kiba": "4t9jJKw.png",
    "Shino": "RPIy4uO.png",
    "Hinata": "M58mwWp.png",
    "Shikamaru": "hr2kmUW.png",
    "Chouji": "cQKRlLk.png",
    "Ino": "K6WiIiF.png",
    "Lee": "tj9WREU.png",
    "TenTen": "fOzZERz.png",
    "Neji": "WNlFpMv.png",
    "Gaara": "4UljVAm.png",
    "Kankuro": "0FeEpIl.png",
    "Temari": "z5lW2jl.png",
    "Dosu": "L1sLdhl.png",
    "Kin": "Twd1eBj.png",
    "Zaku": "q4JzJKQ.png",
    "Young Kakashi": "U3Ivdp4.png",
    "Obito": "JbvGcwk.png",
    "Rin": "nVN2Va7.png",
    "Hanabi": "UgOE7eF.png",
    "Teuchi": "za8CSxN.png",
    "Young Minato": "5269EwX.png",
    "Young Kushina": "mMIK77W.png" ,
    "Mahiru": "RRumWfF.png" ,
    "Taiseki": "kTyTku1.png",
    "Kakkou": "pcGTYHq.png",
    "Anbu Kakashi": "mVhfyCq.png",
    "Tenzou": "IpVJDCV.png",
    "Anbu Itachi": "jmjQZ5t.png",
    "Corrupted Obito": "2oic3VD.png",
    "Iruka": "snz8zD4.png",
    "Mizuki": "NZS59L7.png",
    "Demon Brothers": "ekQ5QZR.png",
    "Zori and Waraji": "EIsg1h5.png",
    "Haku": "1iuyTS5.png",
    "Zabuza": "8OoPNPv.png",
    "Oboro": "q3FfmTs.png",
    "Shigure": "n72OXiY.png",
    "Shiore Orochimaru": "SSVCMic.png",
    "Yoroi": "U0Ziv1r.png",
    "Misumi": "0eoJQlb.png",
    "Jiroubou": "inrbCC3.png",
    "Kidoumaru": "zW32e4B.png",
    "Tayuya": "hAshWTO.png" ,
    "Sakon": "hCiXr6K.png" ,
    "Kimimaro": "oC5Q8hX.png",
    "Anko": "MXeuah1.png",
    "Shizune": "V7UX5TB.png",
    "Hayate": "ZJCc6tw.png",
    "Kakashi": "Ult0SsC.png",
    "Kurenai": "0KdXrps.png",
    "Asuma": "Hk2DwUA.png",
    "Gai": "Kimqis6.png",
    "Kushina": "g6c3TXZ.png",
    "Minato": "AHaiUaf.png",
    "Yashamaru": "0DHwO6g.png",
    "Baki": "pjjdWz8.png",
    "Kabuto": "uBA8Srn.png",
    "Tsunade": "N6D7kcS.png",
    "Jiraiya": "7nC6nSS.png",
    "Orochimaru": "xqD8hwf.png",
    "Edo Tensei Hashirama": "XKnOdST.png",
    "Edo Tensei Tobirama": "D1qp4Pu.png",
    "Hiruzen": "OVXPrec.png",
    "Hokage Minato": "n9jdzjM.png" ,
    "Masked Man": "cMdCFoQ.png" ,
    "Kyuubi Naruto": "hOCQuU9.png",
    "Cursed Seal Lv1 Sasuke": "9KgJEk8.png",
    "Cursed Seal Sasuke": "h62tBoY.png",
    "Butterfly Chouji": "UoRyA7v.png",
    "Druken Lee": "gLFtzf2.png",
    "Shukaku Gaara": "tNBIXfI.png",
    "Rehabilitated Gaara": "bF8DLyH.png",
    "Kisame": "tij8Nxm.png",
    "Itachi": "KOjV2Qf.png",
    "Doto": "1FYSYQg.png",
    "Temujin": "mChHc8t.png",
    "Naruto S": "K0gVNTu.png",
    "Sakura S": "dMRqjIP.png",
    "Sai": "DF5JgYg.png",
    "Kiba S": "O9pHpzM.png",
    "Shino S": "gpdFquj.png",
    "Hinata S": "M5GPPe5.png",
    "Shikamaru S": "tXroLB1.png",
    "Chouji S": "EU9MrUy.png",
    "Ino S": "0if0azl.png" ,
    "Lee S": "n9iULjL.png" ,
    "TenTen S": "KIlLyZW.png",
    "Neji S": "GdN4ylI.png",
    "Konohamaru": "RlmD0ZX.png",
    "Kakashi S": "QkC8m4x.png",
    "Yamato": "bqEBFnr.png",
    "Gai S": "cyxLCgn.png",
    "Asuma S": "1tYcnqE.png",
    "Ebisu": "oSFOBai.png",
    "Shizune S": "yo2xIsS.png",
    "Aoba": "gLzpBBJ.png",
    "Anko S": "4a6vVNE.png",
    "Izumo and Kotetsu": "UeK3hM5.png",
    "Genma": "QRSfp0V.png",
    "Raidou": "a65zmFA.png",
    "Hana": "TvKtEyv.png",
    "Tsume": "8lnIvxN.png",
    "Shibi": "ZmnLC4Z.png",
    "Hiashi": "4lFfFHH.png",
    "Shikaku": "e1ztwos.png",
    "Chouza": "9of6TFk.png" ,
    "Inoichi": "gDtyEBF.png" ,
    "Ibiki": "JTJtZ7N.png",
    "Zaji": "981BrzK.png",
    "Ensui": "jcP13pK.png",
    "Muta": "zT5Vqca.png",
    "Iou": "5ngsQvi.png",
    "Yugao": "YtzmKXs.png",
    "Anbu Captain Squad": "kjZgoI3.png",
    "Torune": "Oz9LkWJ.png",
    "Fu": "IQtApr1.png",
    "Danzo": "s4QhMk8.png",
    "Tsunade S": "aic7tTA.png",
    "Senju Hashirama": "9Tg3WJz.png",
    "Senju Tobirama": "jqROr77.png",
    "Izuna": "bD7rvqE.png",
    "Madara": "FZuXply.png",
    "Shisui": "KGB2MWd.png",
    "Fugaku": "EXmcmAJ.png",
    "Naori": "m9SG8c9.png" ,
    "Dai": "eOYxXnJ.png",
    "Maki": "C7IPOIz.png",
    "Chiyo": "PZss6Oj.png",
    "Kankuro S": "Mq5ImWG.png",
    "Temari S": "hTu7W3f.png" ,
    "Kazekage Gaara": "iX1Omvr.png",
    "Ruka": "oiUJdrg.png",
    "Ao": "3deqvVg.png",
    "Chojuro": "U0wNg3q.png",
    "Mei": "26ZIAsU.png",
    "Akatsuchi": "wEhxeHB.png",
    "Kurotsuchi": "eXgUndV.png",
    "Ittan": "BXMTWdS.png",
    "Monga": "E5JI0Eh.png",
    "Kitsuchi": "TELbKxD.png",
    "Ohnoki": "5QVHrrV.png",
    "Sabu": "w4pqVhd.png",
    "Atsui": "hhEe2LT.png",
    "Karui": "97T2q4u.png",
    "Omoi": "NEbMTYF.png",
    "Samui": "uGriCDH.png" ,
    "Shee": "qts4SUz.png",
    "Darui": "IdBgPru.png",
    "Motoi": "FMg3BXv.png",
    "Dodai": "Jctb2Ca.png",
    "Mabui": "9nmiOnv.png" ,
    "Ay": "DLbjK3P.png",
    "Samurai Troops": "gMFkhdX.png",
    "Mifune": "l4Bb20f.png",
    "Hanzo of the Salamander": "JziBRHp.png",
    "Yugito": "f4YNddh.png",
    "Yagura": "lbMxy1E.png",
    "Roshi": "40BNONy.png",
    "Han": "slV2CLk.png",
    "Utakata": "R5gV1oD.png",
    "Fuu": "juSOHlE.png",
    "Killer Bee": "lixEXGZ.png",
    "Hachibi Bee": "x9x8GTm.png",
    "Suigetsu": "0ywjhZU.png",
    "Karin": "8uI3t9j.png",
    "Juugo": "fEzPQes.png",
    "Cursed Seal Juugo": "nV1CNGa.png" ,
    "Sasuke S": "u1tsCIN.png",
    "Cursed Seal Sasuke S": "m7UFgHt.png",
    "Mangekyou Sasuke": "BttWMmW.png",
    "Kabuto S": "bFuiE0L.png",
    "Orochimaru S": "I8WePdy.png" ,
    "White Snake Orochimaru": "4BRFkgg.png",
    "Fukasaku and Shima": "swvghiS.png",
    "Jiraiya S": "i5t9nfP.png",
    "Sennin Jiraiya": "iFqkAy7.png",
    "Sennin Naruto": "5IZS5CT.png",
    "Three Tails Kyuubi Naruto": "AsHwEhI.png",
    "Four Tails Kyuubi Naruto": "JwO8ylH.png",
    "Six Tails Kyuubi Naruto": "y7ff165.png",
    "Sora": "shkCMFV.png",
    "Chiriku": "aVx7pe6.png",
    "Guren": "fZ7i2pS.png",
    "Mecha Naruto": "p9lIrNK.png",
    "Satori": "Ad8yAl1.png",
    "Kisame Body Double": "b8dXNsW.png",
    "Itachi Body Double": "E7mAnm3.png",
    "Deidara": "Wgw4vZ4.png" ,
    "Hiruko Sasori": "TA5UaWE.png",
    "Sasori of the Red Sand": "EJRSPPq.png",
    "Puppet Sasori": "huF0Rd7.png",
    "Hidan": "1IgggyO.png",
    "Kakuzu": "8qMcAcn.png" ,
    "True Form Kakuzu": "yB0bCwo.png",
    "Kisame S": "H3eQN6E.png",
    "Itachi S": "Q5wnn3P.png",
    "Juuzou": "kf95fBW.png",
    "Akatsuki Orochimaru": "jzYYUEn.png",
    "Yahiko": "wa29ltI.png",
    "Konan": "ineMRZS.png",
    "Konan of the Rain": "Xhy87GR.png",
    "Nagato": "82icmwP.png",
    "Animal Path Pain": "UtBlsf3.png",
    "Female Animal Path Pain": "Ix9Kn9d.png",
    "Asura Path Pain": "HMD3sOt.png",
    "Human Path Pain": "2rkX0MQ.png",
    "Naraka Path Pain": "Wo8IlaO.png",
    "Preta Path Pain": "yX3zERU.png",
    "Deva Path Pain": "Q4gijWK.png" ,
    "White Zetsu": "pPduqCS.png",
    "Black Zetsu": "ManYHFH.png",
    "Tobi": "4noHYjv.png",
    "Akatsuki Sasuke": "VcAy2NW.png",
    "Edo Tensei Asuma": "ErnKYjN.png" ,
    "Edo Tensei Dan": "xSMP32t.png",
    "Edo Tensei Hizashi": "sW5fI0H.png",
    "Edo Tensei Shin": "q0z36Z3.png",
    "Edo Tensei Hayate": "lC5euir.png",
    "Edo Tensei Torune": "Cz2jrtA.jpg",
    "Edo Tensei Ginkaku": "nwwvvIF.png",
    "Edo Tensei Kinkaku": "3MoBPgs.png",
    "Edo Tensei Kyuubi Kinkaku": "TqeWOmG.png",
    "Edo Tensei Pakura": "nloSvaW.png",
    "Edo Tensei Gari": "tEcCwg1.png",
    "Edo Tensei Fukai": "LfsCPMM.png",
    "Edo Tensei Hanzo": "9lql2xG.png",
    "Edo Tensei Chiyo": "n2Cfstb.png",
    "Edo Tensei Chukichi": "ag276N6.png",
    "Edo Tensei Toroi": "7J9wYsv.png",
    "Edo Tensei Chen": "15SniDV.png" ,
    "Edo Tensei Yota": "NfB0w2l.png",
    "Edo Tensei Tatewaki": "xm1Eah1.png",
    "Edo Tensei Jiroubou": "P3mTmLW.png",
    "Edo Tensei Kidoumaru": "hRbJSzJ.png",
    "Edo Tensei Tayuya": "SS2wkla.png" ,
    "Edo Tensei Sakon": "vclnE2J.png",
    "Edo Tensei Kimimaro": "6o35d3m.png",
    "Edo Tensei Haku": "a2dIvyp.png",
    "Edo Tensei Zabuza": "CCycwVM.png",
    "Edo Tensei Jinin": "RKXaoJc.png",
    "Edo Tensei Ameyuri": "eZ4dzrx.png",
    "Edo Tensei Kushimaru": "Qx4mDpy.png",
    "Edo Tensei Jinpachi": "XDOsNLk.png",
    "Edo Tensei Fuguki": "iSYjFja.png",
    "Edo Tensei Mangetsu": "LQRbVNP.png",
    "Edo Tensei Sandaime Kazekage": "wptmeKm.png",
    "Edo Tensei Rasa": "GB3P2GA.png",
    "Edo Tensei Ay": "AUi76qz.png",
    "Edo Tensei Muu": "WH24lum.png",
    "Edo Tensei Gengetsu": "4oRzTmW.png",
    "Edo Tensei Deidara": "2V9LjGD.png" ,
    "Edo Tensei Sasori": "d7SbQ1k.png",
    "Edo Tensei Kakuzu": "ACX6XqD.png",
    "Edo Tensei Nagato": "kFz3dZw.png",
    "Edo Tensei Itachi": "Y8v3n9J.png",
    "Edo Tensei Yugito": "q1TyZhL.png" ,
    "Edo Tensei Yagura": "eCDyjFP.png",
    "Edo Tensei Roshi": "dTTLR0r.png",
    "Edo Tensei Han": "rQfxg6B.png",
    "Edo Tensei Utakata": "iALaJqT.png",
    "Edo Tensei Fuu": "DH0Z4j2.png",
    "Edo Tensei Hashirama S": "9psEXmU.png",
    "Edo Tensei Tobirama S": "U8ZRvhV.png",
    "Edo Tensei Hiruzen": "FgiaCgt.png",
    "Edo Tensei Minato": "TIFzXNj.png",
    "Edo Tensei Kyuubi Minato": "UoCLjSZ.png",
    "Edo Tensei Madara": "DobK6fQ.png",
    "Kyuubi Naruto S": "qox1yAW.png",
    "Sennin Kyuubi Naruto": "sdg7LFY.png",
    "Eternal Mangekyou Sasuke": "td40kdt.png",
    "Byakugou Sakura": "s9erOIM.png",
    "Emotional Energy Sai": "JYozDo0.png" ,
    "Commander Kakashi": "D2fGUn8.png",
    "Butterfly Chouji S": "VboBkPv.png",
    "Commander Gaara": "MbulIVW.png",
    "Captain Kankuro": "RPEplnc.png",
    "Captain Temari": "wJSrcZP.png" ,
    "Samehada Bee": "LWiUL3r.png",
    "White Snake Kabuto": "51WBgu5.png",
    "Sennin Kabuto": "HPQSKPL.png",
    "Rinnegan Tobi": "ufdvAST.png",
    "Obito S": "qPITEYa.png",
    "Guruguru": "JkCj9NF.png",
    "Regenerated Madara": "QnDsbQg.png",
    "Juubi": "3klqUBL.png",
    "Rikudou Obito": "L2GOZvC.png",
    "Rikudou Madara": "Udm5r7Z.png",
    "Eighth Gate Gai": "qqCeniP.png",
    "Rikudou Naruto": "LJ7YI9u.png",
    "Rinnegan Sasuke": "wbcBk1q.png",
    "Dual Mangekyou Kakashi": "R2JSlbX.png",
    "Rehabilitated Obito": "RpPYC1W.png",
    "Kaguya": "I5jpfiZ.png" ,
    "Hamura": "UW1m8nt.png",
    "Hagoromo": "6d546Ls.png",
    "Ashura": "6IUqao2.png",
    "Indra": "K1elLzg.png",
    "Toneri": "yJhd1e8.png" ,
    "Boruto": "2JkCZea.png",
    "Sarada": "qKbMMx8.png",
    "Mitsuki": "Oplj5sY.png",
    "Shikadai": "vr1sOoo.png",
    "ChouChou": "ZPTgA4X.png",
    "Inojin": "iMgasXr.png",
    "Metal Lee": "0YXrmLO.png",
    "Iwabee": "93fSq3J.png",
    "Denki": "6ifQDJz.png",
    "Sumire": "DahVj7D.png",
    "Wasabi": "ViRRV51.png",
    "Namida": "Tzq9Ejw.png",
    "Tsubaki": "RId4yhS.png",
    "Shinki": "HNwlRoJ.png",
    "Araya": "47LZ7GX.png",
    "Yodo": "Aa3SDbh.png" ,
    "Yurui": "xESdZy4.png",
    "Tarui": "oVqBuQP.png",
    "Toroi": "V7TGxXw.png",
    "Himawari": "QNo1Gxm.png",
    "Kawaki": "Tmb0yV5.png" ,
    "Mirai": "JGABAvK.jpg",
    "Konohamaru B": "M7ZDcLp.png",
    "Udon": "MJbEN5q.jpg",
    "Moegi": "YxPdUjL.jpg",
    "Hanabi B": "Rw0QHi6.jpg",
    "Hokage Naruto": "henGTdS.png",
    "Sasuke B": "9c2ixtX.png",
    "Uchiha Sakura": "vyvPVmY.jpg",
    "Kakashi B": "qBXWn21.jpg",
    "Shino B": "rZesZWF.jpg",
    "Kazekage Gaara B": "4Xjmrdd.png",
    "Kankuro B": "Ayg4wZX.jpg",
    "Nara Temari": "5Rl0AlN.jpg",
    "Mizukage Chojuro": "jvnKA0k.png",
    "Tsuchikage Kurotsuchi": "CYMsPbw.png",
    "Raikage Darui": "4FGb0X9.png",
    "Shin Clone": "XdjITgp.png",
    "Uchiha Shin": "e1w8lda.png",
    "Urashiki": "6GyuDYd.png",
    "Chakra Fruit Urashiki": "VzAaph6.png" ,
    "Kinshiki": "gG8MzIn.png",
    "Momoshiki": "4CnPkj4.png",
    "Chakra Fruit Momoshiki": "mkjNSo9.png",
    "Karma Boruto": "LyqYoKo.png",
    "Ootsutsuki Boruto": "AjzKvdL.png" ,
    "Karma Kawaki": "HwHcfGd.png",
    "Ao B": "Khe4if9.png",
    "Garou": "IlCCeU0.png",
    "Deepa": "nhxcNzl.jpg",
    "Delta": "1NpIXya.png",
    "Kashin Koji": "yriIO6Y.png",
    "Sennin Koji": "WzIIOtF.png",
    "Boro": "CJ7xOzu.png",
    "Sanzu Amado": "SxF7tbl.png",
    "Jigen": "vLj69Qc.png",
    "Isshiki": "IDjAsCF.png",
    "Baryon Naruto": "hDmVtG4.png"
}


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

  # Split the message content into words and filter out any empty words
    words = filter(lambda w: w.strip() != "", message.content.split(" - "))

    # Check if each word is the name of Character
    character_names = []
    for word in words:
        if word.strip() in characters:
            character_names.append(word.strip())
            
    # If there are no characters in the message, return
    if not character_names:
        return

    # Create a list of characters that were not mentioned in the message
    other_character_names = [element for element in characters if element not in character_names]

    # Limit the number of columns in the combined image to a maximum of 21
    num_columns = min(len(other_character_names), 21)

    # Calculate the number of rows needed to fit all the other characters
    num_rows = (len(other_character_names) - 1) // num_columns + 1

    # Combine the images of the other characters into a single image
    combined_image = None
    for element_name in other_character_names:
        # Get the file path for the image for the element
        file_path = os.path.join("C:/Users/Ausbeth/AppData/Local/Programs/Python/Python310/Clan_Bot/naruto-arena_net", characters[element_name])

        # Open the image using the Pillow library
        image = Image.open(file_path)

        # Add a 5px border around the image
        from PIL import ImageOps
        image = ImageOps.expand(image, border = 5, fill = "black")

        # Resize the image to a fixed size (optional)
        image = image.resize((150, 150))

        # If this is the first character, create the combined image with the same size
        if not combined_image:
            combined_image = Image.new("RGB", ((image.width + 2) * num_columns, (image.height + 2) * num_rows))

        # Calculate the row and column index for this element
        index = other_character_names.index(element_name)
        row = index // num_columns
        col = index % num_columns

        # If we've reached the maximum number of columns, start adding characters from the next row
        if col == num_columns:
            row += 1
            col = 0

        # Paste the element's image onto the combined image
        combined_image.paste(image, ((col * (image.width + 2)) + 1, (row * (image.height + 2)) + 1))

    # Save the combined image to a bytes buffer
    buffer = BytesIO()
    combined_image.save(buffer, "jpeg")
    buffer.seek(0)

    # Send a message with the combined image
    await message.channel.send(f"Here are the characters that are open in your war:", file=discord.File(buffer, filename="open_characters.jpg"))
 
client.run('MTA3OTY4MTEzNzgyOTQ5NDc5NQ.G0E-G1.PBaG2qPF8_b370O1S47uK8KYAijxpp-qp5c9Qg')
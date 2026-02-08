---
title: "Research"
description: "神谷研究室の研究領域"
featured_image: ""
layout: "research"
---

神谷研究室では、脳がどのように情報を表現・処理するかを研究し、脳活動から心の内容を解読・可視化する技術を開発しています。神経科学とAIを橋渡しし、4つの研究領域を展開しています。

## ブレインデコーディング {#brain-decoding}

ブレインデコーディング（脳情報デコーディング）は、fMRIで計測した脳活動パターンから、知覚・心象・夢の内容を機械学習によって解読する技術です。脳活動パターンは心の状態をコード化している「暗号」とみなすことができ、そのコードを解読（デコード）することが脳から心を読むことにつながります。神谷研究室は2000年代半ばからこの分野を開拓し、解読可能な心的内容の範囲を段階的に拡大してきました。

2005年、[Kamitani and Tong](https://doi.org/10.1038/nn1444)は、視覚野のfMRI信号から視覚的方位を解読できること、さらに両眼視野闘争時に主観的に知覚された方位も解読できることを示しました。集団レベルの脳活動から精緻な知覚情報にアクセスできることを実証した研究です（*Nature Neuroscience*）。続いて、[宮脇ら（2008）](https://doi.org/10.1016/j.neuron.2008.11.004)は、脳活動から見ている画像そのものを画像として再構成すること（視覚像再構成）に初めて成功しました。複数の空間スケールの局所画像デコーダの出力を組み合わせることにより、任意の視覚画像を脳活動から再構成する手法を確立しました（*Neuron*）。

2013年には、[堀川ら](https://doi.org/10.1126/science.1234330)が、睡眠中のヒトの脳活動から夢の視覚的内容を解読することに成功しました。本来なら本人にしか知りえない主観的な心的体験を、脳活動から客観的に読み出せることを示した画期的な研究です（*Science*）。

深層ニューラルネットワーク（DNN）の導入は、大きな飛躍をもたらしました。[Shenら（2019）](https://doi.org/10.1371/journal.pcbi.1006633)は、DNNの階層的特徴量を中間表現として用いることで、知覚画像・想起画像の両方を脳活動から高品質に再構成する「深層画像再構成」を開発しました（*PLoS Computational Biology*）。この枠組みはさらに、[Chengら（2023）](https://doi.org/10.1126/sciadv.adj3906)による視覚的錯覚体験の再構成（*Science Advances*）、[Parkら（2025）](https://doi.org/10.1371/journal.pbio.3003293)による聴覚脳活動からの自然音の再構成（*PLOS Biology*）へと拡張されました。

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/jsp1KaM-avU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

現在の枠組みでは、ブレインデコーディングを「翻訳–生成パイプライン」として捉えています。「翻訳器（translator）」が脳活動をDNNや生成モデルの潜在表現空間に変換し、「生成器（generator）」がその潜在表現から画像・音声などの出力を生成します。この枠組みは[Kamitani, Tanaka & Shirakawa（2025）](https://doi.org/10.1146/annurev-vision-110423-023616)（*Annual Review of Vision Science*）で総括されています。

### 代表論文

- **[Kamitani & Tong (2005)](https://doi.org/10.1038/nn1444)** Decoding the visual and subjective contents of the human brain. *Nature Neuroscience*, 8(5), 679–685
- **[Miyawaki et al. (2008)](https://doi.org/10.1016/j.neuron.2008.11.004)** Visual image reconstruction from human brain activity. *Neuron*, 60(5), 915–929
- **[Horikawa et al. (2013)](https://doi.org/10.1126/science.1234330)** Neural decoding of visual imagery during sleep. *Science*, 340(6132), 639–642
- **[Shen et al. (2019)](https://doi.org/10.1371/journal.pcbi.1006633)** Deep image reconstruction from human brain activity. *PLoS Computational Biology*, 15(1), e1006633
- **[Cheng et al. (2023)](https://doi.org/10.1126/sciadv.adj3906)** Reconstructing visual illusory experiences from human brain activity. *Science Advances*, 9, eadj3906
- **[Park et al. (2025)](https://doi.org/10.1371/journal.pbio.3003293)** Natural sounds can be reconstructed from human neuroimaging data. *PLOS Biology*, 23(7), e3003293
- **[Kamitani, Tanaka & Shirakawa (2025)](https://doi.org/10.1146/annurev-vision-110423-023616)** Visual image reconstruction from brain activity via latent representation. *Annual Review of Vision Science*, 11, 611–634

---

## NeuroAI {#neuroai}

「脳とAIは似ているか」——この古くからある問いは、近年のAIの急速な進展によって新たな局面を迎えています。現代の深層学習におけるブレークスルーは、脳を直接的に模倣するようには設計されていないにもかかわらず、工学的な最適化の結果として脳活動との類似性（アラインメント）を示すことが分かってきました。この現象を探求する学際領域がNeuroAIです。

神谷研究室はNeuroAIの方法論的基盤に貢献してきました。[Horikawa and Kamitani（2017）](https://doi.org/10.1038/ncomms15037)は、DNNの階層的視覚特徴量をヒト脳活動からデコードできること、また階層が上がるにつれ解読可能な脳部位が高次領野へシフトすることを示し、脳の視覚的階層とDNN層構造の間の対応関係を発見しました（*Nature Communications*）。さらに、どのDNN特徴量が脳からデコード可能かという傾向が被験者間で共通していることが示され、一般的なWeb画像で訓練したDNNにヒト視覚システムに共通する表現原理が現れることが示唆されました（[Horikawa et al., 2019](https://doi.org/10.1038/sdata.2019.12), *Scientific Data*）。

[Nonakaら（2021）](https://doi.org/10.1016/j.isci.2021.103013)は、DNNの階層構造が脳の階層的組織とどの程度対応するかを評価するbrain hierarchy scoreを提案しました。高性能なDNNモデルは必ずしも階層的に脳と似ているわけではないことを体系的に示し、工学的性能と生物学的妥当性の関係に新たな視点を提供しました（*iScience*）。

最近では、DNNの潜在空間を媒介とした脳コード変換技術により、共有刺激なしに個体間・施設間で脳表現を変換することが可能になりました（[Wang et al., 2025](https://doi.org/10.1038/s43588-025-00826-5), *Nature Computational Science*）。[Shirakawaら（2025）](https://doi.org/10.1016/j.neunet.2025.107515)は、近年話題となった脳からの画像再構成手法の一部が、脳活動の詳細を反映しないカテゴリ情報への依存——すなわち「見せかけの再構成（spurious reconstruction）」であることを指摘しました（*Neural Networks*）。

理論面では、[Onooら（2025）](https://doi.org/10.48550/arXiv.2510.12228)が読み出し表現（readout representation）の概念を提案し、神経コードをその因果的な起源ではなく、潜在表現から情報をいかに復元（読み出し）できるかという観点から再定義しました。これは脳とAIの両方における表現を統一的に理解する枠組みを提供します。

これらの研究の背景にある思想は、神谷の論考「[脳とAIは似ているか: NeuroAIの挑戦](https://note.com/ykamit/n/n8cd93a8f1e09)」（2026）にまとめられています。

### 代表論文

- **[Horikawa & Kamitani (2017)](https://doi.org/10.1038/ncomms15037)** Generic decoding of seen and imagined objects using hierarchical visual features. *Nature Communications*, 8, 15037
- **[Horikawa et al. (2019)](https://doi.org/10.1038/sdata.2019.12)** Characterization of deep neural network features by decodability from human brain activity. *Scientific Data*, 6, 190012
- **[Nonaka et al. (2021)](https://doi.org/10.1016/j.isci.2021.103013)** Brain hierarchy score: Which deep neural networks are hierarchically brain-like? *iScience*, 24(9), 103013
- **[Macpherson et al. (2021)](https://doi.org/10.1016/j.neunet.2021.09.018)** Natural and artificial intelligence: A brief introduction to the interplay between AI and neuroscience research. *Neural Networks*, 144, 603–613
- **[Shirakawa et al. (2025)](https://doi.org/10.1016/j.neunet.2025.107515)** Spurious reconstruction from brain activity. *Neural Networks*, 190, 107515
- **[Wang et al. (2025)](https://doi.org/10.1038/s43588-025-00826-5)** Inter-individual and inter-site neural code conversion without shared stimuli. *Nature Computational Science*, 5(7), 534–546
- **[Onoo et al. (2025)](https://doi.org/10.48550/arXiv.2510.12228)** Readout representation: Redefining neural codes by input recovery. *arXiv:2510.12228*

---

## BMI {#bmi}

ブレイン-マシン・インターフェース（BMI）は、脳信号を外部デバイスの制御命令に変換し、神経疾患患者の運動・コミュニケーション機能の回復を目指す技術です。神谷研究室のBMI研究は、基礎神経科学のために開発されたブレインデコーディング手法から直接的に発展しました。

2006年、本田技術研究所との共同研究により、2005年の*Nature Neuroscience*論文で開発されたfMRIデコーディング技術を応用し、脳活動からじゃんけんの手の形（グー・チョキ・パー）をリアルタイムに解読してロボットハンドを制御することに成功しました。ブレインデコーディングがブレイン-マシン・インターフェースの基盤となりうることを示した研究です。

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/_pAp-EIUCqo" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

その後、大阪大学脳神経外科（吉峰俊樹、のち貴島晴彦）との共同研究を開始し、皮質脳波（ECoG）を用いたデコーディングへと研究の軸足を移しました。ECoGはfMRIより高い時空間解像度を持ち、臨床応用に適しています。[柳澤ら（2009）](https://doi.org/10.1016/j.neuroimage.2008.12.069)は脳溝内ECoGを用いた神経デコーディングを実証し（*NeuroImage*）、[柳澤ら（2011）](https://doi.org/10.3171/2011.1.JNS101421)はヒトECoG信号によるロボットハンドのリアルタイム制御に成功しました（*Journal of Neurosurgery*）。

大きな転機となったのが、[柳澤ら（2012）](https://doi.org/10.1002/ana.22613)による、麻痺患者がECoG信号を用いてロボットアームをリアルタイムに制御できることの実証です。ECoGベースBMIの臨床的実用性を確立した研究です（*Annals of Neurology*）。

研究はさらに幻肢痛の治療へと展開されました。[柳澤ら（2016）](https://doi.org/10.1038/ncomms13209)は、BMI駆動のニューロフィードバックにより幻肢患者の感覚運動野に脳可塑性を誘導し、疼痛を制御できることを示しました（*Nature Communications*）。その後のランダム化クロスオーバー試験でも、[BCIによる仮想ハンド操作訓練が幻肢痛を軽減する](https://doi.org/10.1212/WNL.0000000000009858)ことが確認されています（Yanagisawa et al., 2020, *Neurology*）。

運動デコーディングに加え、視覚的意味情報を脳活動から解読し、画像検索やコミュニケーションに応用する視覚BMIの研究も進めています。[Fukumaら（2022）](https://doi.org/10.1038/s42003-022-03137-x)は意味的神経表現の随意制御を実証し（*Communications Biology*）、[Fukumaら（2024）](https://doi.org/10.1101/2024.08.05.606113)は視覚–意味神経デコーディングに基づくクローズドループ画像検索システムを開発しました。

*Trends in Cognitive Sciences*に掲載された最新の総説（[Beste et al., 2026](https://doi.org/10.1016/j.tics.2025.12.003)）では、BMI研究が認知科学にもたらす意図・主体性・神経コーディングに関する根本的な問いが論じられています。

### 代表論文

- **[Yanagisawa et al. (2009)](https://doi.org/10.1016/j.neuroimage.2008.12.069)** Neural decoding using gyral and intrasulcal electrocorticograms. *NeuroImage*, 45(4), 1099–1106
- **[Yanagisawa et al. (2011)](https://doi.org/10.3171/2011.1.JNS101421)** Real-time control of a prosthetic hand using human electrocorticography signals. *Journal of Neurosurgery*, 114(6), 1715–1722
- **[Yanagisawa et al. (2012)](https://doi.org/10.1002/ana.22613)** Electrocorticographic control of a prosthetic arm in paralyzed patients. *Annals of Neurology*, 71(3), 353–361
- **[Yanagisawa et al. (2016)](https://doi.org/10.1038/ncomms13209)** Induced sensorimotor brain plasticity controls pain in phantom limb patients. *Nature Communications*, 7, 13209
- **[Fukuma et al. (2022)](https://doi.org/10.1038/s42003-022-03137-x)** Voluntary control of semantic neural representations by imagery with conflicting visual stimulation. *Communications Biology*, 5(1), 1–15
- **[Fukuma et al. (2024)](https://doi.org/10.1101/2024.08.05.606113)** Image retrieval based on closed-loop visual-semantic neural decoding. *bioRxiv*
- **[Beste et al. (2026)](https://doi.org/10.1016/j.tics.2025.12.003)** Moving intentions from brains to machines. *Trends in Cognitive Sciences*

---

## アート {#art}

ブレインデコーディング技術は、現代アートの表現媒体としても活用されています。心の隠された内容を可視化する技術が、インスタレーション、彫刻、ミュージックビデオ、アルバムアートワークなど、新しい芸術表現を可能にしました。

最も継続的なコラボレーションは、フランスの現代美術家**ピエール・ユイグ**との協働です。2018年の *[UUmwelt](https://www.serpentinegalleries.org/whats-on/pierre-huyghe-uumwelt/)* （サーペンタイン・ギャラリー、ロンドン）では、fMRIデータから深層画像再構成で生成した神経画像を大型LEDスクリーンに表示し、ハエや他の生物が共存する空間の中に、異なる形態の認知と創発する知性を共存させる環境を創出しました。ニューヨーク・タイムズはこれを「新しいアートの形式」と評しました。その後、*[Liminal](https://www.pinaultcollection.com/palazzograssi/en/pierre-huyghe-liminal)* （プンタ・デラ・ドガーナ、ヴェネツィア、2024）では、人間不在の世界を探求する大規模個展の中で、脳から生成された画像がAI駆動のエコシステムに統合されました。

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/enx-vyWn7UU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

他のコラボレーションとして、**真鍋大度 / [Rhizomatiks](https://rhizomatiks.com/work/dissonant-imaginary/)** による *Dissonant Imaginary* （音楽聴取中の脳活動から画像を再構成するオーディオビジュアル・インスタレーション）、**[Maison book girl](https://www.youtube.com/watch?v=DwcKed26KQ8)** の夢の可視化ミュージックビデオ、Warp Recordsのポストパンクバンド **[Squid](https://brightgreenfield.squidband.uk)** の脳スキャン画像を用いたアルバムアートワーク（2021年ベストアルバムカバー50選に選出）があります。

これらの活動については、神谷の論考「[脳をくすぐるアート](https://note.com/ykamit/n/n0bf7b8517a8d)」（2022）および「[ピエール・ユイグ — Liminal: 人間のいない世界を表象する](https://note.com/ykamit/n/n47242b97c17a)」（2024）で論じられています。

[アート活動一覧 &rarr;](/ja/art/)

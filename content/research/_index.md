---
title: "Research"
description: "Research areas of Kamitani Lab"
featured_image: ""
layout: "research"
---

Kamitani Lab investigates how the brain represents and processes information, developing techniques to decode and visualize mental contents from brain activity. Our research bridges neuroscience and AI, spanning four interconnected areas.

## Brain Decoding {#brain-decoding}

Brain decoding uses machine learning to read out the contents of perception, imagery, and dreams from brain activity measured with fMRI. Kamitani Lab has been a pioneer of this field since the mid-2000s, progressively expanding what can be decoded from the brain.

In 2005, [Kamitani and Tong](https://doi.org/10.1038/nn1444) demonstrated that fMRI signals from visual cortex could be decoded to identify the orientation of visual gratings — including subjectively perceived orientations in binocular rivalry — establishing that fine-grained perceptual information is accessible from population-level brain activity (*Nature Neuroscience*). This was followed by the first visual image reconstruction from brain activity: [Miyawaki et al. (2008)](https://doi.org/10.1016/j.neuron.2008.11.004) showed that arbitrary visual images could be reconstructed by combining outputs of local image decoders trained on multi-scale spatial patterns (*Neuron*).

A landmark study by [Horikawa et al. (2013)](https://doi.org/10.1126/science.1234330) extended brain decoding to the contents of dreams, showing that visual imagery experienced during sleep could be decoded from brain activity measured during the transition to sleep (*Science*). This demonstrated that brain decoding can access private mental experiences that are otherwise only available through subjective report.

The integration of deep neural networks (DNNs) brought a major advance. [Shen et al. (2019)](https://doi.org/10.1371/journal.pcbi.1006633) developed deep image reconstruction, using hierarchical DNN features as an intermediate representation to generate high-quality reconstructions of both perceived and imagined images from brain activity (*PLoS Computational Biology*). This approach was further extended to reconstruct [visual illusory experiences from brain activity](https://doi.org/10.1126/sciadv.adj3906) (Cheng et al., 2023, *Science Advances*), and to [reconstruct natural sounds](https://doi.org/10.1371/journal.pbio.3003293) from auditory brain activity (Park et al., 2025, *PLOS Biology*).

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/jsp1KaM-avU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

Our current framework treats brain decoding as a translation–generation pipeline: a "translator" maps brain activity into the latent representation space of a DNN or generative model, and a "generator" produces images, sounds, or other outputs from these latent representations. This framework is reviewed in [Kamitani, Tanaka & Shirakawa (2025)](https://doi.org/10.1146/annurev-vision-110423-023616), *Annual Review of Vision Science*.

### Key Publications

- **[Kamitani & Tong (2005)](https://doi.org/10.1038/nn1444)** Decoding the visual and subjective contents of the human brain. *Nature Neuroscience*, 8(5), 679–685
- **[Miyawaki et al. (2008)](https://doi.org/10.1016/j.neuron.2008.11.004)** Visual image reconstruction from human brain activity. *Neuron*, 60(5), 915–929
- **[Horikawa et al. (2013)](https://doi.org/10.1126/science.1234330)** Neural decoding of visual imagery during sleep. *Science*, 340(6132), 639–642
- **[Shen et al. (2019)](https://doi.org/10.1371/journal.pcbi.1006633)** Deep image reconstruction from human brain activity. *PLoS Computational Biology*, 15(1), e1006633
- **[Cheng et al. (2023)](https://doi.org/10.1126/sciadv.adj3906)** Reconstructing visual illusory experiences from human brain activity. *Science Advances*, 9, eadj3906
- **[Park et al. (2025)](https://doi.org/10.1371/journal.pbio.3003293)** Natural sounds can be reconstructed from human neuroimaging data. *PLOS Biology*, 23(7), e3003293
- **[Kamitani, Tanaka & Shirakawa (2025)](https://doi.org/10.1146/annurev-vision-110423-023616)** Visual image reconstruction from brain activity via latent representation. *Annual Review of Vision Science*, 11, 611–634

---

## NeuroAI {#neuroai}

NeuroAI is an emerging interdisciplinary field that investigates the relationship between biological and artificial neural systems. A central finding is that deep neural networks (DNNs), trained purely on engineering objectives, develop internal representations that align with brain activity patterns — even though they were never designed to model the brain.

Kamitani Lab has contributed to this field through a series of studies connecting DNN representations to human brain activity. [Horikawa and Kamitani (2017)](https://doi.org/10.1038/ncomms15037) demonstrated that hierarchical visual features of a DNN can be decoded from human brain activity, and that the decodable features shift from lower visual areas to higher areas as the DNN layer depth increases — establishing a systematic correspondence between the brain's visual hierarchy and DNN layer structure (*Nature Communications*). A follow-up study showed that [which DNN features are decodable from the brain is consistent across individuals](https://doi.org/10.1038/sdata.2019.12), suggesting that general-purpose DNNs capture universal aspects of human visual representation (Horikawa et al., 2019, *Scientific Data*).

[Nonaka et al. (2021)](https://doi.org/10.1016/j.isci.2021.103013) introduced the brain hierarchy score, a metric for evaluating how well a DNN's layer structure corresponds to the brain's hierarchical organization. This work revealed that higher task performance does not always mean better alignment with the brain's hierarchy — a finding that challenges the assumption that better engineering performance equals greater biological plausibility (*iScience*).

More recently, the lab has developed neural code conversion technology that translates brain representations across different individuals and measurement sites without requiring shared stimuli ([Wang et al., 2025](https://doi.org/10.1038/s43588-025-00826-5), *Nature Computational Science*), enabling broader applicability of decoding models. [Shirakawa et al. (2025)](https://doi.org/10.1016/j.neunet.2025.107515) critically examined current reconstruction methods, identifying that some high-profile results may reflect "spurious reconstruction" — category-level classification combined with generative model hallucination rather than genuine visual reconstruction (*Neural Networks*).

At the theoretical level, [Onoo et al. (2025)](https://doi.org/10.48550/arXiv.2510.12228) proposed the concept of readout representation, which redefines neural codes not by the causal origin of neural activity but by the information that can be recovered (read out) from latent representations — providing a unified framework for understanding representation in both brains and AI systems.

These themes are discussed in Kamitani's essay "[Is the Brain Similar to AI? The Challenge of NeuroAI](https://note.com/ykamit/n/n8cd93a8f1e09)" (2026), which traces the intellectual arc from AI's "bitter lesson" to the emerging science of latent representations shared between brains and machines.

### Key Publications

- **[Horikawa & Kamitani (2017)](https://doi.org/10.1038/ncomms15037)** Generic decoding of seen and imagined objects using hierarchical visual features. *Nature Communications*, 8, 15037
- **[Horikawa et al. (2019)](https://doi.org/10.1038/sdata.2019.12)** Characterization of deep neural network features by decodability from human brain activity. *Scientific Data*, 6, 190012
- **[Nonaka et al. (2021)](https://doi.org/10.1016/j.isci.2021.103013)** Brain hierarchy score: Which deep neural networks are hierarchically brain-like? *iScience*, 24(9), 103013
- **[Macpherson et al. (2021)](https://doi.org/10.1016/j.neunet.2021.09.018)** Natural and artificial intelligence: A brief introduction to the interplay between AI and neuroscience research. *Neural Networks*, 144, 603–613
- **[Shirakawa et al. (2025)](https://doi.org/10.1016/j.neunet.2025.107515)** Spurious reconstruction from brain activity. *Neural Networks*, 190, 107515
- **[Wang et al. (2025)](https://doi.org/10.1038/s43588-025-00826-5)** Inter-individual and inter-site neural code conversion without shared stimuli. *Nature Computational Science*, 5(7), 534–546
- **[Onoo et al. (2025)](https://doi.org/10.48550/arXiv.2510.12228)** Readout representation: Redefining neural codes by input recovery. *arXiv:2510.12228*

---

## BMI {#bmi}

Brain-machine interfaces (BMIs) translate brain signals into control commands for external devices, aiming to restore motor and communication functions for patients with neurological conditions. Kamitani Lab's BMI research grew directly from the brain decoding methods developed for basic neuroscience.

In 2006, in collaboration with Honda Research Institute, the fMRI decoding technique from the 2005 *Nature Neuroscience* study was applied to demonstrate that hand shapes (rock, paper, scissors) could be decoded from brain activity in real time and used to control a robot hand — showing that brain decoding could serve as the basis for a brain-machine interface.

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/_pAp-EIUCqo" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

Subsequently, the lab began a collaboration with the neurosurgery group at Osaka University (led by Toshiki Yoshimine and later Haruhiko Kishima), shifting focus to electrocorticography (ECoG) — electrodes placed directly on the brain surface during neurosurgical procedures. From 2008, the research concentrated on ECoG-based decoding, which offers higher spatial and temporal resolution than fMRI. [Yanagisawa et al. (2009)](https://doi.org/10.1016/j.neuroimage.2008.12.069) demonstrated neural decoding using gyral and intrasulcal electrocorticograms (*NeuroImage*), and [Yanagisawa et al. (2011)](https://doi.org/10.3171/2011.1.JNS101421) achieved real-time control of a prosthetic hand using human ECoG signals (*Journal of Neurosurgery*).

A major milestone was reported in [Yanagisawa et al. (2012)](https://doi.org/10.1002/ana.22613), which demonstrated that paralyzed patients could control a prosthetic arm using ECoG signals decoded in real time (*Annals of Neurology*). This established the clinical viability of ECoG-based BMI for motor restoration.

The research then extended to phantom limb pain. [Yanagisawa et al. (2016)](https://doi.org/10.1038/ncomms13209) showed that BMI-driven neurofeedback could induce sensorimotor brain plasticity and control pain in phantom limb patients (*Nature Communications*), and a subsequent randomized crossover trial confirmed that [BCI training to move a virtual hand reduces phantom limb pain](https://doi.org/10.1212/WNL.0000000000009858) (Yanagisawa et al., 2020, *Neurology*).

Beyond motor decoding, the lab has also pursued vision-based brain-machine interfaces, where visual semantic information is decoded from brain activity and used for image retrieval and communication. [Fukuma et al. (2018)](https://doi.org/10.1109/SMC.2018.00027) decoded visual stimulus semantics from ECoG signals, [Fukuma et al. (2022)](https://doi.org/10.1038/s42003-022-03137-x) demonstrated voluntary control of semantic neural representations (*Communications Biology*), and [Fukuma et al. (2024)](https://doi.org/10.1101/2024.08.05.606113) developed a closed-loop image retrieval system based on visual-semantic neural decoding.

A recent review in *Trends in Cognitive Sciences* ([Beste et al., 2026](https://doi.org/10.1016/j.tics.2025.12.003)) discusses the broader challenge of moving intentions from brains to machines, addressing fundamental questions about intention, agency, and neural coding that BMI research raises for cognitive science.

### Key Publications

- **[Yanagisawa et al. (2009)](https://doi.org/10.1016/j.neuroimage.2008.12.069)** Neural decoding using gyral and intrasulcal electrocorticograms. *NeuroImage*, 45(4), 1099–1106
- **[Yanagisawa et al. (2011)](https://doi.org/10.3171/2011.1.JNS101421)** Real-time control of a prosthetic hand using human electrocorticography signals. *Journal of Neurosurgery*, 114(6), 1715–1722
- **[Yanagisawa et al. (2012)](https://doi.org/10.1002/ana.22613)** Electrocorticographic control of a prosthetic arm in paralyzed patients. *Annals of Neurology*, 71(3), 353–361
- **[Yanagisawa et al. (2016)](https://doi.org/10.1038/ncomms13209)** Induced sensorimotor brain plasticity controls pain in phantom limb patients. *Nature Communications*, 7, 13209
- **[Fukuma et al. (2022)](https://doi.org/10.1038/s42003-022-03137-x)** Voluntary control of semantic neural representations by imagery with conflicting visual stimulation. *Communications Biology*, 5(1), 1–15
- **[Fukuma et al. (2024)](https://doi.org/10.1101/2024.08.05.606113)** Image retrieval based on closed-loop visual-semantic neural decoding. *bioRxiv*
- **[Beste et al. (2026)](https://doi.org/10.1016/j.tics.2025.12.003)** Moving intentions from brains to machines. *Trends in Cognitive Sciences*

---

## Art {#art}

Brain decoding technology has become a medium for contemporary art, enabling new forms of creative expression that visualize the hidden contents of the mind. Kamitani Lab has collaborated with internationally recognized artists to create installations, sculptures, music videos, and album artwork.

The most sustained collaboration has been with French contemporary artist **Pierre Huyghe**. In 2018, Huyghe's *[UUmwelt](https://www.serpentinegalleries.org/whats-on/pierre-huyghe-uumwelt/)* at the Serpentine Galleries in London displayed neural images generated by deep image reconstruction from fMRI data on large LED screens, set within a gallery space inhabited by flies and other organisms — creating an environment housing different forms of cognition and emerging intelligence. The New York Times described it as "[a new art form](https://www.nytimes.com/2018/10/11/arts/design/pierre-huyghe-serpentine-gallery-london-artist.html)." This was followed by *[Liminal](https://www.pinaultcollection.com/palazzograssi/en/pierre-huyghe-liminal)* (Punta della Dogana, Venice, 2024), a major solo exhibition exploring worlds without human presence, where brain-generated images were integrated into an AI-driven ecosystem.

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/enx-vyWn7UU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

Other collaborations include work with **Daito Manabe / Rhizomatiks** on *[Dissonant Imaginary](https://rhizomatiks.com/work/dissonant-imaginary/)*, an audio-visual installation that reconstructed images from brain activity while listening to music; the dream visualization music video for **[Maison book girl](https://www.youtube.com/watch?v=DwcKed26KQ8)**; and album artwork using brain scan images for the post-punk band **[Squid](https://brightgreenfield.squidband.uk)** on Warp Records, which was named one of the 50 Best Album Covers of 2021.

These activities are discussed in Kamitani's essays "[Art That Tickles the Brain](https://note.com/ykamit/n/n0bf7b8517a8d)" (2022) and "[Pierre Huyghe — Liminal: Representing a World Without Humans](https://note.com/ykamit/n/n47242b97c17a)" (2024).

[See all Art projects &rarr;](/art/)

---
title: "Research"
description: "Research areas of Kamitani Lab"
featured_image: ""
layout: "research"
---

Kamitani Lab investigates how the brain represents and processes information, developing techniques to decode and visualize mental contents from brain activity. Our research bridges neuroscience and AI, spanning four interconnected areas.

## Brain Decoding {#brain-decoding}

Brain decoding uses machine learning to read out the contents of perception, imagery, and dreams from brain activity measured with fMRI. Kamitani Lab has been a pioneer of this field since the mid-2000s, progressively expanding what can be decoded from the brain.

In 2005, [Kamitani and Tong](/publications/2005-kamitani-visual-subjective-contents/) demonstrated that fMRI signals from visual cortex could be decoded to identify the orientation of visual gratings — including subjectively perceived orientations in binocular rivalry — establishing that fine-grained perceptual information is accessible from population-level brain activity (*Nature Neuroscience*). This was followed by the first visual image reconstruction from brain activity: [Miyawaki et al. (2008)](/publications/2008-miyawaki-visual-image-reconstruction/) showed that arbitrary visual images could be reconstructed by combining outputs of local image decoders trained on multi-scale spatial patterns (*Neuron*).

A landmark study by [Horikawa et al. (2013)](/publications/2013-horikawa-dream-decoding/) extended brain decoding to the contents of dreams, showing that visual imagery experienced during sleep could be decoded from brain activity measured during the transition to sleep (*Science*). This demonstrated that brain decoding can access private mental experiences that are otherwise only available through subjective report.

The integration of deep neural networks (DNNs) brought a major advance. [Shen et al. (2019)](/publications/2019-shen-deep-image-reconstruction/) developed deep image reconstruction, using hierarchical DNN features as an intermediate representation to generate high-quality reconstructions of both perceived and imagined images from brain activity (*PLoS Computational Biology*). This approach was further extended to reconstruct [visual illusory experiences from brain activity](/publications/2023-cheng-illusion-reconstruction/) (Cheng et al., 2023, *Science Advances*), and to [reconstruct natural sounds](/publications/2025-park-natural-sounds/) from auditory brain activity (Park et al., 2025, *PLOS Biology*).

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/jsp1KaM-avU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

Our current framework treats brain decoding as a translation–generation pipeline: a "translator" maps brain activity into the latent representation space of a DNN or generative model, and a "generator" produces images, sounds, or other outputs from these latent representations. This framework is reviewed in [Kamitani, Tanaka & Shirakawa (2025)](/publications/2025-kamitani-visual-image-reconstruction-review/), *Annual Review of Vision Science*.

### Key Publications

- **[Kamitani & Tong (2005)](/publications/2005-kamitani-visual-subjective-contents/)** Decoding the visual and subjective contents of the human brain. *Nature Neuroscience*, 8(5), 679–685
- **[Miyawaki et al. (2008)](/publications/2008-miyawaki-visual-image-reconstruction/)** Visual image reconstruction from human brain activity. *Neuron*, 60(5), 915–929
- **[Horikawa et al. (2013)](/publications/2013-horikawa-dream-decoding/)** Neural decoding of visual imagery during sleep. *Science*, 340(6132), 639–642
- **[Shen et al. (2019)](/publications/2019-shen-deep-image-reconstruction/)** Deep image reconstruction from human brain activity. *PLoS Computational Biology*, 15(1), e1006633
- **[Cheng et al. (2023)](/publications/2023-cheng-illusion-reconstruction/)** Reconstructing visual illusory experiences from human brain activity. *Science Advances*, 9, eadj3906
- **[Park et al. (2025)](/publications/2025-park-natural-sounds/)** Natural sounds can be reconstructed from human neuroimaging data. *PLOS Biology*, 23(7), e3003293
- **[Kamitani, Tanaka & Shirakawa (2025)](/publications/2025-kamitani-visual-image-reconstruction-review/)** Visual image reconstruction from brain activity via latent representation. *Annual Review of Vision Science*, 11, 611–634

---

## NeuroAI {#neuroai}

NeuroAI is an emerging interdisciplinary field that investigates the relationship between biological and artificial neural systems. A central finding is that deep neural networks (DNNs), trained purely on engineering objectives, develop internal representations that align with brain activity patterns — even though they were never designed to model the brain.

Kamitani Lab has contributed to this field through a series of studies connecting DNN representations to human brain activity. [Horikawa and Kamitani (2017)](/publications/2017-horikawa-generic-decoding/) demonstrated that hierarchical visual features of a DNN can be decoded from human brain activity, and that the decodable features shift from lower visual areas to higher areas as the DNN layer depth increases — establishing a systematic correspondence between the brain's visual hierarchy and DNN layer structure (*Nature Communications*). A follow-up study showed that [which DNN features are decodable from the brain is consistent across individuals](/publications/2019-horikawa-dnn-features-decodability/), suggesting that general-purpose DNNs capture universal aspects of human visual representation (Horikawa et al., 2019, *Scientific Data*).

[Nonaka et al. (2021)](/publications/2021-nonaka-brain-hierarchy-score/) introduced the brain hierarchy score, a metric for evaluating how well a DNN's layer structure corresponds to the brain's hierarchical organization. This work revealed that higher task performance does not always mean better alignment with the brain's hierarchy — a finding that challenges the assumption that better engineering performance equals greater biological plausibility (*iScience*).

<div class="research-embed">
<div class="research-embed-slides">
<iframe src="https://speakerdeck.com/player/a0c60ab70baf4b1d9aeedeff560574cd" allowfullscreen allowtransparency></iframe>
</div>
</div>

More recently, the lab has developed neural code conversion technology that translates brain representations across different individuals and measurement sites without requiring shared stimuli ([Wang et al., 2025](/publications/2025-wang-inter-individual-neural-code/), *Nature Computational Science*), enabling broader applicability of decoding models. [Shirakawa et al. (2025)](/publications/2025-shirakawa-spurious-reconstruction/) critically examined current reconstruction methods, identifying that some high-profile results may reflect "spurious reconstruction" — category-level classification combined with generative model hallucination rather than genuine visual reconstruction (*Neural Networks*).

At the theoretical level, [Onoo et al. (2025)](/publications/2025-onoo-readout-representation/) proposed the concept of readout representation, which redefines neural codes not by the causal origin of neural activity but by the information that can be recovered (read out) from latent representations — providing a unified framework for understanding representation in both brains and AI systems.

These themes are discussed in Kamitani's essay "[Is the Brain Similar to AI? The Challenge of NeuroAI](https://note.com/ykamit/n/n8cd93a8f1e09)" (2026), which traces the intellectual arc from AI's "bitter lesson" to the emerging science of latent representations shared between brains and machines.

### Key Publications

- **[Horikawa & Kamitani (2017)](/publications/2017-horikawa-generic-decoding/)** Generic decoding of seen and imagined objects using hierarchical visual features. *Nature Communications*, 8, 15037
- **[Horikawa et al. (2019)](/publications/2019-horikawa-dnn-features-decodability/)** Characterization of deep neural network features by decodability from human brain activity. *Scientific Data*, 6, 190012
- **[Nonaka et al. (2021)](/publications/2021-nonaka-brain-hierarchy-score/)** Brain hierarchy score: Which deep neural networks are hierarchically brain-like? *iScience*, 24(9), 103013
- **[Macpherson et al. (2021)](/publications/2021-macpherson-natural-artificial-intelligence/)** Natural and artificial intelligence: A brief introduction to the interplay between AI and neuroscience research. *Neural Networks*, 144, 603–613
- **[Shirakawa et al. (2025)](/publications/2025-shirakawa-spurious-reconstruction/)** Spurious reconstruction from brain activity. *Neural Networks*, 190, 107515
- **[Wang et al. (2025)](/publications/2025-wang-inter-individual-neural-code/)** Inter-individual and inter-site neural code conversion without shared stimuli. *Nature Computational Science*, 5(7), 534–546
- **[Onoo et al. (2025)](/publications/2025-onoo-readout-representation/)** Readout representation: Redefining neural codes by input recovery. *arXiv:2510.12228*

---

## BMI {#bmi}

Brain-machine interfaces (BMIs) translate brain signals into control commands for external devices, aiming to restore motor and communication functions for patients with neurological conditions. Kamitani Lab's BMI research, conducted primarily at ATR in collaboration with Osaka University Hospital and other institutions, has focused on electrocorticography (ECoG)-based decoding of motor intentions.

A key achievement was the development of a BMI system that enables patients with phantom limb pain to control a prosthetic hand using brain signals from the reorganized motor cortex. [Yanagisawa et al. (2012)](/publications/2012-yanagisawa-electrocorticographic-prosthetic/) demonstrated real-time control of an electrocorticographic prosthetic hand, and subsequent work showed that [neurofeedback training with such systems can alleviate phantom limb pain](/publications/2020-yanagisawa-bci-phantom-limb/) by normalizing cortical representations. [Hirata et al. (2012)](/publications/2012-hirata-bmi-brain-surface/) developed a fully implantable wireless BMI system using brain surface electrodes for motor restoration (*Advanced Robotics*).

The lab has also investigated how BMI training induces cortical plasticity, showing that repeated use of brain-machine interfaces can reshape neural representations in motor areas ([Yanagisawa et al., 2016](/publications/2016-yanagisawa-sensorimotor-plasticity/); [Yanagisawa et al., 2018](/publications/2018-yanagisawa-induction-cortical-plasticity/)), and how decoded visual semantic information can be used for image retrieval in closed-loop systems ([Fukuma et al., 2024](/publications/2024-fukuma-image-retrieval-closed-loop/)).

A recent review in *Trends in Cognitive Sciences* ([Beste et al., 2026](/publications/2026-beste-moving-intentions/)) discusses the broader challenge of moving motor intentions from brains to machines, addressing the cognitive science questions that BMI research raises about the nature of intention, agency, and neural coding of movement.

<div class="research-embed">
<div class="research-embed-slides">
<iframe src="https://speakerdeck.com/player/d96cb75df2254c0ebcfd4ced51754104" allowfullscreen allowtransparency></iframe>
</div>
</div>

### Key Publications

- **[Yanagisawa et al. (2012)](/publications/2012-yanagisawa-electrocorticographic-prosthetic/)** Electrocorticographic control of a prosthetic arm in paralyzed patients. *Annals of Neurology*, 71(3), 353–361
- **[Hirata et al. (2012)](/publications/2012-hirata-bmi-brain-surface/)** Motor restoration based on the brain machine interface using brain surface electrodes. *Advanced Robotics*, 26(3-4), 335–351
- **[Fukuma et al. (2018)](/publications/2018-fukuma-bmi-robotic-hand/)** Training in use of brain–machine interface-controlled robotic hand improves accuracy decoding two types of hand movements. *Frontiers in Neuroscience*, 12, 478
- **[Yanagisawa et al. (2020)](/publications/2020-yanagisawa-bci-phantom-limb/)** BCI-based neurofeedback training for phantom limb pain. *Journal of Neural Engineering*
- **[Beste et al. (2026)](/publications/2026-beste-moving-intentions/)** Moving intentions from brains to machines. *Trends in Cognitive Sciences*

---

## Art {#art}

Brain decoding technology has become a medium for contemporary art, enabling new forms of creative expression that visualize the hidden contents of the mind. Kamitani Lab has collaborated with internationally recognized artists to create installations, sculptures, music videos, and album artwork.

The most sustained collaboration has been with French contemporary artist **Pierre Huyghe**. In 2018, Huyghe's *[UUmwelt](/art/2018-huyghe-uumwelt-serpentine/)* at the Serpentine Galleries in London displayed neural images generated by deep image reconstruction from fMRI data on large LED screens, set within a gallery space inhabited by flies and other organisms — creating an environment housing different forms of cognition and emerging intelligence. The New York Times described it as "[a new art form](https://www.nytimes.com/2018/10/11/arts/design/pierre-huyghe-serpentine-gallery-london-artist.html)." This was followed by *[Mind's Eye](/art/2022-huyghe-minds-eye/)* (Hauser & Wirth, Hong Kong, 2022), which materialized brain-decoded images as physical sculptures, and *[Liminal](/art/2024-huyghe-liminal-venice/)* (Punta della Dogana, Venice, 2024), a major solo exhibition exploring worlds without human presence, where brain-generated images were integrated into an AI-driven ecosystem.

<div class="research-embed">
<div class="research-embed-video">
<iframe src="https://www.youtube.com/embed/enx-vyWn7UU" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
</div>

Other collaborations include work with **Daito Manabe / Rhizomatiks** on *[Dissonant Imaginary](/art/2018-manabe-dissonant-imaginary-kirishima/)*, an audio-visual installation that reconstructed images from brain activity while listening to music; the dream visualization music video for **[Maison book girl](/art/2018-maison-book-girl-yume/)**; and album artwork using brain scan images for the post-punk band **[Squid](/art/2021-squid-bright-green-field/)** on Warp Records, which was named one of the 50 Best Album Covers of 2021.

These activities are discussed in Kamitani's essays "[Art That Tickles the Brain](https://note.com/ykamit/n/n0bf7b8517a8d)" (2022) and "[Pierre Huyghe — Liminal: Representing a World Without Humans](https://note.com/ykamit/n/n47242b97c17a)" (2024).

[See all Art projects &rarr;](/art/)

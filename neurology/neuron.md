## neuron

![anatomy of a neuron](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Blausen_0657_MultipolarNeuron.png/1920px-Blausen_0657_MultipolarNeuron.png)

although some neuronal tissue does regenerate (and some of it _is_ likely
replaced in a lifetime), most of it remains unchanged during one's life.

## anatomy

* dendrites -- little extensions: receptive zone
* cell body / soma
* axon 
* axon hillock -- part where the body and the axon are connected (basically the funnel where lots of voltage gated channels are situated)
* axon terminal bulb / synaptic terminal bulb

### dendrites

involved in graded potentials (excitatory and inhibitory post-synaptic potentials)

in the dendritic cell membrane are these channels:

1. _ligand gated ion channels_: ligandem rizeny iontovy kanal/ionotropni receptor
   (neurotransmitters are bound to the channels, allowing anionts/kationts --
   depending on the neurotransmitter -- to enter the cell)
2. _g protein-coupled receptors_: receptor sprazeny s g proteinem
   (neurotransmitter is bound to the receptor, which activates second messengers,
   which activate protein kinases, which allow the ionts -- depending on the
   neurotransmitter -- to enter the cell)


### cell body / soma

also involved in graded potentials (same as dendrites), but most importantly,
in protein synthesis (neurotransmitters, cellular enzymes,
membrane proteins -- voltage gating, ligand gating, gpcr gating...)

#### protein synthesis

chatgpt generated :^)

1. DNA and Genes  
1.1. DNA (deoxyribonucleic acid) is the genetic material that contains instructions for building and maintaining an organism.  
1.2. Genes are specific sequences of DNA that code for particular proteins.  

2. Gene Expression  
2.1. Gene expression is the process by which the information in a gene is used to synthesize a functional product, typically a protein.  
2.2. It involves two main steps: transcription and translation.

3. Transcription  
3.1. Transcription occurs in the cell nucleus.  
3.2. RNA polymerase, an enzyme, reads the DNA template and synthesizes a complementary RNA molecule called messenger RNA (_mRNA_).  
3.3. The mRNA carries the genetic information from the nucleus to the cytoplasm.

4. mRNA and Nissl Bodies  
4.1. Nissl bodies, also known as rough endoplasmic reticulum (RER), are membrane-bound organelles in the cell cytoplasm.  
4.2. The mRNA associates with ribosomes on the surface of the RER for translation.

5. Translation  
5.1. Translation occurs in the cytoplasm on ribosomes.  
5.2. Transfer RNA (tRNA) molecules bring amino acids to the ribosome based on the codons (triplets of nucleotides) on the mRNA.  
5.3. Amino acids are linked together in a specific order to form a polypeptide chain, which eventually folds into a functional protein.

6. Protein Folding and Modification  
6.1. After translation, the polypeptide chain may undergo folding to achieve its functional three-dimensional structure.  
6.2. The newly synthesized protein may undergo post-translational modifications in the endoplasmic reticulum and Golgi apparatus.  
6.3. Modifications can include adding sugars (glycosylation), lipids, or other functional groups.

7. Transport in Vesicles  
7.1. The modified proteins are packaged into vesicles, which are small membrane-bound sacs.  
7.2. Vesicles transport the proteins to their destination within the cell or outside the cell.

8. Exocytosis  
8.1. Vesicles containing the modified proteins fuse with the cell membrane through a process called exocytosis.  
8.2. The contents of the vesicle are released into the extracellular space or, in the case of membrane proteins, incorporated into the cell membrane.

#### NGF

(_described below the axon but important here; NGFs are synthesized in the soma_)

### axon and potentials

axons:

1. conduct action potential (flow of charge to the terminal -- depolarizing: positive wave followed by repolarizing: negative wave)
2. contain microtubules -- filled with motor proteins involved in transporting things down the axon  
2.1. kinesin (+) -- cell body down to the axon terminal (anterograde axonal transport); e.g. proteins synthesized in the soma to the terminal; neurotransmitters, mitochondria, enzymes, etc.  
2.2. dynein (-) -- axon terminal up to the cell body (retrograde axonal transport); e.g. degraded organelles, degraded mitochondria, nerve growth factors

#### potentials

the resting membrane potential of a neuron is around -70mv.

* depolarization (excitatory post-synaptic potential) -- when the cell is more positive than rmp, stimulated to fire. the threshold is around -55mv, then the action potential is reached, channels are opened and the neuron fires
* hyperpolarization (inhibitory post-synaptic potential) -- when the cell is more negative than rmp (around -90mv), inhibited from firing

along the axon are _voltage gated sodium/potassium channels_, which open when
action potential / depolarization threshold is hit.

sodium channels open when you hit the threshold voltage, causing sodium ions to
rush _into_ the cell, making it very positive
(depolarizing phase of the action potential).  

once the axon has been stimulated, the cell goes into a resting state: potassium
channels open after depolarization, potassium floods _out_ of the cell
(which is the repolarizing wave), causing the cell to become very negative.

__temporal summation__ is when one presynaptic neuron causes a postsynaptic
neuron to fire by exciting it multiple times in a row, causing it to reach the
action potential. __spatial summation__ is when multiple presynaptic neurons
cause a postsynaptic neuron to fire by exciting it simultaneously.

#### nerve growth factor (NGF)

when the axon or its terminal is damaged, NGFs (synthesized by cells/tissues
external to the neuron itself -- e.g. neurons connected to the axon) are
transported from the site of injury by dyneins (retrograde ax-tr) to the
nucleus. the NGF then stimulates particular genes in the DNA, causing the
increased expression of mRNA, its translation and packaging.

#### pathogens and axonal transport

polio, rabies, hsv... infect the nerve terminals. from here, they migrate
towards the microtubules and piggyback on dyneins during rt-ax-tr, travelling
back to the nucleus, where they use the cell's nuclear machinery to create more
viruses, practically destroying the neuron.

### axon terminal, snare proteins and neurotransmitter release/reuptake

__secretory region__  
the terminal is the area, where the neurotransmitters are released, but it is
also involved in neurotransmitter _reuptake_.

the voltage in the depolarizing wave stimulates the _voltage gated calcium
channels_ present on the terminal membrane, causing calcium ions to rush into
the terminal, triggering the fusion of neurotransmitter vesicles with the
presynaptic membrane.

neurotransmitter vesicles at the axon terminal have snare proteins (v-snares)
embedded on their membrane. these proteins are also present on the plasma
membrane (t-snares). calcium binds to these proteins, linking the v-snares and
t-snares together, causing the vesicle to be pulled to the terminal membrane and
to be eventually fused with it, opening it in the process and releasing the
neurotransmitter out of the terminal (exocytosis) into the synaptic cleft, where
it can then bind to the receptors on the postsynaptic membrane.

once the neurotransmitter has exerted its effect on the target neuron, it has
to be removed from the synapse. there are 2 ways:
* degradation (enzyme in the synapse degrades the neurotransmitter)
* reuptake (reuptake protein present on the presynaptic axon terminal moves the
  neurotransmitter back into the vesicle of the presynaptic neuron)

reuptake proteins are selective for their specific neurotransmitters, i.e.
serotonin reuptake proteins only transport back 5-HT neurotransmitters.
reuptake inhibitors inhibit these proteins from working (e.g. SSRIs inhibit
serotonin reuptake proteins, causing serotonin to remain present for a longer
time within the synapse).

## classification

### structural

1. multipolar -- multiple dendritic extensions
* within the motor cortex (pyramidal); receptive to, for example, signals from
  the basal ganglia, the sensory cortex, the cerebellum, pre-motor and
  supplementary motor cortex...
* within the cerebellum (purkinje/purkyně)
* ...

2. bipolar -- one dendritic extension
* mainly in special sensory organs
* the retina, olfactory nerves (roof of the nasal cavity), inner ear

3. pseudounipolar -- no dendritic extensions (usually sensory neurons)
* dorsal root ganglion (neuron groups just outside of the spinal cord); e.g. 
  picking up sensations from the skin and synapsing in the spinal cord
* cranial nerves (e.g. trigeminal -- V; these pick up sensations from all over
  your face and send them towards the nucleus in your brain stem)

### functional

1. sensory (afferent information)  
* _general visceral_ afferent fibers (internal organs)
* _general somatic_ afferent fibers (skin, joints, ligaments, skeletal muscles)
* _special sensory_ afferent fibers (special sensory organs: vision, hearing)
* _special visceral_ afferent fibers (special visceral sensory organs: smell, taste)

2. motor (efferent information)
* _general visceral_ efferent fibers
* _general somatic_ efferent fibers
* _special visceral_ (around your face and neck) efferent fibers

3. interneurons (neurons which connect motor and sensory neurons; i.e. you have
pricked your finger and you reflexively move it away)

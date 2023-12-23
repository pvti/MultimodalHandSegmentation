# :hand: Hand detection and segmentation using multimodal information from Kinect
<div>
<div align="center">
    <a href='https://github.com/pvtien96' target='_blank'>Van-Tien Pham<sup>1,3&#x2709</sup></a>&emsp;
    <a href='https://mica.edu.vn/perso/Tran-Thi-Thanh-Hai/' target='_blank'>Thanh-Hai Tran<sup>2,3</sup></a>&emsp;
    <a href='https://www.mica.edu.vn/perso/Le-Thi-Lan/' target='_blank'>Thi-Lan Le<sup>2,3</sup></a>&emsp;
    <a href='http://tpnguyen.univ-tln.fr/' target='_blank'>Thanh Phuong NGUYEN<sup>4</sup></a>&emsp;
</div>
<div>

<div align="center">
    <sup>1</sup><em>Modelling and Simulation Centre, Viettel High Technology Industries Corporation, Vietnam</em>&emsp;
    <sup>2</sup><em>School of Electronics and Telecommunications, Hanoi University of Science and Technology, Vietnam</em>&emsp;
    <sup>3</sup><em>International Research Institute MICA, Hanoi University of Science and Technology, Vietnam</em>&emsp;
    <sup>4</sup><em>Université de Toulon, Aix Marseille Université, CNRS, LIS, UMR 7020, France</em>&emsp;
    <sup>&#x2709</sup><em>Corresponding Author</em>
</div>

<div style="text-align: justify"> Nowadays, hand gestures are becoming one of the most natural and intuitive ways of communication between human and computer. To this end, a complex process including hand gesture acquisition, hand detection, gesture representation and recognition must be carried out. This paper presents a method that detects hand and segments hand regions from images captured by a Kinect sensor. As Kinect sensor provides not only RGB images as conventional camera, but also depth and skeleton, in our work, we incorporate multi-modal data from Kinect to deal with hand detection and segmentation. Specifically, we use skeleton to approximately determine hand palm. Then a skin based detector will be applied to discard non-skin pixels from the region of interest. Using depth data helps to limit the human body regions and remove false positive regions from the previous steps. Finally, morphological operations will be applied to fill holes in the hand region. The main advantage of this method is very easy to implement and it performs in real-time on an ordinary computer. We evaluate the proposed method on a dataset of hand gestures captured from different viewpoints. Experiment shows that it provides reasonable accuracy at very high frame rate. It also produces comparable performance in comparison with deep learning based methods. </div>


## :+1: Citation

If you use this work in your research or wish to refer to the results, please use the following BibTeX entry.

```BibTeX
@inproceedings{pham2021detection,
  title={Detection and tracking hand from FPV: benchmarks and challenges on rehabilitation exercises dataset},
  author={Pham, Van-Tien and Tran, Thanh-Hai and Vu, Hai},
  booktitle={2021 RIVF International Conference on Computing and Communication Technologies (RIVF)},
  pages={1--6},
  year={2021},
  organization={IEEE}
}
```

# EECS 338 Quiz Hacker

> This is an attempt to hack Dr. Loui's word-filling quiz with an amateur string-similarity searching approach.

---

## Disclaimers

The content is intend for and only for the private use of the author, its GitHub appearance is for the pure purpose of version control.

---
## Run

1. Copy and paste the quiz content into `input.txt`.
2. Modify the value of `last_name_first_vowel` in `quiz_hacker.py` as you desired (as type `str`).
3. `cd` into the working directory of *EECS 338 Quiz Hacker*, then run the following command in the terminal:

```
python3 quiz_hacker.py
```

If everything works fine, you may expect an output like:
```
         curren_ schedu_ing     -->     curren_ scheduling
      _eadlin_ requirem_nts     -->     deadlin_ requirem_nts
        _elative pr_orit_e_     -->     relative priorities
       _ernel-l_vel thr_ads     -->     _ernel-l_vel threads
           hardwa_e thread_     -->     hardwa_e threads
           h__hest _riorit_     -->     h__hest priority
     hig_er-pri_rity thread     -->     higher-priority thread
             lower p__ority     -->     lower priority
      preemptive sche_uling     -->     preemptive scheduling
            priority _e_el_     -->     priority _e_el_
  priori_y-based sche_u_ing     -->     priority-based scheduling
           processes _rr_v_     -->     processes _rr_v_
             pr_or_ty cla__     -->     priority class
            q_a_t_m expire_     -->     q_a_t_m expire_
            real-_im_ clas_     -->     real-time class
                rea__ queu_     -->     reag_ queue
          re_l-time th__ad_     -->     real-time threads
       s_heduling _eadline_     -->     scheduling _eadlinee
            thre_d creatio_     -->     thread creatio_
              urge_c_ valu_     -->     urge_c_ valu_
```
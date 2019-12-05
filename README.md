# EECS 338 Quiz Hacker

> This is an attempt to hack Dr. Loui's word-filling quiz with an amateur string-similarity searching approach.

---

## Disclaimers

The content is intend for and only for the private use of the author, its GitHub appearance is for the pure purpose of version control.

---
## Run

1. Copy and paste the quiz content into `input.txt`.
2. Modify the value of `last_name_first_vowel` in `quiz_hacker.py` as you desired (as type `str`).
3. Paste a plain text copy of your textbook into `textbook.txt`. In the case of EECS 338, we use [Operating System Concepts (Ninth Edition) by Silberschatz, Galvin, and Gagne](http://os-book.com/OS9/index.html), but it should be compatible with any source.
4. `cd` into the working directory of *EECS 338 Quiz Hacker*.
5. Run the following command to avoid synchronizing the content within `textbook.txt` to GitHub, for copyright concerns.

```
git update-index --assume-unchanged textbook.txt
```

6. Run the following command in the terminal:

```
python3 quiz_hacker.py
```

If everything works fine, you may expect an output like:
```
                     _ab_e en_r_     -->     table entry
            access-cont_ol list_     -->     access-control lists
               cached a_trib_te_     -->     cached attributes
                   _cce_s r__ht_     -->     access rights
            director_ structure_     -->     directory structured
              __ee-sp_ce ma_age_     -->     free-space managed
      fi_e-system imple_entation     -->     file-system implementation
        files and subdirect_ries     -->     files and subdirectories
              i_d__ed all_catio_     -->     indexed allocation
              _llo_ation met_od_     -->     allocation methods
                  logical recor_     -->     logical record
           sy_tem-wi_e open-file     -->     system-wire open-file
             tw_-_evel directory     -->     two-level directory
                u__ated _etad_t_     -->     updated metadata
                  v_rtual _e_or_     -->     virtual record
Filled word: 15 / 15 (100.000%)
```

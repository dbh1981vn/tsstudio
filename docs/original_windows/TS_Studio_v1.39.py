# -*- coding: utf-8 -*-
"""TS Studio v1.39 • standalone PyQt5 GUI.
Python 3.10+ | Install: python -m pip install PyQt5 lz4 requests cryptography
Optional Google Drive: python -m pip install google-auth-oauthlib keyring
Run: python TS_Studio_v1.39.py
Original v0.4.21 engine is embedded losslessly below; no companion script required.
"""
ENGINE_DATA = 'c-ri}>u)1RmM{2Se?>Muc9AZMV!o4dsoa!Asbs69vZN}POC_@@G9}XDtN75PWHm6D5BI~xVyAJj7+ef4wi}JXVCLSz^z1Bfaa~yShidfyQUA&Q&WVW3$YfHga=Qn!i*dKDU}QW`oOhgvI2jFkM!kMAolHkzy>4`R!@+1`H2VF)q%r9X`s0O#TrRh8Fu3TC+nu4Yj}qO`*l(PNMy=JE3`WL%W4$v9n-gOroHW~OoynE4XpB4k({8wU(m~-6<<Qi^!e01lilV)+KN&AC82D$1COiG{q|xmf-PevWLWyuZ85_;f)o?O69W{pStA&O2@T4*APK-%obQ(@X)$01H!T&59>&q`+Zm&P-Hm<@^oT|Kh*=QY?!po4$uZQQIX2|8k-n84m&=+0T_4wnHM)Rz38q&w+pjR5Afl=qOG?CLTo%gvIPh0f4)M`u`;y-h0ER9imywuxl^un$F$)I%E>n<!Dv_o{!3Y*4p*d1ILov}e64_n3wt;GbN&%;sYq=TGlzcm_kTE=75#2Qx|52ho`WI9HX<EwaW4hDm+ab7N2C8uO;O{i%sqtP%<0aFxS!YW}!C!=YT`r}cQczGA(x*s>jq35Vyr>{Fhm2Nl2?QZ8d`Z>W|WV$m@DU_!LS3kcSW6@=LFjlEi^nKFlMd?wa-x~DPFZ2~&#y_T$PSl$ie)Ma4JRA+0m|m1~6(uKOFEO6!w9|@)s!ay#QVJ)dFf7%&jGPBZ8;!A1J6PaFX%4zwAUKhOqL3CLs`yGc(Cjt<;rOe{ib{kuS?x3bE;0yOVRzCH$=8FvY;@R|5WH25C-^BoOs<9?EtOyGUlp;`;iz%kMRSiEL;5O8PDfp|P#QKy<EZCX)4?QMSeT5i1QE$>kY4GyJ7}IQgqO{5I58d%TGMX0Gni})ru|lJG#ZQ~!HzopNj`Vb?!5cq_fw$jAAe_@ciz4EPknC0c=YzSS4Ok_?uXx8EgQqDNqf*Y7JF$r&lR|_QKN&Q?O%<tQnky@BySaF$EH}qpE5Mn#(RxV6@ITl3jENRRjJ*0-D^xr7)=js4;-M>><ruCXk2Q9jaIa9wf)Vt$A8M45}m%!yz~mU&28Z$W96s(2koux?rdyrLM$}fjXv1ypx?d1WWb;p>x_$b*f*}g)*{xtL<As<kALzJL3Y%iR1Y2*D@<AWQ4S&`k{~K!I!b^5T<f)GTWhuY);j9s5&|T*@T9u-Wp%Sw->E*X(dRh=A-Awsd%Sy4tM6Bzak(ESL!xH3ch{=hTRR)OAJo?NpxNlgZGFAF_ho&3Yfpg!$^ckqy<RAd!ttPc9_9<gLckS`B_nq+7@duWjb>OMvm%gNSjF6*K9Ma%jiKl<MCx=n&MoZkKHUT4Hnz5FsUkv<m7>|@0Ohsa_1bz?VF)V-td<z{<K6YGjjim0y+Mn`rzpAm^x(<UgRF9c>0~&a=)FIy?QLy*lU0^Q@|9?DeRpSfFRReWs1x>E^(Hi+dTY=hj70gh?cJSPeXsUpckke?YRxVrKz$Svk0?zpC%J`ak?VKDF<M!@)-4c?%GVRH-Pqfz?X2%-EU6eNEop7Lwst_Ra@ou=g(Nb=R$Wvokusp#uJ6<iG`!0IMn9Yos?AjRVt;oBH8Pq(U0Er+tJ?ZzZGUdnumv_#nvBn9>OHO=tUapj-`+DAezT1RGJ94n9PB^4vjHB#(}T78lkKPbbsy!GT9A)ag?t;!Jznt(MWYYYUCE*ReLwf-;@m(WqkQRCh<gu)q?SS?4FvaQ^?p`w6*{QF9D?*Iwj_S?!ENmB0kn0DY=sB7@VL7FrET%A4g6E5|13PJ?mwy@R9CmbcDG&-mim^DqR;EkA8)HH)cVvg%a$Ym@OKEUgX-2!ZBLc*oK&gp7Y<f;b88JBk8>|C%g)P7%X)d~v|e7CL2iM1z+&^)2TP;DVDd1x@TgW@kJ}8?@8`Qj3V~U!`?d{<^3C>cbzSCKwp%xSZ{hLNJ^a7^n5XEjuA8+=#l^C-s>#L)nE<Rl<oBk1!WjNhkjexpqzenJ@WhzfR{p%vorcS_ngwI=A^jD_Mj?#BzQLc3PYeN7Sr3wds*;#lhV3zd%KJV4ZHz{ZE2Mj2Z!o$#?}QgcV{mdZhP6g5(}**B5$b$t+J{g%s}m~aa}Tz1MOL9z6NSU_Q9OXopML<ITL-}1roqRVSuIn$a!yH*7G#UP=?MR?lZBO-SP^~oPbY2eqiBr7u$8e|ZOn|8ggzVJ$|^#;6Jw{D%VG5zojw^4E3z18U$lvc<Btzl3`aCg|D18*Xwf5pBnr^iGZ2NsPyOq+EBMdDhX%;y{i>)5weR@)t#KA-%c<VS*rU97N{cGHbCR5>y{t8ik<t_oRa=I2WIT9am|kX8>(;6!R}C_2n)7QOy$2MyPMbh#+6(Vp)YUPQODps{o_4w|#=iQ5tjK&DW=c4!NBC9*-|tVr#yP7#>`uq^6NsQp+=r<#3FUyYtBIj;SHu_<>E=_6S`-@&#_T(akXT@Al>NX+Rf}P(Mv@?}h<f=eB&bs~wE4yeCG3(FBUK^#elhB(DfBx1Jeo-hn#E|8aV@TLsPdPiY21(6J0h4+--pXlR#ZJMuMk=;s2C!bre*zk<bTM6p}h|KD+i+~z6d$7hGhXZh9gq_q^UiwL-hmSf%p*1Gl0nm9sjl9aKhB>jK-6?T2!64esAnRL&3=DkHEYX4rLV4v14ADVdJVhXte4YBTSVNI4p+NAN1?M4}gL!6rGhSmMJSs(|s^PUMsv*jJeY{!v3@uj<C{PyAWd&h?sn7&Gtwz{z9oU7Tsutv=!lo^(E3q3xj+J-Izhi3o$d)tR)fy;F2+m6ZU&T@aHy|pTB$aH~mv-=66VJ^~IEohsLaO^FA$}|M7S4-u!lAoOa&5`P+^`u7<wR=mS;W{<=@P(c@Lw9j^u!Xzr>+qY@>hpOTlg(QgTc$e%zBE5=~dg8a-S7lX=_P5|Y+RI-Yqu>x2^Ikh5LQ$j7{to`=?21{<X-@W;VhM^R+!a`~(6N`~2N-D<SEM}6$iWti*@WHQQ_3sX-NBtW8(|14obKhwH5fB%Y6)!9Ut9)eq45o!rh;MKBB=@D5IOhE~#srx1TjLMEdiUl(_uEE`R`nFx<+W^gxokbZk-cd|ZAh^NIrqK6b2}8$GAKkDwiKU*8FEkS6pr*p!3u>9!QWX#Y5gr4c}-FNHU?>-fM1%r9E)7l*h3Beiyr|0CxZDzh=2C>pPFrU!GQppMnt{JmzISsQ4br9?l>$)KV$rfC4M~H6)hbX&>^^@|A>nu`Q=Ik15rXr{K=@(BYvM$HX-0fDP38U>oCgYny09at3}vI#S#RV30aAMlehna499mr{M}WG`XnqFjl{U9;rk3W*>gcD<idARC+Ai^S`(d_YP0BIO)!mF1{|fLnNZP^l#9`9$jMJT9`r4X?sZm{W+M^QqrQss8^Thh`_ri*-Hl!@L1?!XOd`un(MUr}>xb#l6q#6O`@RplF6d%Bq3%UcIMgXpH;(UT4f9A-AL}e+Bh@gH=OoBS<T%a~zR3E8r2G&CAEsr6EPTkHNf*nfau$<C@Y_5pz@#IW!@`_apo9y>PaE}7QYVb2lGlI2jwl!(r!`A~8q#G~Pr`N_O*fJc$#Nwor}0H+(#}WjizH~6HzjM4;0oSDs-necv5z59j3xxvL=&mP=gNwu5CUw>Cp(Mefu{DD#)FkaW&G5AICqZ?QZLEBH4OlQ@V7&w`|izuS~jk=UT(CJM>{_1ACNLlLG7HCXcoQUD1_3TD3`HVhr#j@sHU$f;0txPqII2UA|8d@FRJk$vIH7q%6p&bZ+71O@Y{~jfBO%8gVu=|?*z;A!*4p6Hd?`Sg)<N7G(upu1=2CJA-)GbWPtos8-@h`8Q}l7Lka5;ax!jN067J|g)FX01C$b>*?`X3X~KY!A3#nR^c<NWBwJJ}A>KYvuF?FUN&WEmQ{(*YuLrj(m||v8w}+V$F1-K`=OF#u(PS#^wiWB@5{w+0z`zUpu{ceGuE<;JU6@B7DqmH-Eb(eE-_DR+v8gt9jt8<`W7uZ2>c0JTte6S6_367eziQ^BKpizMFupkmQULtfja$x1l~s{vg3u!}M`J~!2WYM2S|UItNBYoU6bf=?oi8l`W1sQ;3=bi#G@32YP~z?vq|Bq>7sWdnVzHU7;HnpTVCeD>Exxzzo1kpX5MfvvucmK*WAuU4|2t570Gr{>KO0@zl%5(rLbH+~6};1Shb@c00-3)34a^IwgM31+Qf?v1-jdb@sT2wEoz(JaHhF!n-x{%bP>8ThZ}TC`Xx<dK1F0TyEq1tO6OiRB9(N`Rr{*e3AEYA*#+p!(wE5{}$lBA4J^hQh?9ex@W1xt1VA(|@*X>Lu-7uGE%~=kp&MYp@jyCpOi`azlyfc`N>!83+e^w1E@>G&u6}6hnDUIMTt@tVRD}jl5Ztz>FO$i-oMm;(r+(?cs#<UqtEj<V7Vb-%I21)Ye&#=YDyUts+bz`G;u=Z$e>);#X$=>e4?%M7)zV7qh?lL&<n1Z&TzV%xT+9ft7<MYn2enLTaymt)2)##RnS3iBUL~XzRW$hc@#`=2NY;?TAcja+A>^!%Jxdk=W`jfrd#@2I+MJSi8+yc+0{&a7fa@v#0aJ;;<6on(G_yjPyrN*$cWG+R~gP+rEwpuIKH#q|LcE_<x51QRhzcYEbZ1|SB$Y?+g*-q0q3$Kb;EaH^FQ$PqBQCrvmv?sY<dtO?o?;lhTw$^A8^+&bm5nknd-`(&%D{#xM?K-yStU7^Rb~c=<W7%cf@dH1wYp&(kwr!c-s%!ayRrS}bRok*%x8`iPwij46H?Vxmb82?YD|_p9#aZ<{r{enFhQH>bs#o;_&+=@m?0K%^IkxYa=&@>hXxs99*YqrB&8pz5Z<{uL*=v^X_^yxtu3HtSX4&4Fx8~M-)2;fe?z&w?d!|=)%3jU)?221)O~2xmt-uyzac#@5SXFz?t6As;B{w|R+wdxw9fstt+8a*AS#vfpmklcJl+oRqyY8bHz674{ReTSF@G;d5G`WV_zO!ai8l!Ql-l}8TmWv;r;{@)8X9AXJ#l}2P%W?6?t6HvO`i^5czO{;ekc}}`F{%K$6$@2tzyqz?e$_M4bIn@?3<H1FUIUz}fQ#)r_9{kLwO6SIt(lL0v0xj173;F$m%RY1Rkkn_-}TmA2Yq-xwP6D;fPlA-|Cv_Ba;*)&=HL&8UBis3eg!LnRk3P*#Wx9BzU{4I4(JUts@OJK$Jnhk)W8@V-$wh6i+Nhks<m!aJv4{acCD&gL0%2L)ckd<k_)`r!0#%sXv3|#>wwXk#W2R0d~Y4gi^^8TcLALmAm9U@Wy^I<Yt>(KYOd+5d1bri5Ja(BK8m~R)|yknnt6a{1%s`68-NxN(pdv^*RkpW5VlNXaXr8427tYb6k0<+gl(3Oxw=)xhrn9LtZ4O32R+%IwT`lYhize`RbZ(PymL{*LD^NywadT~tbtc?%ify5?yMun^=eqbGBD8b(F<^eN>yp}fD@1bD~h?;WgxikS8d0$ZD6P8d7v(o^Xw|{Hn3MM4?TG9s^g=@8fLoY2B3)wN^H2MYhtJ-;SYvo6Bf{N13y+RA7oYmU0Buz@DW(=uKKo1<FV~3s0LJrxq~{K4M39U3z%V<ST%yS?*caga|?(;6k?&23mC0iroHY1a{%Wu`YK~=RUcFis;SsD^ba!hu*!A-+FW;PfHF7;u)sk(0Y-+pps@<_fbW0}#%>YSVd^Md29{V@9v^e9IO`ap3z$^^JIke#HQ+a<0UW`iV0NZ$6Ip@EfXNOhm+FJQfT7+hpir|3$JZS6i5Uf0w+bkxMtq3Y*Dt#@s|*~mu^JWIx5}6e0T7f2PP2i=nZ7XERW|?~VXi>AReRm5IaSQYcPpSe`d<y)4;1U5KGtN-^K8N<pJ3*%0~c3q0(k{|Vij~&LrursaBIL{&jAlZNzYvel*+E}RKN+!pt?2Ca>WL}BRHW4-wSdJg@u@VD=$Zh%v5mse2TL}LRa_Kwzl~9e$3}rx7W?!)mQD^i`rH9?AckTVz$5A+CFG*T^!dQx1T<0^u9Z*zCOL$`numWC$Dy2obTTEtLM81uliW>>D8m^SI?du??1AaR$qVf_`97)2alhh4^F>W{d&tBcRG(>Y*?>1UayxoYs2YgYvcac$NO8O>8W$_`qALKua>IS#_FZ@=wNB`B4|Ikzjd(J3|?0ne%Kt3HlN?Gt-iW{Z1)<ihW9%B;>l&r`p)r(<Kv|-oag<^a<z8SzTd4KTbtX%=Ibp#v<KzY%_o)3Zttsap6oy0+IbcDJJx!z3DUdYT)jAc+<V<R8E;*VD(#)kFHW~N4>rQ3oz~+g-p-&}+uQkKxAR@){PpqaMW?YlY@PRBt)4xz9&HbomY#fP1&>a*njp{B(d&(`md4%9o$}JbtIO%>w)ym%%I4!?Z|nZ%SI^e>AHN=7Y(D$?h5PLBcVlO~e|}c&eYG@ntNqd5)%sxk`f~UF{+C<sqi6SbFCOieH~pRFm(QO*Uc0od%QLU{Z0E8$?3ULrI_I11FQ(^bOQ*wjXR~~4os>_Tov#{=^)FsecfY9a??9;fqpO2cr#9XDX73^Z+cmp88*X>AcJ})6@!Dp`^(M~iwe8k)wYj(Z_3`m{t6zTkA{=>PzkPf<u3b%@t@d6IoZX$1ukOFtIJd{!?MCg`x4QkuXV1P|U$-Y0e*1NGupM~2$B#C*cWaxEpMGQaD;J%1-yDXkJF5rHZToEh<dL&9seHNNyn118PM%lq-~W2oY`aV4u=VO$d;RM4`QxXrzY6@?i}U8@^wsv`Gq1B(4u%`6yI?MjYIXfI7*yJizC0NZzd64+ZLfd5<UX2wvAON9jW&lhXMYrI^v`$B&;2j#>Sm+T9DhA(KVB`DpDeYe!~R<1WPSQYHC#L0*e-WLASGe5=X2A^$zqU85W(tRb*&Z?LUs4B{q$<9H2D72&xhX{kH_YgZ@icuFE{S(I^W!@mp^;nd-2QjFIW0se01^6TC>^zcJ1{SQ|G~nJ2<^My7}l!cVnyjWxs!MQ2(~|toq{g{Ak_ydTa9YarbAPmBOpb{@3k$Urkp}_kMZxA{?|An`=LR_49|`;<NJutN3F7>+aKEPTKcBE`R@Zz4N4d^SC_ie?Giwy_$A^@%@YKUrhZ`&)hDD7q6XW<<pb?-iwXpAphAXAA5(J{fEWv=U-PgKL6?~$ILIg<MYwxvyZOt*@Yu($?NtH$KSNZ%dZYvtL<R-YW2ZKU;XUq$6wt$Y~3GyT-aURon9UNY~`kLTHbu(z4+xX?pGd;Ha_`9J^1!!=a<jR)_UR5M>mb#LOGbcx?C>qesZ!iyx#kZuOAj3uZG*5@AsZBmtNm<S3f>IGVR)larN<+pI`4)ho@)PC9_a`aa8XXkIsL2uQxhhElf8{;|uG_$6ww5e&?(0Up(A8x!S&H9Tm4eKe^vIT^<DEkGA(7U*-Rz{EhYO_4C!*vtJH|ZD)uT?j7X4%WM0qUw+c-H3}au{c?4$*&lp&b#QV}x_Z_BWPDcn?z6^~Jv_Z%Y&O5xTsf#stuGfpZGF7;^wV#wokHp6`stJU&Zn23Pb()EfAQ?}yN|1r)y?~@y;^>`pPy{qJ9hlf$FCb(J7>M%`hox5_D7S?_P_XS>t6kQ^lWYL`e!xk>eC1PPxijs4F{dwntk~B*7olG&s+OHpMHOI{%q^fY3F=$@lk!$9h`1|K5BNqIICLEyw;<7<J|BY`!Bq`)zhzzw+km<o96L@dz)Y1dtBK0sN4Pa)r;$+<>SV8KkuJczWM6v7y01cCl~ee{FD6y@5@K!-7i+l&gJF9y*2x1XM2~Qet+L`zunz$m!9AIWar^8dX+Cvw!R*Gzi)llK5iN(2dzx}myr&UN%1}*aqNn|%!shMG(J%wg&a|+yUmP6d@;-NA96WdvWXd}9CBwGm#T~DoGzl~KG8dpmA-47H|ov7@TxvIsf&G$IU9FH@>3?ma@dm~I?3g7U!W<YN?GF)wYYn-$L&$c!z0-gw^AVczuBF(C}`<*I2r&{E&5TS^Fq?S!o|riN-jL{L*H!GGHF~Xr%P&aPI6oQ^G3Hr=aPn3V*kcCyygaOmaoyk%@O++uA>fa1O%iz<D$Xl-wOL`7e&v)jn|&`&k~LmZC{ascThpw(Jve&_U*Yg?SF{&<5}>BQg}H*^}KW&8lM_@IgUlGb|K+w<vg{xa`%!0d+V2g!}0WFIUXv-UIA<6>cZBIR=r0@MyBJ;AS}6QLQSQ2A&=$iePkR6>zIyEO-7C8WNfh1Fzy}PGxC8`FpfijJ2c3u9uXFhIo%x$h9zzQjSELqUZxfes-*c>c;qrZiqitfC@$f_o}zfOj?1KW>1KE6sJBkkZ-@HjMD|XcEJHzv;S~yftl)Mu>*S$<sb%Rk&cgat9hJtDQP}8lc%|jYbs$$nha9gHc7<oG0ElESao7%)o^V@q=&%-@3o;&aVA>;!OIvIK#OEj$br_M^AmtQ9Lxn`7U0rw<wGoN$y=0WI0{Cz+jzL~7(!glLEgA92ZHf*)HG1z6&RJLSoV{eICg<~iBm|9b(HWOZ25`<qH6~hUr&~_NH6{zsM)9>{H>i_#gGwM%R338!0?>Vm3nWNu;dn-`aY+D^;ePlkLi`GaqnVh)cBTulkc?Om2R^c5z=~9)+ZctnM80KU+!H=%c_KV!jXa~O;OvDsNI#B?A=jA3%;!ayrTBEN)*DW)3>rKamr(4Bpkm4S#lEvX1GS$c1Y+u=z~|1XiYlUDYr&-UJE#2yolO>O3HS_DHEcmj!p$w%(MK9rn_LX!HyI%=^aGxLf7&}nKA<E%H71;W9G-Ui9H5IY$dIk6ZJS9O<uG7_`ScQnAc1H0#~`Slk_l=AhW@Fpm|$LoOMPp^CMzadn2DcCG`1@a%Axn+C_L$05*W4SOFUl@UEC7WqS>fnqp&!#AzPdF#eq6m56ni!L9_+{#m?@5aWQHP2_^*S&%mpUM(e!MZ{q8uJsM0;+Zu3ArroaQg%w`;QluNuaxw>UW}^#aES#OSg`CE>gAs<^ARc;<h`G{s=Ko}HC%5QC^xAU&Xh9$NY&TNznf>rEvGMjElbi_{h_#^uy?q(CZ(PsxdGnc(%V<SSDkj2feP}niRGfjnF+%9JlA)m_#c?E<RBXfY%-D{!D7VZ7OMZ?QESXOOkH2Yc&O~g=!QYPpab|j4&f+lpg2UKp4ny1W1F#06AI(E^`=>(l{h83hI7~sqYaZ!*bk?;mR&e_eS9TV<&oeNJhAm8iG<auGB8uFRdY<Nl6H1?!Q7B}9{)$2GR{;7T1^Uyl&wGcO4kcBjnKjTOUsG!keApUXWv+o#VLmwaRfI-p8XE84PuPno)e^2nTd`T{NxJT=%EueYu|@`NyfRmbP3f;1(SKyrE@256Y$i5Fok_bF5_gZ32dE6oT50Gs+aXDQ(lrW7!&@}+d7_s>pRp8H@S0nzt#5OrF8`*@l|Wa%NDrV9ca*jmH<fHenNsuWsXV=-g3i`5A`uz%!SYcy?Z_6336`FSPm6@Xd!Sg%*RRx$zhddKBR%E}D_19VRBf%lhtV|Oa7qLwCPNz&VU5{_RI0W#sN?{T62;<C=T%Y$GSbP*v^}Z^EgmjQARJ}!h#SEp*1;oK0pp8Q=!hxMpV@*q0!X2aM#F#r03FX^*8X}T0AUs#mirnyq(DxHK-zo?>SRL*$fUflY<4D@Am?j#Lx!awreE!Xa9dX@0*;2#YfQ$oGcq^$=!AC6W5uxI(-h{BC>E^Fcm(Kss=3({7kWT8DMlIPuXBaCzeO`Xx^Z(`LkqW%%G3T?e{j)fTVs)GP=5j&mg$HBel3@+%bQ#j_(v8M1F;T!ZxUWkW=__C6E5pVC-it&a^jdLFE4{*eZ(_?pFENkz8yyo`iu{@Xn~sf-F==-(Wvci$P`^YQwrG$c}w`_T^eF;U7`eAVo}g7*)d~91Dh|lo=8CoOK>Vo9U%)y6`WNVa~;W@Sgn=9uw?8tE<jw9&I!ATE?_+x9B(l?7buB!Z*;H5opC9pPbR}j6Ohypp(L<7_TOp%eA@5OH!)cT#SF}{WqBreWQ@C*<I{r;>Mb6lesE5Dke`e~y8NQGC+>t1olZyHWdfrXwl-ciTAk+P5V_<<9SI6K9<-FhPI#Ls$cWIgP8S7;HU#DlML%_U_e`EKxzpkzSh{mM(ZI=*ILT%Br#!P!oLNss^z-<jblQKAIXz)S4@R9+3Meuf!=Vv*vc}@vf5>VAp+5aR>4aTE8PeB!jsCRJ?Ov6V6HbJ3o!q;=&Yh_B+G^#NbJudhH@RYtW=mQ07r*am^>Qcj+lly=qiWA6>zeM#Q4lHI+}zw-h)n|uYGc<h(`-bs(dg0}2t}hu8wD$6=?OkZ)xo$l6_-@yO^ZDo$WAylI_J9IxO2|&(x#P0)Ms>jP$Fryw!gT!_So2ZX7r}x3CI@}5?*bLjIQnB(Th8S@-iHYw>{_^x+=;k7RAyE_bcBzMAIum44$%MT()(%yl8qyMJ)rrmj%vF##jcr3?>!UbszI9(Uv=f*P%U;)=2=BuA{l;s!gKb#Tr4j(?88EgSoWA{sc>uixHJ$OOd;Ha5W6646v=+Y4U{;OM~VloGc1{m8#Ph*KtveW_K_S_0Lbim=>!r8z%I5a7M9bOHQd$D(j^t<Hh44k1CzZD8@9G{2*|TDKPorbl7Q8Oa1U7)fVS7L`D9M?iWlEUrZn1FDp^>TuF%hJm1`<_yTxL<0M?k<q9(g$j0*U*f{<`Y-mM8hgcg<@S~OJXY#lhxHDl1c++?YJ`i%@yvEy#Vv5X`n61RDu-d;mT29~<|Ao{Yb%y!GMhkynnsF=dy;sCAj#TKlnVZkRqlSC|4VsHjOY+ylWt-1SrcnIOPM`M2)1kbqPjoyS4JL!;psPF%*HQaF8!1ITA@!J*Btuw46?@t8kMx7$r*jHg{<2#+O328Vqr9hV6oZ!*E^P-0V4@RXPP5Yk*B7qcTjY1dQ`1~Yq6>2+LK49)bk20=A(re>D`wf4LX80<kz7LdN9~+6I^D2!>##?S3&!6J1y0OJvoDXoLn$g;BISYO{kd*hU-^?}wI``ckr^>@Qq@RzTjEQHxHoc5XHQSM?mJ_?=dIri^B8!MX|V9#opVQYJSDm`vQP5|0VU6gAWxkWx#V3#-o>CEms3>Fj9@Yya-g={h!_jqNbPx#=}ONPYO{12PVzaC6BBD{TH^DE&aB;_38~%^b5iPp@W#mY#ZZ)9QKXZwpsR8ujajK&G4#UPHpuL#WtE~}j%bR$%gpzlgzSwi4=hlxGamC^#YkT8xytu;QWu@*(0>B$<1;ZU@{-TevFAuUj)ur=04l$Ja^**&wLW4wx;yY#nYb%+_Q$kiv%Iq&o!FJr6<TJN2`Cy)?!n8YFRE^f+<>}Hf+i#S?{?0^e2gthB^T;_q>GE))#T4P>N$BhS{>xlZF@<TyttqdjoJuI5EZ%ZCP&eR-#$5o<6C!Id<}2+ip_9kU(r2ubnuRX<TYX!<^x^XHO8Vw`+(98p;ee;k_c-=7$UI^Qphs!WOpm^^_#<iuIK0-Lb>iH?H8raL?veQ8fA>fMM&PH_8Oqa1LP}t(=8f~o7#zhr82m{3<c!IE2&fZ2?~fNA@#MpC?b9SGG3=g2M15?I)160_%c=$(h$Mt_3QbT6jm0r@}=Gx%I3wTjpG$@VMTb^8BgkiGkFsXPku7!b((d$W+s$pjp!;mInO%5vUJ?(g9j$yn^9R)TT-ov8}W(@Gs~S+J!cFs&3Jpyp6b1D(nxnFr1i8nOr6QS&H>$^nkTT&$Vm*-Kgg_`B;JJ31VI{&akJA&BaLv_lc}>}X{hwxQ`BcB6>e=QRGvDR^}aBYEy?NJ0w-cP`KT9JzEI4Xax~4klhb9QRW8%1?Wk$me3*{wyfgp6u*;genonhg7skrWbPt!^a``BwfE8(iK&Ym^XYyV|c%3zx8<3+M!A*2-Q~^+#F=+@1O+c7@7*FmNhFBMhWwu$Bo^UbMwYEtiS#Leki{vS3`XD*86p9I5O&>;r!6ilbdvY~-syv44`|vd(lvd&~&O~q~N+nL~a;_+#)D_CFw+78A-8Cr+U<ow2NI9}mI#4ONeZASH^O_vp6IG(S)Hg?T3G@4vU!^mj&}qgBQQnslZ=pbafqo?2-NIDF?X>c~SHV+s#JRPuc2g~16<aj4)zB4=qLG|L3RnLu$0#>zJGH&7HNIrvpt@;P4-WRWR-Yc!jN1Cv!S3Eqe=HIm)c0!44A`j%tu{Y8zL!6&F1~0izOEk~zPwm2EgpSZcsc%b1^?y`b1&~574oG|KQFwr?h%wq>$?Zl?d`$>hRpXzXSA4mz;$O^J&txh_>%W}V*&#J#v|VacdBoDB%RZVpySwQ*DIX@^@n-0khXA_qi=R0(_62$$$GR+CIQ1YDNwj04W=OdUt+jKu;IAb7;0ly7iuaeQnXVe#~D)-7c5DZpU-_l4EK{pZ}^!unCSDp+&%hC?z7DAxqG5IRMYJ55BPg`PVI;M^)&jb7DN`%rWdbB(TH-TE59FJ)Kk;fZ>V5Mwd!=+ufPqFlaHE7^8w}do&fs&Bs#_X{5Y2f1{wF0?cb*l5?>4X!<Rb7<}{4eIE}o#m?8k7WaeeJ$>mSD`eX&V&%*qGiwI6~2kq&*H~+P1Oy2%ezinJc^Z(iC#<-la;AxB7@%!}mFQ-QL-4B0Hw}epqPV?>m!hd^cfnE|hO<zDD&0w(*@@|e9B#l<8kSVh;K{>g2UYtSE1mXilH^wRfV+qMERUo24tc0FnQAToz=>ju1PBl&smqiiY<;)k3XnD0h*)?}4iclDPLB&O}Q(f-jle2%sx1t>9mLA3vjmsorALdoPyJq$cAC1%Ot9n#(eY(*~ToDRvCVZYt7IeSIy_MX(3`ib>Pb{Qi7mf3X?<7zi38+OMmye=bC?Omfn9vC7C?l;7akVB>zBJQLnbtIC0oT&__p*A*BWBvtJ3u6M2r7I`HH4SoNHTQV6Q~Q%am*uBXCJ^Kq{JamMokK~aD4df!=q0h<`R-CcIGW-j}EOL9z_A@f*c?wX7~hMaiiU}24D~l&4@M~>C4Gb9N6>B6ooo|7G4!73PG$f_05+BM3;T0fnLHWdgFXy=0;C;Wnn#tM7UBy<B4<{!S@?20+>GFpB@Ra#CgnxGw=|-7o#qVGd*Q<=bx>7AbWmrt-82*Xq@wfDS!Bt;KOHvEnl;FInzB%u3W0ECNu6o{Oauwpn6kmA?OzdUh6}>N%L|Q2%3pI%!4%qQYsV;>d(1!ytg+bi{+N3o#Xuz*+@#4p{R58A8S9m_H*RzpxctnG08xpk8>H0tSJvVKmicV$ZUDWj3265zI(-Jm;5GThSZB(mq@c9)+EtHaU}iJ8FzFTRpdy%X!y+cqHhJQ)tFDlGniFU<+ozyzzP}$x9ZUaW*It$>f%0s&(JT_QxOr+v-qag)7=RCqoDbbQ8mOvC9*cRXpGx~X}4wcY3IG$y%LA%#5;Br4z+bcCnGwbPcaR#5vetLe8rJgSe3Z-W7=qxFNBT9o#Sr!nFwv}G!5utQ*q2_EDn1#8)F%@C}}eZuhc3NvBnm}owxF3920o{_BTz6c5SEKH&G`yE7!M<0UCHQ^8`YVG;g{D?6)1`IvOQyk7rzQsP3oN7hb&qrODUx1}h7ZIfdUbL%z%2&B8S9DEF*E8-CY0YAUxJwR)435Vv+-yoJGMv-hJY98vVE;p_X|qD!#-KRQ@A-85oTuKDiG-#3g0nASsD(0?KI`R%WJ@jP-VVVNNSZ--1Y-J~Cac2mi%CqdF}9EV+*29kAp)1Ev?*=t-zzmg}S6P{CLk*Ri7_{fJvL8M)m*F3Hp{p!H+yEnfw`lr*YxBu9mv(GLkK(1^ttOqO6G(N1u$-6iI-MCf&Dc<nak-vwWRLvD{k_*KBNkEUo34u904M&WTnTkphH5VdK3g`=AsjWx6NvW?3y+2bgm&@wkd3wsx@=pb(2)%wZq!N@GlPIC^d5)nWZ}GnouO=PrKihg@oST-pY)sqnbz{bJ+Ngtq-v%$oJn375w^vUmW~tLZADo3ozI)y+l+el+pQS7F89h2v2<5_{OUXL@u=^P~Z98<3&McM8a!}#pgz`b9=zK->$(N-C9!!0^_N=yDNB<D-a#bot!}5xTUoO&SO3`ovI)~~b%QPuz`i?AVxh4wRPGF&wZ=!@}`DW1wtTL4@yMc{Aw&UZwNf$ZEYG%2@os>-!woRYv+ktBaXvVW`WV){HAk%ZbfDRA))P)!v=Hyb_UfHL{E!zxG-gGRxLVrCw2&nJC4?LQH>9{7wY&lNZGiCRDp%Zm%`L>V0E?o_VzZKW7&=4Hk_AoxDLU*dsSj>u#a-L~>WmmL;VYwE{_;gPd+6rvbr7{&B0FAGV0aOTNWx6(vMvAezG&I|yTiHZArh}OgkWoFT&>3md$Jl+U5P0}x(IU`@1DZ_5_X3o$Y(MaAnx5;UIR#d_Hi<u1Dz-(?u`RmOtV~Pf(XDMr_;gDf?NQUU5%kHiRl+l^vRYZXwTW|G3k`6>vuu&51R}??T~WsK9g`CnjL4x|n4-4mwl2;M00@x?WVwn}5uI0jS9~(dSW%e*Bt#0Z^P=WV)3;<<y3$IffS)1-^zmg13m{ThQA?!Ua#_}J-JlY;>6w9;oe4<GUNLc*7nCiT7kF|mW(C8Psfs812G-j#2rbhti&|K>il}8-o}92{+Z9>MF$Lg}QgE?c*Oz&ooR3`MvdZ@ZTh<ReITEX4SHy_zGDa#>6*(WYQxWh00$Sy$O}gq!)Cb80vV;rh$y7y-)Aj;Sw(k43EEjl|m>HH<td>BZvSW!=bg&?z7F{mpNR%@r3OSA`u?l1G6&{u?Po^prGj0=jB-YLeDvlVP156hqamy7sVo<B&N!+c-5xcg60?^Eg*U0tCay>yvrc4E<uP_~x6Bu3weT$T7ODJOIVsu0Z+BiKLw#Y|QVkDkdkt71fAqmQ>Sh7vOY|ByjrYqqFIt^l+_rV=2lCsKjOulDXGS7D;#K3bT^?;K(lIp;LB-vS(zz=RS0N)e!1IL#$MwgPd0^gEr6a-*^B2@`wKNYaGKvFP38?{*h<CG<UQ=%5uKtdMW%a*C2;z^1um#vB<*s|%#xq%B*Dlv+pAzQ9EgbKKfVi4s(agD(7RI(DdvTYESL<OWg)dEK2`WicN9XWf`^a3>&@B>Bj#C2sW;NhmJc#kKM3!Nw|HbJ=hxIwRqUs!>wm=!p#qzMyfrMf|uEoTpklxWQ&M^*D7BjUCp@8lX_LY`_HbQdVDN4#GqvDB(;M8+lryX{7N(Tq{UbWK;4cWqO$ECQ5j+w~MLH{AfTPA0Lc5>gN*Y85;y2waWT(&e1;i)TurC$_6#=+TXak_BV26gRd4Ng80xu9R7(@0l8zm_Fp99HC#4&;rvo6)u~BrPvu*kT2;EO*jft0jOVg9uW75+lFXYD^UR&%T~blB8dQsmOWMi#RG`Z`bs>21FBrqiN%ivO-U}GRrVF4TIGr(B`mPcQj8z#q@;=IR4kS2`L6871h0r;LIoUKN*_zn8YHKw%45kSWGzUQiYg18N9Nkm%ptXO$qt3aaa1ASmJA0Rfv)dVvdxpT!5}2|kkmGn@WX1W+#m>I{01KiB$ZfnAFga0IH-DbJ(`P12A-s0i#WRM5y&Vx9Eji3R0z5iv#h=Ve`I+Ot7I*7wXH-_=s%w7(f5@2w@AB_Wx>%cZQKEh$+iPW2>=M`Aj%CCo?vv9ilt<C*;C0#`eG3*O;nR&CkG1&@02Z>1QnYyNfJ#av3`D}14zbegPTd5BCf2_CEW&WN~sR!=PFf!^(B$C6dKrAE2*<Um#FwEw_-|6v*~tWUsEw`M<N~&$dlA<3oTY?9%Uu|p@b+@2SQ;fWztjdh9szHnkrNkrFGiS*FBX4AY^&)0g0Jlre!I!ZN3j!CLttLE|$rO+x9A^t#lr~*Hk2-3aO-9QG*2oQ~D8%0|mc;)iaTFB`t`y0~j^xOC?gxDwdKZcExcd3x%ras~*9WERl480<v>xs*-(5^^0y4mR}%ulqv?C50qABNyri(a8)k;%Ccxz(hk-m(Ke`2G98C*RrVq)!d6Mpw`>J#<*THxc#mUOB*8%cvrG-%SZ`12=Z@o-<?J1&qHqumS0p$cu%1YFgxprS6{Smo;sZysXgtT3x(#qCkc93KR>@(Jxgn?EJ4(9;^A03gICM#~tQMG3$q;QrkovL}B6B}dQyn>l3PgfRVpU}U07O-TSdumh6jZaKsi<@xu+&{)@>-F)Tal1*p?^qaA7WeC2QEaTQhp(LBsya0P&97aqC2VOmq3jLyj#&42udk$E?9yTk}gnLE-P@$lGAk^J8)wB=4*LnRZL%sH<zpgSrrQ?IUcMX(^C3*L<_Ju9m!gNqEcK*wcVFX3%$MU%0+Pj9R(iHrBtR|(uqB#+1tuA2#7{xl5~%_?V#eS8CA%BmPtnux=Vu5l4e0!Noa5z1qh(9LQ;qpU*q2%sWVdhho&ZlBq>1>BRrsq#6f8H(n2-pu4=h9(4~~hgw?HR{KNx0^_4y1DcuKZnl05gx&d5`5UU{}<w2*DiU1U7#n(KSoFZ}Cbosg*H-I8ZgYJj+R1!-p4J6O^<*IqC{mLX{l<W~!K%lklS1gGJ5DW@WJV++FtQb>8av6|TU@7Z~Tp2P6OqXRVm4xS^4E;jdLqHQrfv_5s6or0i*(&KMyU!=RQ<lZ*N$~gpNLgzeG$rX0+^izyybswaIWP2~z)`t=AblB7$$hCg`@}S40mt*b7zgR9YRUZQ7IjBCRa{>+=mx&4%s|suwxLJ2=*y(<%XJ6l1e&~rsTbJFZlv{=Nf4c~AuVM<12v=tZV1g^nwFN*Krt0l<AX3dl}!sOw<NqVaa&scWc*6HgzR%om1F`HNg$21MTr(-9fFKk31qTDRV$=(NGlf9ugqBLPj(JoCCNW<NJ*ASM{;%1Hu)CB`anpVQoIFpy}z`40eOj;;GcjQ^eIZh2(qCtP?7+T-pO(XQ?MXwWZTddDrkmnYH|YvWt)uZvPljckDXx<WFGlIg8&Mq#ZEsciLgIxhrFp3Xj86mtU^lo(4AG=Y|NPCUaZiQ40K02C25GzfG7zzh!1SCgNs11v?%G)iwiatAS;K~m@Ij4J3vr+Nh?A&`22;?gr|U^U{DwsB_U(Vu>UCut_H?MZ3D<K#mVst=|>ZCE0km#%u`NWjKe3%PksW2bQR$;0IMd}Nj?ME?%*AqbO1od<|K#&B8<ijq$YPFCmnDNV4`f>Cj+5E&S>JLbTK`Rg$l#6<Xq^~APVY{WGFyEx!@-ill{LHYP<}-z}|^6)IH2oIU>rWVfr4spdlvlt-`KulU#%zxs#E$`B8+5aA{PC$8bIt)+X~scsa?0cDOE7XcDfT>VuvH!E$r|;Of9ghueY<3Ij#tlMjPD2AsArC*cN%vOr!-o71qMEJ6TIJ7Am@H|oPB^}rOaYOu%v0O7Vg@|OdeoCffqn>xZ5Yx6T9oF>K9bVYtZFK)P87sSizp6Ua%1f4Gs-vWBcf<5BE8B8B?iPJFX$k{0zH}rmi<FeNr@Q3}!n+{|hS3E*Aq=A7TOIJB>OnNHCuCS*a77Xzji_;L-6^q9X@LPZc!^DK?M?}G8U_<%z`U$6PdisLb$s{<VO<(l^Rl!qrVDCZ}THF?NLx>gOBf=s<GW#O!5MuB)gz17K5_f0s5>i+YuImv&)BI!~UO+nv0oRA5A%6sy1E&Y87n?7%9MC9uPGEciy~Dz3&n1ru!=O^8xiic`sU9(&$k7Fmpdjx-SY@`ZY0H9S0~rB~mjG0`Os|%(v&#e?`zGgOf)H|I%Y`;qz@LN{jI8}2c6fm`6Q|%h7RZ<$M&WH5(#-;f12H>SY@e7U&4Cvtx68f+lSmM0$SGO|_Nie-z&9<`2dq#?9bPN4{Mpc>H0@Ae&RmBWi6ypTKwcifLhKWe;bXa6m)J1|!gCGC_J@+9`hb2JcoyR&xF7kom{v&!(W5UsUNC<P5au#qC7>JPT|g`HBmikSO<c@k+O&yFfC&W3fk#$8KJlIq7MiRxhxdmF#8_TVJH$#%_Wxl-L<d~PCe73q`Is6e!gOPU6<|r?KEUPaZ53DU!-1xFZLum~J1)~8grzWYI319T5MzfZ0?IP3gF1+<G2CpAx1k(G=L9x#m<S&wDMMwk??)ouk?q1XpvOf-8fpcUEp8X`gSJFCAIpSg7kxu0*+f-pn~azrM18>CPGX5-Tn<q&Ndiv0<eX(3bqHI50}i`HF*;xL$1k6NB3<^6f|>KSo$LeB7RrL-^EU`+up%ypYzGRL#c6V1;9pKxTzcJw`ykf?(3{5rc1BX3>w3gG-FO~YL8~Hg+#$^tE64rOz8nORNYg_~o-JIoq;&yFg}at_eRzHWd6rC{`zC9Vb|6$A6_Bkf))t}~oTAM53XPhdRI)e?Q3^GaZ~;)GH-^e0%^p2b21G-Tu23JO(0D9LrGuE{6IlYnLu?XJayh8^5No1c@@rseIW4>iu1I^NiZR?k%H%h3xj%ZHh}<ly53<albXC~jOx`@3*WdMMV+9P1cTLOWDwjK`<QIm@B6d@uy_lpb5DO+MV7cIudndqhsy+Z4+Vn8ld+m^LXSwZyh4Mxc`J+i}Lm0Ae8Zw^V=nB}yU8c8ye35pL_HB^{e;^*G9Nr*Ehp?7?;U0(ukmIfDGBIeDsq{7y$<DIa!iK13RfL$0L*j<>fjmG9i|Ya<z-2A99>8kYh@PlVPZ<Ti^sp0GbXj&mxAZ_nj6bBrV99yj{P<SItJre)6U)YU=n>{%E(&+agXsm9+{`!0<s{|~&5HI*7*^0FAsQI>!JmLLF5?oq!zg^_(>_a4o7a_SgS?3fRy00vPnPEpgAiDzFVci2KFbNxxoq01;WX*?Wga_bOgL+b5CwXH%9Ps$WCTEnsy<u`Sm!go`YzdyCa)*JN81T3SI7wutyYW!42pCKZp){h1-|+81IWbl3ru1Wj#>{gs!gIe{#KzTSl0TqMN8a}(*ZkXO|ioaSOu(CLKHdF7>6+sEyC!pa2k3S*tU{`fzaKV$B}x2hIu`)EFcMiClr@Zq4%sf4ZRLT!D-t6mpmdMFI-?TJq6^-0xBu_5xB%K9p+J(64b<iX*KYO)q2cRF>0G)Kt#Gi4ASEL6Q4|LUxi~p%WxP+05LKs0<|6iHGpoof53@1EIIAcESNqpQ}SG~e8t>In`IbM@iK9KN<(|`ETMx@90rMO)dyH4?dCE+sIb4xWjZHj3^j=1Tfr=p?p&c)zhKf4tSV$-Q78qcJ&I3YSYdeN=k%2hN2+Xv_$PnE$bjTxUkFN2U^3jugmFk*QX0rkDk$fJ9b@5{R{||um==ym1F&9f8$c^C2?<2p0Z7Udu_CZpps1Hgmw;+V&x>*N3DUISw$EuO&(O6=|3n&V2J?xxnb149XxUbqQD6)t#U0+VBJ8k5TTnnqz;nJ$VJZ~HLVH=no?VwiRUGybniPeCS=a;!&IfGDq|HPdUQiNT*25@j!tqJsa$5QvcqhyvLbXh>D+ah#Xq|zm;5}Fot_vd_OJ(yopfiCdfv?CuD!>v*d>%V!%kdd6Ei$lN(7nfLpS{5r@38?DVeoQ3I5pTg!-_nd#PDoRgO)&OzKZdH03g0x;f*<HEf(9P7Lhp6jp5Gr3e;4N;K3lE=6GDjCH57VoDX&p2pL1ME`-LOng=m^5QWR-Kwo6G(Hfw3C7?}8P6w=x@Yu;ILVF>c_E`-R(L+SeCegA*ND19l>2S2k1gv9E0@A=9dUB4_6^;#{K4>DujC@W9yx&;iT}3F2Kyi!H`~q9R<!##U^p)O@-}Kfa^G@1+1Ts~4&FNh_XemDTO*liwH>W}4rW_Ob^@-GZzmgP-fZ<GY06$f9PMRKMl<kVmOlS|#lek<!vl6&#k;y<v&byqXWLg&I)6SU7Az|d|LpMI-E~X!lVX4B$$jGRaS*Hdspf@pDr>00Wtc~Y!ec}=jC;_KQT{cPXvKi!;IkwGW9RW1N<$<UU@c`8adEm%!q;D>Vkcm1jy~9T`fYRU&uxw}zY!Vq{?{m6B@AL(p*p&r@Sk6<>7`ewP3a>yb6=0~%b+DYS>xwk=x`5mkoMvtw@cwL>)mf%__MY3Uchh)CP2=?kD<E+k@e+spr{p1|Z!qfE&gL{YEIH|TV;Dvt^9D)-QqT{$56336!RIm#xtCm?2koD*si^vZ;zyA_{0$&9X-zpzgzfTr&|W{kpTud8X`TCn2qvYF=Mm73Lz!XVkk0ISQN$u`LD9AVkE=rR+~jsKZ;Aq9z5)Zzq6b!K9K<DP%v{E#M^0fh@lG~Y8uTmD0ci-zCj%NH#jwn@L&_YfOPmG+X2KQQ-zItYJ&qA0BgYhdfS)-5`&uw#lUzMKKbJx*>`1=?!)4d47`soqIBZ*3<jH3JfYV^i6~P}Vn#E>YkJ992@GCr5@;thtKaU(x<d#&M>i{V<Y+fr0mjVZn>A+`Ilegy4nZvS=)Ek;@AfnwUo>RyxqQ5}cd=TZpRPytyKCp-;nH2Pm9=8Qc<Z>>()yX!X#rqTFJmEC-MQDVaCR-3o#bcr;NTIHC-GB`8vho2?WB~JS9#@6k)vid>#tb=lDP(~5<OF?yd0=5IvVAOagIV-6C#T6g7P6WCk`qv^IY!G2mdja?Usx+ng8@`b*6m1}bICQt{W;{T2`XF$h94m~!4R}WHX+juZ3mE27R3w_zoZy2j$jB#wPpT+em#eDaZU%WlGQ#13lObyI-r0CUT2@QZYa~-4k;<Ld8>jRpdk|xRzy4m=HW99l6iy0A{&x+u88oMhR7LU3MVYJ4|C8G`8G$J1l$h!h$&Q5^@08XQ|1!^y~2yJaXB(nfdm1kJ=%0B%eY7ih-G+^V?Dq!aT>fB+9%7BfS;gsRah^Y1Q=cRJ0a~+BrxkDz(X5UE5-$0Lo7Mq01lJlqbeee#V6l0rO7er3jSXaR-e+TE!yHI(joZL-WMp9*NyadOoRD3xv^*+INu>Rs>|@C2Wl;gZ5Iv`A#N)|Mre^;r6-b(0gCZi4+Gga<Z&}Oo`gM>B1#x@=iO0ClRE*}z<ra`9$j#Lh4;cNktPQP*#aVf0XP!S)}2QYCZIG5Xy7!-Y>LR`G~nzr54I`r61|b1id<y02~if|D;CL7OQd}Ys8)Uk$Sd$Z@=wz@ha9P<%k}9!T?&}tv`^cUL@N|SLkz$ZY0{b;Q3k|SCKZX(MCFms62wQIIo`4$UlLKO$9+_ISJ4+~+TjRDUZJq<QgIF;$Bcl<o(QcWX-j$=r77kOl%|4fEPkz;;7(8Hl53pXg&9mw(^j|+xG1~$I5x*2gPwFwdO{cMx#Dv^34k)&QDoWCF1YVR0X(#A7z85Lx6C4r#|wiOGRqZ_Jy4yY@N>HX34E7yL&9N?wg7le=nhH*$L2$PQwWkT>4RPtr}z}YE1QGTP}Jo#Xr;`-=~zvZwkL^~P|Oe(jcJo8n~WloOYFV$%VIsiy(y5)G*ut8he6s6eIpw|_)n3hKv$FG5=Ai6hI5&N+=;RwWjF*0+?XUGmm!_lWqP#foo;$UT&;&ip=M&o%BHYsazpYM3E^Q=&^&B{GkB55Y4Bi=<qAba&<+UEJkk|%W%4|1c2tw@p@N>ELqLAed~I^bQD6+E=@DY6?%b{jSgCM-w9zB>mPq%Yn0;Pza#FgEfFbQtcuwTgx9M$V3J9R%GKmu%kGFP=6~j#CRq0K7Iu#<bpX2|#d&q<8LeU$3SsweD3@-ZPc4t`chUZ~doTVG*`A2++Dn9%c-xf%B-(C$vQM90L`K04L@)F7P7$4AkUMNe6)L8F0m$uE-=A5b$XL(F@f`{fTkM8i5TZ1Vb22GxTITYidXDQ_U<b1n;c%_6N=Ak(crpMioQoU(+(iwKIjB=^M2bJVK_JExz&6k&}8_MaHV7k?)8Hy_p#SrfEQL~fopfSm34Tc}gkcH_rJ9L#ee{`MWVpF<cno~t17x#qB_($^MxZD_DE)xZeZw(zO)D=1s1NiRs=$v<SC^2~&@|HUz<bV%*@%23@7+uLgS3%@IUw+mYeZStAG-}<jSI};O;L}wozg0*-Kr(ysK0a_S?n>jcgnU(6iH^IT47#m6U)R95Rm53GiJKJ?_^(Yld3rED51$DpdSgef&yPL*o?Fw;sLMNLMt}U>yEp$0zh&!uHuJBHOFCUk$^YDMOQMpu)J*7@ZBE^}b=!Rx={pN%E;%5CjSuGLm^0+WIc}9Dpk2U!w`T`YG)P^kgN4?ich|vE3))e`xo|HUG4m<P`!wlhyAbP#B7hgBB(9Ua?bM)PWOQT9d<G{k?VXNB;<}tU2%)Vgv#+QI9oysUa+8C+<20f;8Ypj{X|@N(DcyM2Q`6RAXk5##Zi)tY-PE9a45oBj0g9><it=o;I6AN29gw^jKpa<$POu9&%pPFB4bf#!f*BOj4`XHD!E_58BILdnXETq1&p>&)Q|U7WpSQmm8m)J4{*GUZZCuH-$+<-5GxsCiaYxdRx(h~C66g6>3`q}s%vvS;vRQt-0o0MGtnOKeu2@JOdgpcvMeQVMvhR8KD<sFOT?972sTg5oD&xKdao2+Sp1f}%y0f%9PF)Uw5_EN;y0<IM_m?)igX2c`<(OH0giXxuXZSs#lx#1}KJUOQP|y#*pDL_6hrS?@DZw`X@GC;U-!}0P+C;|?W0MSa(ti7oy<Bok!@;;CuZ5E1A_gj9ma$eR_voNJ)5=Ot3?^rsuh3~^tO?SSm0Tyc^zfd#Na@a1QX`-RI?l0lkCy5<_p+bUmQ0mhKDr$Xql-imsFHmVX0&3t{cvJ1%g+`54H(Ra3o><k(;ecgz?c<J{(ab1e6xi_F#UpyT-L1<=^H0V{GFm|opGn$8}ujbgaEt>8zXg}0ey@W@jK4Q)AkOj*VF+0rTE=Dw2qxW{8cY;DxTYr$~4ta-a~Klv3nX6C1&5EN#C{Be)}5`UZVX-Q@7N$tP}A7Vn|nO=V|P6-bKS?B|`jv^19PM8LT`#SgSwTe!5?muU7X57h3fae&*9f=w&W?LlxiN?*<H#%ER{Ce;C5Zc>C)s7RCd4=ilUyzxyN2soUt>dPP8vmUy357<z7)({BnO&8jsi(RhIZJ-T;7+#B#`xWrUk?rp4X9eiVKSHIbPdSI+=@9xx$+Ro<IPVFb}@%iKJ`oZp(wVj!3M;GKBkq>^hxLEr1^Tox7-#>WyIZ`h_N9t!U57*YK2i2E{lymg*i1LJ4@O>_-x-{qB(s82Hyvt3wxzCqAr1V31qi%FN9a-P{vtId=(cpF1m$#scH@=?tx@6aYW$q6f{bhB<SNy~m6FyV5yeG0HehB`M&3qFYa&-R*bA{SLN%klDitaa_x$8L6X0u*SLo;-5gn08IA5~1g+Hg>MLR|RAT#F*5uw({w1!H{oV%EjZ;;kV4s^l@inKVnqo%D4DT~f^G(UDwir6w06e(He#9*i&+x?JopjVAGR8r$EqOW~jBg$sb`-J5@D8WYkehVuHGxJ#oK>lR}e*I2jLAzcvq8=ju<2kc;y{|#OI@K0Bwk0#x#^EVywLW<-miK}*Y`AHG+Dqy6gz({!W&ymlAW?xFo1Sr)!lh-9i7ljFbjdoq49D55(ne_zx?9GcQ=!uqQZ(h`?e%|$qbiE}#){(xJRC^4!ds5FXrCmij7>51X0(K$sw6<(zIYTXzpXOdVtO+{-)Av+637@;Pu*=5jyC44N(0H&!7uelA1cr1(QwFf<Z=&Z^^a+V8(m2Ju!B`PBO2ff0KQlH}gOnG-{P!AR=2L!&VfWs>`9F;Z*Q#}lyx;!g@AyKfxBrSiYC^M@a%DMdB0N*BLB=!nq$tmhoihoPoSjMHs>~!d=2JkE7r6;LW!9kJ<zLasmj;s<>B@>WxU9!+^|CR==x^e5`gEg`)~$}!S@@`bzY8h<4Z)hQ2ycUI=A<Q&X3bZAx^=1o_vPp^#`B{VS3a$H=d#9dj9!~aF@if8K=bYY)fab4iiU1@d`(bOLlRSN{)Ml6;pVj8c{L3a4+YG<I#j!iYo0iiS8Qb|Cb2zsNaB_GIw!!^vxToNb@|;&`cjfBfImk+)%~AwH{eC7D?DeV^8>-1iZhpge()u)n$Jiq$(%PE{`3XW?qp|}ugqV4b!TM)`ueEpVoY8Mp<Qwk^mCNDKmNzfL%ZWUQR?4#e#`L$XKx;l06_Y*zI1(<S@askT~m%;0IMe_FDk})>8a^&q0K=Raq*<yeo<+v`W)xf)?O-$#*%6-{Y=15J?D8yFc%i}_ge5<K%zsHmNwb4#PU=o<GX&Rtlr376p-jN0cmaGsUa`SFb_u4tg#-&-Z^bp_p|1vBXDyt1u=9RSM+3;cx^Ck0+B91drxV+Rm;yXuFSV9MH`W?gnke!=a*e_G0#5bXKV<NXpgo0{Ot2K{EVG?!zNi)f7(X)kM+)84+dIa_?4{u0-p=BLqWNWk<cut1zkmAr+h+X(}x+iqmA<JW|C9DGLPF?0Gr!w7IgNx6$PTZ_mj36HN+@p-ZY?>r|=<qb_&Cd`=8N>vOADYF<p#CgJoA))P+E{i?P(A#Qb@FbdNrW`+{7q7=wh&3}DL(@|{$|a@k5W-ngM%`RJy4W@9qygsM32JVbR0YTn{STJ=(ES=!8lQCRP^#>?cBC8{}Mg<SdbkNFeZ!Sb8->HxjD1r_O*(Iwu9)t@ERp7+$OO%z&Az4@k%`96hsWa{0Kdab*3)Jujl@6E>Drr+WGlR8(R6t38Ym?vj$wUSfSUNTjc#8alrDHA}hO{vjpMI|*Jlj;k<=k{})-NiAtE{u$0YFkl=KKBn&Sp^}G{{OGWwcg6j(zQhD8|B_<f=K_NA-q6rHt5P|_H#-^K=hU%{n4HUm-tUH9wMcElfB}bOljXD5OYjPKLYYtd($%4nu_Ps!}@Vtl9G@%q86afzYE30i%f)Zb@{#*KjD=Zf{I=#O)CwO0;oW#Gp?VIySVTp*b<pw+}Co7Co%nT^SsB;UFQp>k+}BxIQQ~0+UUrBBrc+y+n<Pw2B7%uN5&fY{8-B%x8kqpUhU4iH-9yi1`YE5i`wlMdyirOk>js95HU~ux@xmA1Wtq+gD?HLAE8UX#HQ4eE||7jU!k4kwI@UCX+4wc&gAw6tx#906Z=~c<JF(7Na{C7@%|SzB}34RYoWRng;r5ik{Jmw=-ka+n6(CM`aQ44e--o0l&jQXBv+${Rg-8F1LMvY2;)Lxx3D!Md4x;~A$-VRtFZ;4r)6u3VgyB5NT+O8xbCP#WeN$F!5YpTwM40iAH>T~Z(@$$f9wh!KV;~t&IgTLRZ0y!fm#W)N}*A-`tM_6#1)d1S^QusPP$%y{2*d-FMcRzNDe__ZYjK+kWf8jb8aayN0Ajbb5zIxv!vR)pghmUotfYZ(Vjk#M8P>u0yXK`>V@L_EWn43Pg{o{F+6Q)itoKPsGGGulzqn<&10!Q77de8t0`+}79Q_|qx(8JXG24(e<`d~CfF?!KUzBy`Qye^2nrQ>c`{*-!~b`9bY#|?g;%t``D_WQDP;;7$nYf;ps;V1fku|o9(sn!A-)`uD_D~UocE{gVMQT1LRw#=#hcW_Gr2i+c~~pg@#t>k8?-Ce=`r5iw(&I^3^y}pA-ezc>8`Red8Qs~QF<bjlmCq!<iFKJC5`^+;O(zF#@qkL=uM%2_Ll{CvgV>TlG8F;YB6H`z$}r_jRaPCm-SUG&Qxb$pb-Dnb%W@EM1h);G>c*+O5JP^=y61$b@n(~F7c%6a6~~hxtIOL#YIEc-^PsrDpM#AzC;HDxUg9=_%&xiBFje12aWqiTF}WlR>=TwjH)ErC#oeGXQHZIGBSNU^0QMis$FQuJS1)i|JBR&#PdJ2G&vJ+j40HiACgRMN=K~Op<m3OrD8egG{v(wL#XSd=K^I=q@doviIj5QUg!SUycRVJNh$C?-lN?1yEp&RP{=t)nNC_6)OePW!B0L9M}yvQA{IaHeZRK9zqPvq<L=cIa-mMPXV{X{X^iQa&8UowsOHzkH2;%)M?5@fOuJ(HeUx9{-Pzr%Z)|PX*l892jEz(o>zk7+NrR(3kU#vjifwMa`{BR$4Sfoq@=MoIV4CPrf2y7vxxWHRHx6rkDM@6xo1;WmC`C)Wpsd`w@I}f67KNh4m4EN$?rFw|szGLXUbVo}jhf>r#*<H)bL4fKvGn7X6Bw02#0$|Ac-qrkiuOgcMz)!$FT1v+#du^zfk_%`OE8Jmx4#)sK+b^T%m0O*6r`ZU878sL7TdCVnOvKcEby4-#s#Rm#3yFdWBNq@FMT)Y^z(9tg+##vp)-l&9)H`U8ba)(SnpBB(8NDl6~T;;vN|9=#h7hfaOPx<m;LQO{%#7fu}s7pu~XtsOW;#N#55^-Dq?Cd9^SqAFFk(!eZ+CsP2r&#z5O5kc1d$V^P!3HS^X*;*ZYHf?(JVjQU0hlU_VZm9u_;N!w}8Sb-hE5?+<?sIR_T<_g6)^v91d}ioVLFpD$iW@CtCZ?iHKg68l8)aeF%HbW6>_@XFHgxTq0;;#R`}2kON5c#=El&?%|wL^Nsv++uJ-FaJSnq>#^H*j%|c29Wx#@x8*$%YII4VO_ef;;vH#9<$3tcps8q)|B7i`d-nvmqfQzQHc)%tx!SW!@UHy-8-5yG+CHOI8#Wr%qTU}Fz0Gj)H$U=uhXnwj5?Dr&%vqnz1oxAy#t1JQ9^pobHf@o2<eiAKoIndBB$++_)f98r6i&6aW6z1Geb~&tDQcr-6X;5=18O&UVOJm(B<$4u<C?g>26k>;DHBp^Z_F}d;5>Fi5dRK>IgyQJv=mtilo5YU6GBKL_Jn{?yM)xkz~zB)kVwon7_3fNJ&30*D3s&;;XlJ*Q(oFI~%*u)?}>p<LXXzv$pq>cP5&zZ|?0reX<`hp4`TOj-Q3C4PJKTJ5br9C}XeDZw-2>Qfu8t|8dwm*2?XK7jdCvu(OPB7N4Jt2BZVYZGS@JPAd*^=8WjjDCtCk<m1DA(Kg)WF!{UNIiu$;^{kU~;wH(4z}Qk*!%j1ma}rV{kEAkgLvNKsM-w}I$!J)m5*m|1ou3+}SiRIPd$q4yb2D2uk?jxQQ1m|<D9NA2j6(7`%(xgIs!0}P2&zKjEO4^G<xqXS9H#3MXrsFHBUOL^t-ez_T^~S?sw18Hj0I3%kxVz8T8pTgRDP<OSfrd-C0+p$@;fGn!{L$U`A|Dg{KPzQ1o<?j{$jFHw-p}T@<ym!%cvphPgYNa#ODvLh9Vxms6824m}yAXO}uLg1+mekV=eVwIB5`_%|_{H8zad_X!XsI1WBr0k>qql5XhV$|LAnUpB(MKO;g&!lngB(ayGbMzS%q$2kNvqh-V^GdD1RYVG`A^_mw>?A(r%2$TsOsS&@=wy<|2YSeEY}bKf%|2szE!sK_DF)CNZQq3!T-FXjM=rYL)>^`VUoF8cMDr2s;rG0M^#BhcO6&}48H_Vp%2#{0FPe1<|)EYHQo<SAq(UFK@!WlTu4WZcX!vFvfR#2&vWm>JkR6QRII6s7l?>%{>ZVh*`fcz^^k30kTb1DW7nAa0OLIZjdm9ZDw7c-m$|rlm<w0HcsO0aM|55sl1-g3HqLqne}U66>KFTv1X;O2L)Gqr&WC+hQPxvg{GxXu-`aq{pKztlWgn%c4nkJv&h8pGlS0T{Cm0CW|T`zK$b_Djyk7M&U_F%imuNp{!pm!Q{hlc}KuSJM8mgxnml=n6p8Rg7wivdX4^-gi<MM#bQYf_@q#U1v(?kOySI?#1#YlvT;6<SB%A4+=WmD(&6x`-sLdW5Y&OJR-iA;Yl2mT^l(^h$Q%x97xUU8UYY<9GuH%cC?|Uy4R(BLU6CS^s7pDSb)ktQs*;kDsELg10jCrb35U7pc)KFQ&V^Z+&1gl1LUAF(Ew7xTQs@;GZ7OwQ+U;uE1j*TYD?INsrK4Pr&~1m!v*@F2yf>JH^$CcB*iUYWx>(}omL|R7(qyc)eLbCaS|$3A14FePUfz_BJJO(^(Kzbkb_f=mij!&%jcfi;e>FwN`MuiX-Gf>^vZV?)$?w|u@adCJW<va%?cShe&~3`MRLo`U1Ae``_ho&3Yp>KhYjr3@i5!VzKFwK#q5_q(J~)$yJ0phGItCU2;JKm>IdO_UnnQhm_vzkRO*jyW26=v9$gY@HSst11^dWq*!F7@w^^C=n+vZXf>$oCrLXoD5(1tRHkO+Lz{cu$2E+2lR($TENaY??cBXOQhskvw`I=eX@!hTl{iAm!a@`o=3kTzFRQ=o{SUT2bVE-~d?8MmPVk!OXP;)5nsPl-aIrtr7JW&U!M^n4im2M1_hTv_wIaln^Iwcq}_-=_1QZ+?}v>xObl9}vHG+He20mvogZ=8R8`iWT38(4pts6{V6S3H#GtIBH-qc?w0tETps^Vz#-W^c9PWN%@)bgQf!zxyxne1|z(d)rH0FQdXL5RFOy~9WL9}5&qTdD>cS6IaiEkhM4qKm^qfli$NE|hy_l~;Urfom9#Tcvh<=TePf)x`{DN!<JI)t55LVRSDZwt@nAHmpM_TvRLe<SN3)z%#F((05;s-l(?HO!iYkH%H7KgJEJa$`pYhE8;_k+x^eFAr4v0}1>s$M4yU%KS-~8mA()|GSt@ZkswQuS>)yK8{$f{yJrlTTeA_Z9fWbu_O!CCcmIfh%RpymOMb3qs3C|QuRv~n;#_G;VJgRR}2`lGF#1I-yGRe4#l&08U=JLwQh{f-NV-C_Loyff}h;>!K7bJ{+h`8|y?n$SN~y2lPR^=mw6b{bvbOH*KeR^5JDo4Fxjl>1g*L{MI=)EAGg?V{)0{6+5W8wYm6$;DuFR%@Lq7Kx!X!}^R{PCDXe^5YZXk~F#vjtP$nKwW6j<#8hCr}B&?hp9Y5$=sAbC^-XFC7GM5!jn@a`A4dNnyxCNey55l7^q_E_pA%5-lzQ@x(+}MiMbTT#Y87{qS%G#5NK&UJq8jSek(EHh)wY#h0|y}sSw@QHyE5jF@w^rI#C`kfL>^Qkl~34Yb_|Ai>AZk<xp6uh_6u-XNRU?!q}BXsSD{JBW|BY@X`r120l+2-7h3ZuV5^6RWgag%Sm4T&43cqF5ibF%V;2pByO8j2MF3Edq@N=sUoty)RjMCQtg-y_;+sFKkI`F<<#KE%|@RC`|IdcL4TZ&LB?wkpRiL?D$0>g`>ol#8Y0Kuk#zdS8c*^(gIqcyHEr!=^p-rh7G1$KdjnH^yiX2|b^dGl<7O!%J}5$Gg8v-kChZr03mLwUs4@mMD`^OCvXGg_nBg#p9W&IWD3$4liC`TaC6AmQ^UzNROQDzqQ)*`Okbvu?susmKv~zE>%Sq^vT284zMhhD2k6HIs-7z3-i4TRIctZ?E4oo06K8_mAiGWVnirYxti#Z>4llQCa3HrgfS{y@Z$cDvfhOPCn(a`Sgi<c*2z>(aMCeA^-!@eO9C=4}}ARCHEY#ffxQRQ3`%%U;q;{)F<MjoC4OacmR9EZII>NUAqFKqP35jw&2Ga60udxx#hWFyi;)SHec24N`gO&KJw0VNI?qpKnf8semb&PHQZlh5^#9?)tDyeDsXe0A9p(;X&4Yt~1JQP`Z0#u&f4M^=IG?!%ioq4XMkp#($+P~MBxXh#bO0WKQdGxkm_Yqtue&zL41j`97O>HyTzHTyT{IDT$nmOs(fb#zS}mlSZx=2Y*)dWh}(R9q(-T?Xe#GLy{k%&5BJNX5)z^Z1W|<(x`H!SX)PrJoBfJzKDl@_zC#h77%#v87?A%8CQa<BQIuozGnhZ&~KI!(0ZGW)31oH{Be6mpqTC+MH$Ew;xVSHkj!nrb|fZgl24wW;Zd9X`*s56W|fUOyC-!I|=!DppQ!Y2k1W>^dAx6G9XVJC6bN2JxpLufrUAmlF5?1L=*gl*eh>%sq=d4VRYmX0?){kIEsW2Bnj=Q3`Zf!8;Zsqj9THSG<$K@EzDNjbrtr-spDk9qvQ!>p5c6<Nb?pPKAJKKxfM;4#`05J9vS4%gSg{dFN*L9+yskFULSO;*q(pSjf$p{VvCmkrwFE^P%2|d<**0fuIQ@yaaBLn!Bh^E`SE8`MV##iok)$Ybtq{&Vkh!Gg4@(Q-KBYwd)Yro-<~6=@P;7&cT>99?)TAFXDNAEXbLq|M461%<QA3k)$NcM_SLk(J8=VXQ(k=ixh%FM_PE6%hf8(pV_u}E>`%ITb@y$ygI8fM|A=h;Sr@NqmS=ptx6(jTb!Vs~UB3$23HPmR@o?ETkMJ+&sm2eN&GHfc<xJHNA4XkR5DyDvIP%19Azf8}&VQ(bD35!Kev#Wg9HoA$&*Xm-ojj}V&Fv)7da6Cihqd;ESuGCCi;LG&u8eq3AS1R#?V1u4<J)`{x&NqW9ql?q{w=xyVw;JFEcm6dvUV#-rh|ZskF_ZklU{)gH9hiGAN~K=6_CQzSuH`WYXUKZ!Jnmd$Thl4??`I#(y{*mmcCrge=l}^ayTDi<;OIiw(pZTSj<Mu_r6^yw?SJ1;;a=f5lukd@}yh?<5~2NyGmK9q>yNVq$;=%Y;-U}FY@l}gv&a^aJ?I2;=x7eqWUPRXIL~%=ikDLj;xKwY3h}e+<9Y^OO78oDlSC}If!FY<^?dtWU8vqA#~NjErcEgd!<B1mUTU14@p!*zA&P$Zl^?+(W8S!J*OZ>bvG{%`}wW>+>cCfI{V4!W{$b8{wd%7`Q%<?=^XxCz80Y1dXqbX;TiRGb8miAg?}fWmOGg`fja@w*yF+%zGoQS|KZa35WD&|Wg@mf@36+DRJqd)l0AS?nmcA#s#$m;YgsdX-~Vv5{Ch=+lym0a5Fh>w?jIGo8!IJgyPzz#WR*4o`?Ic80*Vjp^z%a=*sy5S@qZdx+?qUM$d|r{V-og<`Lr6LYG(i}Zipj*N$BhS%OUZ(DHV{d^r%!Awrre-7Y#>KMz{&}GTn;&%~DU+EEkOX@=myM*bSTFr5Xy46lHnSdZpXw9k&`r_k1~O@?3^6Me_p5lIJ@-7Xv$|DJO=-dfGWnR`n#026Vf14I&9x3Mke!C??@|q?>lC*%;WxRO8C3lZQ6svo&3Q*Qjw3t90pDqgXlBUnLV_D{@B3ds6Z_Lqy)|h$t+^G!Et-uH;x$#;25eB9bKDZ6D?G4_Cf_u=4%G?;m`>QusXovUR_ZlkfAy2l;2(?nU?Vvw}z+kyYJ`F5)lT)h%_jcxQLr!9~$%cTU^VY>)db%=DPh*asKJL#~*lbG<$KQ>2_3z>VlMY_1rWRww6gxqKt{hrjN;d-Io5IwDRlvk9AF<`RRF@$BtC@hRqI<Dp5<-9B95KlERtJ$U!S|7?=GV9_d<)#=y7!;A9P>Ae2@-C!sk1k!cDnLK$7w`M~<BKJi3me3BqrkxFkhq;+zqJ@W|-*oYnx#d?fD?FH2{y}!}x$Qs5Zhvn1mF)5Y3*tKR1Oj7E*0}@OrXXJ3`@<MC16<_-0y?FZRz6tN3KQpLk|9$^Ld91ruZNV->hte32FQ4k^lOz;<fqzCz2Ol#F4f@}9^b5mpnNe=3_Ce_(nk?UFeK?U3%LoeB}xlyE@Zsj7u(#|Gb)01qB1k$Yvw>@)~O6;wi)%*`O1u=mC0zbY(R+50uULsXCmI>nyF9o#-|0V#dV|1d9~y@gPeFmbM^oNDvD6@xge=);cuyRk3VH}e<O7(wW<`eo7c1h!n9>0zes-%CG?MqhWHsTS27FmIVwc=gtyegd?)I4y~S(7tDD>m)eBcG$_<7$>LtE~*=q=*8OS4QG6J{$xO%YmsJ36H@Q!$ztnRm_z2P|NNVv{LgX0UiWSTtSqz=j3RMm3?$d*Zbkg1zu>Vd`abQIPb<7THLLjQ}YTYD)IWyR92JWJo3P}FZk>2~@;by`T1*2_r*`j^5{|8l~p{c@7T)0Y#4doL#vmt=()E4cOe>SS6+aj+`&aHkB{(Z|EHO0Ih`ZTsbCa7ELqUXpPF-KsFJn#8!d-vvR>|DGb-`2`~yO&7_TjHjZMqQ@h7+_Idzb>K0OGbgQO^=IG^+kK1&(Pen3Ee{~@dMMB42NB4@{<F9v?p-v=J(2N1S#yyyA<1J3Nr+apZ!9*IKS;QSt<y+4YN6Be>o}ZD=sug}ROOkd%+%E1^B9rba=s$>K=SPJY1n74f2-ag-f;IVGC6sRO!EFeIed;%7D??Z0jREXABLD-pMaAn!O$wC+89eIFizE^{6k8VRA{)c#VCunHmJ=1OWwQoIC33{g5UdBr0LNXX;rf;$*St^lB#^WtDjcC+*OjSDb)~3GD)V2%%n1tRZX?)!@yWv3<iT4!+S9>W@pD5!I-@s828S47lW(D?)^~4{Ez-88;|qMJV~-zl5IhP-Niib6DLkYoH%hJj!pM(E1^{-y%m65cacU#4p$_CwIXG+t;!Vv)C5m&K1JNDiE7eD(t>g5B@oH)#Tz%R-plR{Tzut2ec5w6|2XGldx|QVW(r?5XIl~gSlpUe=~>W9i+lIZ{ksQWfm%qiAUwwWQABR)Tl*_99-Ff~E#i*<aRh1}obuu?C@ZB(PkU)_HkJ?dBxQA5;|SG+^rIym04xb^Pevc;7r!6GBQLx7yf-4(oUzxv_&=N8A;pB$4-KU&w1P#6?9}#~u~OgY8SHO*+G~XBOX~i*{KVJYg~N-4a!j+N5<PR)H4N_!ODdXv9@a~Dbpj$ZYQnahz2vO=lrtA$vW35mYtr|G&{W7|@^(@5pZ6Ynu>W*+@n3WC<W4?8+9~<iJP1FXp?P#L_O4<G&7aE<-0P?<`Cl<!=5MDaTD*SsUt(FN<b9L97<p`D{o;bc^1gocOW0-@Y8cwgfB!Rbi;CXre*g0T&6F@)?}TD*j>+dfI<)(IE}AASx7#x&X?)Z?kNjiPh>X-@eoeO_oE!@0oSB-na?zR6&}-+kx<<EZJ#{my`PQ_S!R1v`oV#AA*mkVIv>uKsi#qa_dhyRQ5vBlPcho9Rxn+6~(Y1_J-}t#<N_2wP=!kRG!#O}a$<cA`2_obdu?&}h)@Zo6{{sJ7YPlnSW5cmP8>am1Xcq9|*BC<X;y0C3!2c|P0Vy_YO9U)S>x<`d9|rgjkvAf0r%fTy)GfLA6^wjq!!>kFHOIcB8KbBT=Y>--b=e&@N#s#4QGfDkjLC-Y2-Tg(Uj4MM6`x!1M<_cR()qGIJuGUt1nVU7&Z8skWavYvbX}_V;@Fh|2EI8r=Tdtzgl+Lx978u?+d^~|8)o@BBwqY8%weOsRbB!}bon*lsvYVGl@1_)=5^JrWp1WT%vN%rRJ%iMiV(>d_9Fv~H614zq@O~)+k=6G?TyQHK_S^yy!Y)528Sda!pXW|@hGb#DI8Dg1>UcO8@}}^yv=ryH=&L}YG@7?6Pnp*HW-Y<y4|<Kd7;gBSb_;19t;n{uwMuji7o>1WK-zFt_GuJ$F<tQs+@rBhSe|_$AaF|CtiIxPP)MG*j}|^59o35g5TTfmKBY5d2N;S5)0Z}+a54cC8i8=z$HRu)nE?@yn#fG@}9D0ikPGR+adoK2Kr&pdx1Vit*5gbHlbCkd~j}5xrV*{`pf^86Mp`S<a86}=p;Q}1?llB#pS+A--}(vR#^&vg@ZgyAI}MWgu{``*8u9<DObpC%g!SDqP9v)p|9+z^L|D2GNDMS$_=71X4)?0xN~(~q6JV5R2u)0k#%e-F$(H=qg=(K?1FVvSwUW_RlnA*;XCY_+tDCo7c`_sm;>cLD=rW@;}V<%bjxj1)Gt|;eBZloZgp5{Ne$@vd?1>)-AduZ5qf_CLU%AW+S1~=c7w%>%<mZ!R2Ez*`5Ehbbdl3X!fKu`L~0aEOj-QcgA37fkDlprjM9zQ9(}reHaap+sEi&x7h3$_2NIY{HB^BU{xY1XMk^CJ81$Dw57V&5h5Kq(N?;h<vTQ<Vk9xOq%w@j}yFFJKg3hkL?uh2ibKZ5&*fh7;)hED0DXHZZ?mH}X2ETeDG@y5rW|?;#T*ll);&zeUF38xv`T)$hHBEqU4)VIC>5zrcR7lXW#rR9^^pUUbX@<J9Bv`pQ6)Vi4bSke;E7kfX3;EZV3$zYLR8Dt3M>M+Km&PE^ue~h8`~0}%+DD9U_hn%oP~Vmz&P!Dp&t9?$&^T$x7b)c$by~$;dLBeS8|T6xjMG@heBLO9I3$J0jH3CVqrws!_O1~#!RUtYQ}lnO?BcK}keZ$o5iJV&j$p8clebF$Z?@aTV&u{VfjHS|bsA<<e5l?b8#?u6^lZ4!8AqoMl2S=Ox=w#{17~Wre>$-gyW(%r5uMdE14l3mhmT5DdxF3r{NCypQZF6X_nP)I+Bw=%UMS5wvRw~lv4w?8fTn7t)GMy(b%c7=zG{=-mi3wAQ3X35x48$3kih;smD*oDbcY_eXv}I26Ug31*_^Tn4sqQnu}xN9t)6k)=<ODuvSJGwXw=4$)Bf|Nw!%1Fw;b<;r{~o+rpkD**wxX_)<)UN)lQ-3I)(MQBt-4nZvs+-Jr@R-g_jx0#v65BD|)0Y@g$O<JaPd-W@-*mV=)qwUgd|5YPFy8LD$t}?W4N~HOJ+L6B91AqulQ)6a!z7%S?Si0kT3YyJryB`f*AAx>E7<XwiFJL17B+ZVipQ)F$^sIM7d`81b|Bj?|)4Zunw4PJkT3No6nyQC284*G+?%M4%+rWxRA2XH9wdu}(c+H$*E<=xIDIG&P(B&{!TqWBDk^wbxy7dV-M(s^mfLB*}6*@_18VkI-SWWXx}=lnkA_!)uTUP@%_iuAVOFUfr_k5}9LcNCPEb{%9RL(5tb+wk~MGO#AVLoK6)~2qMUIT-`=L%6iEudcx|ALW~9D)E1ajR)~+)9tm95^M!K`iT>($rSm3OVfPxL?4_!^pG~A@U%MsQaZy?0q_(^~X%H+Jme<_<$f0z8saO+|u~dhJ^)rAfFM0Uy+l7$rmpi*U&aaiSr{nypal~1gPZ;K~-R0E5*6on5bhs@$<g4<EW6EOU)exT=3^+TmQB{$?W;H4>)ZZoBby>`|2)#-FH7c-yH?!)#tUjsGuq^?#rB_)Faksi<;nEk?E{oU7GO=CoGSX1fSbI$*yDOfT7y0{c78Uf;B+Kxbhfqmm*LVRXvuiq9dN}ZIk^bYh*G-@-d6g%s_mg$+Cnoc9DC?HeG#ih0wF<*o8i%0)BV6vY0&n&5Vz{dkEJHuIV4IXRh6cy5FwoQLL#q|H(NIxea19lFicm_9*F@VehX`3^qAUM9s>H;X3t#VAXW9PZm%f+VC2Ue>o_wl^TUmkWIvw>^;n>a=jw{IS5@Y0QqvR#V$qtdY_*SxXo2u_L%xD#Z+RJ=C4S^u{8qE$F2X{K>G9JwzMPH#G;8c|k@t&4X==OvhhciBl-F^Q2>2thTD^xH5_y<yF8jhpb^t60Aq-1t9P?f(+7Xj){)nG$(3uhNpM3PMAU$|IX&DM8nhElSR;Ng|DtKzMPomjedFz!KVdz<&7cG)fm6)LOjWVj(m;4M4mPxbYOd4DV4uo&05uB#Ab>uY>fgzidCgh{YSDBj;N`pGi%(Qw_bxDB`kx{;8&t`MkEsAc2pswiqdBQI`-z1;#%?5v^(LGM^}w`>?Ct)OnV%#Ui0R`b#8SAQE6?VDZ}*YdpS-Ff}$UqKk9Yw>1nfws1rhQWyi0)3fdTac7AUSxrujl*zSw@OM|DAzt;w#Qf6-^=#)>ihcgdwSLV?B2`neZ0yZUVZ<rvUgY6w@dac0AdnEG3qo4V?;T=<T0)IFTbT}nbbw&*RZ(>KRT;Ce_v*r%`M5t+ABQtE7TN^-Hm3B<+;3Lyrnnt)r<PFozr`-zx@9Wy&u2-`pbWI7&n<#N-NqZp@ov&$`gcxX`rJo?W}UBD=3xY=OI=(wn2LOo>flbo}(m13AD;G9@>#;F+d181@L~XOEM<fW>e@uP#RcK<Zg;kz$!m$5yT_chF$+Xpuhhx6^4$|K1**euXe3uh_#ODYnxzKTT|gfcmwwrFdsRglr5g}(Z%NsCXe_IT19=H3(jL2vKs!!@TA8!N-MPbKtx(W)*vnLfmKC|yD+cN_jVVW15|gtk9MsSGSOUQ<Z7d>F#RK6+YY-jOn2b#;lT$LhG_H<rC_Va5<*oM=6g_QMe1xpMaXY_BQaziKDrA8<<_0s@bB}dPY=KLJ}A_x6=xYENf}P$iUBT0K{gsk-6mI};uJruAEBF%x_sSdo&MQn+B1s4UTj}m$djK_*5j-i$P2@0C25e(r4v?k_Cp6mj7RiRc}_iVI^vz>lWDEcOq0fIKtjCs$keMXRg@jU$?2LQzI4D^Cje_}HCRk`cctEft>OEEwU0kuTdUDSsWlm-BAuaYn4}kGS-qD`CV}z+#KB`lL^2r)cbjA3X0xuS)Z9-d({Tty^BE@`>Cj2v_ukJ!1BPf5flm3eJPi6?GBBHY_VC$V*u7qGnnZoC8=#F`)=Q&lj!%KJY$mi0-zR6o9<GCzC6my5HqS?J(r-8YO_<n+QQS|?GV=AGjL`{yJcx#~l++nQT}O3sRAj$#D2I0s-S#3++^wCx-32fO8NjxWiX<$!UR6brEnSxl*+m0zQ19pv*sRhQAVaZ1g8-JIUa&)=^(emV?MLyhQSHv%51zdL=uxQ@#*s6}U(APb?Ha>dFUj-RfcU#!@CB-3%B?$$l#EWBuvjPc4J%J}=*ok76tF`#fL@PbL-j*b0|a{&wIA7TO(1x!*aNqsy1G;=(&0}vj?100u9vdOwXpqlF@be41Vys?-TDuJhiAfDOKEF~XnpK_K^U!EV!H`G4#d3k?AGCfujGmv8rkt)%BGYzY7*GdF2<l5ID)z?iS7xmW&m2i%7^=RI}h)ydo*WFN+eDxF^48C4w>XJT!Yg4p5>ip0{sO;a#Sgbiq!@hp%bv}(q*B0=E(S1tgOE*b$;Fe5Qr|%Yt=5wVO>Q;Mnym`vA!1Vrl673R&8Bv|I%g@8<74*<U+>XdG`G7y@x+B<Cv=e^&DmqkOqwdFn;7T4F}PSy3IbsV+5lyxj;se+l`zUeX;6kkVXOUSKD<&HuE-spLth%=DQ_GEhUi8ShFPSHhI??TuPg|v(YwAj@=n^{}$y%kP82)RIm_4bPc%A)!CXE2UKBwX`u_@HI2K6DG{=|g_PofGW@ZSw~VU*^72mDg`FTa2~f@;Wj9)X@zam9#zy_m@DHF2_guJ`F_&*wfX5Zjs*uBAme(^HUa%>|1OeD<aUwch(=O{>j}Q$K^ZTFUnc<6`*Sq-An}TpZ<&{QdmpG{WG9K<QsPrpu9*+tQW&}cg^KB<^W!Jeo3L8^JU3DXl7z71fUAAHAEwvS3w-CBC$0PVIlLI*OU8Mwic7}*leBsN*fmGJGx!N*<e@L%-a}Lk?QjzL&7!*E&&R&1{{{a7klhhCvn_8EPJ0qJ61NJrAFO@^9ZPes7BFe|vbR6Z&8Pan^2Of)!6zd*!hYz*B{DMNv!T_P+@1^G|=qCj^COy$5;~Sf6988dw^g@7qQV2u*?AHE!x9;C1$F&X37na6G&LZU8-(X<mgIgcm{T9bW{)0wBCM_HXLjIb<AK#;pFPDmZJPA%h4w>EQ2ECKnw9Yma;`qAmje{;a`9qeDhHKDajqn&xx;&iQfQ;`yyUaR}TbMi`JT3T+fqn+~S+BkI(OZ+Z`kl8Py!H64gPIlpME8jCQ)(|&d*_{(G~V;(<USmUwRLLgsJ<?YhAg;XhJXtnl4%R$8zA1Jd<WcDuu0Nrh$vBZNY8ozOD?uF5VB?iNv4%kg$hduR_%bMBh-$lY|5r^oZtW?`6!qZ`T8%>JKpHxi@BHcvt6KTk%yDCm1x6JBp=qAs6l>Hi|8U}0z!8;1bP)RkZTUFDo@`(eD?k!O%1)^5G+MEZ;TOQhXK&pNzvuVUWerdP5nf3afolS4Vs2hKr<In^hA42C}q`BP_ioy$~6s)ZFYl`nhfdmoRkt6MEDv#tGh-DbB3!YPKfBCzo}SsN1ulrw0cm(G9bKqYj4fGw}#$Z!P)}4tzW;Je3UsRIk>SYlF|P%{|_vB3C|`<_~Mz;9O-2&qvG)OtDpDOhEGX$H@Z5y>L1%f)1yK?J5`~5)n0n&)bYBhhq7x5A$u5IGn*H32tLY(e}qE~>iJ5Uiwc&L;T;Te8Dk$b)@=-SFr7twxJK-hWz#FG843~WzItiy&A8og#qo0s1lF`F8iftCs6~uCPomZN&dVXb=6aJhP_%f73-l({C#O{`o$4*xN>xo(O9>KGj;gjnO~b7x1B@xE!m1s&uPC{!vV86XDD5~&*PfwFf+$3%$I~#426Gr3h9(t!fH^2-vxcmXaY$vjI@m!_`OQSzj;wA{dC?%X04<uY_*C(N2=Pq_#>TuZD;ir>UBa;~=o-bD2-z_BnxtKOPzB7eKu-_b%n>-{UR4^XxfH$@(sY|Tk~}P!4$C@%z~klJ&oL$<vw!b4bM8FF*lxLTGTrf5S7Ok>0;r|)M?)rBFH{i90$}(k9$C_pzBMWwzm+Uein}Ma)Gb*gLgQd8F!utb3nr8O09ba~<O`5dC~b+xa}W14Y%rF9$plz5O0OoMD9LN$e)QTD-{WNDa%&n*LlgwWC5B5zmLRB<W3PM@mxvFa9Nv9?Yya>eNL=Cx?bqJRe?p?u8wXi-h5q#pLV^k}n3RJ%3i9GqP|$>0WpywsM=5EbwXl$|fVWR+H7&Z6r?wS_qzf<X4)t*KZ18f$r$LkwRTy*pEIuUhDT@9*UN|IjomX@KQm!B!V;Cjb_0BVX3+<{SLn;Wb8as9kM+JJwws_WDL~re)E*#7Jr)iqN#>(d^6c=yGI{FDI_{p~;Kn$8?RI^@rBM+r=1_D{$;wuKw8=>Fnl|~>42=-Jjb@jd7!Z0xrW7c4z6M@Xp8NtcWlr18PX+x$I9E}bmdR(^Zd4Z=zJ_REIYkI<w9$Sw1mRm<_i6ot?7>!<%-6}1hD$BuAS=^y=byeH20(ER-*|yGdcVGkA?#j`ut0Hc_bx-@%65h?Me58wYt1n~tmImO?-TkL`?%ok902RZvRPOQ9I}h(YT%q8jr~9`aJ$!QSX~%B5YBW{*XIC#=MOlU*{A=f%i0{ZY$umi=kM2C92&1OTyJpvMFSsMMsv3{Q`mQR9%V(9v1iP?ad-2Q8c5moH94M=#%?zAH3sl)zMiJr#xk6v4sh--!G+f%mGTNa-2rF%9r!2N~D}N<*wTbP9OttPgI{4c6+8=ql;5kKyxL&eB$~dqbB}*HjTtuUPHAa7Xa6gz%$8(Cx&8QDY_)a0Bs*V1RRTFhq!X{DH;Guks>#z>MkTvGkD{Shv!2cV?FgPm+L(VEya*<M~i1qPy7cJh=#xbe&7c6hd_fEx#^?kQchRD+{lak_~*VPC$NC=)0RW+%Q(y|-Uk}CSWVx;zBM~xLEsk_v}HSW|)(UsCwRL;ty_6gf4|K#x_zKh6Szxr)ZtDr^h8v<w15AHsHc<&=oR8FbrG*PwzXHIb{#LG55wrMj??Zi=7+K5|x@xD%7+Or<RmW;F6fN$?>-qA<bV)V?)-o2=*aG~KH&96N<mfmH9I6EVX#Xeu9LDAcyEoF-V)CtPjDtE4163Rt)mbC!)62;!j+8iw}VTu&doc>AZ-;3YX&XsXza@IMC@vVn^WndEn>6ps7DaG!RWfpBP>&3wR=;Cwoc>34gh#wE-q^8lY2j~%min2R_R%kNxV?Q93IzL63P4Q>=0?ss%4Dge|=L`HXgcc4kQsy19Vc4nmfQ4aaGohRUNThYgoYuW^Bw_gkgX#+(?AY_WVjG}C`P02xIV3GbE#55-@e*-7`%yM!_rB`l3{L~<hN+J5mQicpKiuy;d-VQ6=elvRR{ga7t^T#QCfDBj$b0L-&RdUn-a5br-o9RQ)^I<tmVi+KkG%RzF=W%tTH*O@UArS*_nscmkBYb6Q&h;5AHhL?2-_Y123iY=_(_f8GhK_AIiKpfTBA3)rV;(1_PFgm`rwf@Fepe^M2{uf!qb)mos<E`AWA_5Jd0w9e=5OQ&FcRi7DdxztAE`hzJAajMZUCF@5!(S4P``yj@{H&ppWIlc!b3c(Cdyl3~mYU=lI7;-ODDQ3}>%j{UY{?u$5ymWyWINeb{xz<+oXVZU5pIYo^CNq5cpfdhfx-|Mukmnl|YP`%#W>tHNQJB4Lm*Cu9I@!86cv(PTCe0T3s_3-$F4(bLrkmL2{)8TX5%%7&W`>uu3xG`k!3C6H0Jle=5{lxL;}%Qm8D2}Vm3d@zHa%k^*+ycDSHaol<R>fi8{(wF};7JVZSU#gzZYnASpe}cZ#V;n?mqQIryF3Xt`7(481$ixFpJr@FgU4yGUX(RH0Y(xv{N`x+sxJLk{Ddr?!jW2#R@lJ8QdZ^FB9W@+9-s#1!5)au+(?(`~^W_em@^xXS$dmY~>>#R%p-oQcWm^FSWk6?1ri6dOA___j<a|OtukLR(oBqa)o9o6+(3f9KxKLxqt2L^eR`6JWr5_%A@bFoOgU3I9_@t0<>n9BxWtgmF0&$iDK)l7XrJr@Lo?u*Pym2Kr7~E(%_NB$G&Uw#}li+cG8QGOP>+*YwNBl-R>rK&}7Zotu`^ht5^R(&?Fdu5N&UeeFiTq5Q7C;ggS8H$Ewby0HnXL^`;l=Frm%q+gea5@%`-~3Wso(OwVeWhNNqbD2>(dwQ=6uJSO;Jqq=+#}@`v8!Z)aZm=c-h>%^0=+B3(#h3!$`S>=F_c?zj?j0d86Ig-n@?2c0USE1MeZzBtBIDr=3LkI<FuNUWUU6rcHGrSrkqRngA6ticF&^LM=OOgL0jI(wm_vQk`&C$Ug$ScChQ?(radH4{<j&QJ3(ok8!?+&0dg&1HjpOgXMmpq9{zGqB$Ig6MPsI_l?+|I!tP@YQbejKAyDc{Lt>;RcU8@I?njJH|pT~amc<>;arFVb?8osnAg_L6dpsP!at(4W7m`lAIcN##w9|B@3q%GbLAWI>i4}coYFNdJ}Jkz<0%}zQ`8#(F(0OIp46|{;9L&toS`SMAf9WtVDtz!Oq=GBk%FRYpMvsKxx1ml83Nd5QzZT!3b<I$ddXCqiW*{&ejivtPpN(fUEY|_MSxt66C7*@us}aAG?YVzR~Y$bnHma)8IQ(1oC%9C8H2*x^Zcb|>2&Y&j{qSip=?B(rx*VNpAHbAL5;@GBj7`Ns0Pg}J&mRWGM%K1Bg4I`l-(F1@GI)hP_ay9MOg8TM#HK=MNr|u_(vA*@@FiXWVOR-%?PwJBpyr_gu16fN9(!+D<Hag{f96<+TnT`o>%LQV<42+!P_F2GZE7pJL0(vsmE}t_+X}vf!HGqF^gg8yR~<(p^=3FPU&n3pNT^L$Jr0|$YB62FI0Zmu+~?!PBwr3iVw|RAS)B0yR<=~YiR|k&qo)(nFyqiTm%Y<aK2&)u(%Q^Y%>J-P0+>z@S2zJ)?RAFKd-Ivu}mhEIkdRR=hYjmy$kGu(0f-f_?maRE6>&JK#F=hzqYrgV0fjxdUD{naNQak63Qj)iuXZWRF;Hw6nY~0`oGLGgyf<RJLWAv-N|cXX!3Q%f{vUuK9v#S;VcelhA}tE;S!TmMN|tRioAF@o0FLj1{B&-5rta7Q-P%dN3EHMBqx(>6vEeI*`<Vq!~&@e8YNQll;hm7HDGkuS@&S1GYVlf6K-{s@hOQBIKmQ9W`=xl_~>z47@RVoArZMsjol0`Z%1T74fJgAxJ@dC!&#oBQ7~3-K(R$1|LK<61_X-5wm+h`EFJ|@F7E!va2i4h<>T(rU+f*zR##oqW_NieER#%4E}0ptScHZ|fQmL=Oc4iFP!KuN6<7r66ylL^puzM)&Ok_Y@5p7wXJ!4@uYOGqB$T+Uv^^q(biG~_M+$3JI+GxF@3Xw(T4P6f=m4)BumcX#h?e0Jqt@B*!Z=QK@G=XB1~f-Wruv~VC1v|4LIC;UO>ouofgG(lxcwT)6!+3Fd>#^M+{GZ$lcYZzhlfA~cG&?%`|zL!RI6c=EsBZGOQTmsq`>fGp2<^n6@?JZRBF`mCJ&$9*SpYJtsvj=Wt*%_?8|mdmGn`|+O64IOHrXCS!^?#brG+xA=~;h0B*O2C|w*>K}ggLhq`$8n#8F+-CNlQv#2Ke6)!T)+Jbe8{d8naZs*vwzwj}%XtfmEafyvT?*%^C^h7Ari{GioM+@Mr*?%?M-E*jFMv5j2ma4cS3l>DSS}F<$lg#i`=#*~oj3;SZz4?P5Hr~BPNw73OH8Zc_O5tRASwJL)KL>V9T_jd!p9O+-8KOl;PnKwT&1!{db>UchLdQPc9||}U2y~Zd&YwgUG2uO)q=CJ%G&Q^8mbAv<-deJsb)&GJh*qEo)tf18#exPe=(EHWb?$mq!$5;^NVP_3>Q0}1@_bMLvy=3|ABXI1jQDLXQ<lKp^h303Hy{K+%rgRnqK(92JXeguVB{K|%Xn<I`6hU*8B+xoLqBF8Zm^prieO*$)KqhEMw2ficWg8+v7|y4zw}zZy{pzwGjdf-Vzo&J-xd{3il-`Q=}=N%MR1M5O3aaE(2iD|`>at~JFAjT{Ap}iHOw_7pL$VW3M;j}wc@@r<fgZ)7`QU{sN6%cQdTJpm$s2^^eZp})vvvMblc_VWF<?m()KYMxU4Y7hgS9Aagk(I?xSHKrMVO)nk_(a-JpTw=3q3c>!QUCS{*cFVUN_zu}Ovto2$CVa&O;<l?S{f&9gTM#$$R*b2bWN5zpi_L|<oc=GF*cfU^`(<C5EQ)$?UlvlxH}kp(2k;?dHriq<DqaUGupGwa@<X1y%3&-J1*X_5FuzW5wSmm!lV9(kfOa$A&BwAaXfZ?DGnvIghSjtnY5S2{X=6b0~dYfFpgx1GZI&CP&Bo5*}B+hqt4lGWJINgakMD5oYa=jPp^3Au0h3b9HLv-I*%EKB(UTV9AQFnw5Zrzn~hmx>&Q9-ob2kb4X$Ze1=ezE%_$C+n8dtDyL|Zxn$NC21}$6qkX-x=yqqW8SDUCcWcLF1~>O|0+h^yGkUxy%9x#&qwg@XvZ@T{nm9M5AMiDtmD$fAnqm4FpW~=XUD$hqX_7z^~}*#YCO959QIoutpcW_i~kEMlUl8L`728X!5{R_Qj&>3(c8)$Z#LTiv3Qz!wX+C#Po8+B^1GFzxoQ5m&9vnmy4IX!z$%cjoL>91dF9^2=Ld(K4<A11+<SQU(H*><a8<1t1uL#Hg)2oQGC+PX3Rj<4PXH?$$Kf!@qf=x!eAlUNv5Xr{Z8TNB&J@>7I}3OSYfqIqRjsk~+KFluAYkER>HHzsf+BInd#dI47*6n-cU4LU>AvWIlD}ll_e6Q>SacU<pZp6>QzVTv4T{9wXwe+9Ru#z30J-BD)IytvaTVcO>~%(q)$bvwxa%Hb1MeI}@Zep05UVT?O=jWs!%DXg)*R&>Fz;I-lxF<Cmp20oQt#mGf^LT5Y6K*)-_KwVAthzkqr0_;b~sB_&6VyH3OLT^TLzx<Zef{_rh&9XPSX%Dg*0B}RfRO&*(!2cVX8aA{)Q)ONkVFDe>gGdjm$#pE{f5(l!Z{ir!|X01|>0IOp;O4drYq><BMO-B{{O#uVir2wSJYjMH{EkxL4n3HubhyEM#eN?jk2n6TgK(mY7h6bpgPax4`1q*_Rh+)D-`qGL5mTz6D~<I65Vwr>vA+vdp80AKX3Aa*Qfl6FJ|Q;KC->UqNW0p{^>h7}Na5g%xcT{;if!Xc`XbMB#-gnG{#^o03XY=c}y2*C36kdHpdZ5d(R@vJ}FASt5b(tlwPv;7(SNJdCL=kUD5Qe>jQbGOs_py4vnvvv@J#SRAB|7`}e>+sN!nh#Z%ZD0sM+mnN9b7Pr1ril_vfQ-V;l`NN3~)a4&kWDr~7PfA>n?p_XZVAB|QJVS|LibfFlmd>>4Mri_#kIA+hq5OV~I<9Nak;MmI4nWTu%`4BIKgFl1orA+$hrF8)RN%4NC>&2~u)AxwdZP%qGg73^VHix%Z)a^?U|y{UG6WU7Hye-l;bT7;<J)iyBcV&B)G?LgF&yF$Ec+}@f0h6MGl|!=Fb>n<oa*7L$v)Zn-Q`5_l9JOpp-Q}4D7eoEjcuOWQ+{;o_T5J`WjWj01N^(Lrd7ik;kTNA7^hb+FGr(R8BA19#2B6@CQ=wxh3xi-+`y5{_Kq-_rxm}NO~YO^h<a>6U$mW{@-RE-A=2XXC*fQhFKcH+T9!LrF3go-pf@+PFFjg2@N6|-oIQFP$8OM0E`CFYG|e$*Bs!Xb$iy35M}J2!oa2JM^CHR9emuL-M*Gd|wCy`g=k5RHWl8HjYj%X49$O4%McI;XyB5aMRsR8lDWY#<!F69@Xo`^w8H2M85p^m4ep51QaZ*b#)_5iU)#caXq-nOcEK3dsIOH~L&>$npEy(%t#5>Ggkrm@7%JtB0E+k*l8qgB6ARE(_>aItNQoKXO{RAVEuejJuh|)E~KQ<XUwWfik8n4=vfW^lJd0IN|F!yw!+10OXmr35*Cq)_bswoA2JSN2Rx~wJeSc=-^5jR$rz8&m+6;Yhuv!D#lW05jjc_@}_ZcbB*=oUx#rkpA`7%-th@hzc3zVfO#B~@IZ6`mT3W*tbpK-w4F3=OlT98ikEhgW~JGhqSf9nMe_1f?%9Y^~9{o-Ph^#UxBlC!~zu|2$wexayg~=(YOH;2G44j|grGuCUC0AG*?FSZ9ZC#}m=7>4YH<;Fo?2Ezb<r*}ym&RO=8?FZdapD$cUDhc5{{zqR9S`Y)~n{~HeRga9Xnb>NKrF2Wm(LC~QS!v2FpX)+HIY4Zxd6Mp>g$z7#gJUV*0HeB2B{Bs~T{A=A?OX2U@q_t)xo~mN2`~q6#Z2EGoINSRQt$cm$Va>Lq=9{&P<u|SJRgmNMPgjC#MXQ%eDfai(;QdBW_?pIBU6atgx3;L19^Y47fkpLb9No1`_po~2@GGrp8Rv(WTHBRY@@r|gRk4Q%!byA0*rr>T1KtWLTh`KZm;NeUE}!XEHU1*GHo90)WoyYCR_?MVdbEMPGFpl@st}64yAc)|rXY&?Z^n)s<Y6I!eWMnuP^~~zBrbgOovn<pry_*`J(*>rG)X2-SUa(6)nAolql^8HbMA0T^B{ljtqFpOavhlq^8Cxxqu*)1RvH#Tl-ttv$Ey0cyQWDtH>-<vbvI_Q?n<SKeRh3kvD?MQChpeScDYoQO1o>uI=R-?zx*n{34&Hp4|iM3<y509)u2sAmNdNbuN4PaoVJroeU&k3HnX`_5>!@b$XQ*1*I#>s$uGu}igrwHsi)zn?i%nn(0Y4G>#|@_MkzPnTD=n|?kooRW?_PbBGsJK;^hTK&{|tzqh208HjN><cut`!$11KuOYFg}G^CZb{jqhDest?TUNarl*Y5CnoIDg9jFPjkkJMJs@5Z`UUn6TJQEY!4%vUQVT^^89CZy6g@ZV^0@$AzLU1Ou7!h;~~XL%Bb%ZKtD7HN5@gX+fazR1&{m*W^ei27l&WL{OpE9Z45%<?puuK+Sf$yHi)Ps=FKTD{-a@{R@AF|tmnPtJRmh95*(lviX^UU|SmZ$y{6@|Lz(=6Q&&q%}snr~V`i`?u0GIeQw5qG}SN#N!}}7qw#Tr60e4_uvpWQ@ytT;IJd=b+8T8?VD*&$9;}tkX2pGTE%%f#YQ+)!l0(TOhs|nNxGkey}V=(M*+9_8Y&H&^cs`zqmI{w(`LMtI^MBk#T!1z_}#C=4armL(0F$#9@{h@8mddO=+i!u&?Q(DFZJJ4R>HEI@fSF@Q9c<rXK|SIf@z2z!OA{@>0OQT@32;*KvEC;=oo1S{$CRqRa;x9MoXhMpKV6*EWEPRv9O3s`$?9>6jUXvW5WeM4h~nn=+T3n^*WvDR^HY8=-}xS5d)IfL1|Y@AsK58w#k6TU4Vi;7sGyzdtn_X!3fb<aTtZZ#cg8`I{&YMM`L8PEc<cBt1#@3Z+qne@ttqc1C3lR*NayQxi0*~F&bG;xv+~y;lb7F@i!^-Io*8Ci(p1`fd1=O{|z=6z<7o?9Dn<cipBlvw;Y?(zA59bEpLLjbNhf5qe@?b3!Ml;b?**VmsYG8bd)Y43nW2APsXAJAA_BB{2$>jnu=osmXATYr`9Xg=iVystg+;gD0Pepmhs36kF5)E=HPNO9=f`|HnCeZ$+MHlU=74}Z-;YS$qv_i_-&7Ci7_r>1G%A!E&u(>`#cU5Uw<1u!d#fJ&P7+ZC!pf4wedH2bqI>ptK#+yrm$?WIRW-jGAJm%_RQ7gWW(V%%mRX8m|fb_P8^r->1`YovzBl&i4HlpM-pR1zU9iChm~7KlY{ZYxF5ctbbs5-z}tRGE?!z)c|&i4#7X+I$utvWIgGPe3YD{76mf(|VBjDSqyf;*Y`0!pN9wr)TeDF%VW{+&fq7+z8B5--7mpKfVhZ7MDPb8yEcBsjJY3hvsX}sFmzy9!sof{Me(riN4OghOMwPGCb3s!x;WNrMN-01>2!k?2fiO3deJZmQ(b|p?!UWcwh&FjJ;Ml~2wRcawSa~fp-4j~<i`E*3#|$ALSGtZ=C2Ut$)!s5h@vq=4L$$GlYU-s@-Y`VPLWqGRBR?7<v*<)}f!_$IiMTIeuDwRc5>Q~Fhlt)NuYxR$eg!8aCTK^w1E`k)tPL;;v{7DeQF`xz%%ay3%X>@hT?N*?S^-i9?l}B{NXx-Daa>~3$O@+=g%d)-VF>_Y&mCmLfdmz#Q0BY+2Q79{val!ZqNL!Oq}<absNFJG9h#MzuP|7iSk(>;cjzy@?BbtUzFpm82lHO(u|s~*U-*`6bO)Gd)oEDThjhq3gj{pP^&;ab_}EZW{sVg0&|qHfUqdfmb&v>_(5j89ic8{jsR5Fhw5~Fa2<w=>Zi{{e<0{)##=^M?*|chkrn3wxSa`0YjnsBXX#DqFM4SfX`XZ)j{(@(SwnHE&FwX1(#@PHlPx+NgKDvO~eDtDv=<I$(5&`7)Uw`?p@te54P!sz0T4d2PjA+nmPQ2h0WXaU)!N21K4l#L)Y_u|O``Qh%!5U12(bf%Ve|77FTZgxvcOKGvj5;gA=$38^|JlZWuH!$XH@r!@GE%7dRMMwgL!T=6oAfW$^QoeLU8@{hRK7*!TU5S9<y%y~Mde#mzQyIKuQv77=221IHq~uY-8R*2Q{6VzZByMg)!n38n^bF)YHd>aO)9@h<u|G17WJ}4<+rH(7K4C#*`iuoRBMZBZBZ{<RCk-|Zd2WDs=G~fx2f(n)!L?7+f-|tYF(#V*QwTZs&$=eU8h>tsmJRKe5!k$>RzY1H>mCns(XX#-k`cSsMZatb%WQ8YTck(H>uW5s&$iU-K1JKsmGgC_a@c7Np)}Xf{PXBCEwsR-{3{x;8ow?W#8a+-{6Jc;FaIF!GE|Fi8$PfKplZQ0(k`X2=o#7!wBU2+)9gEX$kz}Rv4pvMk$|h%4ekV8LNCoE1&VoXT<Uuv;4L|V{V0!%V+HJ8NGbQFP{<2XAJW<xfRAVpHa=<6uW_2VVv_B>3qgIf0J8b?DHA@e8xYY5zuE0^tZ&O;#L?5ea1qc(a>i+^cfL-#zdb{(Pv!r85#X;u{XID#!8>j(r3K%88LmvOrKHHXWaA|Ieo@X|GL=X+zKP8&lu`6iu#PBJ|n5mSnA*4Rv24-MpyrapcLE+W3108>od;!jI=&ut<PxdGv4})xISa9&#3D&?zR|rTa3Fc#@!a<Zi{iZ#kkvI+-))LwitI?jJqwy-4^3+i*dKbxZ7gfZ87e)7<XHYyDdrlxE03TmZXJTT~I(l0tF2eM3Awy#n{?nY;Cm#5#{QPtu4mZ7GrCRv9-n6+G1>NF}AiCTU(5+txZ9TxfRCN7GrCRv9-n6+G1>NF}AiCTU(5+tt~;zxjLh1i_x^jXxd^lZ84g*7)@J@rY%O(*0$gUT#pg6#faHr#B4EQwiq#6jF>G(%oZbN>$>12+zKORixIQMh}mMqY%yZC7%^Lnm@P)k79(cshG0qD3L|EV5wpdJ*<!?OF=DnDF<Xq7Ek?{1BWCNS;B11mF>hmxY%@l-86(?_k!{AvHe+O)F|y4V+4co%<m!xyZAQg5qhgzJu+2EwW*lrY4z^o@r*d^h#WvH=He+O)F|y4V*=CGv3%)EEv*65<HFGP1IScMA*t6izf<ZGzwizSajFD}|$o8h-@Z1VxWScRv%^2BcjBGPTwizSajEZe0ob4?kA#ioZ$TnkSn=!J@7};iwY%@l-86(?_k!>cN?QJ1wa4U?TZN|?w<7b=kv(5O~X8de3ezqAu+l-&>>q1@;0t;7QRBSUUwiy-MjEZeW#r6$RfxBf?Y%?mh85P@%ifu;4Hlt#jQL)Xa*k)9011hR`uOu|`rElqeQNPyIzi!3z;}u?P-lBF@2qY3o`RGwEik=Podh(?hQq+fIhS1gSh=4dX(GnzJWbkvof|TXyr3V*a?Oqm!vFNn1{LZuf!<`R;^rv^Ag}dW$(y(tojRV4^Bh{cruOqcI*zIgQrq6m>;}_FmzXQ{#f82k&VLz4B!JI7RnbD%tF@5QBQv+$&s4T|nTWwqLL=dj>1eMp@dw9oKzjL}s>%D&UkIKsl-=QrG1tAx%8T9*g)s}GrqsUXMJuuY`<{ZNMWz8430|hqVr%<-na!ArS15A~<=hP;2Yg}E@ZMS(UMC3hEqdlgsB<|8*3wf(iR^B4PeyeA2To3zoaStl4&FRt8?l_oq`+<jPbb(aIUq>6qctOA$TOg;{-l2FZkJAvZSs^PL2i<YF<2{5efWL5uA8X43{NlA&WyNk%-wm<PI7+*<*Ye~fjOjj-e$n3JU%dCS={N$g){fTS`8Yd%yG9_D;hyRJCzZC|d~%!1F7^n=VpgdDLIx%&vPMyCj`VBR?t~2q1EX>U)uy?j@V*-tfy<SYwz{aeIMAS9Njp5K6}FY(E0kSF^n-ZhWfz|VIUwqK&A6X7qR7)CRqd;?^0R_s5tX_sX%)};ic4E8NfX{vB6ukA$UjEKxc+V(H&zA1qt~zgEg%bozlqDX5Wp^IFz4@hrx(8^0^|AX?e(pzt&IXK#>v?_1&kw~_r}Q9?SU1XKF=svhhB*?`_UT(?*WoCypE;!@Cx3Tf<2$R>@}#1RiW`7>W99-NB=x+6D@=;$a$4+Ap@(d>eR6v9gB&NEXZUBud0oEZ857Eu`t`elbUc=ATR6QOmIB*u)NaMx2&RWzje&{N-}V0=?(=zj5}^5_1B2N3)rv>guJCF6P2jkOWg6sn!4~nO#j@ZU#balbFaSN-4)$80nC<hlyh!(^nMo;!#B40rdQ|;g_RD_4Ts5)B7_A_&tussF-;zs!QIpq`W4IQ2TPleW>M!z%STxiYqwOSD9RJY%VQEPSfqgY{XM0Av4g7v{e3SzH(hw3`#PTj1WIHQQROyjmUDuamPCfvWDB;tgxR^FX*W!8{*>fTTV~Q?Wl^e>JgVRa!6{TKF|FXmB<slFq%zc_zBr_-IeBCFuAFS`Pa>>iRSS@gA|jwN4aJ-vk0Pg-Z-BcM`CVgv0!wVWHhE(y??UO`a2*HaviMNAM77X-q)%lTt4>2e3u%*KI)-puVp0R;Yf>GwL>ov5hQRyeDy_XGi?V|VWOn%L2(R?)t<=~#*4BEfno3~S;z*C^G_SkdibC207#%JS!^s9Kwjo8~5C%I%v{DG3Hks!0s)j|oMwqK|<7PZhY>Vue{OX&3D&)HRUomP(`2yay4d5}a7BHlA1MdzNvg9V-z=m2Oj0gaR=KJQR6_zd1;>-VKSb`Qsi*Q6tWXHL*?oh3(7_Yi*Y<ONYCM!^@bpkRBZI%RVU2JQkf~IOzF$`^Fpwxov8(Xxp?n{dvZye%=lpqubuVl!pyTi#{Vxq$qVivO#5jyY9CiQBe2uHcX2rDcs@+1$&!X!eK1?~cDHtdUZNz<zAD@1d}R)A`owc%4us;Z@6jFu4dj+_rPsR2=vr8X)DB<q;<*D>8_mVZjC5B}~1<FPnql(dsohX#3oaUM|Cy`uVYolXKuZGyM<vL0=D^Hf7C+!;h;*#8`=dlz8@q{KExS$33=;<9K;%3O773*drLXYj9p4#s5XMXN1C?AvHT0%HE(^dv4<9RT2%ieVB!;>G#zcxb8cGjvk^e?Wh9E`qf89$ft5mWYXpUJ4)l$A7!!?O*)D+kgG)f3FFZRdQA^J68z5P7&n@?fG<5dix>I7+9|QSRvtr4+aP}bhfZg95ji=;;O4P0pW6c41voxC>N^S;tE<?S`*|ov^FHF3+3UUh7k82z5eo7@_=)0DokgCLG%K#u_hz^9Vva|v5-Q&qj;EH{3<flMYo>4cdQvKE~OMq2Q@<zzqg6bk!V=wFS)aV&CkcNQnitFj!jqTq&9i|>YorDe;0UlftBJsF6yxtsy?cU8^$p;LgOHkZIN!&H`a-a;aGt%w#$|~-cLO#Kh|DCv7L8YH$YCrrr?Y1fX}icYIcVkf7@$I;Z&MCJwS6S3XlLN&6ldjbMG2|F-F5T55DQyo5PETqu;|3990d5Vx|ZP*59GJuBqO9l}TTP&D;0A_wdnCfIg(rd^5<SZZwWS_C%gM2NoX*UvVIO%{+grx!hFlY=q9??A>$;^SK4ouhNE2Mx#}{)glJi1rA4`f<;c)i(}moxdc0^XooiSY7H3&A6HAH;8>|4iBBKLSFc{hHSn1C0G0x={U@}gqq(0$!h47lxY3vuLdw4MI7XNQSz=u09<){~_EPhk-cR7vnUna^gS~|+pwf0M*K2V-wGT1!6%4Liuw5t^@T;`n1?8ffR?(g{k#gxR3XmbU1$nH4p|h^HTzb37uo8BKc5$yRj1FnD?Rp!HT6sCHi~bByz0_u?#_i;}R<XHM?T)5z$iaQpwpW-)ZKLV^coxhBAZVZWMi;-0M@G@!D2aN^Wy#!>4Gz(WRNl8(hWVoOF5QsXiaKrm=zJ}yYm+qNqvX=Ue=sn6ZPR5QUKY5V_NaVuC*`9S{+2>g8$Yz9w27aR3!fkHcnYd~j^e9KZ-0$0l97S)q3Kf%PrV||X0z5<?GdSlf|BdDaAe!~&vpFgMkOTbOD;K99)yz2cdaGa;xRN9Et?pu^IGOiW6=|J!&X1-tDBa0EKrjDY{Q9Z#W%gdncMW<IXkM@H<X}`drl#)XN@XI!^qXqnc=;IGhdg|19Z?>MMuB`A>4J_HWUuh1yk(8A;pRQ(1pG@DfnOx(=G~rD7kwquRFBdltJR-LtCGsJYZrw=iW;Zvv7^hp=-yALjBY`Bwd1FL$VkhOR?Bbz2E;GSydMbh&jt5z*vC0e2JXM<Va=(c|L?HHRtnhb%9j1uoi28h5akfq@$)%^4*7b_I5X<UBU^9d=tJr!Ci;p9lg`Y64gvE{En^<M?vD{$d2q7PZq;uWP8V8x4%;^$baU=ufP1aNtq+iAev=}DDBLyOF&x$BklQI*<f6T#ud!$2bP^Zp;L35oY7l5a~^qm@f$lX(@KW-3rDlW6yMdsVw3z2UcdTFlbNndg1p&w8|iPhN=Etx*8tW*-RTfOMZS3b>hEz!K!NjeJMV?_ZW5&Zhe&4A*)(@G0@9`iBQ7u_rTuo`4!&OuD1yR4FGWKiZ`y7*0}SPmPJ%I<uJF6-)w5_A<6#RQ8jQXA<1ihD*K~k^M)S&@yZcX{-#Uav=-hw)^!;ZP?O=`DS=+(41)Ccio&8Y?RB{qz9o;us)6YX7<M`_qtYFx=5AzEt=N2&IG@4Cr<>LSrzSjxjUIe&Jd1=svltcN+MY7HyjC<t4<aUrn<IaANkLW85dZW%MhK-naL6D%dq??VyXgGQvh$=~P(m6nn1@twGhj4^G>x_cQ1c(Nv?FWPKaMlgw@6HEN9L{0DD&a%GymTOX*bmZV27IaWw3jE-Stio54uDUnNjWLYVd95rFqtM}Xps|7!_Kp@7~1{_-?oRhgE$UTBjHXmG`^mEbO=jnC3L3I5WRiR%w!Fv{ZZ0O#xUl40Sqyn)6#H;SgqS~E;>PvK_tm}T8S{7DDK=&qy8|oGCByTLdqyf1$b22y&$rC>D&jY4k!z1B_9W|o%gU8cCr&ds(5H;8~|Pfod-BRM@H6p9-<bYkQKwS!vQZ(!z?RjO^ThrpLT<|lPlQEbYx{VP)x|nq+vA33%wvRhiRdgDU1ftJ(IYoGO}J67uw7b_>>f-y%~ahGL@i7#!1?_I}{(Vn7zD14&enhCP2Oc)`OhC&TggXD_(qblX>S5DLZ|`ChY9Pt`Q$`cn|$?%dTfxo=o;fv*;uAx)Ve?@lF~HllXQL<i#|-P{qVMi5Nd++@A&UA;9;(QTTBf-JeDKqc9%c4w7Q}eW?F9jEl)Xih}r2GSkV=g18^(&mTuY@?Q8T`f&E=k(oL>7$vjA*@s3y2hk{;&jO<h8sRLt9UP2|%7+o4am)OUhaXw>J__&8{(NMP>LYYt6eK?~lV&*#BAV)yKaU<kQ};zn^BxeDXF+-*7M}KY=N|E882nVHJ%{5I$kHb|1?h-diaSx9z;+pkkF1wy3V!g6tdj45#1bMM?Mwl8so-6pYB0?W|GFY7oOF=SCR6=sl2A_RbZ2oKg_)6}wvGHY@a*nzKFyy6(>ah3iBg<43eq4MY4XRZbD*;kb%!Ko-Z63ZUXYD2($DQ=mPem*t$R@%jGu>RFviZ1nA1KCc|thC(Cp|gRD$3l_tIIELl;Rd+0Ok@lI5Do-3R>3O|rsNPE#zK>ODwuMYAb)%sZQQxRszA7zbIV>F|Ag$BUk)Lgu>nlYE4nRBr0~X)p!6k)-cF3I`)>3)A}Olme3<poa1u2to1#s)w<)+A6j4G#&EXbkZ|{ZVy0gn|CCqrxcjz7&?au!0Ao^<v}=(Ui=8~1~D^0hZzquK(xNfg9bnQY|J<V730o>AUzG4Y*9lUlSu&-fpZ?5iJbwT78Vfb2w9>)Cm50maGSd?Mp2i;LZvgw5g($*rSX_{Mh8BUNgM?-BPAR850msH6T9z6Fy{U7j2yE5XofBkqn-rJdvNS~9z^4_V9uZMun*J}mAeG<M^PG>V}1l=`;lM``1=qCMU#CD62}O+6TyvALOf={q619$dl>8oC!80>5#U0c3Ci*~>0%rPXyhc!Ie|Of9|dDL!R{xY%@wK@@*d2x6C-m5)03;9Q#uEdeLV@!cxS;j%d_rWq;)<Dd6@7UWktN{=JE+ls&hvm;nVRP5Wm*}!7s$UMl4V)u*~Ca)*A^Ki|`VY#d<so$oMB2bn+336LXOm=6QI~n~kTr03a+9$eIVp@d+l+fILNG#*!fAq-gjw>+!&!MX_BS)(%9jM3e+XKIy1!!=FD2!>RsK1EjAH!!$fg#sf-$Jplw>?{=B+ID}IqCIAw}UF70Dl7yd!=#vY#@$FeO?h_k&9tGn(F=Vv^Ks<E$7YuR>aSi|$2e?<|R|0qr1Y`bKc282(0g2V>6J#try$Jb2LBiNU0%iwca1RN+Cie#;fWzJKz}RDybTE$kqChlNqzgYf_n>QT?IcowJAk9e*pkf+ihD4HRez3p0j`I!&Vn%<8D=?<rg1j_NM_knC9f0;7__UL1ILyhg*kL^;>brQjN=3dv7Uil;51Ke<>Y-*0?*3VqIfYqAI;H?-snzr8andB@L4oY9Fw^nrTM5I%qv?45PTTrBZ0x=VCX6n527@b49U*i52i>Um|?<tXRdkSF(v5qN%pJC9YoovDsQB)(UED$*3N81A9;*&6#%3OPom1)Bt8k}j@&4p-wEa&^jwGpW<YX6R$UOz`T0r(xj;AUcLcR@7n=sB<0!7q&v0A0x=G;l8=r+hAq+{%E+hR|9)f5U$4M5<#A&Wj4A@dH$sG-_RQEjScB8y1_h3HhCgZBy!(<u->AWhtqYt{kqAE-AA2|8P^Ce|qwSitNYsrmAqR73Vi@FqX5?fNF(;d&Mn_|d4aHG8_bAZ~R;r%Fe!SF>d7)RZi1Ap$N$*^kONw_t*Mmh7nD9Id@k7VHP49DfjM2VPa^&}j-2mlIvy<|%8HB}~sQVA;CNcMB!;=_0V*nlq+So=~g0Rq^2QSQu$huPr>Pdw$!M@(I4g5_K(c)@uh>4%A{KtBpkBMfqyMlPtz0*Aq=lZe^*LAiiXMZqcAH9)58RgDYT;zJ-64kUV>Oh`=!$3-Xacs`5b%*~LV&ti~sZ$+s(J=*!eC`|FakO^G>zH3t-OhHJf*n^DH_kf82ngwxHfv1DRQ7APWt^z2|9|8*pfzdJL1Lv^t*zwFgQ9vtk@OI$rA<#~Tn1K_#ohCh?Z;>l^);lrOKX&d1Akd*sJrr!DCnYhf6m7=G(Rf^uRUy6vu@GsC$q`6no!nii8zqPYt_&7UIw;(`$U<)v4mi`Dt7Qs2raDT11PCX{QRtc{N;GMbxGB~^qES{QdH{4`!}qHuJs8h#&vKMb$8%?HCA-1A<jk3VXXX+*A>-~ioH{cMHFYTujy$PLV#KU49?l~7;NTeKPIu!!<dA&t%sHH;PD%|~AL4=2kt5EdofJ<!aKesV1Rd4<Y0`DgZp2yySmB{O0$KSH99A&w=>&wYfg}Hu87pJl(&_|}hE-983_f)ClEEMh;RNPf$)swvrorqa86}Q(r(rq`^VwuP>$$lD(cfE>DW1$+n{Yawp*G4*#nZ4~B@AR?FhWl3$RRR{*A(TvoQ1kh=n|36f-!0~0q}1A%_1wv(PxhBe1`a<ume{|lE>L(g5siF%~?9oM|1jmmIx^nKb`~i4D{!L#6tKWwOv-Y)j2o|!@MI|(qRNg)Y~kz9|C$tSuXUo)~TDwE1m_OMOh#cVs$@4_bmHK+@JM?ZVsC_6gKpk1t)<1{23+u7qE&i<5WFLVHx0dlnDib<`GIT)=B#_V6qwc-nTRE$zzF~d_VXs>?WNtUNU5M)-#wx2Oo!ZvNIs1b|!P%&Lc-Xkp=MS;b01x$ZVb69ftirFcYC$a;3Kl8TyE!6MI2kXty5)6P(E?6uh*^V@ohmco?GShzyK(mo7nVJ&Yd&aX)k9z`pK>nLtFH_X!Btk5P~;b|_A$IstnOgo4OU1q|+naYatAG{XrhgwQKJ4(yZ}md>4q0W#T66ql!H=S>_y01^=<z+xRa<5@Psr6?o=yUrvx(aBkuhH=m@v?1vb9Fls4EJ=n4*4d&wJ?sxr&geWg6to}WqbJ4xNp6x?%m>fNr^|<cd4R3$JDTEr7(u0H%$ex7K=zSTq+<pU0@4;B@jej=sJ;bZh$*hPH}7;6bq?sNUEWv*pUwij|AASIqZcv-m0GOQH0Yzu=$w+{nSih1L7YSUod)v0TBH-r7oatgKY_Aip&k-RNsvVue|LH6h>t;t`Y{k0#r3{S4*}v@BN${;fCs^-8w@cW_k0*gVGU)%gHe*;<*=S&m$jFgeQ-j?KPTNJF}mmmNjK>7uN2@B^H0_^i{C(Q@vGy%;D~Bua?lS*p9w9eI&nakLK86#N&@hsj2jrG<{_?eC!2LA0CMIZNS3nBAeclfD0Z2hwGE+IByFJ-5!01}k-DGsATc*OV*Sl2-q13eAys+MH?qZ@)({Qq%w%z?C2SBx>iq=xGVHl9wGv~q%%j<hSvoH@_&7O@tQ%yJF0}WKoCAP4u#>c}3?*d73<dyblE8k6&AA+kTY>v2dOdK>Hs}Q)D0GIv1qXxB$^an|$UWe5G|tU|%l*|)XA@UC?E2VB#sg3WYYscZOozkC4CJr5l?Iq#9BNcD-pO}xGv*eg1LWFqf-;PvH8M-u$OMMQx|r8ZX5;WwT*nqOM{ocgyE0Nd+PgCJ);DsXA$w88{CKmZb_OvNtpk-Av$X%&2+3eHFhSU(7CLwui*h?1nYyBXR&vi!Em#@qFlVJos;LqkwNKH-FEHSEIJU~dfKNIhoWB49c`4(Q63%h@II<R>6G4tjt*MWqaUVDv@X55WvH0v;z``Edfsg<_>)NH0c)*sl0LdQ9bt)?bQa@Dppei}fgJFo|-c0VJ`c4r!N@3Z^N@0DmmBeC)xNVWC$*@f1ATh%&l1Du&bqog>3nBU3Uuu(63GIwz<{ailft`^_0|uEa)-$ux1|{?fUjR{xkRo?ZVmOwBfQ-dWYLpoVUB0NByYn67-N*%DAe#ggd1->dH4?L9;Ay~yfrC%1M7(L#7uH>^?<g+@rB2kbqpLI@h%@?nL8l{AISnijacU88aKL|1PI?^nXIWsUp=wrKT+2idf8+jblwmuAeqh3Kh)UW{q5Loz_fhHIG46>~Rt%_R_Bh1-8s$+3Utoo~vglLUAfXM@1W1zEuM*xmctH%?C!J4ocm4_BRt_kdpwI)P-Rzv8^f(yfelZ~%^};)$g;b=a&~lDS#CeueKonQ{93uw~q$gIZM6KYwBPAfI@fZTlv&s<_q?@sFYKoh^xZX0az*R(Y2HQ2C1r|s}R*o7{v&tC8T-t}@AO&KT0soHzbLe9hONzxOX#dG(q+O|CL1C>-XXP2D#Pz0hRIvF5SMRW(Zc*83^x0>yRfCd%K-w8-Jq#wL)YD`(9OWREv+GHnHy@Iy)3Q?GyrlGOG7(TaHS7S*WOYndiCGx+?Q&^2iqN!x#C{usaHs-y3@a_<7Bg$s?~g;Y?6GiW%0^m1CnJj=rm!Uw>pSTuz>NB-H5eA$0q48puxE`t3!-s>3uHk-xXQ?AL7k?$N`-}L#E{P)nVrK1Qhm#?S>=8@OQOI^Ne2MJ#Kb*BgZIbtEDJN!%-P5-)rcmuF|r43awl`x4pyjTt&sxTG3{E7<Vg@yMQa%_Ba@~UGK~--n`h!OLM6}OydOc1%_}lAt^oR&!TyJYf<VE!6Fk(Us8c9qWusYc(=Cb;iZ-5BV&RZPX{2i#MHYF=NFP)d?m4}{{_-IG%rNYgsiPq3z~rZ6J2g$H4M16&9s^qltX0U7n&XagAGf6HuhWxvbUGs}v)vphMLrr^c4#7NHZb=JEYB=MCJAiBT%j{u^n=1GQzFvr%*F^x?*a78ft}HfU)EvYNscK&ft>bZ99v^Qi?DfXbIgH_@@JaPNp-1dKs0<7^<p9GMZ?3CjMi~i_GYpK0El}K*F|vH3+)F7KojCVj7GN$^k8E{o$B$crN5FB8igUt(<#EJz~8?9PU6pCp=JW{X5oo1f3)O}w*0Xve{9Jg+w#YC`Qrxv7?1Tuy#6wl9Zs$}UkKoBgaMbHzW)<H0rcbknZPeP*N9gLN<Tu0Y{Z`_b+*dTCR+SC6!xh6m9otlCm04lg6VNOQ221nZ$640h-VX)V69S(5sDNO0%=ZW$X!6i6OjFc#HXbnI6O_dctkWcXqY%fL$uy(%HL>!%Bm^;j(R8X&k29XXAj9l0#zoF9-{LCezi8(!*)-<hX^Zj1jB)O2_|Ud00EXNrXK5VZlx0#ZbVknq&?(35VNI%g#G)rIUQ1Z`JbaQOJf6>@rxC)@BsHUoEl=h)g~R<P)Me|RC0zMh_gvQ62P3LXeVea0G*{Cv*@f>3R5xCuNYv)Y3a$m1TW^$po|dhAR5wg^g(=m9`%VLOD^1x&>#XCx|Xi`Xp4?*;ERO`8k5S@85wBc0mERX;<zU?y$8=aH`o(<e;&iJbb{J<14?|@d!Qfxgu+NE8m9?UH<1!`yFza$4u}JOOk<=>#i^G+Sz3^6h125O!DlR~gg};z>v3Q-=%|66jj+}gj&iWgZqMe{$1Ul96jKL?A$l?cvUER_i#Q0zfEk_9ES3*u20=Pe5aip=0~RAJoE=2t$s{P<Pz{73ApFHGk?`+?>x*-ACK6#<?<4(vknjzqI0!0wBECnVP}Rt9DN~AXDQ3t|Y0ItdSbXcNWqrY+WiUW2&g^6~v=8}^Wh9P+ew2)7g|dK;!b(G@O_S*~G7|-$#K7mb)vr6sxDh^t(Gb%Ck*1!Zz;AWkaGMonSuuTIUVQNpnCxJ!^#ND|z|K%_HWVmeJV}rjP`>%mGCwxW54xYT64VrB!kN5}mnmJo-yJ}~ej;xVNDnU6$eJHhGG2rhl0Zi32?>i+f&7i}DnMLA;hRi+pQOkRE2>OFPDlRnoXo2N#;+lon|%-tL$U_Tj7<YlVk+)|hvZ%D9vO#fd3%V8R$2_y8o+s7a={@SgT|~W7^XoS<%UT!B%Fqdgpi6r{ov3J{IjKhZt9=g`sWSxQx|RN2DbFCjxL}p-BiEOw5D%-$y;9j6xuYMV5%=UMVxze0^);jf41z;w(+UVI_SHbypWO<eaAr5BL2d2to|iIsMRH!%bRJronSs4(y4$d!(?8pY-@;g`Y3=lV81J(q_cpChOAoGX;YyuG!#2<icA2CL#8UWMkwrw+jN~QH<(U2!`nbd5*&C^QIr;uE+$F#IF;0blLdK&%>tZHSpJyYa)bu)^LrG>RrB{zlCvSHA!HB~7<K9Artx!2|Gc4oa!`(_7viG?Lw}2!D@7OK<B@oi0zcKOflP}8sMhKWeLyrE)6=-fe1RkALPSr6G}-thI01?v$m=KJ80a$K1n<sI*jQih@lR&hjfphC7J~^kKpzNmTw*z>lO*7c53G2O@3BY5O(d$LnEB%=1D#^nsiTD7vfy~hY)BG~F*NZYnWeg)F-&GS!#8PgLgoa98~*Lkp`B0*_{B*A=Wg-`#R>QpT?iNW@gXWr<%e-cLZ8Of3w~?WKcuH<UTG3cp+Hlk7Me2yRVKkafGvq9Fcx+uVQ<81-kFf;Dr@90`2fzT@`(mW6-ge<EOCxa?G1d83US~3Xqg{v^JCNe*fKvr_)1tbnBbM<V?)u-32Kk?Zny5INs9V0U(9Kt6po>v1R4cnV90px5kd^zerstviN<%}_!}`v<@0p!1LP<}^SGDb^CjH{DlZ<$8#??5eD$lPer>8>tS#kFu^G?^!0-4keDk9vKU!vv5VyonRDe$y|6~di_e`i2>{R*Q)6g`FpAUPm6~^{KX^Kyo;((w#9VIdDo)_XH=Nn#|xKX;0F{Vmm0LNaEGn9CMT3I%PQ0v0y(~|rolKJ3ZXMFZq(3|BsYmbDwmaXU_)|2qdQJH+A)CBa^HooSX!I6UYeHb^sWVEM-+BekIX{ssD7Wnr-T2A3d2R9!eA##9`N+b&_;4)KAVVxrW9SLc0%2wW~xKS6XSo)3Lk>rR!ouO^N-hF8xwseZ(GS)UIL&`51=@cXAl+Y2N8Jk`b05iX`B+E%k3Hy(tF$mSq#54hc2Ksb>8rk$T1S}QnEfQMAg!YTJN&s}~1gAMM4tf-UL2+yy1log=5~T;kS#DD}`kw3ux!!UqTJh6!1Y=vKXa|p%v}weKJ86Ohf5sM|>1@~~IP}F0JZhxXw$1qAT}J{x6Bp%KFw1E3tJiy!ib|BOrW=;<koADQpgtbxlSx`L;-ra1O0zH!nt!@|6-i2*h2LZGH%sXCa}OYv0wq@up*idQ0c^(^EWepE5|7{D2Z;1aot&X$685DnB-ve~1h0`n%3b(ZKZ7%LNSQS1(TGMWZ25*ZJBhM=IQ5tsN$TI=NEyBi>}bKX!-3dP@go1;Q&RtlOd>BVbc13yF0%}D$bkF8E{qLMN~&$mO6fC(gV9(X@H3RSU&xOf?YYb$Gab@*DI$T4!0;quq=9fUu}k5duHdRNWju#tlbIlnWMTrGID{dl0uOWw&>*{c+8b8$KxFZ}pO37{XcOBj3?zqHpIDvdY!z#yfYg!8B1vlAwPiUOVk^>+(eqsKqS)NV*-R`3eTcJcHt)ybypv4D`9BXnnFKIou?V@i<Kf?MD4~UfImIX0kj$s>F?E`#r-N43sXSiZCNr_>e09z3&Q@klfKjN+c?#qwHaBuk&ywhIzPab~NSykmxuQNPsTBJLJ5S~%EgtT`6ZwNF2uPoN%%IoSJ^e}{r&BIkm7!6wu|a8%1%Ua2{Lwd%2C1K>Z?*y^yyvv!6Lft*-rkJKrg-OsM*?fEv$UIJWL%*YD*0*7<_5Hwvq7>ip3}{yD52a*&e+L_rBqd5&-g1(=K;<CRET2wPC#ka_})b9^^RXoYUw2Da^p<CO9qB5H7pi0q5|-_4}3)*Ce8rD(ik1ie^RS227iW6uyZ&ikXBPsqcick<!odrCFqm*lssvoURVuK=!gxfeip_3iMU$h+ntZ#7;lMfXKXe4q3luEk?f}dbHX{`SFV0Yu|ilq;#g?za{$Rum>dakD9fkMk_6vfu;@k~YJBts>>8js#w){AmtmE-{On6pTl}C+HJ4vNpZINuBpjcy8XXTJLjQp&l-nSxO-~HS<&}1jWnVtI(pyy-?W&B;s*J6wjP0t7>s1*ysxod?Wv~jsnd4XHR8HQnoV{N;eZO-4ekB0>N(lIsAn+?;(5i$%s}csSN*J^%=hLo)LA!E3?aKMIE9bLWIiJnS`D|9>ZRMz0QAEz=S_Yh5i7i)R+m*QKN_2L#?Ml4vO1$Apyy+bLhBMVUC)fr=LGS_$$w!7RJbDqCc?{#u!xY8td@e7@3fcHHvm)!@S?BuA4f^fKJ^Vm_II@LpepPN3q0NXpQ@z&oH<W+Bsv;Fl@NITwuD&C!D8PbWRW4fAS7ebdtqw@{PsAIzLV-RUKr8CfjpRa@_EY0oVnrEgXIhb~woj|oX|*;sRw&qBwcuu_)n2LK)~W@!JFU%?3SM8e;EhgeYo&rWS1j1x=(M(1D(J6T5LV{;N(I}i76drntS*T6w@dRLJ9E|TWmWYQoeo*{62%g;G>%X?U)6+hzfo0y-`Q4VN2H6c$i$aK9X@qel$c0=S5^7shpH-bp5^GVp%b2l!W5-YBE~~lMQxS$xT-elVoB<DWv1aU$n&7n@~f9#m1(a~W^;KNXl8ktMdKk8*d=*>hXbZp<v(_1&L&Ze-tr97>_U-jlAt@g5MOCk3_<H?stTZiVO1txfmE^_JSTO|7T_@&DO7K?GxQN4FsX5Fy4Ah+{MP-)cb^=xXI<ynV#iy1*OlQ7XHkE*R@-|QpR0MOLpu$3F&t(W_TxdAKaJ^*50kF#eH_1w#?AhU<ytG2Yp+o5nrrlX)n}%v3AesAGsbe8Zwi^#UiGQ53N-ES258!Q)#v6a&}@D;K(o15tvRRy&DM7VG+TSsx|1r<Y=1XEv%OcXJ*ooD_3s8~uJ2Xr&#FLk<GTTx8++9n#46C-{BD5e=H3DwY87n!jqe6<{EfW@dgMyz_}>xe_<IX<>6Os=j!4CRwOH&|%f<e8L@@TNC1bx@H1@wEvaw$+9Q)PMvHu+rkNs--*sm6l{qKl`>{pA(ezlD3e@BF5zgkN6tHoshJ0d6h)q=8LEh+oo5mDK%mX%x8vU2M?A}hD5W#v}2tlavJ$jU92mCIHI2$)jpw?|W68v35wPQo?K*0*<>tv$EphijVcZ|^kQdv046*EBc3z0=&>b6e-Qrn&X)o#xh_+uq1E&FydRG`IKM7F4cjUjOz^^ZK6KCd@U>ONg%<-^?^i!@sfTwqA1$|C^I9OT)UkS7ATr<kNqA(XPyZH})!Q{hTxK{{&}HAu73rh(7^!VtEE29-Lpfa-|;*JhtlYbTQa>9V20T-FY5n>s}rVcf2f58{XADFAbZI@lnkYWgdG!^`0cLi1ALZZ9)~>9f}U3xQ|Bi^|V`ix8}W#Z8gKVm-NGW13n@7<L=R4>>dB$hu8Lgy12w%^9MhC_gY1f><4?bb&o>7L$?Pa41F~4#$j9+<7#+&p09&Hr$GdZU`3g(4{G}tzw_cz^!n9b&b*V+>sLRIyqD15`8zT``Nii`umAehuPG9{iUTgfPN!i$OJfO$qm5%6f&>c%mPcsW08c}90aXq7b&v8yIxPeJGN2AHFRmZeS8$+G#^iaRQ0!=jvYJ^ANK|he13;+>_=~xm8OHs3W9OKvhxE+4a+R;8Ns{aJuvbFVZFt|?UA7c5;Q9*;l8!+B>v#lz|Kq>Ee)UDq!%ismXRrzvznK`Zxy4dU6C9%G5LQA?@Jey|P>?2F`#7!{lb7FE28zJsdDXPPx=s|MeOi*vja8%7=|{c%h!!r2^JAVTjd<5P4aN~hTF0R4oqp1zN7B4pwbC45$Qf@atW9tZ#^ZX8q7dS|4zNJY0<oyG0<v4U?rbs*v)LF&{qkIPA)41M50cc2VJpH^WhO$qG}dAOdlQa*=mOhl4#T`&i~4{%wL&QSXi%sD-SO~tN+IvvJKHetdTBLv?sWmXyga@5AGoR01pYl4C4~WSXGd1eV;DEk-V7ZV=XE`U9@;ANB-ZU=uX`KoUaRA8Uhiz)Xm_?ZuUiPood`_J!rbtVm|3JD>SsINL)dfp)Cy7Uc-^C3cM#<W3G>+$vP5~rNP&m|$$UNy>r}kqMHzrT$66k(WbXOiySv;N{%CD1!J-2olHQp1B>>KV@^tk2%P%4?fBouTp-tGVU;fV+n)B-UC``P=gAX1)YX~5tYu^}v2~(~&nzI<H*MDHx^4)*_^!;ZCP1roMFsloif)P=BdDs{A03>Q7;51aWn3np6Nl|}G=5;3kf|CLD8JUyHQ<yHybCkUP^51)254O<5J6=3YE`AkxeO-m7CwHc#6EM;$^3hmA%iVjPHXM{^DvfX9r}d47qW8>lfGFFQ_ujo$NT^xcyP0O_W&>6N$Y+M{3hP}EAj};sI|k~X&ALeVuOZF<GeG)o&C&ik*Wgjd;aMj_r?b$&5i=E}BBlMEB`K^|T`ru_{iic@9g!nIeJ5!s;m%PFO+;(Q3=+a_)tZ)DjwUpc2~!uFvB@b(am1ce;XfGDD4&c0l|zgv8rGRikpGhI47Ox_qL!;+lf8zwYokg3_=?eNwLtS#NuNRRwA5lZkE<rpjp)3U3-Sh`1j{pOu63-XW(#wa<Por}E?2T)gHhra{XN>D77PgmdwN@BQl2TGkdOkaY!6)_T{D<YvG`z3EvbiM`Ag);yjsTCEpRo?Ym7QjS`PdicE*|#M>PeK-RV)VL?U(=qE;QnCFj0&fS@R*;NRvaNfg&rR}CYdYq8*ht<9z=b@VlDDT$qB8e<{&APt7(=LP62QCvYy{}<0?bKOKQGj#<Gv+|C;?~2q;3=~FlPgDx~9DwR^5C_9BH9$1slobeIMO%BCGMYpSepgkf*?WW%SD=^nXe+4ZrN^=^+teWG%6c6qbVYe{t!s|TP_59A1>0gLB{pMCzyg`7x+2ibAuVM#2oY7GVTq_!%*DjaLf2x4U@mm-!t#PNsHlL8W?IXj23ZgfOENE3E(^HMbt+Rya{_N01)UVrO*J*$G8V2(yK0S9$5<d^g&|7frpjvqR>Yr9;Y3@c2lVS`r-;VpF;|W7ZB@Qld^ulX=qO5{V6&WhRg73d$T2z_8cRs}aza`lAE#j&4I*mLDW!@A8w&(B!4$qJK@A#^gCv>B-aDvNko~P975xM?3zI0e<olw0l*1wB*ExtuUw&Rt@+kPetjT%TcK8S`1y+E4(C?Shy{r02AQ)w1-6chOUQN=cOtfLqD<w<qFrca$iIa}1M^4yb;7~`9z`DW9@gU_|686$iI|k|W>LP~UI4`S7rfD*n!k)uJsa6&q+&wse7Mf}J=?s1Kj*|c&C1@ux8w}<GNPy}Gm_a&${&&3E@Bi-gt6zY`8qit&;<vCuc=r59kY52Da-dL<be-NcPhWCV0Yomyy&b)N^)oomUHm3S4braw3#O><tFflzY!r<{?=YPiyFJLVFwND#d$Tk}fP&~G57DIDQ-lE>8P<WKUA=nM^S7G@*gQxw2!SZ+H@%+#t1u3crx(BSGV6Hl(oTr#t)_Q~s<3Ol*I)j2>cxP#zs=!*ib#I(yV&c&^!_F;*K0fL<%IT-^o8hi^7_>;bI85;-K5;crn?O|6vueN_@&nks;X`@y&unlxi`ig<^hV%V5AqnjZIOwH%g*j2#65H(;3v+r>VdyHkv|+FiC_gz3bIBYDJcgTURCJX@OAa+N=}tU{w%nTKG>J|Jf`GD8^JCy?*s?fq=7A7sJOFQ<&VV|J-yiN%X4{#j~(t5J1qN!^-{uVXAk7_frorqPz(p9ag*&{mWydy-1tT$BiR)A^~MbZ#aU_j@V!4M4he0;^jA&tlSe!oI8W<qzT0;+P&HnY`qL~$8`AkQl@d#^D5$yghwqHk82gplkTmKO1CBk_9WU!av-uz)?zuCpVDwqL8<}8II+>Fz!DQp9mu&<`{W>KWw6nB;(qvIz0AWyboGh;<xmH=?)eS(!ZFqkYA>msoz3%Rf!pr9yR~tS#BIlWsTpL6(XV?Oa1eK*kFoXrntK!iE1w`=kG;F-g-Ki_e5%M$v+3Hbl^d3^@~lXoyo19-uYTJ1{Pp(w)>VJw9jiMi^Dpy;lZY8JLOKL(?_6#)sJH5oMoZ|OPJ<j@cN3#W<tj9}?$uEN6Em*Gr1AnX64w27k~C1j0NK-TG#U%B9DX0+!qTduc;FvvY{6E=VC+^{zbvFev88qe`C!pcE7k>6ZACNiqrZ=sv(^1(vjr#9BmdY0Cn|n<UsyFE0cHs0t??*n4uohBi&&>@sox#jg!J%2@oqOKasA>i)otNRZuw|Uid$>P=QRFz#1$6I=pQ0oj3h@W^Nu$nJ}Stx%2$#hwnKE@u;(k{uizNKF24Ntyh^4(Dfi#t=P<hXoD|)E&76Gtj@LE##dro()*FLt;y25;G-7y$;Cfui!1k4JQXId&=@aZUd;R7A%cCJ3{Fk58{p$sY3>I|gYGLyF%YU7*27bW+okDT-SZ_Uh561Ez|2-g`KX+ku4YbFQwz6RM4vqb<#Oi`9mk@13goOXG?r!m5$|PT%`F34$XyxF=T`G>;xU{~EM1piE$WA)*Fzdugoexi9JuIP5pQV1dKvequ-(7sc6maE1$oZo8;W^IMK9IUPum<*%$Bz(cVI=^U|8uYDeen9#Uz!5vy2Q23wl^F_ykh8GRbKXNw!9ZJl8fPh9gNM9hc9~JG`FP^fET9kI0?feBwxVipul;#o%g~yx!ZV%{34xAb5|p9w9sJ0bxmM@e%`}jUAgjo#(!@x@p@=%;&0*c>nv;Y=k|_wn4HBN(bwzm){y0S@zuTgJFr0}$!X}R7%5)T#mJXglMZ&X7_|!+prl{C_O7~dTy*FC2-=aCS<oNQUDTj-W^wfC3_aDS&@+c=6&3WbaTnpecuk)fV^m(?jXk!-x}F{S8OGuk1)bWUJCR;ErlaMCm6|4JIuU0(MJ*5}^PS61(f*}qj6pXINlf@*_qA?yqOTs4vx55CH_tuhVBbbFfU_oXn|ikv+xIn?Ks-Dt2n*KSpbfuh1kzoD^<P6}9JDTUNYp;6SLZdlRamR7*+5phSgc$>`it7}+l|`Vx(3*~DBCDpKakCZULI6+iALYnD+kLZ6kXr<FxnNOcPKEL&=a7GDr1<h(m}H2M&<$Z=P(X-VU3qN<j|XF3ZPw+S`|erOjuNtmgSL7W#bk@Vo(N0ymk5tg-{M+gA%$>#2CF{zs|iI#Ic+7Q97q|rD(sREhPq`;STM|3<bE=(a}OlF~A~q@7C0ACnT~}{tgQZF;5GfifC1<InLgNri&oZD*kt$64en)aBUBu{xPtW^%5x7scyre78Spab{Mdx>KA)^TNU7ZQ`hSzSz4uvWD9vb3T^*XsTZVui^@5h5Y%uh8p-&HsSH$}S-;bTwb+r6mTEN$%JBvYwM*!(%95~2@+%LEim^ed9RiCMRcYQRre6HtLfTYWICsoJ8EW_rDvSQs$Sgqwi!x$p{?yb4P^*eZWw8j&Q-HCbj4pl`T+^%%B#3`O;q%pR1C}lG(M;;LK99>XrlDY3A~X?%M6cQ)#*&#9%1TC0OC+P!B_eTd-SXY?&(=ms{?UTQ^hLWF!=4(w5F&<;O6jpUaPk=m$ltnmE6pFqgT%uf#Gybya6q5?K%Our8ps*cV(0Pu2Y26p+`0Aq@Zr5%`{c)~zQ*x6I5tN>4oo>ZM?fx01M*24kQ35?yp9IsW;9^Gq5(S+4cLKhz}|8Lc8wdbAKZYQ-UjU9Heh$Q0sF2E*imiJ5@X<2THH#DTVe0BL5o{yaVsrurNynZxs^7z(iT(UR@g;t(B@X!+zNZA4cHZJz<y@~b}}2VN7-PLTiFy4;a1o`Y_Q3#Y;r3cQYhHuR<^j6EpBCtTiN1Pwgh0g6^=g?Y;h}F+{zZWvdyh*b1U22$~L#M&8=*U_2E{wxs`2hWt&^M&aJSIyWl#v!jYMS>)gt9ZsodIW^Uy=w{o3Zxxua6;8t#MD>t~68{EnbZsi8IazkJXw{nA9xyh~E<W_ESD>u27o7~DxZsjJoa+6!RDUeQLoj|({fp;4M@iqkJZ3xuc5V*G?kZ(g^--bZH4bh%LW6_>OWQoZVl_f4qWR}=0(OKZLFA&;q$$cT(6FBV)r1k|?`vR?ff!Dr3Y+qouFHqYTxb3&)MicD`^!5dQ`vSpzf#JSDabMuLFOb|9Sndln_c!Iv73~R3_XVo^0@r<k?7qNuU!Z$SjIY&}TUhL2F}{`<UrUUyCC1kh<7<iWwKnBe7JFH&M_a5%TdYT0tVdg{M_a5%TdYT0tVdg{N4q6ygJ@5zM_a5%TdYT0tVdg{M_a5%TT&WHY9y^u#749y$&I8plHf>+BT0^=IdZ;YJ=$VD+MAMkiT1>Lw8c8K1^nBBz_bO0X$#uY7F4Az2uWLzkhY*9ZJ-_vn=3qh{_y_8C+yo1)|DQOM4RMF7{eR%p9CBg4D#qX2FEkYc9LEg#QQQxG~~7y=58*`-CCHty)gIs!rU7Rb8lA9cAFjmMJ;C@L#ge|TL`7?g;3gF2&L_XP}<&hj_KT9?R$@I-6#HEV~OFAB7Gc;lCzN10G#?hNj*CCIY`3LQP{r|4To@Y;}B%e!z`Jly)dg)T$g(_QT}<z@mrvUdr8W*vE4pr-<yrc`w50L$E*K_kkEy&%p<a&b3_x2gD{!ycogSVyq$q*;h%*XlocKih~crwrv)!%t_R0lsolT6(a=U5(srL-7|;>8_Cb)EVyHAE!(%c`nLg`jjbe1=`^mUd|F{o_|8>KJKZZ3F)~qF)(t>uv8fi1=_v<LFQpqD<YCtXZff~A1*Rbib+caikSj<e?o!J!6M4bUXk<v%Ifiba{R!isV5;($t?o)VE0dR~fgb|D-tlbi91D4!H#Y}6-;v*`(EJARuz3Jm7>%E6)Y_(@iE^}ZLceFh)54E5%z@m6R1|<na*t%BTb?!JX8yV}0cGzoZCjD{tgB|#PtsW5K0U?3bD=r<?!VqdHwEF+4d)MAbj^t4E`}~S>?_C#r)kCuRm`9JO1<Bz&R>K);$QeB-x>4*dc9+;))mzoghbVq97Wc!&fnhJsH4MYo_ew{1;j{Kx`1sg>;TahB1BLw`^G|NPvMRGGtGYQWX>9FEtj>2vMn*(NMn<rL4^|u%j<^};aCgq*f9A-<G2N`{GMX=?(q!YQ!6LpXpw`}()@ng`r0*f?dhDfr@a8SOzlL2N2Y$|6Ud_zJ{dB$!2asxQ;0+JEo`d_5UWUx!*M74F8!H<ejNGFO{s1kNw01T7qGhDAK7K9YtaF`PSu+8wd8reC8LH)83Bl0tE-4z;@Ue}p!oJpMc7Oj9Rt)m0psLXE&!EiU+`+Z%`ki11=S|XeqMn`_b`$3b9&G*j7rO{zz?S*UR>VI;68uFHh4bCXaFop9*cz}l7}v1vC7mExd*H#G8$ba@9tE6B*5+yrBo-~$wfn7`O;kP|xs6(vEU+%{Piww;blCue0pK?;FWu}efLA@USI5NnJvuxGW%lYg%(~4c9ifCZ*U(T`cK-*T$Eh`WoZ6F1zx6cz{RLINHj6EJrX^DptD$<=*beFy@+d%T{(9sZ+iA!(?_q%~YbK4;G<vcHQKzS0>!nY42z06SA(?q*6j>1iDy9eq%#!ZWAuW3j=Lrc%+aAnK_v<ubky$G$1&YNq(aIG~cG$XM+=Y4=1~i_H{mDa>lNya4?R}<NS!%;3JFw*U|8s)2Wxq>l-b@CT*+7&XWRAz9rKN(Tl*k~fl&2DS_8qBDMIxN4KxMeJN^bo%NT4n>2h@9{QT*4jW<{W&KuT8B^M%d{Y5z{h+<>36EGx~T=nD5zg=7n*0yGL>`#izDhN(yldskndleHpUfOp=!{#%Fa(EbK0cHg}E2eblw^)22{ejWBSeQlM3)R;d5<v*`>RIXtYr+I6kdAs5K@@#n?a75k5CeEFOy9>=`%ZW}yAXgnP?q;^rE4P|TC%U=*{C@kR7wb>=9`Ah$xCL41YjR*m{=gr$@dho)-_4>hxzEQ7m@hp{ZfNh6@dfFD95z5C=^SUW1~q4j9(LIb_{x14!xoG|U7UUO{z96RJqgd&kY9|ITnV8R=Joj6Mm-RDe<5#Fpk908pl5puTvJ1W&2sh6Wcos47e4p@n^CRs5G@8sA%m6ITb<+iQIxmVA|NSFJtvj4Cj`=hb{z5tGQZj0!I&KwZy9nO6<!*m8vvu@yj3Gls-*3z=J>&=4)<z!v;7Q1-K6z2J#~Vn?b)WCfI*kL=F?}4`ADgd0)4!-<-s%BX`9%RjAaPoQj8`D`*R@J9jY~BX*)|m#JB7=IyO)N?F>whIk_wD>A*O<QHR$(x@D~?f{sN0o8X?ncj{4&dNtniBDTWfXL!zK^aq}NjV;y{WLS~fRH#d2x<#GwS(mg{_M}Up487>WvgUO-TN%im(lzhG)f9^_at$(6Fuf`+Eg9aXDxyvG=syT|#~Acl{T_N}kM$($eY!mV&p(|t#{`Yhp;_L}T3AB8ew{n_!Xgw1c&%Z=y098~iw6a)bdwt6QS8t^>kKAcV0&1m-CVhgutXCN*@9ji1L7XWUI^nZyr$E*k*+bAvPF5|Et`?8wzTLPLF8Mkzl%{&YuB{C#ZLLr;MN}5f8&-2dpv@DuXT7}F?mBku&!>O%$-EmrsZZ5M9E}t&Fz<HFEwLmY=&4Y%tozjjV@lbE;KrYgLvGn9oS%0Q%gk#B5JrLHrDz(Yoet&yj07jDK4l^LmA1e;nN$-VkwkmP`13(UCsVs>tHrB715<ymPR+j191s$hhQ}_t)|+0HCYgg>NJINodpv^AzA`t<r_!(Opk`BM@$pzGn}=!Ws5fxjsIwmr-LMsDIUzQbz!%{u?RQ%{t@HCMc7(gf@7h@e!O|B$p9cnKPz|5rO|p8JYxKoZ)iw$hFC1A@*qb6#B9;)ve|G6WzbrdzKfWZHj(1(k(-i3@|d!wQG^e&EL_?(wW?B(v8u)|H`ZzwG62%cRBl`T$IZ8%V=~f9fS=L@90cCBaf4rd&rK&!{ZrK@N^5DON2n=#+h+3|wRF&$AmP??3bEYtW)@!3=eyZPzEMGc^w-R+JWJ82o>Hc=SG#Npsf-|Xr(2o%qyALFBognj1j*>E^JCFET+~>DiI1{U@DX1{3Pu||eKu-7Q&nwdCTY4ITJZ=`;k3p|c<dKJ3bG}#iVldy9AQf3LFnk3!k}rdYdkhKd#$o`oIz~UU7k!A+bn_^0<kERL1IB7vmn_uJ-k)ol6LwS_&u*viB5|K4lQ0<g+Xq{0g5m<M9l*aKFOFcwJvtO7*G`H`1)W#XSaEqGJuy1<(v{`R?0#PvvcA%um1`y6M3xJ3y`pX^$lw^|I$e&Fv?N?>fiY4rj|S9mkPsMcqJh%htW+GD7^qEeF}?~GYLloOy}|a#A(jYH*Wz<MSOOet9Q-$Go+A3yM!_1*hZLj=DS7+dgeoM8UtU=G4PZM*51zm_Cd}q4UL5_5#C?Wi<xgMr+5=&b$-F0U|x2z`xSh9|AO4D@-PUe>&Pi0zKxHRI2<h5n2LXt`W(FecI0Pd`lcjxIW0zx(5H#kEn3tQRe=$=L^hUt&h|NNPk91$_U85PoWa$<leYi0Qd>YBbx$+paz@kD&<%~Qs4clPU}%X-iDs%4|275Ek8%%C)N5Ja6sF_jKFJFLzBg7RuVzT;e9c-Dc-M@pgbS*B+0q^j65`-pz*pLx0=9!`ygFaWi?zZ_M98t)XG4~GePF)S<W@;ntywzHJAyf+qoR8ZauGOm$gT#4w3%IXXjcZ=#F4(IuMK%a9OTq(YNr-%4G@W)E*+5yrCZu48|n?;cfTSe2U@|?`R>;qWBvDHeO~e?uhN?Q$ha-hlzy`6|LHGF;NaL|L5EaBsW`Cfdr1`T1)XDmOj3dIFs&C2Fd*~@w(9rsKJ6hj=j=dpwfZbxj`h)L0$afqZfdtP-4*UpZIhlMeD~|CSE(lsy`Ou|`09ViRq8pczt;R^w$F%*4X^&qgXQ=wvx)hd>31^c*bnADtD>~b_g_I09s$t^*p9AQtF8;_=&_}P2W~9BxVTiaJ|`>4x9lI#F5OP!HQI`o@tRT<vhHzNQ!1)CvtF@TL(>2)n`bDQILVn!0rauXbdjz`(sJe^r2tGv$4ioeTrVR-Ojki&scXCKUEQne8@}{%U74ITXig1u&sgUROl)kPl#g=-dU;ecXw3z-fZP=K1*|ar$%e_C*quwy2zB=oVQ~SSUA{G!(3cnpz_$**8!}(OhgV;p{{fGXOeFfx{}L%UTAJ@T$uX&^$KD_UDuQX<1%ClAEO9aMA<|K><m|-J5qf$;Spx6m4;`=558#kVt_#$y`|gLz)O<aNfl7tG3!B5;g)Z7Er46D`K*rQ&a;F~yn;3e@(jr^)o7sS0z&RjqxtN!n`u@0>d>Y_Q%q}8sF%z~J8d_T#8=V&uL6{0cI7=qMiDl?VUeX8Y%Tg`&4vVR~JImI@){-sxwl&dS_HHq;4?~XtJ|TdvIVIcHXfgs`Q%sJ5qFB~&0DB|o3;|A^V(ufYuT@KBFAf7>I&FU6l*^pJ0(kLx`}T?p)RpiH*VRBTNT@&~%q?OHrj{WJ=GpLsTFRjbrj=p|W#(}K6Z5FRX}2wDcP%5xuMDOZ76uc`kpOc`wiZFNY(X*8hW40V+~Am6zWUTr$>LL9ZtXYwNSVTH?Ioc-j)DIV()wv~-}gZB0Qy(RN{lsEsU3951M5EU3Rz!F!rs6ywqxK`+Kz^c%Z1!LW~uZ(cAONFt;nS^4}*Bz?|SFZ(Mn}zr`VmgF2%a}HCE~L45g4d1Ub)G-V_qyxix)5hSr{*TZG7mVbJSWK)rqIb`cgah*hW1<gL4fJl+TG+e^hJ^B5SNYS<T@=1?9}>~sio0Ly*65I4&s=!^tHsik6)k)oE?NYqz!*~qaGI!xbu`l<0dr3fo#|0A;_Z#+QDJ9FFtND}9Ts&)j0j8TC1b%o?3ALNe{eaB*dItk^3&R8Q%nDm7=@<MA5=JMDG8)lSXBn}C!Ec`aV#mySB5H3ph2mWCki~(ns31=Pv&|^PIGQ?3SZSTvm-^rkurti?mn`IeGWf{xGjECMhIXrKcWh|9tSenuad9&S|R$ysb0ZSK~YV#Dc;3yebk{M$y#bdt@O+~S`%xPvuDVCQO7ipCqdGTQsXKTd2+q-+&JXMm$k|oI;n<Sq2VW9D8N!9o0QlW~X5XpUQYfEMr#oeIuFzV(ra;!;G?L0^_^?k1fW^x}%Jq-rkQ`nNmK9xM{)|NcKcRm{D6Ln5z>@t;a?rJqXV`EEVjs>Kvb*GrLyjo0KSuUon7FOEEGt~T2mO;ql4}wlKLPX3EC{1hQgG!C?YB_tR;G*T2v|7us$S7KF*B|>7<;<38=MP$e!`S;Wunxz<7_{61KhW|lbY35?Ax>x+1&Kn-dvO$%Bx?s59sbc_G%n4s*V!HTfMMl1_F7CkZ8__}!gSoua>k`N0JwG{?|_ToNq#x;W3Ovn=)BaWW!c%BUe_i?={PbO!=Ix8@VBNdAH{&c3){D?t+U*1?wK9bYT7mqWt8s`&Mw<1oLjkDxJcEO;S$sK4VNn2Je*y*gLXu*Te^+7K;>SN*_3Q3&aK#0sz3!^2}nzkOBSST=Wup8QgeRkM&ayITFTjW(jZk!$N=Y-Ze5vm^|lZcsNNe~Xxa|sQrb4c-Lez(vK<0H3=WRJP0<0X?Dl<slvSdiCE^F?4JL5ZdHSg($D%0UjG|1!>BT+8>E=O()8gnb2p>g-Hgfw(7495|aWu%MADi+3Ct8IUY1}5e6tj}@ywyC642g%+bQvt)O{p*>3q|6XCBw2qIm3=uoM+d;a9$4aWui7r=BylM?)C!%%Yu<1G;@L`GE;&nFjG=aT&A=#Y{lYMQJJ!AND0X~F`3frLNaCP8;l2I3dodJf?+`^f(1oH2`X^`b4{_BCu0c3l=NYK3*aa$5-bnGkY9nt2AW!pep*jZoMX|eafXe8aE_tn;H2WdSLyjJ&gr==&WS~(1E<@STbyU#m7G^lKS*=M-N+fa<7cjeT>9?LY9ZxLE(Nj4kHbQ_rD95}khZr{=wNSku~_PMA*ld}990nL6f_|+;k?d+l6S}C<v52|l3JWnma$rvamSuvg_+7MSqznJTR@dpx&u^!vW=kfOZS5+P}~+Or(}0z+15>>vTb`s<&|t1m0huO3Lq^nV&6w;A0^vK<=c=iZP|{4>DUZZR9=#H_a1M4xb>W`D4}TB_2MoeW-=yTm9WM&887pn75=lze{S)g+x+Ja|GCS5*y9}hm3EraP*YlJN>fc~t0|2&rM0Fs*Oc~_q`f6IE@^K`+FO$LmZZHUX>Uo|Taxycq`hTnZ&}(~Ruh%>mZiOAX>VEDTbA~grM+coZ$;W$k@i-ky%hyHX>Uc^Taorwq`ehsZ$;W$mG)Mpy;W&%RoYusOCjy8N_(r)-m0{>D(&5p_HIdgx1_yW(%vm;@0MCyY44V_cT3v4CGFjo_HIjix23(?(%x-p@3ypeTOo_IcU#)KE$!W5ed8{Ng<%{VaoZzqdc-Y{xZx4EJK|<X-0FxM9dVl@!NHN>;7D+ABse${92^M_jsyosf`cQ$!I9wLNN{kpq{b!f2@Z|~2S<W~Bf-HD;2_QoJ;mU>PN@0`RX$<H@C;o|Q)bssfU2fDbm#fA2alg@(FT1%b}N2&!|V2Z)|<b0`MCFD<IYD%$Dgh|U0+$*_;T@+m#2#-n;TmnfAZ1V8g}tw_vPNB-RSv8gY92z-ao$o@$<(E_s@@?ZJj;edwQO5nY5kl8QS@DhIZCxXy?TY?QG4^&PS!~ynLR-A3pD_d^T8l@nHSM=;i61mCZ+sAHDo?JKTEy`02+zZtLOZ$}b;$^!OK_EJt@gdhz_1n|sIG51+qS*xudxWNZEIix-2fT%V6;7<;FD>}i>gW|-erd0%On^%=(V!rm7mpu(-Kv(a;Okw@6o2_7G9?XEw3w*JwJm%a5;=$YlVO3Uq>b^IrLFP7JL*YB<`J}8B<S#G1WoZ0W48OOIW<M{5*IKI`{${l|;W4Z2Z^F8g%Hs8}vXDs((#&RFc2EXIyGtT$rjOBhYW4Wg@!f$)V`98Ln(|65-*c%E(e)(YI!>4Df4_*YlyARJ7#}9gsPd7KWnHp_%KYh~wMY6v9q9X6pio8xm-g-se<BGiPioDZ`yv2&Vt@6C^ql&y7Tyz-kj?V`IV_k~Q4l11}0<pJ;pP|nt8i$j^L)LBdKzPT$V>;5O>~($f(c`U`TNH_scr2Vej{WgQ6b+%L3wJ#;>T7T7S<PFEi;I`g;1J(k70XI$b47~zUOet^Vl35S;VmPtd0VO^W7KN*&Yx32ibAd3eD?Ax*F&#OQGEVl)I)7pvAYL_{FS9kf*(Dbh>A5fwVb6@EIanS;b{~f7mDs>8B2>Yk&c%HVe}B)vld#`vlOfnKkTA5CMguxbDDRgID3eF2xr1#1v9VNOozlX+VDDb5VuZOWj0q=jY^NA&_6G$q%xZ;W~C^8%#Li!ftwXrrkbNT>fyEg$KFX1aJkIpEn1dtbQ(T@vv=RJ?Dvhl6fuYXIF3fqASjOPaoCArd->g+XfzoprNz=+sEHPb)g{}TY@3XIEu~N&4ksZVLc36N5RH5ru1T5uT9MoN4vVF<{%-S*3&*iPf+T-p*#p5~@GJ)G$64QQ^6&=e)NVb7VyLAr)Iq<Hu)dRos8Dk`KPD|-8_d!zTFVSBhc?>s1AsaN`Z4K<I)$P&+h@e&AfQRDtlH+3me4v{S!Eb^2WU7#z7>lIw1XOx?gN#1dqr)(q1Ow6c-bgn=x;_rNW~ZBAFOfeb&k*5M_xR%%;TXyPCIEX6ET~_hh7*YXt6mtEcQcjI;akAx4YCuKMJE5joOZ4-v^KtYaxa9yF#s&mh-^U^7SQI6`B@Abg3PL?QR^LSf;TH|4}OErDdKsDyrL^zBe4%SMNFG<8rK6u@Q6iMO#sXr7M`xgJDf93r8gY$GBu7#92^ll8mDvURq<EB)oo&quDkXI_Vi;P%btijG|E)HQeg;u;Q&0VS)iH|EX6>cekMc0((($h2bRW$F{AeDrEW1m0N;jQ8Z|K@wlwc$B>U}gS(6u)jRe5u7yph^ppp7BP+tE$;~C<7qQ>-#@;5bcwpg8h3qEpr*Wsh+}55T*yt)b94F@n%TJJOB7|2-j=8)cdWQDny{+x`ll6_QC%a`jhuukdgd3ZLt|uPG2{w|51ZH{Z&kdi|vYf1b;kdjc$uhKrO(5`EhWy&`M<c!S?Dxk2OCS&f7XCQbmbTuBSS`*UrRU!#!I!8H#j!`;IIEwf%UmRPga7P;0MylHl>aToXsbJvL_c9DUN_Pbh!kWw)WgJpq5MJ-&;!1e<>)Eq*k3$&Rvb7cmYipHf{^UzA9@4tjNt#6uOsCm@IkunTd5@eAc(2RQxU`O$6k-WHYU-zF}Iz`aCFQPxk5pTXsqF2&BQ@`y#8o%&Tqjd_`WZ{cI>$%?59OaUB%SQ31h_%`xA}`Z=O3aYo{N{Ti$-{()8MokA_TdgK5azmb2}RMsP4;hnbH7MjjkW_Q`YRTR$&F4S((prp1j4mQv48?S4{Hrz-pi4d0<+oe$n$;J>vS*L2c1%|V|uYj_`FM-_VPI~pFjXD8og=<Q3vv-svt#l=m-6;LI^Zwv<t7FSUE+br_NHO`uNUw6Y#MI^xYEPk|h>FHSi&FkMv)cS?T_bX$ID<7oNdp^QJ&P`nQfOww+f)8!3RMDl8_I}vn<R$C8_(C^(oy+exgD!g?%SAb_j3H3|9GRo76PPZj#Y^4km<AYm*eEMnbOCfd-;5k#!0w<i>*?Z*fJ&jK`{UtYeiE{m^f~Rxt#{%D1Kht7rD8rA4FX92iXFF|U25K!hKE5&SgHE>DqZOtn)fjFGslkG1PgDfD%n^g6sFjXnl{cNp3*4TdpGxw&zjTt7BZxpWk{a&NA9rDd&F1bmPH1Dj#(gW>WWYd`ohC-(|>RA<u=yRAARfKrV-U=YK9+xhaiK!4E$5kbZi|R0d#TQ7OS0e(I5(s!a0-j@;;A>9#42+M=tF~a;9VVx=&NBU)G#-qGcs{_E6F~t2LOD?wMx>M`b#1sP<AO^A{g8dEaDHocimG$e>2kp3@VRm>MZlxuv1MP>TSnoY$m0qn>Bi@|M@&*yxqgWY2HUouz#hRfk^_1Bj@xxwDMNX`5K?;?wXZ*)C@+xnbdTDWA)6k}|#~BbgR6K#gB9vkEqrF{SnZ4;8EnXamk90t_Wc!J%cmHH^N{JPKbk4o#sY3-{1GaAvH-Mx@@3WoXUM#4k>24c%jd<_R?89SwtbXnZ5>EXO$1gLODf2Sa51=uM#U_<jTby{AGL`+)7oVRRaj3ovhhF&oa6zuW{M%Pzp|j76dB?A%15R=T^HeF*nBsx>aoE*rJ12gOfrOo`Z0hD5>;(Cb7oe8)7}qVRiW`jTVMsXIkzY#hPF)94ZmlRUv0vAcjD^MoKC3TkD6uxQwZ&`t3E9))gd&lI|qIYXt`Ers@}{!D_m^2YGP$=+4smpR^a%czzQiZDTEQ@Qgcd6KB%HC0WoYz|9Cp*+pjyf7HzvcACA9H*%1co{?ke_XT3agCfDcg<sk#lg4XqT_827nyTo2HhWeyttrd%FYx&tfZ<a`?aN1avY9Sj9vehx&2FHlG~+Il|7?;ivH1~_<LUSw^;Xd7p$K^UvZLiAuf0zqrHxo#-rL^KX~)%|C=}pDKN^+ah2=F+)%`aW2b-h-%}4-CxTeN<DFlt+lBs|*I^k!nUCj6aes<XFOZq;H8MpXt4yzQP2Z8sA>?dokd0~lRng-aT`peKh`j(0r7mX{<8_xiKa?o1>Clxp{|Ct6MXLh|;W$O|)kiUdP;L)<sevnFUiw&!5MO#};o&p#%2~p%;fyF?ShtM`sC5Q;EB08KIXQ(nn{^`lT6+gY*=6RCp4<`oUgrI19oDqXV65GAfm6pfQ|`>8zewD0nnkzA#s+}1bGPM?I7wSczDxE+7S0L%n$8|NmXz!X>ciO~7@*@nd+N+<(cl4A;lPOSqsF{uj|xg*5z@eSq&isO@EVo~PAX7>p{OkK2pP^iLwZh=;j$)jy1l$=PtKPEV;1V5UojI~WYe-355;57+fC)fh^nifI`fB4+pOfYGIdf~)QXv=H{04+$E^*!ZgC|)6VNGi<eD|waAEY2qX!Vv$yJ?1^=eqxc{x`qmJh?qQczXg;zs+e1A{nRApL5wn2INH*;qJbl?MB|gf@t8#grag$H}6!k<cX^?^j*n+|bcKr^IS#NMxRpikESDl6PV9+?FWKid4RSd6_vnHb%+UW99%erJOOi^qkx%48$DAWloi+ptFy#Wub|s7UkeoDMTpiw2$%-2B*<9P_sL+)Llz{9^SlpQ=Iim@0SiFX;>`&5}WhRCx9T`j7%@&JV1WsEX_OHNV~~JF;MZ}bV$DVvk>x@Ro<Id-}0dv5?3T~Ol}k@>nmq*-uY<aopZ29{T`<u1s&XUK{%Sgh}b<NfEG41-z45J0uOQNHB`~JECH!9(KJ3UP#mc(vdSEXc3nziZ?D+mX9=L5ym|dko|<<-sG6@?!Y<ijIAw$Qqms=}n-&i1XN^q#>xaNo(Uy~M1Au!sOJY)|?zyRn%X#O*c4tm>NG?$2e!-c$V888zk?OMNvTm6eHJz$Ou|H$!7!7a%0i<-D2e556NKWD5*NbiPRE7R0``pD%r)h~7MNtUMao(_os3I`y>s$ge7LGEnuQ{Q~>PQ{;R72fC8(OWBwN!LCTS}-^zK)6+;jk=*H~Iq3)$5LpHS=}-T<JL+WIEuOup`&FCk^NvZy0~Q&qq5dQ0EqLCZ%nf_}5xN43vJzFTDHRUtIkPsl)#bgoeJa{&dH=|K|1o`}CnJK_ACB7U<+ayxwj;`u#tyJDXSk)!BUW`v0QJ?q$tBFOx(xYvs@toPCO}jYEeF^W;4L%alyb&(GJ&;a3`@jn8POd79?z?(I2qCtcVK%Z=5W&Bc30x8(e`ZY6w{I3&=1>+ME{>YI+Q-D{9Cqn#e1QBez6g-4pu7Qcf6PjmQ<X1!iANZO>#mEn7zh(w)ni#7#`Bs`E}3+YghVawr!<QFp%US4CBuPXaEPk+nK7rA3!(Hk^d@L0(~rhmwdv07%%@t8d=Hh{*FInY{%eJdk}Rl1W@FC}a#dGqSuv&6ke>z|^_ZjP|5aj(2j=cyA{R}*hPb;}`WI=IyhthHOxt`aWsWvF=<VO)?Z(#whU`V44fiB+A7-)k!k6$+cyM2|0V^5*rQI$;l203|3R&U6POS16Stuj%^Ehu2yNL!0%3f<*uTg!!Lf6=7~+tER?NI10_`cKq5wDyE52*9%*rB;lV|h<SE5<dx%?;+WjlLA8VOmxx5L#uL;m|1Rt|)W%&|w!17}St__J&n}}o{%CCK3ISx8-nwC9+#u)vRRAX}C~#S9=R^PeFv4(z$hYFjXl!c)jvpBqacMC)`!^l-q@KD`KWQ#CTh8IgncMK<5TjTx0``U{fHhHkzVKNT)hU*_Gq>J>6X)=JfnQfGtanemaP0Mbj4w380%!rBERexyeLj7*wSIqV`%|(|mgh`l@O<d?j<la-kN{t<JklSW(T}C(t>)dk^j7<9v=N150Pi*z>2>!IAMoT8$HCCgrzL%VaFix4xoC%d=mAa3^(_zfv%Z%W7w`NKeMggDPW-WT{y)|jIxzotJb<u!{%%Kr&(q%V2%=6j02=jfM=^-T{U9vak9UguarK87M09lI`|o%N<8c(e)1~M}gTXt6K^Hj3aq>=wAf30#!F4;J$8jWSy_+RD@{;jU6m{PzUL5gj(098oAV_xlv7d~+2^>Pl<|tN{i=$ZlAx1HY!(cp#-z}-=f$Zgn@0w=zBfRiCf5&4OccXU=hDm}aLjT<|^PuD7d*7jb5KF~D-2EX2fv(X?$<>dwB43n2;YV7EFZ@$~5ZgD#QgICI0IWEMS-U$9&>k&B6nv*(ANptSoKxZR-*-KLf!TAj*fYBio3+W2H!9)1Kh~s1C8xz73$x&4k1s~8WB9Q+f6@UV@SQ>-@rS`t5C)L<Zs}{%kKXN(F&RZ+?;Q_;-DUdmyOn>E3CM!)77&x9AG}i-jD4^DPC;<u_q?#<9r^EO{-=H4AG|xU?^5%Bec?89FlZJ=u)H#(xPuKZeZS2ue~-;!d+dpc8VzQhxzW;HT8>d19eRhsAQ+!7ar?Q{Wl1F&d+EpOX!*zLXywQ1X!XbF=u-KN+gN}86s_6rzt|+Far?Mc*^h?uE7I}em}6=XCGU6~+>UjDuK0F4J@n(4ykU%^A=e*C6ueOcd?@0UIv#z*lS3%K7yEwpi&{d*H?o20W0bl>i6wAA93}oP`lF#kR5A?IXizyyb))k`pZ(?o)jb5#@3Ln*9u#Cv=xgAe`1sODrb^v;gUEm4Lq_6?piW--dgO->9qN!DK60hTK9>A*d?e@UE_!mF%dkSw(|&aZ9LoSN;d~hq`!+c>yt|AB6Kbp%gKSOXISP0#&`~fP(Hx>f<)$R*pil3SG#JxJmFpfFbO`_Bxx(-#=?bO8hz1hMW8e>Y1PBe9niuvWLPPH)>WK4}PIP)CZHo^i^)tZ;66(h&=&8>`-&dasSnBuDAeu0!@Lgx>|Ip`=_c$`pDERVAFGHxbC{Hc@soLJ*>Zlv-asxvzh6$(5bfXD}upylUPsI1xy$^@Rz_0VDH;KpTI%Pj;GtkF*JQ>MG@rK+LUEOGDDU`qP2Lr;-g!hWVTB<;H1iY?;K``RgWGqwd9mSJiOpUnecI1$U0mzP}0)@NbShbR5+jTP?m%3MRHN6aX5Pj)~*)*v`*?WF+91J4^bCM`N<Y+InG1Ffo6#0U&8cN!o-qmn&bi|Hx4rACcyk4Ej2ru5!1rk){rBOKppnW4L&*(ga$-}B^`%;Q##7U)``rU32_S8?N9O*AL&@_RlpZY~}k?(N;OB*B;t;=-%32MXO%vG0YjJKndro!Je9d>vaaqucwLD=o=<J0@n@20e71hDeEiU=m&VC;7@TE>d!qgWO{fmJ>Yn5Zz|4kvL>h!Kpw%R4BeDp@xEYG)&c9-?s@R!m4xKSDQOJv9aONqw|C<SsIWS(_D~1S*f?RfVvFqJ%eC90$x5zVKjs_#u5C!S@k^us<2XRwhtPU~z}hz)z`f+eepbgl1v3G=t-$FF%lIwvS+^8*AE5h7n%m`6jhRA9+k!(R(CDdT6Vqi}3Zo@2RB+@XIek{<NN-;4}3^nA~VI>2v~~&@ehiQyBh%&@(pP;lS%0ON*!IsZqXhFUjXPfE^{@z<?t52}|8es_cMv>>Vkl=P`7UV;uoy<j@xC@=pCuNDrlch3C-rxUZ-v9GHa6o%&wtla?8K-xC7J`y2KFtc@2w;$;7X)c#!xhf4Ql@^J*j2nhWsMNx0SpFm2`dWrx7>%)lV`<#osbVH@$k6!@Dn8q9ePX*b=PoUwEG(d`|^kW>IGBTY4bEFj23yT?Iw<XNsm}~m6mt<lA8Idp!i}&45-wPyr!h7s6<zi9X9(c@~N5Mec^mZpFzCbETCQRCb1W;bO0p=I7moz%4YK*-d2E8B-H2$8JNFruBK!GClja#yvW(XhLmES$@%Morr2EYVH2Y3Pl@-;~T=!(ficU1xuK*ec0EfEHtDB#LSmD(ZXGJM7WA1F6bq)I-1IRT2~Gqno*Zd*w+RJ%jZ2huGLB&w~+HYqgxQ>0WnIF9{O-tRCUzq>7>YwRI?!#VmQ0UzNTnrOgOtal!<2tZyW29uDNky#&{lzm$3M4LD4vE#AFk;+I=iun65o+L1<@tBE19D9d{fycjM?<9b-ENdp{B$NpPkBJZD23Pxn*<!}A+LA(&hx(z>EtL(DqWWfOQT;+X@(aamc|}zgQIM>CBp{j40~@T<XSC_!Vk!TUN@$sgpsgfi^r9)-gjhL>8A`Z~k0y9f8IL)ET`TTJo(Qn0p~`ZBhr{V1=(GjCu+x}2`=M+}6ds0Na?B$EYCb}}D?v0E13yMroY`8TX915T|5)5<lXM*VENH<urZaH~(0I$u?vl5(%yD$iq{Cw`g-L&cW5&M7^B=4*3|kH(vDfQL*q+e@NRvn~0XjY$$QdF&WHvN8o(%kfY?ZTUgpvfqoyC8z)4@<@A_aKiC>RM~ftm}qRbPY}hta8spdhK7hzv7^)1Ry@fD|VovQh#Iu|bZ-6PEo05$^<vJA>#%1cx~2`eK(QjKLpkzYk$ij06-&Nw(6`2%8uMczXep$04T$(%q*w1Z*tf&j41WM_NsgBQ$&(PY&Jm(zzE#LtpLAzN_qakWa{obbtgmX4<TXOb=(uJcJjM6NO$+hHyreCFShH6lqDh#e1yBbmV-L9zaKYbnZ-`upE#9E`E%Mtn*{$pim~kctz~({S-u;V<6SX8C03;h9D016z2tsNu3`D-9(Z%VmUrM9Ei`+9awgcD<hn@nL38BIplNXfmHJxHaP$E&g8_7>*Jj=DsY>7PxqKcb&k0)Sx$h-f#?!Gd-klo{`B$oy0}{%dEGAB0>g0!{R6ujzNeTpXB-W1!}ieOuKPf~jRIf#hp~sbpW%m*1v|SpA%&j1!=FYrK=+t@m%E#NI4pbNm%eWl7_i4#_X+$pGC=kn(TE=5hmi%mIA#^9`w)bGz-@C#AlJp|Y<KXNQ<(E{1RNCeKg16s3&_Bz&t@a;mV6rpIx&cP-C#f?*i=8v=HaZ42O;V~zKsIF&`7WJU=lmKzKCGy1S4Ef8s0<xG$)8c8_ynw=Ir24qrf5RPSjeT_~y)G5`!V{Iex$vh!S(`z@m<yk)8|q&2e<*hkEWfV6Wfq9)9F-!6QOUxImvq_85+`13w%0UIc<+kn6ldM>m8kei&I@pF4i;<5M9eUP{{_1Cn=bcaOeISRYS98r3d-7+DcMoB^=|GN19Mp9i%#w|6)2kbuC(1fviKjXa77X6y9Bc>r)TTY|&J`H0noJMwLoKoJ*nKMn?6^rCBa0&=525b*J54)%jUAh5%q<~BPIX>?EUuQ5MTD&kth;qKH#6y$llJD>BXxt!i8U_`(VBMZd*m}mMiedV@1(9(drjK_YM+ghmBOrgDrQjFh)zmROMX&9Yq)MXcbI@|O!M+@T4gfyT;3gm~m-Mt=zb;AR=Z{aVKI{G1qDYRGVtGKiu<B{>%=|BzS+<_lC3>kV|Jctmy;B@ET+<;vRGh0_VCg}a{j@snF7A#wwh}<chD>a<^I2xRoBLigRV<Q%lZ*whx+*2=4@FQ{47$)~$u0P#df4C)K{C3)K_)EsSBRHMB7@;5dE{SB>tw*ki3O!v~-~qtIT7MjY+~#k3z<SX+H)+-HS{hhq?8{ZB>m^{L)bz6C@H>DVVD`aeXsJX_<yDA)d?tonc^=VWS8I~8HV1Ir_6MWqKFCNs*`*YOAH4twKHhsQARI0~VKkgmpACA7jV`i>%NwY^=DZEoWM_HLVMZWLZg_)%6wy=klG~6#!<@^0==qO;nS2?AV{f31C6}m|e+d#D>S46fMv^f~I2}xmjs~h=_B$&@KokG}xc*eMkeDlfKbn9Xn!U)FvnA*12#OFgBv~CZIag;J)n<eVSp_XES9&iP7RRI~TFUPNM;rV33TdjP1|zOnUefF{R)K8hEUCE~uz&DvmO}eEOKKiM-r0Q>TVO7qlpjxF8_(G@a`hfzP^08ClAPx9Nx8Dc?Kfx7$kls-WHAo66;>A#ix{hJ?y`6~bESE9e9s8toHgCPp7%jC)DhB5w$~~2luNhQ%3;2dn$_s}!zLA?4?F|)I?XdzvX)fVl4LEVS<5PGS+bTn>tQtLV#om%yjc6a8BIcUtJXX0aQWQ;cwDU4FjDk7iK?>^M{w@Y>li6|okLXzMYJHC4E0*MG`-$P)f4ataE1aKfsDXqC}0tw2uOwkk%(KMn?42hi0em7dK%Y`mi4q1PFvB_Ryl1|OJj9{1Z0$N$yMxY^Vy4?XHWSq8fH3*LU9hA5jZnl3>@;wX;cPIeG++HN)kdN*Cswi&q+kTf(h%xLoa?DcCxCEg4h?tKQMXhr+Rdel+n81{RKX&{oAnT?DgNg`e)WVrMwpKoHcSe2J3FVdG&V_d{g;fRgILdx*J!oSbbRJrS8+7rz+$ar+fd+>p$zb1wQG1a`jE*?8R?h|20RlDDp@5Yzam`aUMl)UVWotZ&<h@mV4U2`r6sP`sUm%<Ad(rcfUe#ym|fWj<a|5^~AMuKRBShdG+nk0RVmzI*+ct=6P8dpV45k{~XsdN<X>!U#^wc8Kuw>!nbY-mn%%i*$Cde{#6Fc9FKE9nK-*w|1ESjyljj*S9AB?y!uyZF@WiNZaF`5ci+7JEf4UwSvj45!4Y}r?4n<rz5dlJx14RcpI-g_#9_R97+k#?LDz3yf8*L27J9_^?;(1%_;a_CMY;62d6yshLW{4yjoebM1k-u-ZRmW$rEMseXG!MT(-Zc;4V;auZ$h_}Bbh5!-bspydU--eH{(JGh;N*aCRhLNG~J8?X~|1&#(lJ8BDf~!F@9S3OfJE~RdNYd9#TkB9K+q52)YMMl$Q9U$f-}?y#7m9F${O}_y5yNw;6E@_oE5pEuxK3En*pI#!Iz_iEE_E8wh+?F%C1i?|jH(AqJA~g8u%wYw!|{mDpJZ0zf>dK80=ALzMr`$fO%Ko>EdTLum`gDXF7~UI{nSYGKI*om!Y|3iTJbwVxyL?m62)c>ed$+38>XuE4>d=+*z}eAtijr3!pa@4i2|`g{2A@BioT(J=(T=)Z+<wj_USZ4Y0xcl<8;Qu2GgxRPu+0lK;**9GF7ap;`|!^x0xfIBX=n=7~5D|eRLw^nYG+crpVDL;zn4^f;_DraF>O<ayHqH7=akNN&u+VG7j-jiuCmo0Q)@OS8M<n^zeus1os`uorszj^%+&?-5?2%QUQ@zV5SNgdwEPdg0*kvgYDe?yrwI!bI!iDZOTOjrIm>&%Z``K<7_)9K?rL|+ugePS0E*x+SlWF&TuKcbuYEF=a;(IEdvbBFE+E;-6MP$QG#wlGQV!UwKX6(`B%I7xtO*lt6$g&iEa?=QIUm%I`xZ@`rPfvYb7wOLqz)Qx^|0mO-_d`sj8z${9D!MTB(U!z*Bw%dWRIX&`$>U3DLPMjoig03HuEHyZ%KDyjwLVj3I`+n@B2dHxgYM>o}-<^ln*mE8=))o(qF8fy{mr+GrP`To<N`5A;v6dG6Yv{e0D_?K{OBoEPG|oT<9!pEI0_7o4v>Is`l>AEJ-Fn4NfxoSH39YJ79~!{kGP=i6Z7)`50N$P!Kknidrr^h2!0#^dysjVHLmDWH<KYqxxOyxP_XOF(qKjU#cp-s>gzb(<opS^tBIYLXE;0lvN#O%w1Z>5u!4Q5T5nnD$c6AX*z|x}gGcHuDako&V*~B{Bp>xw&u0!Re)k4ixOU=bx)w@`Cb+J&lxwu%Uyp*fFN|kS~-Y{l!XH_o)?MNX8ZsL#I1Yjy)?2;U$HDYxQSfkg?H5=8WxRS9?VJtVjq%V?-%YLD$2@{7(+IaM$OXeY1OJ?~e&T4bz*4;bJJ9p~NA3KX@NAiz}QWCFKnv-7^vVgw#InxZfVHm7W<(G7{7{MX@w?pL$lbkq_Pb+bkbs_yI4%!8=s6#Q-s&3RRSLNCzd(IzI#g+RE_v@GXf+(P9@B!G!n29Q?<o8I<BTZ2r?WBn5W?LoZoN70iE6#|LRJK89)L%OT^6v)ne?4{EZj8Azo<EACAvuj#y=zj1u!M57$(%k_AUrcEL{u6ZYM}yRFZ7c^Mhd93vG0u|U7ssmn=@sh8Z6vEcSj3_bRW<lg}wA*H}6#1KP?aL;j#seTh9S66Z$?+-W!A5w+8>t?SJmp4(j`Vf`5MYd6OhT_z$#H8Kq5|g%%bB$EAX`X(jTZK{QObmgu5wFAOn|Z5EIHd6jviFM6Oyr}H7+JGThEov#SBU_gXnx!t4O4jS}Lyn$6yHkV^hio3C*lV8PhyQ%+XbF-mSOhX32lIU(NJZHCjwjr@ky1c9IDZw6GaVYxuemYtvzM9ua>P3bu;6sFvFX--qDIi*{ol=y83+?q&76UwSFLke(>g5|_X|9TTJ!d{EG~W(hDhQ#|e;E#X29<G4nfM+aHL2FrbwZHBx@b`#q_<+UhmsR`gX=HR{QYy9zBUsE0f;?T_@D=PRVf3Ks<SvPFt4kGi28IfJS&@z)$6`5Sq^G)f+$?8tzd{<NtLr<4*4>;KpGml;8wFBEj#HgM9aHy1Jv<gCfPpnlRMSazN8$a@9(l4{C#kF!{VzoeQ#+{r3AH$8B(*%ts^9?O}!WdRz(p=ORgawlXa9fNlIlPQcAr%LbRhl5TvGz@ub_RLCZd4L(9_}s#gSW65J>6*X6s?*t;5HTij#H4#3cW3MZh8xpaM4OJ^Xx)>oRIZNd`2*R(+UQ1k%9g5*Fj({9v5F(P-b3}EHHk4h7qg|0L~rpxiHeoh(}w=_mF48=STPK|7Zn**Tja`*>x2g!jLM?GsmGgnc;3!KCyM}jbp#cp1t!RB>&M&y_zB^fr5kaFrq4!tze${WiXMyE2iS=LHkuF8dA%Skk95+yNsRrd5SXGXj8GD;NWG8&0O*5@IeII?aaMJqC+hR4lLhNgb!izEs&(6r;|)I3F`S*hCXgw<{+hNxgXr-bVVDM=S4Xc6c4*KdC2-TbnBu>bjKYyKukk`lcQ#s$6BXN`br34Y3M&odQBTE$piELBj>S{>{bqBsEM_Mis@*gS?JN#@KA2u;@uZfoaWB8JhHX*hf5BmS&U=^LHkC+G(d8SWf*%pt+@;U)p_D%>K&r9q=KkNjB5SZ#$KfKSF!Yb~(2Te13@*ju*C%!Sh0YA_7Dli?_l$@yV2iJ@}R34*l;aNxoto)2s9jiWeOn{yjTx>|0%o|o?Bh*8{*n8#UaD>4kejG}f2W7(u0e>EUvk=R6}509c$=FTJYXHoPR@^dI$H!A83fYV@Y-5s`?1l9q`RfPLMS65Q~e4IhMkWQB*!#A)0dhEz3#o6@)(mKu<ojW_}D0s*Q!cRl?!k}qzhU#)Zo2H80E}J6T69tFR*6FBrl)#M&pl<``7rW1%8p5}O2O@0GI0{)elDdq_<uaqh)kYH<{9B)OY-71^!%E~({I4k{<E!6|O&YBL#T!jKoGQee7A+71I-T-GT;*}}8j%3C;K7BbA2Y=ORL4SN-qj~VjoQEn?YojoqDeLev>21zJdgj8$Rn5|)SP7qNZ?3FeT*5=H6jR$sWPdmpwoR`=7Ux~=&ptmQbofVNfCh`=s95B^#TwM{o$c6tW9f6l7WcqAJi*`B;^XoS-LW+KXYlyj;<*Or&>5Isb7d_R2Y+$MP)NqXP;5vcl?AjnQP074GOyg2cc!Fi0g9r0W|Azv%!#1kNChp_w`Z-byW1@4zWu4GL}&^n$v4((W!V*_FdA5xp)|$t0IPiu`<T`#T21oGa4`w<WDkbv-xt^0Wmx+EEVJKdqC&)4J+wWH=?>t?jW%z3kzfA^PxL<lVZsAoGfXR6$~Mvp)s<$M#$*t^|+l3qMSy$T=A@o23VzQF&b#%s<M(2KJLOlQ{X@f>#Kip*cwc+3^EmHDpLV$Mon5|*tsFhjiXfH7vfx*h+GIp(Pd0XfO`3l0R!lqh}Ufl5I&2#1QtSn!sxES;<4>(bNFY6U*Kgy))Oti){l+gVoxfZG?PQE0wN^=`+5kG9x9MTciY3sU>uAF0f<XF7T`7fIPi;Xt?Qj9VtS%D-1G|ytfcNI!rs-_XkoK_Yjp-S7jFFS77pfo+Y3E>jW&zM%T}$Z{3@10PH+_TUMg)^6SZN*Vwz%%0Cmoxy98v{(J$bUcy?vNboBubXODRvpf>;h!*mEVe>Kqy{#&L)5Hd(ulHYp8Q~PWu_v$md{ai@L9T+<S*vX)>R#OwGIk*9~!Y(ACi1Ho{+WDDt=hn*NB4oSyp}N^#S*tD0FXsNK0YzLNqyB50Y)4(_3X(iYU{(q#3m>@kVm$8uAUX{jrZ)_ghONY`+6~L5%qcqP`X`OwVh|(_L!^$p=z*-AlA@_MJ}6pC9HUfv&K|wZCOp&CLKa-6{Ql=ijkQ7_#wF|uv8vmK3}X`CODK$)odE7q_Fh0Q*(|lP`$N2vOg=xHBN|j!G$_qz0s+JiOyt^GYbsXH&>JOA_Hxb{N6!7A*9*d)yuy1z#tPA7oCICp(Z@FbmO#>!ytb!%1u9czoM9O&Dl(dGx|VX!yy(_viZQ2FCT|nQIil6nV}iTn00P0RuNCYgpKnZ-?~-Ha)#av3VG=1TgBbq=h+WuTM&c_*i<oVF59u!7vcIBqo6TnVyH0l*>Rqapx?zn<D65$&>KBp!EN0g^7^NvM11NyGGLGj^#$+~B3q>}(MLoe587z&HA_fuCpxkCdnYx`uV*ACbeY^SP`@2XPG)>dM8y<E&XV|hS-ZZ6~oHrf@C;a-p>6S;8oK+AYoIs%`RER`4taodXGg92;kNp<SKhKNdujEs9p5sij1~7?}NmfusQ?y-=Vcg2MZj)Z&SnlGIZl|eukC?XCD5xh&tPpz9pzDY2k(VSG<u%WWaMGFaRHkBA=&0fcyANXDCzQ=&@Dx^qg-ZF$^$CBOsH}Du4%&dkeugFGlB<sF3m<%CBLDo)e*XRfr)V-QMhKkWtt%z34~?~Fg>^&41JzC>u$%{ts-5ES#?ma34M{;i?B;SRTkYXSg(1R<<r@T2z<t6vNy%8P{bNyLtpwxrrOCpwlAchHjjHrdQbJ5h=%^m#kLiK)J{+y-;{!SgaBuZu*wtxA_q{!b7Pv|fVqJiB8<$(LaTramn>D4aq~0LWehPRC=s6h-=zupDyK;xMc=K-i;60RQvg%WJANNl^Rm_c$pfD7II%TDhM>LtzrAGgi5@c}oHAZLs-FRXA=G8xre}v7i;&!t#7B}b!fywyD7e%_AU=&g`Nv?Lo4E~*J#grP7QiU$6eQb%&ZhJtH?i2g_3hj+W+Yd>Pj)n6NEb?Vlx&4+_**GQ_*4G?x)=rVPOP-anXH6IF__WefEc(>bjsk?#u-=pDX|vNfG<PJzi|@s_Wq_nJ<{RpWugpXy?2^Qko%#{VZb)Y4hD~=!N)ytQjAq(zeFZnDqhb#wb*!2UCRiMN{8D?<!xPe^E*X3#<KfRD;xWSMg-h{HUBG5V_ge<amENTr)|=&&@ETSXd?#WOMZJd#vOT?RrrWyluXbq>gx-KhzGln=c~<r=g0F1!5$P3Ce&1_v_VJCW1%Il?T=G<^U?JP-2ZL_xBdLWAS1_JZ=5QLjzfls2UAux|n>XWXa|+wS8X8R4GN@G&QQpR-Cx?vN>P;Sj(0ZYi;^B~1f6c<7v(czUrqfH>iNUiCkPQg@uA@;nRIbtqJ8RXXmUQ8wOuXG<uw}JEz-*2{98Cu?W;Gu+yI;c}wS&tV4-JxedY82e9Mk2(2X0Xr#{__|8v{JDO%!bAtVeoJ$K7dWPZZN!!_+_0F|}3Ed>$>o63kpEpk`6yU>m4GW%86iqor`VW4flD@AT#r50O&(F>lJ@clvoi6D`ui0j@~0mNAk{*s&cYbpgg^RDS*QC!b2js5zO*?gX{YP?qnBt;Q$piopPaBqhoeML4IjNuCf#(X6!6PLSMWJ!%5wH7~`|HZ0~@8tK9##E~*8ecWwdgqM63hLkJKAhouZhrNe%TEuJ6xn{$;rR-zU6Y^=2H%5g?rxsG_@ETOKZoCDgqSwB9lNY-TdE)ooH?RK@RtyN>#2H7PGsbt~2KG=-c=e_oRT(o*y<QZWhg5|!!1?8Bj0@$Ds)iCfe-_M595-_j6YIuBtk!Sob*xqff2Q}BGaT;_Dy1hNo}nB^`G;{Dm3;j$8kP<+q&I^Z_DFlvH1e`?_Iu-18L0k%Aw_5H0mG)SGB-j!=!W>7O@EN(0lU}l?udU_sd*p024Cuv=JjP`9sR~(#>Wfk>s5u5*Lb{8rYzSK<;H}Iw{w;L0B-8e1nwBl0Sq?-McKqURedN<_~z9=4V|zTU40$E+33ydzX@Q*uf9Q47%wlmb(6!UhU?V}rZ3W4-LOz+ISEe6k?s!-+!+Wn>L3`n^;r%o7ci2`($%*Z3FzDWrt&9{+fM}}DyH$&S4P9JQR96;`KFm|F662wJ8L0sLudEY?8g18zaLWS5LZ5D;xzk>5M8l2C=05s%2UelKi$GCQ|dD>*bwhib7*40J}K-M85#=GZTn);7@4e?%rP}`Pakt_8i;FYRa+c>Wrju_RZlW9K8|g+c?d^5cH!*!yVLhO7y|%*6Lv#&{q>^Mcn}A`sIgSrEjfy$^G^3us)Z_;rxeAJoV7~ck~phixt72ZSpn0gxc$qCN0-lSY`EH~MWz>SIJoiAT*#t8F6eX7uLVnEiw)wn$g>;H#U+fAgeq>zw1?b>9Zai=e^G41@%aOP*iO*@47DMm)Be%{BMFX`u|u`VTOI|KoSi>`2`zd+Om544&?tXBojwLAK7U1+QX8bNkaw`Q({+h<P9r$Q_ptY2s#`Es8!8p7I?@TI(jqkm>u#8rHyksW(4bMOuuzT}G=+t-gce}ZHoKVf8i(~(hrk7&jSd<8V3G9Z(~y8DYszDJH|JdDBE=B+e@y|WcDca*EHv)VQ*XfB>TIEb3me5_zdJ`A<9zW^pTD*jPxSTT`!m`~)P!k_pPd%1Z*ye}1(n7bvspgBjlnQ^P-=^mwWgk^rhG#5R^@!6^wPm#{2ArU`}WN}+@|Nu!+>n$*9wK{nc9sRjS%t=<_p`0ySbKO16L7$5e%C@aaI@at}NeKxxHBM7hw~!4DXP6n`vz^)RVl-9?@tCxi1EANdWFgbQkMRlgP4#F-!$#d9Tlh{3ohE6bRefSbo_pfR({gWU?t;<f~8GN!`>Jjh*djJ8P&jCwk;!wOg|rkW`yCZU<q|18hkwdbXc9JF$P{#|}@|L5q@mF#Mwl>>_V?81yD=teA{_4^HxUGlTXicw>OC^g@i-5#x<HbunMG62~ypQ%oAw01dTAnpnIJzVViZ4)e)q5R6IH-e}h0to|Np-Lq$uF8rWCC39@$J7gR<u!%}!K8};iYZs;-WinfC);6e_sx?5v?qAWN^k3nCc=a!Gv>D=mdzLlCQ6MwL!6@5b(?~rYzpVimHd>+fk){iFOCu5>>^q9d3mZ_<X8IY~PnH=qm3g4RfoWT2#Qa;FPhh5P`^;o)lI@p*#fw3o4$&aUkC)DD^hw$FY7TOfZJ4~f+b55sK(vza($ffCW4j;w{_)^^J4n!mIMIwz8t%4t9>vK==n2%wDBT0l*>L1z=TX=^Nt$MBe%$kywm{VFof{eYsANzZK~EAk(TPxbhg)YO6d<5KOT+6i(7)JB+d}=+F4`Cw$<Hy8Sw6L5o?e1amCb38Vip(hAuQld9Q81)o!N`u10kuRh?N7|jfd1Ciy%RQOquSXGl?<$<2m}sISJrc)aHu?4rqvH@h>6}pZs%`UT(i=Ep9O@OwSfE9~LT)3YLQcKf?b7_ft*<xu5HkK~3RmbY!_<0^zxhnnUWzM&mS2>LEEOJG$+AtwZz_v94gRY)Cd`d3I!V=rR^79L~gn1x-qNovlMVl|dSpcT;hlg~fvf&Lak}wc`Ee!9lsJNYYE0H~i{EA-wtXLqv}?GBP*{pdtE_ERyUvZx3IkKZ$xlhko+Sg*Jxzf$g-HKWA1eoXvw!)?*HV6!HL55L6{0aZPM3V;ay+99sQ`g|{iBDQHy4@f2-sugm1m8|+2L6tPBj`#AlL!N_)fKa>QEJg8Wy4TYGUvc%8Q{*5Z+7haghUIVRIv}q41nws5`^?K6ek0<E;7((7G0^U@rmJ{qO0Mo>_dkO;#k;@zuKKL%VI3y$V+`Dybuy`(1Z_eL(T4`4$^P)rgQIsdsGClm0JMK)eb%yP=jcED;_Qe3Dn}I)O=h)imSJ1xX*z~;!kAIlpn9O8v^iirV(RBHL<&5JuufKIj`)t@sX6Naw@rab#MGvp&1ur;(gWIzsIPfL+@z@vpUE`5#5Nlcz<zN`vL&Jncx2RPH5*L$v1BGPc!3MMImfe;skKXbwI860OYED8Wfmw00E!@u5YBcP9a#Spg?I5*^LTwQ@sPYsYU2NpsU7KJ~@0txD&*aI_4rNGhxbt5`z=ZG`;j(pca_Q<X54czD;Q_r(sOzf#f`TpUpI@oZ72OJ?7U%S<m3KIox({GKD?vD#jMHcTc%?hnY%DicZ#K!*#{efirU(F?H?O`0Ai{58Sm(|F4yQrO0n#d9zM*+$S<7LMG8#Y73Z*2OIV#8S{F!0+E{+zuN!|~FaDx+In6W?t=mUCgX*m0I*sNRZ42TZG^xtdN4@_frNX6@SsCKh?kkwQ@9u%ODQF=}HgPD_cT7b;F3=k<m#A-w7b~oxw&~Szkhw7w&BMe(}cDHtSA3u9KF9HQt%Rn-UahUFhn#<HaECwnN{xX=ColR`tOOD&;a25|EK)<U$9ic(PZ_w*8J79NCuD*_(Pqv>xT@RZA1o%JDzr&l?zw>?$O9Aus;PAsvT(m_|!y^db;LIn~GQjWt;_6$(nBR?@u#YCn^Nyg{>Y}JS&M2_N!igUTN9RsIdh_aEJI-oTa@pbvNOZ3sIHYKD^X_VgBOvA`tkvLR|Cf^>_S@+3#P14jp7w)*@1Ux?Rqh;!x4C5vj8g1bS0_1E>T7lBTQ?m8SJ9;mphxcKAyy(Az2A&r6|wSV1J~=f>;mAoAQk`q8#D<2Hgqm5Zldd#uB~aeIZuHT{&g&EANM22S(<k~@rMf;T4)Y?oyB?Qqm%}?d8^1M==gccQXmw%epPBP&5%7=QK;$KL>QfzrPHA6VrLGS>95HU8wT@t=k?OjXeSeBv1Pwrl1)AF4Fn+ClXX3HUG=rywJ#!#zLj4~HW9dV=J+JUE`UfgRiC$<r1LbZ=;B&g9oQUJ8z%{E4VGNHE<9}Lo`n4nh+T|K)#4)>n7dslP*AxDTg#X8nHy+;gk_gicp)wze2$A0n5kuyR{XGgh|z96!m)uHf|rKxWwp8)CKkLi&w@ggORT$-Zlt4DCrZ4~zaVvvWB^hb`y8>s_MBA_jwf$k|C6WOj}#11bYxUc)C}Rbq4|%h7aU0Gm;fF96>bD5aGA0J@d5mUaRQm-=b`vVY&k$EDKgFQ>YH<-kYu(3GyZeWahB&L{LGI}9@&MabAgo6O{1~l9u=pW4R;y7#R2Li9gMkE>kT|PQZAuY)7Si-ooLR+S5rmAG-tLMVu4J{Z)~(Pj7)~ASKirO$B}2Ms>p6fDjbknJsxH?@1-N(*B&(la5g(o&JWGmWCFa!jc)yhg$}Ft2N@BDMyy0vBe+XQaLEBEZ8shw4UQfr)R^al6hDcig&GhI*mx{C@KgVbQb)i0HR3I`gFIobBFgE3C9gVEMA(jSg0IYwLD+SY!5Ik4e#E1^Cvv6|4cH-c7hRR$y&H(4nEziw@pYExtmqDcE_yTvxS4z1gK~G*`<X9Y!<DYlkmi%tY)WnJVq1E3t=*hbBz5AQ+bo*B7|zV%`io;RVZ^8(!j*NUJf}<@=N9MZ)1XjOWjK=GWWvhyASbP{kAXBMR{h2_rmDG}XMgiLQ&nDxk*%68bz4rJ%>wWLO{d5o4fc3_j+i<ge8;Dw_DtRYvnlxrzf8Fp>2JGQBlh-}_w$$YSvP8srTk?zxzzk1*6m#WvnX;l=@nEzy81dqo71mh_m4podY$vUHn+TpG~(N^uX(-8QwXNQ*C4`(pA3qW-dd#BG5b<ST}i52;-^tH%^_c{u~@%cSYEt`^bL&&a5~=vjw;Hdrc!Rk4@Wr<hWiKgyn{dnHYJbb*_CFtn|Yv{%3})4!W;s2IkO+w-xoC5@0V3rq$lsh3kIk?LwZi@WxU=~-N`F7f)g*3_5L7jt?s<<7`wie!e9d=MpUBZ$ihvt{$=L)&j#Z8qM=e+w`HYXhF{V~R+=bQhW;1%VGPjd{)ZCg@2MqW5+*JO-!1)8&!zaSQoB*@J#ZF}fmT$}d<5FBU_{GzhCy4EG?ICJ%vvu~7_omI0JZoCl)az22dp(}TI?k)9TxrSU*<)egOdUr2(NxSg7eQjdRok5o}qhD?ixk&VycVlRp%T{Z*1G9HjK_YsBD-FUJb@=G#fbZIv%mbk0jOk9yzd0gM?@VtrXT;NBGQ@**ix1?6{kbh)%pp3;1U$Xv#zKL*ndsNkWHU^rqvSEje@KwXyymQ9Jl{j?l`_Ua4ESdWjNDWa;T#UvmLjG*Xr4tA^pR0Zd-X5{Ce$6Yn&dAbKb>Ts*F=HB;YZH%e~btNf^G!?395te(^A)AW8MBB0O@8%&zNyk|R?rH9RQNl4beuHvsCILv;|Otrz5V^!{GRjoF(9(gj&b;(5eMvnZyR3C}5aavD9NT{qmWXGf_nn>$`$#B%D9swX3&Zx{=Xqw6Mmqo!Uq^PCB3Ijc27F2{!!|*h_*s$1-&p4@z%Lb08&gKBv|M#jh{R7X0y4NVQ*^J_M%xB)77N;Ca=RjLDr<U6&kU;LJ#5kzzB22ksBhIGzV<Y|UF5Zoz^pB|v>{0O@bGv2B?#Q`1VlZevXWnbx(_I{i7eA|yBkhcibIxX>66O{cnhhtTQus9YAFBxw!!2!zf6iU235u~v18B|UWJwLzZJ=#HMm8i_%U=W}u{%4Uan9HsJ66nfMu}<OV#6e-_35;y)D9`<tU`wIo~*3l-U+FczI_a2wlGaA%M&-8a^H|TFr*6y-G|}Sn+EdS_kG_qOmmo*c{9s1dJ%fd{VitaaPm`P)%dWNEkpR@hG$Z}vtu$`=&nCkn~aZc-l^5EqXH?le$gEHW%e&`r&7oBXfL?>hW7n`Nq0YOT;Qma^Q*rP@3Gwn>e2AP`u{-wBHk|kI~-^K+0&i;6poYP`$_17?rLxD1lGVy`VB|<%rWQ$$}q^#@~6|bx{)=Tln1;ebf$QVo3_+2{SOxQvYckyxj?psVX=?5bXdBFKcuVWG*DGUw}Er!04b|sx=A9UrUs=smMaWO^OChz%*6(Z?zN`aVq`v-D9X?N1-n~n)o>kajT*tI)@m*;Hfq|SYpo-+JGwl`I0K;<MpYpUno0j}KW>5CV$M_xj)bwlthGub9!+to#nZNUX)t3PO?M2Ijkv)PW2SY?&b+95FOI$ZD+>-OT;X4p2xWuJ;!c>JoESE74MK(n?+8Y_Y>d@+DbP3S9E)-ss;ay$9BT3xCV6`M{Rqd|Q{}f2is@{fC`PF12eS9Q$ZnU6Jb5Quh~bHn+<yK6Y$N~Ttl-MlUBPPQFOBRkhZ_9Gq+z}ZkhrNogia|laweV92G45YiFdfL{pR(bFYKWaMX>PE1Wx#2Z($P^<cFR!03L&axV)w#AsmbTE&71*LbiHxoE1pLR~G0!EMC}Nc4$8DKr|<6!e}u~^a*V40RKSA=bE~wO1+Ksr8>Ttsd)OHUI?+xphOMR{Ak4iNCv%GFNdVzPuow{H@2Sarf%U;A9e|x1T`cFnu6$uw<##o^US2<$*#~z*C24rUSzqv#l@SUAyM3zRgq(8j|_DO0&cM}^G&zu#G#?|Hu`e~xhayYAL>q<>DN2I&z|OPtw8a}@T!%XRip2sK5l}Ljt_INt3im?>}c4R7jGG{9w@m|o@+PA>y5d|ae$R446;?b2rpZ%U1?4JpY#L6tuoI&{@4o!v<r?~C;Ed1^66s)Qh>z$)Q1xFpq@ZjJV)ictr<>^8oDR1oFlLL0eK=q%B(q2lHM-M#4DLbb}Q>R=qyg^0UAny%gWm><pS?}yyzkvD;TTL`r$=ZdYe?Y1+~o_ecfyx>^DtK4o$7iT&nb(c#D?K>edmvsPOCv*$1WPMce@VTmh}F=#@c>p2#RWhIDZC3V6#K0#ff{i}+SWJsoJ?TrGXELT2Byu8Cc%ka3d?jMWcWn2=XJRmtZ3_NVdh{z5lnGtS`ij<$u?7L|hu!cYPqn#Iv^T>N}3h<~pI&5M_2Gnc1FGqA(T4PL&b8=5c0DldH{_a=Y1eZT&WU!OrbEZE^D6Lwu4k8X->8~iS`&G!KncQM4QbKVrod^B=5c@4x3Yhaz$R28GuhiQWns!oELctC8=xu6=BV;mse4|nHY?$DL!6B0bASkGO+)0F9b)>{Y}aB}tIu}y%`-HhMRt%6a)Zl8GZoTXC3so_&6JjRUg!;os+ON1A~ur1)wHXIqT(Q79)s8h4Vea1T7AQ=sSC9NTC_Q{17Djm|M<`Akz<3K=P>}|Gpp1jy?-=-~eL{7I1P}hFiUHIv6;isQEKYi5t>2~X<yIASH+qJZm5hU7(oc?S#A2;0`s4_^wOWr^0q}DFnw4g!lDP8P|I5p;Xh!@5@(2PuL__8h_I`_TUA~4sUe)p@PdXP~AAW#B;wt4q9UVJvwD3m}i`nCr4K%UFqbWjtVgpI)em$-g+tS!bIj;6tFQmOHm_=<W>TLEL*_u*LR9Aj{55G)s)3l~(gwYb#1T)4otE}g~27X6<W1a0Y{W_LWFEqT430z-ND%pMBXJ|U@8DQ?q;g+H&=^G^_K^umw$>U^!9d$M^$6ikfMZT0}%M$~T88|*fX+`a=epww^J9~?@{I&^A<2Z!{wad7qZ&^bXw>EHuI)ZXKJLVEj1j|yvboeX&4Id07#m=a(Q<Vr$ut=daZoJ+9Ij-?~OqWsfZ_8-i(tGx!+C=?;Kn{Ftv8v{Y%uK+FU*C0x&O9SA0MhJRiGXl<2!<Ki(Py4h)X8d|>*3jA2@93$jbF$W4T5gQjijR!>p>}2gz`xt{o;uUu0=#NC>KYP%sWJs<>RD|+62#99RMzPA-+2hyS`HrRc0mA0hd=I4<H*ts81$V#bwzXIyv9~z9Id5&s(r*O0-_2(pwAX1dm4=<#QWqzHG7~Q`^jW5Zsqba(J~X-6ebj&iE|TLl=yhe=bBTo0jM=<rqk=%T1^EU!qPK%Yk*Zo`a1y(ef67(<F2`KWWT@${wTiG7D#hT%sw#GFxHSK80DY<JJK~JR#ln)7IM{VE&qJ_z?mGF$XrPnvNcf>YUbnEgtxxz`HeWsny0(if-}bM5frK3!8`2c9Z#B9zyolD!9kEk!cwABtC!9zWea1k_XD#9?7?IUylCivHYJLC@g(e(u?E$`EUW?DxmIETOYKoyx;|PwFCy*V{RQxVKb@e2LagBGe++Yj2O*%j<{fq#UURK^_s$X$_8XbJXdHWWKc?1Mu&_U6k%6R!n&~v1lyO|&{rc(^K8o<Hj1b|d84_73sDgDP9k0m^0K64Ev66%30lPN?vm_r~%ZrPPd=^_<%)vG~@#BFvl2{DskexrK-+5*wrK?xKJQE1(q;cgIfgMcn(>fB!zWcQmQvj`<_Z&RXutrEmQO_MK{sZ&d9O4vwW=z4LbQape{edj`#tjvK`J}njY&pL?Tb@TkksK!t=j_WRXV(wA8_^m3=&j5ToR@G6IUhIYPn?&_AcY?<JL3tAEbs;n1}Pul=;m+m{mkBry=TuKuRm!&c>KxMF5QF5g9JE^x#VU9zR0RBICD19tE?E`?@61eC?k94gsQ0I`@T0o^^@=4_s*Y2<DlbXL+>jwd97AavIc@<tyy!%Yqi4~MMrXXkAo4H{Ma9KqM@&<KMM;jSC*x=7p2wb{)l{OWA8k#U3ybswpUV$T3W(@@G#B*TfDr4HZcyZ3B4tTo>)<{v3&{nq|9?5VduF~=vfv3Wj5L`gCrQ+E34e{`jqW=?bRjIQoG9q9!v(x*H@tpTM<i3Pkq0;4#es7Stz~c+9?*0CDmJjB?CGv`2g$PJ_cqfuB)YxWlYaOEP%7O-<7i4lf<74pZiHPi93D~T`EhL!=7-$I?`eRX@%=QK%b6MW^>@3TidV~s%%FgX`5d0O=-_8%<bNp(s1(2#cQ>lmN#~>UiuMQu8ct*n+k(m$x=X&gWGA1Wra%H*_~-ryCoyqIvdAcXN<sj8Fc-qa%rjyn@dwxwrpvpmN%B>K5T?II-iP6rRB`QT8fp8v#My>5bb*}pKq*-mb*0T443RvOxZ|Dvop+escfocZBLu=lAR_JqoWG~lhZ9Tr{f!h5*7#CIaFEP`hzHL?@41hK3-PRE+Lea-UUdY@5z~)mkQQt_x(Z8iAG~THs`*=bAOa(Uk?C}^k%0IGb=tbD6%R$XncOnZm5nGASfJ}pjc&4u;YlE&Tc;#E$l$4GKc^vK8)gx$Qz?5YejNf5!=Qw%av`Jl2Vq<!X=49KZ&B_iq>*v$_JMgtR7vl*!1Bo&C=e|%mZASafC}%L+o?e3dzt?!h+P?XSs}2$ggf=X<8#orLAZZD3>pnP&vO;Kux==kWX`EEaOqfyY>-!CGMk%+}I!G8nYLo*7Sa=DTr;hRYfg>Wuovn1d?(D6vcktuou!=3yjv1ZEs|SU_RS29yRoql)di-gL5*AZ&{n1T0RpGh&l#gcLMD6+@z4VghEQDG8Zc&kgA*%D?^yFVwP!35!*pi&$86qm;{6Flz~{wSeXYPUXg#?X6USQUKvmzyP7T+3)pC$UaE}VS<6^x9h5V-La`k)-?lPA1(7o|Ewu%nRpi!Iq?*b>ujM2TGA;Bi0ltds2YbYqNTfysg?!8Awo?{WYbG+J3ePMgt*7`nTjNmH()JGax!&pc1GMY}NphMDKfQu+W+^Rxy~g!TVKl8pqnX}vY2n!#t^`R{`65If5Nn%0Vp}=OV9jEc<18s!9O4cce)$h3{$TnzOAA{DYbjef;;Qn+VUs!2OzqlBPHAz*=1M2O>vy8CJ8P3=g=cHHdiE9NEifQbvKNdJ8;P_Pp*HTW<W$aIMv=)t?=S;JhfrfX^VA6VXH>g{x<jUgx<4CqA;T`a8F^O8SJb0WYN`rVFJqyzrGv<gpit{$FL@42b>hdis(NmP$Ot7XMZ`4UJ_Z)MpZi06*KcR{C8es`t8Qni7`!n_cE{0(OZ(l*`B}?aCB{S)DmHO5musniIH5O<Sfom>DJy1`JCmV5fYU`zEWgY9W>+%H#c|+BAPGn@+pKIwY(j|SGc~4YY=Cuue?&qGQ=C@3Ok7v>D&_S;p(5Ze<=Sxb$+M?h?cKfgz4n90TTkxqk{{K?KO3E4pYYd5!}AVBXeXaY7>v$w4a-=!%)36OKYG#SD&y!heClzm_d#$>VOrdW123VEo<B@>M?ME+JBoe(aoAZO9(wVnxLT*nDewGo_)yyDd&8k0Z+leZ3$Js`3HU37qnu<wyG{AKB!4jmqRXkA#wpw98(z2P^XFdQ=UzGkq#g;UK8U67?epF7`G7tNL%q1W84ct)0Tq4`qDKh7yV>`~Tf^v!Krg%Nj}tz-^#gz@#-P}koa5%9z{Yxdd(ZcVr%`-N(0T;GrKs*+5RRYwU76$v-#jGVsai6QhlRJCdr$YwM2->2j4K#>1l2g;XA%@Ia#z+M88*-O?~?poKI5tH1fB6Drhz8Cj+E+kmej|x`dFcljX3BWt5w}P!{}%*j!hMOkB(#OW4zEFZ!eQeDuT^@?>yN;y@B6VE6%Y4_wc?vBOOTcf}x+`g-qEyqhBNGJfiiEXr&`s^=O6H*E^@NFy;)GH=^Moe?0<<@g>G4A3VXEU`pHeV3o)G4g9P>IXW6h)=P}b+R+O?hgCX^PB-Kg%5XV7@f;Ml-_G+bb#=e5f?|<}JoTk83ZJj!kwkv;V{-yJKE|c`%Nd5tJkM<1KYae|#SV48&n}B`AG-$)M}G3Bq5zz}-0r|Kv<D}=V%y7`{q_*%%zf_eJ%JA@X<cK=$xx1dS`nX{uxvBRC_@TP--%$ONXY`tO41*cZ`&kUTH8+(^AR^WmY__b>yO5?N6~zs&A$%Pm^DC7AeG(9k#SI2KzoV!!ZGaeK?@nW!4I~O=?$VokajCvv_GU0Vs}*P)lP3m3;IO{#%Q@?^uvCx4{}y+Nvpj1G*ouIP$_RQDigk8zGdo<hlBY^=qDX-<j;BHI8Oq=d#N8igioDc!+7*gsLI`Y=3|#!?xi-Z+5_5LY&LtaFb?rf=8a*Wji@w7Eb^$d?@jJ0+dh77M=0PLR*s>6Mm~mP)qmZ@7iG$n*s&!w>TKzYZH-fhUiB$dSE*Nhv}UU7AR!<*A54b_n%N0V4%rnATA7(My*O@}ODb=e(kNV0T_?(u)=L~7&6Ke6;?jf|n}CV8rLsLH53vYz`Dph)2oPt%DmJAQn@BOEOaUvv#CPignR}GG<_yi4h4Si;4G<BsJXZz1meeY`%|atltcVY^I1)`h_*pJ`AU2c_na)cQBLyCNZ8UH*pJ~ft5X{FDpxF$Rj*slA)EgaB^i3+1Vik2^slsigwNg3=Yyz3w!Hvq`6C^r8S#3$BD+-PIShG`{Ex-iB03WR8D4G#(g6UY^s9fq=9!SC}KvhBpDzbmOb-??AeyX>yyj<egK)j5o7qL>b*rbYA?zTVgzW2Y;&>E6!jF6K|t9Jr3T1g^8T;R-F(oe(X@|b{s8*Vrmx~)>6U~a>00#wRFQ9F)%f|u>3jhs;AX>8<@hyD|1edj|5g%>aO(5#wvL82nSQ)FFqwds!nBHKQ{$#oEd_|V_$^x3n>e1=u?NfeVy3>DcHw_1x{G{DC`0^y)~LDKhyNOyo{SZUAp`LjWnQPXV*PS(vmDyXjzmhDTSS=pBO`b*!MCQ}hVT!DnsrZ49!GK?2DRC!97?K~*z_k4*7s(gBq;q}ltdGq==Zlk%ls9x_`N7*LCD<c~@Ap$B?6I0&%V^4Dxr#3d*J`dl#`Uhao{i|=!(K7tofSkE!99@lDMvP&BX%Ab(I2*}IWv~XhAAj6+jTuOLCBCE7;})(dFIx<u4wi?WCyeLlH7UJftV_`8Q+&}ti$=Q~5_0rXZEq8$h}!*p0b>Efzh4!yBxG=!%H`a~p_?LO<7fb!X$=Die?_E{<yDlPJ$|yU5ns*O0f)iT+=JjMF=b2kL+7W$M&XwhygC&Wk%i9%-8C%0d#yoU>egHz5vWc37YG>r+M^70vSLCcHHA7Ilu?^W;>T;Ua19_%QVq$}K?CTF{6>m%04*Q;p&Yu_$i>5Z&3c2pJFdCS)kTDvH`ofhc!1>s(WyrNnMdm@wD3XZuSXM`uEpFNCs_~avM6E=B@~Hd>+~SRH!}$l!59x2=xJd%g!2zn8=O0b{t>ziWiGq$5}4q;dRLi{{3W=Sg*3-98DCW->_+-HUeyx>ZdGh;eB8jh1RIq%CHSV)vU_#Zr?351+LtcRfE*W!7mO4-b(K!hlDT%FvV<$PZZV$o98J2uz@fI&^yUZe6X5dDFr%FBdB<ot3`hXH>_l|s4fhd(1y0IOFdU2V4lk9A;G8}g;VMc*KDANly@R`mj?Lg-9D!TU$ze7pr$V@uU}cUueMVO9AJq`!8r)jFA~-8I*+_{w?l8Cfk=Rji)=o`iI?!4VKK&e%OOtKkdNtmb6;x*dBsBDJA44<EW%+fJv}g5T5%E=zR?@lY*xqc+Q;YQ}EKQuQg#D|39%|1)*t?g9!9n5JDgM|6N>u^nQx=6IFK7|6T;d{tu$%x0D<5u(sWL%w)1krFAXkKO>gh`6w9JIVzG~@UU#aR3QqpFII!6lb+cggy$39a%<Ri;-)%ph|;XaPidzA7ctx2ZUw9-RizFX<i;)@KAZ=9JA+HMP;UOaqB;B;%$^kU@mLYwolN#|gF({%-wPLlO|(8YU5`?9Q=ce-FtLkq@Uy~Xj$CcWk?-{K;E#Xh<g<V7!PMy73TDkD$u=sP32v>1FWMBTsNwTt3&KW_oi{OUeXv#o(YtQ+E!+aMi)`Np|;M#P@-aUpOtE;%sbd03pJ@iCk#YuG@Ca7xrMp%}KD!558CgQ=8zb8?PTAnZnA6x)<0F}<N`5jD)iG#PneCLX69#8EVEW8NIK+AtJ?R7df8jeTJ+N-EK#G|_Hs@%S>q-mTx0dGb7RD9Qs8E=a@CC(WFYTHMFsFiczY>8BAL%^_uTsKC%pG$J>kN5MewbVe}e0ZYZ&qLbPmW{Qg<;nP4&R42tQ{m=>6tI*c18w%a5C*_()hp14`tWf=r)=DYpeOjVY^2yE4HYshLu01P0H>7=4k$l#Dl#V#ncC<|mHml>(4AjaQpwo%=dl~F>z2<vT(j?-*t@}|tGkDS~qIGg`mbh;PE9taqW!2gAL_qXAXNQq|AvXf`%)5W}_d`>KIf`&v(icKP0Hkjz1wANR3O5qV74)EBs(q9lh)1=PX7#pXLS<zbq@CR7a!B#STY}UO_94II@%jLjJnWJmjTq2zFq-wS4gmh(vvLkQ;3miD53Au42PH?q7&Ra!U&DA8&9Ows1Nu0^%V!EmidWD0;mI;X)1Acc#CWT0c<4~W1k6#NH`M^k)DBnwcCNhLZXyVslcvpMb_F+A*vQ)nD6_p76Dp<>u1;bz6#@DYBd8(Tt5r(3onQooserB54d8q_Zg={@KuNgL#a?t8J_LjbyKX(F=q%Oes7WZr%{}g|thn@KsCn2wC+fjZV-OnJs5=nBG$+WWDlIi6l$BFr%)isjwKbL8l6^u=nr=rFPfAaq`|CG9^KO3GKG^^Kv^9V8;AhzpT=bR0R#9P)(T;|T!&ll8=)7K`kA?Y|%GfI9I14@8I;y|3`SGbk8-pfD<`BSyvC631)Y?2p3$~<qo1sgi*wRm&-3ZR)s3=TWZ|soK4IIuB)RqKY-^p6I=S1T^3<(uSj^`x7;Q(Ve=caI&HZWaya?{?5$UIv+YM!=+&=;#Yq?R=%xCP$(xr!o1<x~Aai0pK2rip3Vi1VmGfvUFl=wy!0Si)Y01SGZ3>C@HSy%ct09+s_CLCD-FpU?9=P&}xRO`%?H80Rr7<z;b6ivgLT6(8@>X@gtOi^%@j7)6GC18uX(I&)a9?jEEf3~?hXK{XXlpApl7|2__n<m)4}<plUCkW`%{8kr#4;Gt$CV7^#E)Y<I7qO*`aVCcbf9$_{Ar@6zNd3=MjTkgcB_no8Abeps`?fiC+jPUg9E3!#)Eg>ld%w<-1vJ$onBN9pGMyaFQG%j<gNl~4GvCL(XhX#2H22R6X!v`z79D1l_b<`?jPF>+viT!AjI8}3^uiQQsK3Fp$dc&YQYk6!?bfJI_nX<|2=|is6Bdz@*TBOPo#Z15u2*Wy9Z7ExJzw>LuAk>3sSqv!5aFe_v^FC@DOUrkPYXg<n?6(NmTHZupCSBKBrs=xJi(1fYvC3(hPD`t7S74PXt}>RhW>sC~kSfn<e&T%S`y;v!+3?VA3AST^DoebcPvD4vQ5?J@dNxi<*u()52ndJ+AfDG5t$m%#;}#HhuHh<I$g6fcTwHh?)75sAuAXS5X1ln?bJX#ltTtC}-M!PibEp2ti)TmjPu<*ev~R7ni0uno7MIm)`=#<UpZ9gPL>(LyTUjF$s=1TQA+lTz;+4`LtpNpY(A~Aw7jwBdkmrijeXAOFw7+;?lyFwVP|`G`tXm+oRt+EPl#0{%iL<@TxBDoLdV?f#Fu)CtXgdf4G>)WOw1#u&pGUwH82{%jM1f|noh?cfp|c+?*r1R0g!&9C4QeE~2@s(ipi9pq(@!9*c3oSeb;_SSEQT*uc6trT2-z)*R=Rkk@6B1-h{yIe@(NTmE>}@PG#}u|nb7e(rI&14D8|=KaE$lVVL=&~DXiX~OSKuh^taxaOZ6J5Gzz0g`jn-qIv&Jc4>baQcf<E4<MVAV^m=IGbzmsZ#RdHJ0bLM5En`pBElPp4!3j9jR0E^(w$4V+z3`ZGQ?-oBeZUDk$#b*jE+<@PW~Dl0ZFZ>qwkxLzPen~sD)SGoAs){t7r%{6j3bx~1|%TN#fH86=iT>Qp6M*aS2z6<p~pRR%l3xLx=M%aRx(Ymrc<*5&Riw)E=mTo?{04HQXAVa4E4P}8YSA#4ek3e#+Mrm;INikQ1=rI455n6q<v%M9Xa|tX}T7@s%(iHH{>zE%jNcyXPfI!+Iw5uJ5Sd4w%GOrkKrG@{}Q$;%-=cTziYLc^8nKDZ|cq*e;^xq+=Z`&58hw@cvq~Ks2BzX;|z{vk%)su$X%RY%>6^fBGyz&@hm0AZ`gs|XsDV3_+y*|9Lrj*dHe3ttzwf7`kUbrHK!ZI<8yZJ@ct7o85_+>+9Q83;?6b)UbyWK5Bb+q|1>MOGfDdB?C|Kme-d<jq{fbSIL3oA_5*0j^FKUcaAgqbQiVN%i~5PSN$~4Pil+c|dVUlTjA1N2`WtoVjU0WS4Din|>iYB%B~l;nq+yQ_*J?fZ!H>jXF}}>N9Lz+C0XVA#T6Wi>OJAO%O9v4J2bNvN%GQw0)S@_<fLa&~%4TJSR+nwXTGP@GFaTviBVW+Ve~$|3l0xbH8txPPL)=$1|EI}X!C+r25BmX{9Ra>n7PBA}jz%_KRZZEXrn%x842x-@Qcj~X07qe@rUaP+13)$DkP9&u=Br9-S~bHbqw@dH+ne<`j;#q|@AWHUa&SixW>j*Ks3r17HzbmhsD)Z6QA^%LfIBIQi%5zhm6L#tdGdn+H*90jXbe2<Mq}I_G(7WQ3~(<DKir=AALU=-bGT@UP-Ioz?r{N?As!x{_4~f_?dMed`up>Xlt|z3jVu)5`Jiqq&T=zFInTzMO$f~f2QP#&?<{yL(cd^%Nq}>u+UreB(e!-<f3d`mB_Pb<9|2+gq<#MjNG8+jcrnFvx1Qf2x)(KWhBCa`>c_98e634QaOin|Pg?r>yueSVpO3}1J>`q~?co>p3E>y?mjldG;RRVrDSPSZ1ZUYZgo<zHyHHNF7fO`c))h0a)$F1ZB&XQfZC9^e{u!2Y`=uXl-u-$TC{Fu&hRS!%SU*4YtJ484LNT4vX=2|l?;(AD9boXDoxYUTFTIW@_&!IKNrmsbyJz81uR{rn#PugdBG{?m#dL!g-Ftyl1R5LD2bk2j^ze$)%Wu-m8Ir6qKTD!t0-xd!pRq4U>8XTVNM!I9vgfa*{5S+J|7Gr3dF@4)HT?j%wDhzrJ)KEJRsiP$Sh&>7KZEkuKzK3K(#5%Y+0<om*5LWXy-^RAX4SOlj8U&}=c?cIfG$0~PYOD!%R*Y$qG7Y}82?`FjQkH^tw#WFrK<>tQgQfyuZ7h0*oQXfIiL0zZNFFj6y9Abzv?VyD}H{gu#c4S_+HgfI+TJf0WblkciC6UqkOM{Qye*HCOm$xW^ofQlznM+E5el^@G6!H1h;78w_ivOZXMCtJ&;*=7GR{{MRLzKJVt-5UDV8=|KWW>tzg^ET9-^vJA0%S<GJuyfmv>zFFp?btb|CV96RsN<#&J+_)tP13zQA{LW5&IAf*q0Q-*5-HAj$bEWZ1*(!)7A4i4RfLoWsb2W3Lvjq?Y=g=c%d0k@R1`39W6Dm|uCDSXz2GBmVi-s*r`GkrC86ockk$clzQN`NsvqMY3aZz`}Fkde|0z+vpo>EQTy;X{_0qzfMfI3CCh2G6;z2~IGDzjM6Z=QDeh(+a2%D44CBY+dRBK;Q3k5oyU4HHSlmrkhOLcR8rf;MJGs^9>=HRSOW(?=UGDnSJ;KP%Eu@iva&{WgiCRY5(~bSDt(4p_G0s2!8QVe(wr+@$mVn{N>@x^QlhW)ax2~YJJyszcYa`d`|&z%O~+}{X!PF_@J0r`ps!l>C^SXrbS<#Pj7Re<4qfYi0G*9K7e=G2LPb<kT&0mkqe<+Hgc$wf&6MhMc5hc^3aVNpmh`HtTS3Y-K-G3!n-^|<g)3jTVem%b98bUx~z0@5d&yk^&P12g?egp3+*h$K@JLYQfB4-rS^+7%l`dkdyi>koa#L0KDEzK{(E?MeZkFzTKWF-?>_vl^yT6H<A3w#55I%y8***3_$2035`RGQ(WM`~);4Fmb|$G`9*Yl&hX>@`$Ybt*e2!c?g$ZT>VP_UHw-i8^)nW%zcK74m2>N+sR3Ny!*F<=SL;?eQ9`m+fBT&7rhVsXUI~g=#q-`6}nFLVU6cQd&__Oyxm=mj<eqDkI98$`1ri|nbt7YL%4J&3^{OoGpOE16cM&7ev=Ehv;jd0yqZo)i;w*T?3z4Y!A@KY$Cd%EuB;{1W9>htwmXc7EnX7(#yIj!=1+k}wC<`%Ysx1g3@sr1T^8o6Prxa$7#^y2YCg2@|u>wbN0`pI-|fcWU(gJ9t5yt;$oJ1LC~vmaMcJg<=A<h1!G+E^eV|0ghqWaBz*^Ht!;RlLqAT>H(OZXWM9zkLMLzAQK^A%Da_+{u8C&J<)`nmH+}$tqC$_GiEC6d_!^Dh95@1Ef@0Nd6$Ra@lBM9fr+4Uk9uWVFGpMcM_mO_kaHMTlB0N1ie7j_`m$^>mu~e9!dpOInxtUOPhbX@M;hp>-p40%4~fA=qaWb0K?yf!cGBH_DTuptGhIh%JT=j0iK$2XhtT~Xu=$AsSXh<G=-}3;m%HFf$XiQXAPuzQ;MqDW9#$`X(6B3r{676woVUYF+BaI+-=sED(ZXnqBxa3(zH|XSuoYZsc}I3rT}qZ9AuhD@3$~ZQkn{ebtE@FsfgK2t*>&U%+H>nLiVbFbs{so)Er-J&}9_mD_Q{e=S&LH{V7m8eRYZ1sn6L>(9gE>66oPklE$0MVRoe0Vshu&W|-1{QQ3$v5bo}3m>=)JBB|ls2A&3H7^J|HhwS_+Y|4l8_zM6Hy$<iWZQjV+{hT)pNY<At<=wRk_dCSwY-9QrbSzUA{t6-nY2H=D{n^jy=Lp*?-Ssb8lt0<#^9ur`PO45DX1gj>!#6+4C8g6BuN9qFVJnYWZRkY!$A9ZUC#Ap48IN;EkEKp}pZS%36-~JxGz-HGGw-JCPR@4~uchx~awyF}4L83O{WRjo>|XSX@J0z#aL^PV<p2D4C3s*!Ov$5=;W?VWOox)r<h$KwGdsxy#S}7oL6*ung_!J0_flrGy#Vr@$2e7czQamiPWcub<po|<{*tFSx{g)5G?wIv7GCA^u>m8P^F(Q7crWn_EQA_|Y@ea>E#>Us!zm-q1=4*@^EgAz4E!)d4k*Xuf@r3hznz`x?A3m~f`#7q++cX2Tg#Mn=XZsc`nw%nXxGV)_($wbm)fgV)93FtS*YJh{B3LRYMRn7FZE2GDZgLwoDuJJ2l6RdS?Q^iYViuKajEp}=M==*(z}jk>eo!+e;p0620e$LU)kVaWn6o?|DA$7ym7jLN_+VAwZa%o7P@>q-<;XWvoHUPz|0_D(iOUpRW3TnTYKx*l%LL*YyIUp9nNR`%e%EtJMrc1Lgrmvr=5DWZf_%MeO0vHzmXN3X`&AglAIRYXXto}sgz9*uqt8xoKg#C5ADr)Dwgx?vMTS<vSMEOXIX!l(^p=UB5B^wDc&&6F!y)|!2IIzy*?mnpQ`1E`j{H5FG_J(W&?Ic_2Ffu*90!lB=c?$W^}tgm=6qGf}OlgNi)vYSjkfkKb`O^6RgwJu$g8qTl>cnpOM6e$NSR;z>_5Z`Pxe-yY}`9J@TL$?8nB-k6(}iFW&J5{+f>9Tjr9%((hWM%<RZe{paU1T-+4Sv+<|?Tc=UqdD*4A=k#+I!Ha<ZzQ2I2Qyc`$@snFx@!vjQ)cEZ)Ud7(&9A@`{Rf`_OpZ@Ug?{FCL_xu0HxdY!_c#6H*f&xw<h1<SBqx|FjC9poG=T(uI6YRv>EJGJ<J~mzmqWn^>5ieM|`cfw=FSQ!^Qpal7M&%O{6|>Ed;oZf}=9in5!8lDNUF<OUG5zqGtvRdPPf&kK!UMX?{Kbnm55-;A_jvV@s63X5pG*AkdOTTMcTI**{m0H=1lXPYmQhggZ@o`<Z52Rk3U#pJ>wAX5w*5yiITL0?DlQ;}70>e#o#Z}EegeH};Z#b$^Ye$3x9xqpAdjhW4pM@L+gMQQ&Sv8~Bb7VeMF1cHLZhLkm!8Uik#OUeFg4L#koe$CNn!LO1X!44Ov`?Ly`-NQp?tffWd*=JU4tO}{M<f_wlvcUS<h*2S<zKn&}vY6%536k69s9>KTpduHY3Znk}?wDpKq6~K&l2mRh10+;oq}Ia>mX<vpM*GFNfen2V$gkU;6E?^ymg3_kL=ezOO$(F7V;H;WG|By+*GvUo!aX>m^zE5r05Y97FJY?EoiKdb*&H`I>-@$(b0*Rg#xY;5yInpO4Dk_JaGbX@#eY67c+}IsssmUc^8)&F9pq=P^+8ENsE^J?QKaH2rYSm~~pw(0wV2PGkA@i`&a!IeNZWFPun)NHe-lm1RbkYEm<TanQv3Bm!a!D-<*kC(?5(2V~We{ltSFZU9R=)bJAjKjtq%50CoM^ithA)Cu07R`aCDf3#E23GC8`9jt(%`k@+!Fwo)o)Ya#wAMxs!$MZ9I%=Hx++64f&;1wcX_#*?`Pw!<d720eln7R&(VfZn#i<jVC$7W`0MqN2n!yf?{0s#xuWCKn;Kn=j0WgHkc4fdu4U{rn0JCx=D0IQ}BPgMYMFj6gmSIK>a^y1syebZ5V7Z6vx{E#{!{3v;uVL1JLVfF`)7uNV!oq(6R2VuJ8sE6#^^a;a=5@JRl4K==pf%ba#E3J^rFd6kK#Xnv-(|o(+=U%ZF_a!3?z2FH&!+bU$y{(w|W(;={6+IKh(HubjJoou4A-laBss;ZMh?<&4CgdCQc(JD^Ab5BqMMAIr`<$T!%+RZG-C(+2r-${EE1ir7$f*igjr8;2qvwLj70m-=*%rflJ{1<@P2D?ArEtipM%>+p&-Xa_ScbZCsFiyGuhVebAVblIOGlnl$N2=9v^ce%1+dPg4vltmE)32gvz(|t*r-&SmReK96tV#Ug)h_7GEYz@-sMC4`18js#A$FI{cFHQrCJRKusY@^nAi9Bf1T!o{NrDnclu9%_<J)?K;r-L|9VU>Q2$pps3qpEWvTr<^x--CS28&5if^_VyO5cj!3-~16avG3`&?`aR9c1m;002F-<C1#=TgTOV^0s+ueVzH_H<W5PA}vP(?37qB#?EW1`$x3(mvFFtONAP)o=yz^u@#T>n}frfvKEJbGXQr0V(!f8jfM*D~>wN%mE4ki6t8+mJAeJY3m^RzQaw7jZC}r(;xmP^TfMAV^!Muy9`Ew1#n6?C^J}ylrpEtlX`AIdI87vx%@=bz!3{RL~gt#YENY2%j-y^9M0ds^>@K9-9i9p|JE_Ugy1Y30BPV)KBpLR_b{LIf0WOxoOiJtpKinBYp^SpAw7a11muShD7(Va`w^dx@R1p{(;p8{o)`p|pbI`ZrHuKSQb%}FzlFiaQuY8Sb2`fcWno%7)i*U09wRB8_;wy*ro~E6#jPtUZwGkk5BN_x28ajQ_a(Sc?_)`ZMJHRj8JJM93nZ38d7EaLzJmYkMTRaa9D1h8x-53BELuGs%j=iH9t=AOE^1t>N4^VTsj4<7pQ-2ulYab#2?+$`HGjd_Y|yu;tCuhGRd{%v-2E5s1)mM)wBnb$k@|~YZbsVS)e-$)VaM}MuCqEBt{bQ?saE;^oT({SNj&BLDlkqHNKKr+2k7V&Uh??IyUe8i4}bB;zsYmX-VyM!nyq@b91hUbIFzYz@5&!f%7Xio5chC*SNV9?f=AJv^vD1GtR=s@!#>`1fBM6}D?~RiPE%H&O~>1ZMdCoPz0eloo8JA|CYjZHE@7ntci=?cyv9qf!t|echUeK4_c8PCff>eL=aD$^*3hki9&w}TOPd`qAI;ze1~lD2WceYUAyVf8R=%+3$`9|h`i?*NDci4dky|FU)}7`;l&&0HjOQ`<=RRMmfA}9ELH#!{qvB7$|M#c8JFi^+xAfssf%@J=VDk^3u9qt968`ggXqlG)3=6H4u8GBI=#|pV<S|7DS>M6WF3l@r3WTLkIY3_cPUqaqYke%Vpg-qcKCe3dn7OI|{u+Ax<SPNIribe%#S9>yTr5!t#fJN|y;ofT7CC-C2e#*1!_Q{<c<(WoOdW#z!{ydI!YZXl>@k(z(smziEmzw98*nfFD`F?o20o{Cf5g9h%!{v+d7SFzc$Q=A8=(1>y2Qdo@STnP871P$ZdB~fwdDv>?29}ZY0yJ9el4}!+<pFfGO~QgWugx$o&S)<J$(4~<#KND%{#W9B2eONXt?Z5d)*l<IQ4{M-|gpY{mH^Bu2J#v<?-cNgJd&P!=!Rk;V*ttR6SlKnYe+Y?J3J}H2*@gQ#Ah;y;Sae1Vk^7OL#Z2%K&g`Vv$ozxy<tNX4~En)GNo+?4Fdg;Oz|yLF$tT*w*w!I-f*ElTgkALf8u=PylPQ{=gEQ^TR*ClX<;pA#<k=Urw3WvqMe;r`%<3-aN=SOV$1DlyUv>?kniy+ubRbb)h{4)ac`dsyNO2o!-p?^SftVz~7f$0t)@p@BdSn+leno*=646?1(i|gLcMAKi&c61Qe%?F=~T4^5flq`44*_8vgPBaEk2zKyu6#sKu}#gIv%bsP#Ti0krW~CLl#0Kc<=OQyK9Of8ppiNz-d)Ior_es7}3e&eRUPzL`HCyUd_}R*6F$O>+M>vHy*od(85zKWe2{dzO}eyGvK4RA?P8?i!E(6!<zh!QV>s`*6)ET_%6MllJ=EeWOTo4B6APg@>mLNO2zXz-iUl+o_k=J?QTde|RbY^Q-gi<K5SrNru6vUp{|Gtp^{ze7n292!Ov?GxPHJ@C87$40wZwd>ln6{Y5--Rs@G~Vb96)dA#1T_mWlL+PG8HKG?g<wR#)WpRU?z53dp-{>n|vvfe%4WPE?P&5@mfIuDtC&eY?8@uo5bV|vLcOeclr$)(V9YN^LOH`G&>umDYM$EanvD9n}dO5t}(!0>ePyg*M$74mchPkB0mBFW-YiH3huedb+|rXzUW>?t+D(|f52?(S1Gx#RPixxYx}Ym))$n^yA-13>)PCmHG6pR+rHQ9&YhD$bJ%JeB&!K8^p$GYLGE#)g}w2LsgZA_L@89>ji?3i9by)cCh+e7gz|zx#jx+yA*ZqM#Z98obhf1JMQLfBZY|8uQ>qCz<W-;Ti+;O)q@Rud(rofcTi%L4Ov3uCi+8Wb>SQ>I`NlH%sVQ`+S}D^A;Xu%)tp=E*E8Hh)J5V^nWp*pxe)<yOW!HnmyvGa>0UKIy!-`Zg`2@8pX+}<~A+AcKA9+@!yEY{*&mkcK4PsgsG*!FIZg%+FpnW@A-Na5`_$%#WTl8SnEH@@SOQy@1O|y#xd<5Lvk{gyl2S2Bx>;DxUVuNTsnmPdFe5C$jV|7ekh{PuRhN_!(Nk@ciOqoZbM~T?p1dKGRxnA%$pnYn9b}Fj_=_X9!KS$hgkln-~Zo$y#X)|Ht=uGu6?Od`?L+8UPJW#_hg8Nx4vX&zoHy#FW2*r|J^B2-~>*fd-u)|O{f3?=qEw~2T0L>581k({_ywWn-#v?@)TckXaUF&r~#Bc?$7K0ig5%yp=|7b`u*QInF=iL_v2lDvqH)t!lcD9sPwlXnresg6$5o23jikZi~B}kZy!r<Z8d)aY8Fm{&o}%AZvo9saCrqHC*Ogm+yntLsTYdC=9qmvrJYO>JF`2U;p5|pR;O+$h3uBQpA>ZP^VedWpFd<Z0b}(>dOOuA91@Ep^|?v+6gquDq6(G95C1>uAKpKcK5K;zAdC5fXJ7j9mCCc2N|BrM`mDK-CeB_vr^6)8lzs0RfBfH^?39N(sK4E(hw|SgmjZ^Ar^LT0V`TEh>w#Q2Y(OvUG|tX1eSZA(y8x;jpiVuF6n}WVCpQ9F&u_1h{ak*DrNx;EEpj-Jma5oO=H-Tgr}PIX`jp;H220>yy!r@FiGOXv(mNbW>%S+GrKY}n{IUE<{)mHyu<uG>@aqe8XMWX-4}_J^aG3d>l$SSBrrcEy1(3Wz0qt{oW7EUyi>&ZRyox`3$&;#|eM(MvlY0_f;>)?#hcBt_L;C6W|7QrKpr8Kmm(Yvrr{Dj*_u+fUbm{&0!=)qO8x@+CJHXt{9Uw#iUeSg5b1nx{eEKI2<?LE{a_)M>f6hZI_e*)J@VjtfxywcZ9nAjS{_ZpWW(*~~bnQ3xCe3BW!9oKVIJKYw>&~>(l;inhW^hU~^5iA=Coh4!`!nt-DL(@f9A&Rk3H5Y>KD@s;nZLo8E2cB`)k+ukjaOINZf>N32IPPEi+}i6sVxxh!pA!<{hQYOhrfVI-ONC3s4?^_Lx~Dn&Ky!6F7O7@!Sn2fuiVJsr@umpk-8aNU=cLd!S=7Mqj|-540hi&h~60A4dvOjQ8SHYDWH7@RXf>Pa|PwF()SOj)Nd=_DpNi+2!3BR1fIX&4)pmdc0BWyxJ(anqL&#}J`vBW3~ecSOD|UPl~+E{C;y8)Gsk<b#*b$YE?D|_;p}$uge$zmGIyBNV+{=c@jMkNyV&krpk)PcbFbCxc~i(Uex)i*S<s9JNwpTm=%HFA<xldR`kMXy_IT&$sWHYZFy!lp$GZ;&k9#_TzGY6+cd6@N@a?g1*Zg{(W?l#{_&DWk`B-|FQC(*KvuU5XuLtY^a!!C_`YubF-;;N}%c*lqdZHArI~NA11hRlv=IyLL^eKY=u5p+-1AT(Nkr&nSFF&Wgc3-Z&8-94}_x}9Kizx5q@r0WfJPeot)Z9Q1%O}wK=aZM^7ib_Ye5A8ip_`S$KCUgZXDEgH|GJ$Y;XPBQ1`6N&+)(=kh%@(Z{2;FU8UP9SOPGrHzx;;_7l((^8{dm7n)1f4=ue(-W*2{gYyfER;oFTCPYH9f$A?cj(We1nhvS8S1w<_P`KNOT!TaCmvE-b4C+<TdJAEDt>iBq<U1gg=%o*l_JD99Lgy)nCZ%hn|42VCR%%6+Vw4WL|w9*+yzQU-o^lnkdJ!Do-Exl#*!*5o<v45ky{HFVx;cxg458qzC?)Rqh5&lyF6#<q0{8az)?IQ%$%se87u5HRM>8$~&N%Zl;Gc=#;EpJX}dvn5P;+)ptO19~z4q7`Ps{IXE#?;jM!w*>o(=4ynXg(XyXW%F+W_X9*os&boxcd-L^~{QM`Ppzpvu&24-~G^bmDFh<`}Fq3TIVYl-oLheX>VaTH<%+2FT%R?At=(4r*~4NR3y7A%elL{yaE=cF*Ogxby^>xM`#+jeRZ+VFUVG|-@!4XKX;4!IfwT}vhU1&HZ`SQEyvsI9NxK(J$-rUv-oRn7E7-Pe{-?e(`!eR^y0Mh9baFvJmWCG&FA8}uiRS}^c0vW6Lj<Pw=_ZG#YJzI3!Q)Z{tZf}3zR}|zWgEO-JERc&$lBz=dHYRH&Qy0^kSrJ2H8DGu=Mg0r0*z4ZU!L!qjiYTF%Zxn)&H66TTizepX#5riGV2nMd5Mq&+mjx|0217+?{F%C%4YjjR)?NYNiP|pb8041~>N(P3QaZbPPi%xx9b!bEYRM=HdFLZbG;^b@cF<2hx6Ls;}aNG7qsAsO-GYXjb<7vhN1~8?xxQjtN?W3Y!#ve}VVbNoSU|jAoq`EU^U+#J}>2bd;AA_ZDrtRF4(Y^RnQ#7f&?(mtwTR^T|P?sFwj29JqeMxz}x6X{4UhryMNvWqDKa{x#ZPz}U@JF9U3T2{3-&_qTt(d*uv`rxiadCjU*5?=oMX=kKo`kW_C?<hs(^h>!2gr-&{9i>N$b!q|5g>kNHAybG$z8^HW-lRp=<bY8}P1iWTP_+v4^ODdR`y}lPzRMO!55OTQiPkz9phNqkNE5em=ebG;zODObeN7GrNq3xkzknL0ndClS=rH_)Cvo~4FvJ)3|UrN7$BauYe0w1S+=U+VB@WW3JGDF>Np@PN(@(=v|lEn*TlK>*pRq1KW;KjfA7XUB;OLB)*E0uSvT`<OATwsj*?Y8uIs*qmxkkN#bA3siDZ=5;PDj(BTPM0u04>U+Qx9`o#x9@(`-XGZ`;2>nHFrZ}HncXl|q~U|e;=W|b8Gq&g%TfeGkG?cFaC)2HmtSzA733eVT<@O<-#ZDuT!ze@<BCqo#8U_Fcy$%0BD6`IiPz<Mm|pe+Css5Cn?0J|{bznOpHfWfF!`9`4a>DhFBhd>9xu9o?TiN7JUeCH<-J^O@;`enzW*g&#_ryi)l?os&qN?|dOaIi3-e&+$5WVCUd2op=E<KGfJgxW51#-CpP)-jug8?tAA`_+g*@XX)o*r~7p^&EPAHIJ6xin}GaSvB7rrSlkNNM@;(hs)Ne7@>MuM`%eM_1y#eCTAX`#;%uW*a<PS4x$_&LoHSb9vedBPMRSNrlVIm-?2ziva)Tw^{|hFvA=$l`=kL+sfl`4{fX>1-_QLuu~k_k_mMmC#svKuR}gDij;Dm_k4{_a3~a@3{qba6ZoI>WP<yZt5`e)~9pLkG2K=g-JD2qs7^(d%6zl4c3&-MlLAGT_p8RpRaJ{>VP`;ie9yxbqEL$)XzMB{`JR6I@p&?8JNP$mtt*os5s0DLER$k>?JV4sjhy^*8{wP(Qg;f_@=3B=)o^)OA@W`w&kh5ZKh22D|Oea+Ly{MAMDNL+3*1>eC~df?@GVf-~C3v`;Az-eg1ub(4@c^u9F{jYQlPW9aNO|0q~;?2^pltH~ekWD<xi8dcyYz^XLEwF=}71E;l`HFIMBEj!j#A%i!ds1xR;keo#QpZoS37Tr%nT#-$V?$<E5RoCKUt_W5H5g$1nVZRVvAo--Z*dO*RGKYRa>zki1VIB#1CG99_ILCUiH_=~ufYz}}BU((C0@HL&xr+b+s@_Gdzg8y(<INP@9oVBjSTIACKNbz_NknK?i|HF-ZD7wqn<1xdq$BR9DC6E<8oUUAa%c*5;y`D4Z8?rc{x&aXF?kgC^x2LaQAn(_Myxdnf%$rrd{OpbtV||B{`{#F^G$mnh2M<h7RX*O$4ldY^^v3x+KtO@)yxYT=U~&5iq7aZ3!t91cO*FTAP{DV%+aQz6;kJDIc_6W)H#}fEpWASgK?vNpGc|$xmG4syB@ge+@B+Hj*h@!#`!xQ1_7wT@y#x6dAIe2{w<*aq7YWXC<t<t0y_msELU)A=*W-Mn{?GP&x`&pqG&)}0CU=2*-pe!_A5^2H{3_%I6j#k8(!esa>+aH<Y~S7ombY<*csF+8`#An|GZjpcG47Rc^qSHXH02#Qx|S{8xgRVKY|BI(C{#Wb^Ezwb)AnxNj9FBD`kq<=?z0K~IH2cf5wi)y?V#UQjv{$G4-em4$$tXw@>c`(iPO9d)PNMEKwSvDH-Y+l0kMAG!j1e+H&xZ03+^+E)&6v9BM-_>Lu75!F`n+e7O%d2ylbVv0?N)D+_z7~Q}FGzE&10EBW0tnHXHKJDNd!5-0dOU>NoB4XJzYLv<7fgfYBuuTyi-1Nrz+<^x-XD6!(drhE?Ea;n)Tf_TCi8Un!0u;GMK$xq>QlqyvImrYm`02YA8j<W&CoXH)^VG?{ND_h(r3)0_8DIeEje?y9jHvVNw}{B+a(?)ke)vv*pCK9!HJoY~$_`}ZBUzv5Nlc9#3PrApjS-&fM!tn!{N_=;n_R6pEcXlaHT(F~ove>b4$>XVyFjC`j*y;JjMH}88!rrw}XkcAGgP$ls{$hpjWA|9_@Ws!>u0!mknWmtVe_NP*gJSUrPUg50}{#1G_4wvFGw)T|ayDziRf_rK5JTrUYyG??u!rW>YDV8;Y#HG5@z_bb}*Kxci;}Th`mMc<4lvS~c;SH@JDUDjKR&CVlq$JkLI3~$jLlsN!bOGAFPv=u&HduLu?{HyRn{}r<va`ewoXKzkEp=Vd@N0oQIPeK#w+ORYw^=<3RdTCwTS*wsohH^t*3E4b9gC85a4Ym+!mfz}LabQ4Khwt1NUx%YOl?}?d%+Ip*|HY6vTz)l#7^>~XgNej@p8uL<_r^u5~5QkQdzC-N#)46#BQNe?KSRpTYDr-nC8-oMzh4?e6vH0Cqt)?l!w+}5%ALqGLa=c@5-Fb?9tHauIR3`s5Nj-Z3TR<I-L50{&v?8W)0$CC5CrIlwD#BdUJV=CQge8C;R5!M3-cziZq5TR%&$xg;N_#*$BJ+ZOnHPyEpFC4@;(+ceNjxvPhICEzH$B-L(<%LYUCCxxg$bwx-}~x0PsG9Q9V^w$1Z30_jG&)mSw`6dx>vXo?<U#jEV9EWX<<-Ea{^jKMd{N7NdP>T;_}ABDWDZlC6co1-naRz|?cIw@d0O6ZAvbj-y_Ic|e!7aJ3c=#2zytVFeqSsg25+ry8@fml|$*x1=t$SHHE9cX&6#pg|W*b@fLL2a<9ZK#E3&+@K}^&B6FvmV%HWE1<xYV#1=wd7E<^k7w=AC>)1BCQ1?3>azEv}|*U4H#B-*v@e|>_rhpSGx6bqp^!B2Z|^!sr_IyN!sJx5eJ)msOs9>$h*>Mv^>P8F(>iT%0G4{O(~>8vQf4rO*|fh4LMsKgxP_s)UdJ7<IVA49rns{*_5I_<~GGnr==vAKHe%0uOx&13@a}N-8s=!Sd<-(n&V+5?`mG=+o3-gc=j|}Z^!*5ja0i;Qo{^$lS~*=-Z!k_=Ab8i(~^nhv7;flJwMPkZRt&HEk&_J&n*Vg1Y=UusKY8qmeWbQKDQh>iFaczs(N`>^_|sd&K<9-_@30BZ4tNGDEr#c@mjb<uf?cAkK+CT-^D#}jB9vgl_%?kgiX*gJKhP?U`KZK&9S;|$~z8iCy0I+*6Oo?J11r>)pBDy_VcdD{es~JL^$dn%YrH^>;Bfo1$W{{0|q(hjJiJ<h<qsPeb<X7OfX}YiOM3DOR3H_Hmc)=?x}=e`e8jbjz~2g25}t^c~W)tMZ|Z=rBTePGC`NM-RfwlDiJOaSsrf!OK7g6(NT35)m4v_tTkpbSY_0YM^bBUBmE<X+EabCnNrn_Iq`VQ#7Ep5?Nw${f2tku^>kC`8Jbuh5T%J8nY^nqpS0bGIf}--*|DP8vai>~0oK;$QEle6ZPf|~Yn}sdl{sxEL(U=f{wAIZ>iC$9-EtTqa%C_kYm(&H&eq{EVSp~sjZy20l^yC~n%&B~YS@eZ&|@NTy=GTs#I9%^yv_MlVWaeRraT`u416VuR^N7a$QTSqZHAMrLoBBQu6>x5=e5<KRoRTYl4=E1IFI*yA6<$zu?u>f;Ss~hszBk!9BHnUeYMg>Ws7e*%SvTY8CnZes<W%MGr{{xSEd;WS2yHgVNS~{qdn?UF{UManbPG3ooxF=Z7oDjWzlKY05B-lAlmeketF*Gm)lX5D;97R3-MBHE@u0L7B*v@o{@UFIc*seZBsj-bEzX4on<$%svW7;wvGp8?9W+xHW!uN(4X@=t0noK;iv&d?|8bhS+@z{h%3PmU&#Xz91;Z$oU~ZXpZ7If6DC1Yp=u#XtOxw+z!?WzFwAMxh?vTPnyB)GT_B`c>8spKniGV~Z7h$N)0i4*7(KD(3Pw~^%x*6#@u6nR?LZpIGh#F?2-9?F>63xQ+cg2H2mv^hq;B6Nl8QzNjEvz2eO_*syDe?FpLp1DWQfE0_(1M>F_6cA%=Bcx$1Qd=zHjIaiSKn92Xql`8Ln1q;VZ_TPANI>%Hvp~BbogO5a(SWRNLLLQ|s|0PR_d8G~%rFAeKg`7PPkAy3VaUK5PuDtHsu?%ng?rY1V+QO3p;VD_pZz<9AqNysFp47Aj7M{GmMBMoHe4Jr<WSwnTz;Qg<+9tYc%M<Lk=aZONTIH_`^Cf=GI!ZU*D^!qej_!gFJm8B<zwu-BdCV6C8w@ut0RG22D5I->Ddn|o-V!Rme`5(2?4P`J4OG|uD4H5+B*y(ny`x~O=axT>$JtregayaBceZ4IXF!+2K@@MXvtTD2mp#B|*>+C;1#tVU<ew(6UsVcUx#wQ5fj7R=NaBTWtKd_V81w`?)(ZmfiQn_f^nwmFQ)EpsO>N5?^k1^sf|0w)VbwnM@XXtJ_w?sr0k2t~@ZXZ1x_qW!)<UDumYtKaF?wvFC?K~lkD81<?H(r(N`pDMcI8bsArOr~zpIE^}Rxa}F*K{mBvh#iD!)ITWVplPE-d2dryjX=~u-B~<pFR3*Z=$+-#jhFN7AnJ^q?p~5Ao}(U;fZdV1YGkfRe_W7TVLj7hq-<!z4L#blhTx!Zh1PPn*)?kxActYtr+r1OV`9~%7{!?C(W0IVyIXHln@}>{?v{f=Lv2lKQxwIlS-75?Tu6>OmfCTHDDH*@wTR??=O`|hTdS|tXY_IFQ5GV0(KZ{pA-!AHmkKfGR%@%N^gDRXKs`&K*Ysi5Y>+zZ&-g`aVvdImT<xzlf<St^U9anEJ9=Hw%R|rGuY-bGjQyn}+tzH`JTCl!)zzAO%V-_2m0^?PrPt|T)fI^@nlpZe_*DSW$L4;TbPqU9wWJtX6N$JbaAs_10|CeUXh|IP?P_@x76!`rNwS%u)4VIKFL*nr>#lnX!z&B>KEAW7?H%S&O?og5wnKlR9*zEbcT}386CW2nUiav-67>BRJtGzlxAy2=E$A{h-#{WZ>1jI6+L78?&)3p`?H+;xEIb)&hJyx2Mvi`5ho+#H`??TY+PcFvtOMY_R`hbeCB{Ruom9c68_d##o_ADgNvG9Nb=z3%S>?F#(DH=Z%@k$bFc<Egtd15lZ$G3dCC_$I!dvAwHxgOyAnCNXGY@SFDSOJKN32AGmCVLy9<b}yyvEU!g`{+9w$k;-y?Arj&V*{bOS(K;t?juDV%9>Uf(uP_FdVhaRll+<$7rR}UmWwUoEbNrIul{cjs}NlC>aqGv<=kcXvbR5>c&#kcbhKNJ<`<)iY+OA=kHp5aW*}aJ+)r%thvw#=bE&@jA@0i4J~R#+E63gSlQeyYVB4ZtLI&boiWQMbl+@X9eZTeopP5t1p8zG*s;M*=nS}62HP@T4$9+0*}+_t5^JPG?3lH|&eg=1H+)a1Y+G*GMSY>Sq1FlJ)Y>!FX$2;oEW1&`2X<Yh)v!f-KXyG$X92^<%Z{>F$0jFq<p6K80dAp!X`tQJpcmUzx4hapz8*<+Y^r({z+D>ltl1xsJnFO5s8{zI%6ikQ4G%M9SZUArT_^8K?wQrDR#`QX;d)eCs-vxutXA{ZAY_J84Vio6_RyS@mP4DYS8az5iMOUyD?UW<o+hoKsfj!5R%+3<K}6M~UGM7bpxTyfjpT;2UWZh}UEUSf9Z-%&H0l&}5RoZOi~SgH`{Zb{ZXQ?k3=auwNi50@g#)yvCT`1!Hl3)1=&!2Hv8AAzzE%y3B_>E@SrY{rH>o;HN70a8n{mUNbd7a!3Zs61-cy?vwb_&>>_lx~tp*M@RByM`F5Mi5#@gF;n~|4{ZAPC@Fuualdup+%1Mbw)@NP4S7t1nom@?a1>);DB#H!CX9or<?>26ook7nN028qeWDE7=Htyi3*D>f2os4oOb^x_dN&dK@+UlKEh5~&8F_{&~<FgxM|$M;rpYeydSiEa)>N!izTC|2EX!qsS}GsJj{R$2tLowW~Sfx;clt8}_tJlN>#`mTkHII}fJq|HdGt>Tu!YBuWjmgAw)Rmzga1cHSSQCG!HS*|UX0DuCLVbDoc4|?sru}^{qf{+s4rgm=ATOL($gf<JjYA~o*^_0Lu^^rvn-D;yN_J!WT1>zy#I0x8>9ytxRI%q_+U28O}l>x#cRZ^J72Y#atLvw7cj+7BrMSi)Nl^tT;nDl@Uuv4V6=x%!ZazO(}$Y|d2Hk@vRD@{jQp`n|+>9>hw-%>ZxK04S(MDn*Hg;&b<XnyP)HD)^xlRnqSXEhSTyA6EHGrNH1RDIJK#Y3tSA7d>Pj2U1>n}Y(c#_qygw)&P`-c9>`bv=)obV5?#S(lO6_4kxXL{q^zPMmnRS#vziwZ{1PFe76LWw@C<C5HGy?kmA`(3&4njc2#JY8dwy?6Ta$YGlmz@~(D0!Qc-(<JyyEdqfa%)9L#YpBC0qm93EM@qjj&ZFh{}`qnj^mKMliEfiLrXf!2{0;X<jRVI;Gt*?w)%zQ%->Y8L{0;nfPN5OCRh6S*%>1wZvHfmZeKGr!o2*IQsoa^+F<J4#4cDviJE~<lt*VA_tbL@C1y$LGBXx<oCqOeDLvPAcH<+^cHhiZ$DdUU+p9lGjxRomKplOc4q;Fu;N)+V=7b;XU1gkY&=KbY&g9#x$Mvg=F|Vdk-3-)j*hXSs+_i4K*?A{015ON4Da_UeGXF4T2A-LDy5$NX|zmW36d6T=>EG5!J&*L~iVx|A#J-KaOVbi|obOMYD^!}Z?X4ivp^A9vK$>xy_nm^@jYu2iuXja5!wD>coay5V&1DLp`w5Cxno0B20Z?+iI@PFUNirfH!WRYu;hkVM)szTyu~x2IMdVWEtJN@O3)Q<<B#q8(FhuSY|oZO8mV=EO0xMh|19Ob(~gPKmoyvXA#=v$4TO<P4!U%t9ZN6_1=&tfj_8tHo|TKhF4KR+eEYfvd$z4NJ7HLimChRJse%)w>A=D4(#ODP%k%F_~<Wa}DoAV{UlVoY8^<GOTd0x%yHdnu6jJlPZTsQ?X0|fD-z2c}#D6<%7A*yTXK)hso8zWZJv79-83f9#^rWItuJ*yE$69d$-K9<>_eBAdg#TMei7KwrE=BzHWxQwQbf-TWCwQXkPD)-IZH$2E0(gkDBOj8e^p{IEOs<R4F(rs?--7m8v&b0_J&H<K_)FZ1$9}$>7t)d}eQ0Z{F5wI=9@ooq^wNkIgx<A?6I=87GT@x5u<29#lsz8xgHe8E}sacQPD~$T6|r^DDtF_9|=+2&;CG8-7!tSiCtU6)|3GJ#A~Z7C}7Kt=gL1i8H)jK6dM<-^NLu!kgyMp0zd_JEX@Z+pGCNI1VM2H>R~6I;LuP6t{!&9A8$q$6~K~tASo8Cfk9AU=3nxDuCoVBi5SgW>RUgd!L;etx2$E);(d@+RoSYc+QK>o;t7g<@NTk7-5!gOqB7qhgBP8qL$1%5<>CqZYyGY3{!QdWZo6JHu@8rJkUdK?;l#5x>xNUoUq@eD}&b9EH|2t*5<jy(AVN|(;S7N({fiq#qMK)IkCEXe!<NUjag7?+=#^0#A?wycU6`)1E)jILZR0!$ZfS7$q~Lf?5)PKF3fzKQ70<XYcvUlC2Q6FKnR-g*c1&{#`xN_(<)=bHrtEP-F!)@+n$T|oXxR@4tDCEv_|Goc4w%obQ;J~X;xb<-RrFi-a^p2WQer*usv(m#W)yf&LG$b+-j+AG)G@au8dbY?7(1qgHD}JXewb^CM`L9TT&YMa5Jkc5@|(G#fBtII|Gt*I*uQk^O4zD2^&k{=XqCBu%S0Yx4UmAtHx#&P>MkIT+K$>4UU$Zw9lz7ORK9x9C%_xPdn1KO0Et2IPULfV|I?#TP;95R@S!MCA*kv^g^<0<2Wu1j>g{eSVy4?=1km9snKkXd+iqPB-LZ3xihJz##BVITaCM0tF=|yfF#Y0rN6h)2_DV%yXlG(?4CaH8e*d?sdGxzm42H(h>AU+nTEL7&z4nXw<oF*(<pSeafh176`AJ`6mkUI%xvl&dfV+p=ri7^g%Zn6pzIEu#!nXRg4EbOSB=E(!4fCcs2(fAvQH4qRFDQfuFPVd8BYv;KT`=tS#u**Y|D!i1U8p+G>KfK6|i2i+*EhngUNG2ciS^vzMLQ{z>TyHdvzIY8DCci{9ZSFv0v+MY;s@=ert<y6{Hp)8au|?NBo|WMnuw|j!g^j+N{^(dIirO4}Cfs?zCMvOGK-UulF)P768w!ht0`aZCHdlZnV1ERBBhKCPUNR^$-kyy9sNX*%~>lN0BpF$ZfkrNwL{$R8^zqB8Y-@h%yoItrd<J+L-cSOd#Fe&WoyE61l5+cUabWR%M9I@!<G|MhiPHj@qMW5w4{<r-IjYaO5pJ!y3EZI^B7@rnI(`@<`^lv$`xFt@YM&j#f`P%JzKgkAp&QAyzFQgGANCY%lG$G8LDnid8crzZN20t?v!SwOMu88LavaI$umkYtZdD{e?)+orG3KqfKud<GV6;6j9#eb-ujn5aeP-id_oVG5vTfYu&u7w%Z3{8iC?uWnz@YX6QEY&RRxiob9)QF`>08)L?IH<vzo(!ydA+LaG-G&BoHKnUf}h)EdiUXDOLGVudy&Me9mSuyxjon~p@v#XB2GD>Twm)RX*4++}x%S(4y9aqvB^;Rem!%+ie`N)M}L+3RSU9g7+z1IDlCb$GMUP-fkgNDDw1NtDS<tF!DzAgh28p#hA$47VP-jwm^cNugunVxJwaF>zwfoiRa%Xv5{#L4QsyCIVZnBy*zM?jsC<_;sbBSv_aVQ4{*mY&Wf7>nnB`hm~;DU!!(eQ)S=S%h*umY@QoWxQ=fvb!$~9zkPN~#YlbI3xmaqIHIJxAaq=u>TWXiI38Wk(1ozjd7MEEbL7-*7f-tFr71dn)?B-7N>18AL*Ez^(OU+`*jjHSpIUqKq$_&eVZ{;01z0e3th=WUahaX>X=*`MlelG)hSt`+$<Wd9N*kTIGZAqXn;qY-Q@e&HA8IYCE-o3{_esH1ntHP6lwFy@h!CX$Zle1O9S2AI4&fJ_!?ajHqP3I>Ut17<f+>f&>%`{L*6XuzTiRFJdMrx8VCPffaVCs7q#<$Lm|HQG(8T#(97@a(aOJ|b%1gsWm)fXqyV~^J6;+?|bIq9z`(?*2$nAn(JAeZ?@W(^jwUGX_Ki$<gW2?1c4}7ED44JViBhF;83`Vra^#c9a--y(488Q7K<&yhw*{v>dj>A1swYzmA#1YSFwJ2pUvSQC2SiORcX-5Lf^GDT`X(rxpU2NGFhTIOH0q}RlB&z#0Wnvw7R!6I{LbRT2wo|*S619oZK`|g6;FM_3n1FM;Q_fP`jq2Qzc!AKo`UF`@d;=TQ3c?hPTx|%Luaz>k@Ni>j+d(H@JCk;o*0B&TZ>^}gn$z`Tb#hpG_+&Se(WzFCN42VBSJt(1Q(Dx>_J%;J3*PeuthKRl)806f`n<KA^Yt(&fPFCL8Vh#AaQj2ZC<47@gj&>F&1>CNGSk}|oTlbP%Qpe@vg7M@R1}ADgbjka!Y1wGqBWk+qlt*BF1=REgGJ3+Fq=WotMe$!POuT;4GRIaww)jibY&B&v_>`uW8K3f8l6)Iz8z_jzG-VKX{>5axZIHPDpnM6JSXX%(WW|6wbIbla1^+F1D7X2T30&+#tmx-Kmgf{Cf-b04a#i6TS$}2k!r1{&3V)t>Rpovn=5<Y-OhHw%H1X_hf~Wt;dqetYgwOAv~*ORXtW`_o$b!|L)vmC>&=+%1k*zZ*x5G5ud6c7L?Y94yzy4(%tpl_(gD2HPH_abF^^ev-QOt|)|en`cU<=U@nO?k?CDTn*yAG*Eq3!UJ4%FpbzG^6i*X|~C%e&nGNh}aBOU44F!7c=vZt`P(J>~2`hG`@4Wf{*=5eJgXig3D!bus_#}>lSP$d00+oLmm+^@0{F=vNHYz>ZHd3xj)z0II6?x&<kx5a>O@Iul=maBy!Ps>v};S(=JEp{QP>QbLCaBMy)7-{)fUa##o&(@Y5rst~+)t=kEIgcDy9YN_-tzDwC8@1l(m%Gw&!j1V&e<m!1WVqp7d}T%bp(P~#(V!C-+o_t{9JNhjR$XnAc*Dtu1+&{0dJA((w;HU^*U8OBQ`gC6Ia3EUb5<df>aJ$%!X9gi%z+uVEWJmCl|ggF^jDJ!E4k~=rn75D>m?h~Hg7bOaBIkH-;!71MBYq--lXZseyiY^xR4&qbkwCClLgSQP4>re&2?6ImvvpSJ=YQGz{k5ixgM$Pz~WJ)?ohT#wKv1#;^1{`cA$1bJ6?DkSySDevKrORs_3oS(_z0Rm{p}+=q<vaw@O$Br|Z#XfFPpD^eEcJ-HprjhldKa>vm{#-CPOu#Ar)^^43CtbSqjQ%<g)iZSbZtm`j00dgCKuuMpp#ioLCfbw{1LxdIe&A{D&FnA8!ZoK&VZy*fJWdEY)XdyDE^W)QO4K?i-LEj2rYziq5%F<3@>;E+Qz77Y<2gDCFVf`>QVj@sT(MvbgdJgV`6)Yupn&2ttmt}It6v@tQ(>qvAnuFrg1>`g<h>Lf-jup_q8^YmJ>Ap4=6xTH}%@C<Iw8dIJ;ikLiEY`t(#H)W%1w1-<JptwCoE%z%$GozTCp+Ep^1xMY+3gtJ_0lV2**QJWS@78O6Hv%WgL}7bnrsr^MfCspv&Q^75D)mXG?~8uFLrBKB(eErQ^w4x@S?r87E)?qvwLw)WZsY?RH%Iq0Cw8WLe#sX{qr!EyW~CA?0)UY57$>(KtVt6y%{mOlj?e7Zv)N>nFzRekb+pk$@X=(T*4&z6`fO!UjU$7bOuPH?3P{`Q?G|S#wYJ$dhNe70;#x=2xI*<fnY1<}&DCkP&-a1AvaI;4s4RdTw6)mZRcq?BH=kJkf!-ivVY8S`9jcBkD*Gr2&;`G2%;IP-XjEIqqI$bZV0_#b>!=`0oz8JF@`72Tu=M!HNnF*ai8D961-+!PU;{`8zVC%}lhLJw9}O(T^?S{Y>~ik0)*wPevIKpo?WECO0AjZ|-rBC*qY|ER1`6PNld{rRJU*EpTv_G2<xwGtw0nBBH`gYe+EN5mEVPxW(%2ohqXvLov2Uwfp9?K<Q>`?51Jalsw2seq%k^o*HyTsSIo4MqG8gNVKDUNCsRYAWQ_~2)(<hTIka4)!Dafs71d~mD>)9i5J60^b$F@*o)}Az~%VeyN+o*k*9Tt3t)q3SN(h{R(oho}vNmkoK&1Hs8%bIp6^SH%Udup@Ox0D-N>v?t6OU!T;w)v@5ps?QEOc#xw&62|%few3W(y^rkJ?!)<(`f9;2(OaphN}f6Ql*BAVbZCzG)0SsNk}fik<fQTn6$RzP^?ewtHz`kL~`4+-Pxv!8j-bX6oz%JBT&o1py5t@j$VW;qc&F})fEYCwzXrf-(+Lg+AMiM6!sI8tDB6mCF|hKBo-}sK5-iTeJvKp%cke;q(w(8uL81+<DFSos?TW6p$1j8Siq>SwG~{f^5vc{x<aMhFDskMnsYH;c9(`ntW-=N9{m*`$HXQ%^lNp+;cx`-_VM_DBF0Ru_JiIoaLw&}*a-%BY?LR#vfL6Tb9NI<7sYwSw^X-I4K!Rj)M>tNbXs$ya^U+_jSvkYShU;QF+g5%?;-v=8SwnD)jss(3g8R&*1Rgv3bpL6lqJ=dkUb!4C}SAWg6(2b-DSpH9if%NUBIdLrADjfc!WbAn8cY)$CXag*;W%OS+<m++ol`Vq_T}Hr)4y^)IhFjh-ctf&oR5S;+e^~b96DOVON<N(<U$>932m3OKco%(_E45p<Ng%yzYRPt-iEcPspxkk9Ee|hMl8hnmxc^jN+O>qElXF#!6XhtXq4Vb#_g)ywzKjw(9Xrj4_=#!&moyV>qyrSQ}6G6>i7%Y8&2;0V0*-L2(L)yRycbt`v_HcYatOtS+zVGPUjFm4;ebZM1fS8w)eOv*pX2EjPU~x8I5*2VG(t$5Lw}wckSJ&fE$_kyM6gIcRRf$&74EbSMTDWD|yknwU<yo%+=2ik%Hd?^*FMZyzU1wO5thgJ3LrE5Yyf@S&xwV*{{@I5Lte;-*KiTmw^;sjS8Eg72@l>~<UOO=;Td0g-T#?6qcVyc?oZV%#p&#7k{u?34bGRGdvKW{-S5QHb?!omAwZ-Ux_Ed(^W=7~rFAsV<l+(~io?*g|T2Z@ZN!zFO@p>LTFTYZT=)WQ;Zm60lV$hofjUW@nRXabAf;PmG(R;U<we+aXwjrQ*e~feK8!MIFR0*`y~L+vwK!Y$rel1TH!A1+!i?R;09=1kJ9I7-WPh*0%472_o?$+}1ne1COkgc5FJM=B7CCM^mKY88b#~i;b#}DqQopnIE<XrXr4pN4dV1Dzmyf6(;p%rOc2LRiTmn-i}o)nz8LFGv#Cy2}5mEpH|A%N^4oG)24keS~l7e+lO7hMipjFNff%;Y@=@*%XYaTESm<ZFyk)TK<xg!6Ks;oqBmc(-STc9H?(PeevBC^jLJGvmdBpaUfb&xhgixyK~UE+j|sb<PZH4$lvQ~@q|xyi0>RlcwWqPP=ZTtUH*qsS6usR$C{1P=tOngpjnGCjgasSd-2gyeu3ekty1Tg2ZjJWyfS`oK)bnvpBzA3&=6u!bhC#@yIKl`MzOq`M+y&O_em^-F!eGVDH$;Q)9E~0|PZ(+M@`!zCO|gwHc)@;94Q#TxsmLAcI6Y8@ojl*oS|PiQDu4|>b|n`lhRn_u_dN;2{H+@kIHGkqR`sKTV=7meMt3+>+Z}(_Un|F&<ks7!ZK|zSzr7jz)iK{TcSvgn_)4KNiaOM01ddT-T4N}}Z!gs0Hg0pl+P4Uvuh!=)#2jpusvTDOn(0?M(V^I@`Mx|Oj^3fJEcPsR&^cMujth*Hj%$3`YpYsplgOB@1pVz8vm!n*X3O}1wWfVxgN=lGr4v|-9o04KZF^a@=pDMM#Er?Id1%)B{R~GYI9q6>YotnPo^Hv_-jKD{vJ#h-g}rV{s?54%y%R8KIUz(fFzWhXzN9&7U^grK;}k!R;XGGdjiB*^apbhlCf=&xkXeL8tc<8G?Npn@v0I4UeP)Qy%44$6^%YE9tp;OykIyvQs0zn^P$rzkemLOpXvPUinI^%e&AM^L6nL>BBV(ny!nSLY7;uU>Y!3D2sz%HLkr^ALeC$rG7UQnu!rG1KHnIvuh9`)*ZLvvR!DyRli<GX@4zUu3$MtaLmaRUH;yS5O*iMVd!E#cuHSIWYCx`CF_IrYB)I~9xPUahFv3Dv5E;^zSF+!TAUM_S@?%He}03W4Q2;0@<vMN>3G204j;CPq=v3oQ3bj(P46KgqJW1&fha;?7Q{YiDtj~hZ&$9H{%WGfrNjN47k4+h5}4Z{;qqdlA9T`KMsr*O50a+BGBsYQL60KC;A9>`U<H&nDvFKSlsZe7?+cg;bPaJyKjB2i;LX$iPH=c47j-}A)XYL9^9epyoya#}Sua&t}ZgHgAxvq1P0b=i#zv3rL*B;Be^=Pj%o)ugIOw4BzoEuwx$v8t*&mCfq5W)W*-H&ueAi46y|40>OQqcWuq^k7Jinyn)iabCFD<7JH@`h+TkGPQR`l&l_4hV|igpu0lZ=neS_MFQb|&FRcwy+0CK#aXEeZVrb$kD&{+3;6Y=Su58MgJUHz7{nDZ)5NOHPFeEiNw2!*oY7cxX;bcu?A^iW7*^ZUYV~4P9N@yagVQ#xur;MHAqa_0sP)EME;@)bTRYBKOKykm)EXv%x9Zfbam7gnO+W;L4e8f}VOR&eP7t7^73d@UFeldJt`g!6no^DxqaxG`>p@un%;tuS6RH!EM51nLQ&s2;gH=4&be0gOrjsC|wT%L%)2VAiY>e;6#t_8?O(ix&o#{!tif(Cuj+Pgkb?Eeh0gI@!VVUXoeR(W&CItjq!fMiXtLq_Q9PD~`sc{R&Hk1I2KiTnJw!28^(QGx6@wppRb<}JdA~;1@z2+WSQ#wpca#Y8g8+22j?^srDE|QR{Hz!_4tms5J*m~8124ad_r^L;i@Ta|AXENxs03joyrMuHmH>L4Hi+AddRgp!tx@6HAZuOL!aY&;5yeIA>1`{QPtJkNDd_=3|L7CpP^@<zOBhQYP5?Y-RNnt%;?S69+gwd2<EqGlbgYBr*YkL!Q*VuL?kr+0k4Lt~2(+<9k9BeWP4vQF&{QeOWl6JV%?SnU_NUvW@c5~13JCnXT9$Mi%D$nO$eP)eDg?E-YI&^z=XV(J<<G$RVvz?X1&6Gr~?RLh|003dHDwriJK+<pZk^wiy_+T2*OWm9U0v%K_!>Gk`e1j#mwbF{070q)6%BdI~i(KQ~z^oQx_lBnA6{{$Lnb6#FG(qNlrq%Qi9<acZLj_q7+xbe~)TtS|?L_W=?IYz5%|_j6)EoFwyaB6*3F<&o?d@^jHw=q)x6T5sZPr?d@%o_CDOk=O*+1@edq^(v%3kTWTWoU{EGJv47aoUOZq?Ke{BkrRv11a&wBwp(ysyYSc31_@LXT#Yb3{-{REBFKTy~K0N~^jYCYe$=ZPAA^)~T%vmA=^C2eue5p*Do?VZG*h*B>0{gmQ!yE+wO`Fzuoa5SEo;S?X*X^HETlAJxiXB22gTLX=kIU?J6;LnIOEjlSy5D#|YLWk+^ud%x*&O}fy=@P6P;BIrXR?GL=~1&f+CW~*hh+-Yf4f(KX_qAr4xQA1OGuh!;yBa(Rh7y%qb#ren{gk*V1CQE-6?}oLpjxQV2^?};f)nN~B>(a@KWVEd@9lnCk+Up%&9XY#wGH00J|0C)uwp?Y}^#w5?K(Hb1?#ys^=ju<swf^2`)EV>&p{RP~HM#-MO#OjL%(gVTA)*xUjd=6SpPi>o<mpCkFLIz{d;S(QgPOJ_6GXwJ<CJLUV_VIM1a*`De*Eq)S^G_}W*-)c#~;PZ1U}~WDt>6Z^Y<IWW^v$JaeK7QcxqC6%`Io!X&T05vu$5fatp{o21PUM0QHZWY9JH*%%Q_=Q86M_@F9XVN&oJu147%VPTp4D0(_+f%5o0w7*&71Y{jUOus9k%gWdKX+dj500F&2)>eODlwb;6F`3^we7uE;VQy2RRjEkzA?|rTx5NmsED%fA2NT1jd|1-;;2x<8k`5uUrSaJy1e%)vb?p0+4pvAiZ`)vVI{`eNPZzy)pQxlRdbKiEx<Dku;%%`>Wxb@3&2K@0MONRx}(0Ls3k3>`f`O)XJP<vY%aqM6nqGY&-z5+03q}7UU&@@E`5#`%b%lZAO*=HoL<_QS$=6V*1IKoQuD7#IDVV?)+=Jd`RR;t#hUAWwfh`;nplZ%L*o(>Xs!Z^2rR?DxoZ|&RUjJa9m3l>Bc1gGCg`;P-6f()pZ<^hUP9B^~kQ46pRwP51#`^&Q|q1s-pX?<j_e!^9mDKGvbe9)VjM3GSgDNjmpT1VMGV2{vOGO7o=uPUuaWk9GHm9^>ju_UibX`njDUGMH6s)shj&W_?bF8FfJtr#Jigx}g0VCd_K(;=Y2UlmD<z|63q7UJ090CSgSf8_0wkG0=^yGLSwE-u<#9JUv%QWNQnEu+S$W9Vu*O%&&G+X(!i)@Z~H9!SJTdViSQDmo~t+{U3Vnht+(`{CH04!*@1B0texgT5j`7Pa!K1tXGfo$P)+lDcr#6GW##;sVaI8(J%PJj_a{o>s?aSb?cx6Tl6EeD<OcT8=UW&FZoQCBKUP*HPiwq(W2lrUa%Wb1fn`uWd`H*e9kF8B~~nwn4n4?A^)I{OmXI$(xZ?E5gQ;1OGbaL6J4w1jj5`{*A&Xj()!Z0b{Ydeq!c;zUH5h4t9b=_(n=8IHrH<(x_Qg+$=ESQe!#moaJbK!;f2om>-}98shzyO*Fcr)V?*q$`xfmX;QOA-OVFgI|dM2)d3?vxHc*r+&9Ghi*la(qw6Btr}DD(fjYE&B$Z`BJNwRwG`ezwCv!`JZ$J&W&6HMloEB9)=0>{*!)mU5H6rhZ*~s=2XNs@GQnuF>l8SPu>6>SjPWwk9N*=`Yho%u}gJEU$K1-8YyUoux7^-<k7oU&9W}KJy>8m(u=lZ>-IswhT19#Vh6xBVrqDKg45)7F?ZtOqiQ$(^kj=a7|5tL5<yOeu$qdoTM#uWNj*u8iZ6_Pq(43)F_r>U(aRN!D@^vB}UwWD@S)CBeB?u#mrC(<ZDD9#|OL|KNoBi1R&K61EVg!JczBY};j;?Ff&6xO%zIgM`b)FsJ;<Rs{HDr_vvqMUtRr1Ts;J(Xo-lu1t17V+gi!!Xvf;sWRI9-;^5_eQ38Q}~f51i!Esf@rDH@h-GO_&$G5guke|>1XYpaGbA-5yR4|J2>uyG%D3c|6owoUC9+d11fkoLXxwj_4@%_cIh<VP5tQ6N6cLm8K80nn@O%x6Fb>n*4NLrlheZfDJHudlh&bB@X?({GoGJ8B^gYgB=p;3(Pr5&KuG!Q3|u#5D%-9tuq(Z*(a$Iw^FHKs8qO4d{mALmT4jw<<P=8g{QO8UF>T@ym%m(NKDy^8p6j+*@+BVoS?)(+9P4UZuk6?>^S8&n7m@NCK#W13IlI5vHIv*It&5dYS(4u^<m6`<Wk$SD*2Sh(fu25}FzJK?{^{g@A^kuzsv1pBbwH}}k$R5##K}f|?K5fGeGy{_hx5l}sjU2wub~n1l{FMe6$?wL7JD9*84C3W^u-AY25WPWMxg=1*-N{`O$NlpztCg2&Dc@*6f4%4{G=Tr_a3t8aYBg5=DO$d{h9S298)Kure-*7A(jDJBl`_fU}(da(td?c)$l8J(~5Q=z#`mT{KNSSHMfS89r~|e#UldPnMwUp!8J+f>CQ>CiKyL877E1}X2D=oQtV())~PF!cZ7(bp4q^EC570Ks`~WA&)|$AB@s8{R$iC9(id`?`?$Yq=zc`=ug$@HY+rhvpRTQ|@~Do}o<#&DZ)iB_5?(HQ-ioKR#$n}mmqM5fJn$WnC5nXkaYmy{xZkpry0;}40>6&zOKX!CvclV?DZ*vL4^RGgDPLTguY!}>d4=&xlEVAFSE8j7E%!^lzqF)C)#mEuPjof~htv=Xo8zK?X>_KR?U0X|hRP8?Wr(m*IALqck$GB$d%$l4%oCCOF9l6UCCwO(^l_zF#dPxbXZ&G+B4})!MY0}9oXJK+K$_dR=3IM{H}At1zHZ>b4Z*-Di~jN~fGf#RFxjAmg`uf@5t;*P(?YU;q`yujj9@}<nJ>18+I*u~n_po%E*3%E(uEbB6x2~jx$ICP<O}-!mfNm5%xqH{vOhNYQ>L#*pFgrx6U-A*`2()I;qd_p07{D5v($h8c3{Ve5nz7;Dda`3U;XX{?>0{Y{9+Vwc7Rn^qFwBk!K&P*{!y5%`;K2%C(v_4ALv3**lQD!VC3FDyY<!Au06aBz%A1WahZa$_>0}H4aJQu-yPRi5`dEgANi|GCe6GD<J4fgkY;*;2I=_jjAQ7&yTvxxZgqLIX5<zheTk8<Q2G8n?9&h8%|;4WP=0<)n#28k8bJQTz`kk#Pq>LGU6q8oxG+9qqMz*Fp%!QhxSfuV_R72Pqt@=&J}mdSa&-o@E456K#KuvS^;`?Wj&14zZeBD1Ti<wb+q}JHuN!zK|97c(rzZ9a<+RylPdM>UK2UVYdr1^eA1i&@&HAB?Pr;UmlcC~G57|M&7{Y2wM}Vhx4HjbL=B7ufEBd!nRfvF4dPa0%7LNB=(fn@#KXd+L%HWI;$77nD6Y=E7hF0R~hoYOi;rB3a<Ykf9lqWf(&>$<vkE<DMXd*gdGmoNCF<5Rq2q8n&k|8Dw>OARy3_OO9qo(`c0$yKib)MHLE%7D4B7b@MoGjxF$pA$7euHW)VLZ3I?&~+r1#T~0eUHF4<wk2D;~E>`YJ)2ns`Ev%LSeqX&vtIv@E?Fm<ym{<pXAIyW#?oqPt)bHBoq97LYyKEt6O}x>;Xhzz8F3Vv+!%c4x~1pwa($Fa>|hiiLe7H&JVTxjFBX-+yj53u)x8`sT@<{BtsrU_pcasjQid$dsUJ(p&YNCiIp4DY;1lU_t-6~*3>98h=Yqz_@=ou+dOi9g2k&Y88QJAIzHlVzfyto76sNQ!RW9zCU4b6a@9c=f=_>Fp^#B?z)tKygp8b%?gL}sBM-c;G4}Z#mHU0yt|@>}+(!D^7GFg<7^HtvP1XQygK%^kW%9DVIA}gf@iPNIvQpYei82ypkaQ9EKgFc_@kIoZzIBQGy517hRCuPM_lX>#=o-~yAk{Aqr9CsdK%}8V1?TLDbv%RVo{~l!NclkRd@g~+UvxHpi@jb0#&)PC`D~Rgz<&wAe$&UF3{7m~C}35y4e9JOOzz7<Y`0WU6LP(`4x2I=K%NVdRTS&P-&UQRO9K`0XCv~`(YZw7EQ=l7%m5DFMmM*GhSyAd&q$)bz|Zo%*(I)7AnfNwK=pIuBKE)|S{q}$ODRQ_4Z0(xp9@Wfx}`1e=Yv*SM1!w{4f)&elBg61DzjC&m@UdCYBaEuEq?A<7j-&ToWF`6o|s;3HDvn8khoF=B87j1rH4^H5-70sF@fjW@R;nI$ONbI+TBDLMk|>{M=>O`K5#-4@dA!0WJo4CwG;D<cIH^G^v)`rp!oe$Ocvp^jFk8BqEO0DW^^`tuPg?AziE8+w8rAOr?ssfaEk6-ZWx#}zh}~0i68(LfJ2i+f)Yd_7+j>Li1!+n*C}WCVsJpi<&_xtA28vyiD~_)06&*I;yHG@ua4-H^;Eh|=xUy|G3ti}w$3VZYqkaJ_1EDezsHC92#;QG!kjhg<-9u0h?S_uR4@51CookH@C7eACjU~<<OOD-n@qI6#jtc`0r<Z4M-)+T$2}_-e){AFTld&}E-ezIM1~nNli)&vXl4wfWPpa+XQ=2|hfeM6v($ByU-u6tCUgo#acJm2E4Oik4Yr(N6kApng+z-(=qp$NFNG-MTsTCJjf1r#gec%nQAl3Wz>5Tu56%M?V<#0B52{)6iOL=_Z<AI()Z610)&r3BNx)aW{%p5g!S++W{gFE|SX$D&3Q=}?o0xrFVZ<7`>KALnjlmZy{~A@$#h;%k)Z1+R=E5Wb^~J5ty}>=g!PDAD6jO5hH}cP#HH>Gg%>A!<gODmVx?!Ukz#$sct-#pEB&Mv{47*lyjg(loV+!YylfbG|LL>H-R9-|EVH>CkMUR3Ywv@|HIX$sI2oBe$(Dg^Bt}XOHwK(~I^%lk=1{JuiBS8m|-w;-()$s2ma*0;${ISMdu7%ei^gjj2zP!Lc0)?FAlc*>4d-9!(T#%%z-@TBdePHTty)AI(*U@k6UWOzt5B}0G1r--F=bn0xJLOP2qb^v&y;7!}vLD0gbqT?H89k~-A}}g*VBuZHWfr2d=x2vSzG3P_)Rn;r&rBb;rz&{i&BsegL0on3d;>fAM~zK@8glrF$J8#~`mycu`7NN#C5MlN<mcte_~&OZ!7vR3flAQLW2VuUuYYi~yL-!qH8TA<1UiF{LK#h!<hg-MuM9~u{H%HT?^2oTkW=)jx1UApd{rw^R#vZ~Lxc4S_*gxJ-k*DzP=AcvqVMokpM6&9=*^|;xcxaNic}tBB*z$6bYR_k&$VZKR#jdqP1P;b{vmtV`xCY(Q-;U@>WaQRI$o;=TEQCo*lD^;GXME|MC-6HDl&{_^|B!}AgXaWAZ^4KweM66k2(go5nxwtM+elx5P}Vk$5&_%zJFn2ZD>yfTjsBwANGBgaY}!ExYgj5$#BK+F*}<5YY;^_g3b?@J-abD*^$o?Cz)UI`7m$-UA;gPvGxfgpSlKxV79kJy7fS-viWfTY<C$a=TeqfYRsgBS@I+Fk<s2%U~eJ5uU1}q#YTn}#-97Yc?+)u%*bNd04>Gjbfij32N1p^t7wfh{HS-_W^|x7I=md=smJa9BYeFSwzWLhM^-_V1Mcv~;(gzL^4TgC4pfPi)uVK*YX;|h2F-B+bPF$-`;-!v(B_?l@1-@j)yBdMzC(zCBsF^vBMkn~2oWKE9{d55^xB!G_@gx$9+PhE6-7e$vnmrALe2bILnx_BCvIQiuw?vA?fE<sG3WWBQ%5$QKTi|Ci*($FuiFK{L^jcF5tyCm64gD@$m(C59gJXL_UD(66;B4e=@jWn-C>WtIX{wS=u2h7w@I|G=G=C-e~r|Xz5cSZx0I_aG<`i1J*<}FkqPUHvvI+C#lzv_11=OW@!W0t3(|SUUH2`)0AbE>6OUpB10pOY+-|Efmw9}Q-ew#){jM6%HhT}sX~-PGs)hIX9U`P9?Gs+v9Wi3pB}5yD0!IIwV2z~8LZ258ZGVw7`~F$N`}$ZnuOGlSz?|hGnjO<&t^8VG?<;70hx;{dK!zkUiEs!}$bi0|;9CVm6+e*gD5s~<_kZIsY@HWz+;3U-`Hs`W;6U(iY6pCq#kbR3!30m{p%*+DFA1iQn#Lk#DFriO?|Zx2`-5E<-X$oi7V;NM^g0<39|{}!A=+pnOhHNShY4Uj0GO-2Cbm07u2L~_{CieC^#iQ@YqhaDVPqnwz=}{o-K<f@z1@d5B!J&54$gDtdpvXbMH36uk4?;>dKS)E$i}2FY?mkoZe@f!O^xuU-Nb?87gRb2{I>qG2fQY77<i4R?m4QwLz5uLSE}l?#Q_WLhGxjr+Mr$3cRb>v)enfI(EDXZqk16lR+&^w<U#++=9+%U^EsY?&SH|0gzcx@aN(8tzj}*s-GTskY$tuRYw1^>I(P*!^c63Ef;ZvEoq24lXpwRW9e)kj##*t}f_bbvf*UFgtGw;t{60)f2*q3{8vaQ)E6K<FiXlpFIp*I2HgVRZl)Fmk2_dW^J0ZXN--b6~838gO57D^7KgDEso$Yi1U+J-MAp4|F&&;>dBj{QtWpEX>0yVZ}|7{%NXOjF36Cqdr3CHKJ45v*RS|x@b*0EFe(4L98?#+Hzlmn~zQx(o4+#$N|Q=7(EtMPrVelaUGkOv7p!FHhzRfPIW)cjE_0o{CkiG{cqhZkyi6e?Nbsr#2bz|NVWH(-?nMhZQp%W6@br8IWCfUSd7|M;XV3~o~UTg^4r{zNE<k<64-1@R%EnV)7uT$Ga|8~0%naTFuPTJ=GRBJ))OY5$v<V1B+hPm(mLfo=mH%HEJmts`^}mAxM-eK`&VNaAP^&cF|_LM9G8`GwGW8y>y#fQ9%p@IG4mEwt^6F`JZ9xTLxo5k{6Eb5*Rl{|YQmS()S$PjPoJBIdoRAz!QBx(mDaOp#98`V+5E95T-OfydZeo2JqHtz|?B3`tVtGJ;xSEnp>Ni)Tsim5QcCOUJ+PM`MH%`Pb7UTk$J|uS&pEn#w@hCSt}GFQ+At7RFb++36u(<M$_&<xA^4^u}A{xKFzHvaEawxYxq&Q2MDJ1IIM#lf~&o;262V|I8C-V9B2j#HSiL`@@29dI<F$-9D|{l=xc|0&LdrK*vzm+fVqmQxQ#iX2@LeEOl?0O?`^xDWjhRlSh*1$#sSVH?L6UNBIEen0IA1nX|NiUigJQf{jkMC7l+WBRrY2;QiS5B&rz>w&g}6t9h$_lnGFyJA@osk3j5#Z)g^0A13RJ4_<r(_bD~v>$9K}fa{Gu`9l`nH{SyG`YUgn@t=dM0%z`A-{&i#o$0TDmoO_r;J(jSt9rh_TU~^r_qJ{De9qc9A2x7eThg=X?j9-`w*L9ML04(EdisW>5QZkwu1@8er(7iex?gC**_<uC_GKO1gZxMhcc*&mvuIrU?Uh)53#0&K54u86c}>`GT_I$VFfgC})+{5dZ~JQIgBX`-^5I?8+3)Z(!7765w?lmGucM-FQ@c;1FI`l1r*E#?_!2mqSD}9*P*%P5uJ64qHKW(EIUs-F*m$lNGz|tFOV9ko)IEW}2X%4v<OEAH&@1Wr<fTY_BOqpgh}|EFEN;m%g_m?+pi<w8P}4n@W2ztW^w6wf%M+{R)qr(c1wxju^dT9@ujl0}%rPyFC8~V=AHN?&IZBsEt2gV(cO;0|_riZp1feVbkA)YBC|P6pR>JTQ61ZgZ*@!}jkFQkqb9Ihh78~65;I(250ba5DOXr<U1aA{Yz%7Eu0)ATWz)!xb3bSroHI`ND+w#oAAe4m<{$CYI|Gk|}!^_HcacU)jzCCe<kR+5$a|xHTbq&Ox6W!MMOw$oXbCdgFTUYEkn$)|lOB}`@dSyj7zeFW+_Ey0#JWD@RD0)DqSXKUqfmOvVewu8jWu&q7L2toVqcpotTn*e_SJ?)kBEC$PFS|UET4I_R!Onf^V$H-?z7G;h_|G6ZN+HV^Chk4lw|qiQOiwyOar#B}Z*I)xhhOrZgCC`8L6BCbr8e{mHEAp^V_4i2A<;^KUJ7Z+XRxP}1*afXZGmDW?1?pB$IA$nlp|P)%xGfRWF-s20=_+havd{u)1Q^w3ACXkX`)X&ethx>i9D<6=fRoHKm{g0jl|{XZ%t}?wz<eC=iph*Z-p<h1Q8p=>mC3}&0$7oaQC>Us1FeYB<j(%@xY@TP~>0m+bN7~%5*w9`31+|0!c9{iSddII&B&tECkUonW8Se5;tA{>-vx$My6Z1YY`2b=AoW`jw*gFq(zV4_M@BT*%f1P!>rE6`H86VFCG{`EjxWcd6q_@Bgd>3xUYnt3UB}Tk3*Xt8-4$69xJo`LS#HwYeIryuTGD6j~;fz2f(sS4l!&4NsUT`9_gwB0v+J11?|&-X8(=SAbN{v1m3-`;A~v=3e9_V8tA8BJXAQDxIyH4=Y?^IO^LAgTs=?Y3fnPtgQG#v(*c?wuT~oo27{mk0tWTdd0!t^`|pA>V|M<<m?D(F2_Q`C>XafiUh9*VKbnvWWhxNUntzKVUVRMLIxutk{Aw8z1enQrpJHjy>76Gr**^tR=KiAR+-q1tc~l!YF!+6ZvcQD!KQA1o?r7FZ_)zRJilag5g<-<%8GhEZPs7TNiSI-{_gHnbrC4%E%?ggqt==p_=R5ORe2qs2dS?HTs=GB`J+F7T>ybxfe+W3$j{dhTY$Z4(a^Y%$v<5$;y2ETrZ3eT><s`#pp<a^H&xv0>IXzKn)+Ku=WYsgW9}6FO`YDPCzL5_ry-l?HVlzVJHdZOO*M<BN3|?S=(HN({vi1RLm`4f3WNOCn-2aByd_gKzcMQ5)#zh=kM~31P2pZ#0ojvl(7%4g{F2sE+E!HHc_I?NIO<;0ozQv@(((u9vl@dxEAnv~=UUyzL5d>X)(&h685XS(yP$~2P_9a|Q^Ez`Bb%eIy>3dCWJyEUdP?sdOk0sk2^M~?eys;;u6TUW|HHeyLJr9k@^tFtu%*?-S@dHT&5OPcZtc&Pm?&=Fs?mLjVS|8_Hk3`R4)2Pt;JzqZsc=Fa$q6fiX$=#pSTA8wr;7)JdY*#%^1YncxV)BG=7=ua*Qqi9IE5qS#qN*9hUx*TdQ?qa6T<3br-FUk8kT5Idn(p95<ihXGj+#Qw^jZ6*In_Samr}%kdLATu*5ptdEfoY7m3x0xszsC}=;yw|&p&E>sYPmNJIXM52@5VdghJF{anA8s2FEkkjP>{5>di;wB0zmW0RU0-72*h5&#<L@P%AJqf#*E4o*iLSI-i22T~EWE@_YPt^053h8(MP*^~xO!Y+57`$6;$7b5#?2p(=yf1b1e<YoMukLWIv>OI9CA`mQp5Jeo)@7ZZfdqVDNE+n5NXFr?N|lE)`8E{_9skdZg%pSHLX*sTV9q-A@Ej5Q?VP&2SRmiqi%aT-yoxcI3&4|++LXQJbhxACKLzSSW~s~xrsra9jV=v!U%$}0^Uf1zs4s_vZkAcsQL^8PZY$$l6}Xf58kiwxb27LQHt=ZE)iR)%wrZY`T+UZDFYM<ob}bI$#HP8-ATd{kc$V!^#yiWF~sfilWyf3b#(9TWB16STI1=_i@~BGRs#Oj5O5BgUhC5w!>2I`)AiKx|~DkzMgv?hN?iRf~~<C1}1YSjSI054=JBSWM@5-PFFf{@d+zVb%QeJCvrzY;_vA0|r-dhy3Y4ie&;5`1FNIDw+MsRb+S44r%InM!9mQE_ZAlf_M7V`l+<sQ?lrow8D*Zg_;k=#uDK+9dET)kzQf@D~g`J=S@DefpvL1UGV;&!>_({Za-5y``JhjJ)Iz2|JW5~^c_|>c^iEKW^tDCX%Uh*Um`Ace8S>>oM|2lSf(lRcrcnInyvkFe2GD!BtFtkxl<Ym!<V1X{bOO@<3<4o#}H~Ah4B$)5FT31VVYM{G|+V#`-J?Y5S55#EdnY>{&o2OA{`_h`|l0C#=-sg4`B+|=2{Eqm7siGe$3Yx7Dh#!=zmSTA7}KqSCh6f>##fS3-(7nt8vpwi2Yz5mnYbBhHoOIPB{MvUh$ev7T~Kp{2gouOI6E(Rlmx>)ItvDKj%+%6%MK~uI$)PH+s17cPW!N<kr<Ahc|L2HgfztVP(n@^}buP3bZxHZ=~D(+Zzl~4<$X1J(lZ{`wPmr*L6$F@HLpoFcP*~Cd5AvHWbX*L@PZX{_R9!`4@V0g=Hw_!QmL#<0A+f?6J?j`sEz#gLD(PIxRInMqSg<#*0OYygM$hsX_vYK7m>QeG2BSfmTkxnK>+ueKVw8J!4K%s3&q|N9Dj@DdKu85*B^E{rt$!=WC7Ch93+FcIg6Ap|YvMD<_bLlKGeTv?^}&!5d<AWR@7qT`Bo}af7(5p!LFy8@mr_T=)IiGS8Zu6ifoi{nLT*7XhU*z4s|hlMpZcdq4cs&&*1;=P5CLo51Mp?rnbpn4{mKp8`ZJBJ4pw@r9ql$mNmsFd8+8&p3aoW?KXa)#e>1Q@$iaBlG@(2|}2Vh#k=1s+Os!cu!u=H@YkJc!tpg3u2n)7s9E-ZWDHUj4<Q<I3S38wyl8NFCKji=!LrggX5Ro>#sA^m2Z1ZX7Zo<ttIRT{zasPPo^gtV?xE~e|j?g)Yw;1vV!`r!8zc$@#opNNWcB;9r0JD>5bzXLn=XN(QpE^+mVZT!;^W+fV8);CU+n##)9z7{PDqK=>KN?ypyCd!Iy@o+hkwkw(XY%0MfC?Fd0!Jj`b>M_BpXr_r4eCiCn-{^3l{`?re_^q46pY*Yo7Iistwoep&U5nz_uXC0L##f%oOFxBDAR^M*a-IBTAhNpQ3tBM<E=xsphl>FF?N)Xd5KX8~H}agj|Aq`Hd55dzgc2Rhz=TgqHo#X!14Ikmw6WDTAh8@n2*vd++0|A1+T8yUB1Ap5N@F8xeRc(Xf-Mq&*L=%YV$WCkGYKydUJ5d}{yP_g1hQu8-Hcm#P)GZhl7oL&b~w|ecggI3pfW!IW%zlZil^YllJVwVtnHGkU{=g8?t0h?F0u>vYI#F^|jV4sS1I1ALZpFU2x%>Rkmd9=fO#w-+ws_!r`&I`+4Apq7@-TY4snSI|R&9+y}@9y;QPY1H8qcNbgj+FbUsOh{}P)Ec`sH>fv3IB$p#dV9u=1k<xlOe$sN>x!K>EH(8wX-CQ6w=iMc$N+zP3+E`auBPZ!7lx98Rm)>$-j~*@y%_1tO45ATW-Y5layupx6$c0wLDDRy54(nO?B(dg8Ew(BPUOCwUp-ZHTWDxCK&RjVCYWvPUAgUy4Y;a3xE)<!f8%1@ZkB=fpY)fRIFup7m<E3&ge!G#(lTgm=HQ_yN8fjS6>P54Pxf-^|#HKimc6$ck1~bXr=?gP_qHgo-Amt`I8oVI{li#!!%^mgEgW6e>3UioR;)u10R)l*$B;NHoVrKJ87Ap_~t&(lsxbTb4w_bR+lXw=8}TzGYDFWNk91%2u_kwiTUNWlUke``zV~fl-qZ^_W#P<G~GP^66@HluV>&%kN=qmK-0FU^O3fE-eBAgGoDr9<nic)iQD&nX4QHxRE@=Vf6X5OpKb7y!zOv=D_(%+nn?ob6O$mN8tdzTfep2S{fh@evycZh4h8<`M!;#W?6{c~2HD{(0j^fXCgXjmT_;GVXtMII<7OpNm}c&ID7~UHHX$O=L!6K3WVPtr&@$9N_Qw#DC!T%iz0<$a`Jx2|=4!*_%tAqxlo2*gwdqu6VVk@3djtJAuPn)-Gu?P`l6dDO)mg7Rx=pEgOqe}~3`E=C@E`;cd_*Y?z&5;duGZj{`<<<S>Q)t4gYUim3yu;{{Wq6Ra)y@_2q!(;XNfTLsfUj_Z916T71j^Ow8Dc6y_g2TcP@Ob)(8I^${=*eeEiVao_2FpK;{x#*RLzUUjMYk)y+PxLqlDBY`yt?4@;Kc*B}oa1}38h+o^J4wJIfM-f$BZPa%5BAA#XF#!o}a7ZW=DY^t5=iPsC(UO7@=%Je4RKDS+o>_^-m3riIWMtZ8lDWQRc)R6c~1k%kd!LSJ`159E@$B6siOr5c*8Jzr#m{f0vra;77fhNKqQRto)H_Rgk2d%Uj7qgTjZoQBnf{S(Pe|MEt|4re%E_gp~@EP1^JL!rb1y<IipU+|CV=p91{al~zu{}0kz3!?-HGE*GqP4!LR^yz$;ysHC_OrM!D?R9~c#p`a!K(KHOvQhaGc-2G%APE69ka#dl7to@_aw>n3LXc%?lXTUc-&=GxLod*e;2Ja+D<!J0b^bCO6O=|far9yCqc20;#-7&uw$CkPTNpyN>bqdbt;u!?ofq7vsqR5B2!L2iY4}Fpy;7T(e}lV>9ZoekL(are`gvgsN72eXr+kS9;;A7OlKxs#4N+TTHCwma;ARw&z>e|74_BeE&p1*BwLo8;%vF#Qyv_I)5M3{OdOAQG<ts4@iH&Pn+gS1@g50I-l6^*pIFEQ__&O&2MpcA0<^^9C#*4+i7%f^mE}$q<9%q_u{_R?|AmQl;>4J*^8Fc@w$Oc(T8RrTFzD;G;#phLRb_FuD(vM8Gmr$ztOGAk@`pVAWGLi`yq1o-5O9>|>3~|RE&7x2QV<=DT0&pEtN-E_c@59jv>e24ti`eq&7HnvV;?)ra&EcE5bQT2edX?C($q98s<WmaySwfH96pq-)eZvGpQ)~6Ox8lU*7_DZ3%_^Aqc*GCgfj3CEg-SN*xaK;>$6sB6i5#nSyyTncyz5S$kf;2@?6I^LKJ3G!#15%Ws@HN0Gk;0{+l7^np|XooioYDb+XEIMBA1?x|))vGK-M^Myjn6h-*(`#kLot%^eLDeYHgU0r=T{=wPy%AHwa*yS6r^(a;=X6enm8<tfD4<&Qf^cw8gzD@Fv#j?_aj(oLhpc$n_3BoF-&^1p0%SrK^LZy?8Fm>TMmh@0laz~-Az&<9VICc6o#hE*t6aQ;Usd*o);O6b319RPbcG#EE293d!q<egO4QP+E9en-`a1yPS{<5c)pT;#Ep+P`r`-BMN2X}a80cSrOccF+$X5DKhZ{_LMEDLS0RtD;{(e^SV-Wm7an-V49-SH7>t!8rPe;%V_(ZIkN~%;UXCWqdBVzwVctQgTnDybn~M#Q?X_Sk7AxXy-={DDhK~Iyw1T!PMRZRRl&XYZqxBvXixb4rgee&*Y22?yZHv6I>a60UEhlTTvOW%23vKx2nI;<FtgOl+wLb9{kWbFE)HeWCa*^k*z&WgfoZ6;|#XZ>W3IWCV-SZOpw)TINRlUnXtGXw3_eZgNN;keG^XRw30w3WPjW0%c-vahZX~W5jG9Mig($LWoZ(h@%p3WKulg$jO+3X0I>0r+|e3^uPkK*!Lu<=->+dh;?-E@;1i$SO-JOqd-|i+-4!m?OL?ovsx+F!tMTt8A0rVYlEM#H0f2gMoHFP{U@r^Wd6jE56cDXO)z4343?0_lL8z5^@m+gc@#4upPGx&}7Z?1u5d;ji9d!hdT;}V>zvs8QPFnqYR^wy47RiG;hzxP4$^!Akuk_~dBWTVC&QO=2{G~WdIgM0AP{fWv5I@8}!oo_gyU;wMh}X359)M^Kiy91nC^>do2|qsa$akdtm#Dz+<p$NjA;2;p3-gM|K^sm;qOo9OsWX*@>LQd6izxJ$q4gR)AACcX#M_xAIeCc}WJw*Rjx;Bq!Lge&<h;5C3BQ8048i8Z0Dq}6cEF9c54F1c5)wac^K%md$%3aC@*#z4EO7}XS$|c>%PJiUc@=i)zJkB!H~dHx_(jc=Fn8Qp;mbJg7%cBAX$Ko)9}zDCxjesrz@)V=@&s-X;KEP~*<!1q-`EMgJo3j*C<ex)6Up%`%Ny3%fV}@`I=_S;WD%;+z!yRg&`1F4C(PECHpz0k%Lfb>*-*_~77)hu{(9wxG6M3%PdNpI)<OW=3ZEvbz+v<g3UEamNTYjv-c_@Ch~e#W!x&|8iw1z?hA>lY@reZV3mL0gl==K@&lv%V&dY&t$NBy41M`>ZX*gQ0Yr#WuMi-^c+y+ZVdcK40qDw$avV-yGFkoAM$f2agH+5yBBlS-+1PI_rRvdS!7VAIvcw4U)mbXP-k)FL8^o5AwLCe!m{uS*#YnZj!&!B9|&jyr65Fy4{e}aX9!^HuOq0J|E3k*c$L#;^AgCzZ_>R7|+0%MKQ=VOaHU~R7*C(_c)0pJBNVMVUdw5ihD(_imF5Lvo|TIi&dEjqrUMRVYG*?YmP*EaniU7JgGZ>*#Jlr8Ole!{5#lKW7!q4ezMmGPXje=a8(tchv#u&k}?>Q9nlLjyr=7@_mO65lFyIqYYEfxOYriT|C%Z*fMg`Pc>mXmg4eKTASGqwgUc2GjMIH0&Xk@LI}cs*uV86_AAN+Bg~;pan4Q<OwKhb+-k3_l{49z5WP);xdM1GLwiW42Lvi+|QV0e?Ijwr}H5Ea%9%v3d6X%_0J<L+lz~zmg95HqPvlZ?m6BP4f#<0B*Us8s$G?RnaBCojE1LqBOA#7zc_-}^~+<VS<bTQUg1Svhr9P^`ld=m&5`g4s<k_DPwQ4w9~JXL*t`Rb;N<*?0TU%jrj`i%M-JjKsv!0bPq~@5({HoF>oolM>**m6YJi4m2M1GI@-TWQre<p41@$Jm!Z>4GjIe&L{<kSiEF8)pU37t~)k{~{Y^4hRiCktr+E#=?7<g@K(}ohYV&*F!GyiQYT>NVcZT@SPX^;S(whKdxH9p9L0Ist_!qSb{DMVa=$nmF0%nwNjuVCHd&F$7Cz{+zdB*uZR);mb(C5AQo0Cx|+-x2?e^mk4cyE1|F4{nh`G`KZL&f?SfBdj3+7yTS+cOw}lhpR^X7+TJf&?72M1L>xOYbzdHfF6r6K<RMjd~dL651-OC@vu{O(<jpFWFj_S7pJ!WY16-4BdvI;y4N2mVZKb;V20L4?@w=lex^CzJ$fx8r6duWA3!j|N`XkR8%|<#gS>HWR5+EYHls3apwJ@o|Eg|ndu{O;n~MchO}W^>zaw0?oX%;C%o0iop+A|+sJ>YI_ofYncd&;Ar#1#kTAB?4`yH=ihF<ccNBuXFcpxB`nDK19gS<tomGTk!4}PlnQ!iJ0XFJ#JEbzC0uN)xV8bPZ~sPLDQy@1gA$_Um42a9oQaBvQhTE{?V+WYB8ga@dSaiTA2pTykcVmqpLM19K=j1ADzzIt4$w?2Q9*JXxS)X?bP%mnwt3u0gCu#V&=#u|}p(ZbF=#k*>F4#&dK{nv6YTEh>K7y&x>qs*?2fl-VQ;BZfwsu^rxl|St4j`M+PXl}4En0+Gq{30~~{}rs*b^k_d@ZljyQt?e2>n{;70@bIV<LA5NZi9)z5WEBCPOrU}M7<!y)DU6or|gAzYJb^=$nQOVj}2)FmXYYWfZIaq@B*_c!#(~a=gow1<6N2a!XjDrD5TqXFnwT?qJT=Rm6ac`=DQS27$9_rioauYY>#Z-y}^9QwA>ZIODNsAhAzTOxx2lUhX7*5oUsEDXIqQwZ-#1HQ(vJG8DMK4nc*yamlEPk>pEgLXf+Z9T=6+obrI?|VcP_*!Voj~Y=z-+BXVO1<?0>2`NW*31UY=(cs=8NRw~YhpQWDOZ~a$b`DC6Ja6NuodpA3acMEE5(9V)XaQaY2wGF-s*lkN=Q4yG(r&CfqH~ZM&wMaEY1J+hTgzpV>o~Jx_Oc)9qyKSJXKl>mxFlJDHowZf_q2QX0;uwZnc)LwSaDZosbQz5K@VwOJ#^2}EzLzZEfeqxa??MfH$8CRQv&3X5$;+QezjpowyznQJ5`mLg%T2uvy09D~vOmSN<s_O^b5xYx-UtV0#vgMF9M;sf7)Y=i=j_O6OHw%k9+@#e0}1Sq=3)M{x-fQyZO2cueGxqudz&Ithl@t}=ZQ?^gpo&`scQc#+S37z_LIEWU#2;l-Zo(q-{JX+3vq70I^hPH2vgj3vSkl(xlR=rJJRS4ym?l`&nb9t8I(v2siousKa+o?6}?*fWi^3$*{%8cH|sGSvDb)n{j&<|(4l$B#guDb{4NNZ>9g1RbkFm|#Bw6s@u{8gIZrtojOh#hCpn*XfSb@~JPL%5WaFc@@e@ys>Y>@vuW6?#QT-j^JKPN%{2fr4%7I>gG=p<NjN3GBGFz^YVds`e5$$hz4LjOo8-3{_WHh=vjyPny<ok6o(E?BkD#aamjjNkt&P3z};Lyc1U*%t}kw)DdwjIRn&UQyVY+W%5Nmnt2ES1*akuO}%0Kkr-H!i<R@ohzqd}E5<e|pD5)hc?ho{5VT1cdI`%sGIF2b2nRhLP?43fdR>yHvD)DRBnEjV%6qhse4L#knEu<{jYpfemo;+y&!7VpmgOB!v|b05MQ{jn}n_y;-1VJYSYorDRojG5u8`9}DF{3DpaMvbd|JBKS|ULqqg#)Ei~MfUQ#V35n*DWHoa4Uq1YX<ugiy-sAj0@`NvD3y*H<@LO7kP?2?3*ns<wTV};=c18J&K|D3?=!|>AYfiK+Q$zmcL{4qnyiS4uqfSiT>kY^y`cmLOUF;Sq^0^0k`fXfhyQhzR9?1go*fbm<`CGb!`G7XmaIdIK)1rQ!iH_655veLIjJR*nrzuYW{ENn<ov+pWAbya1p;G80AlmJ7ODSr{Pw+wQJ7slHh$<6+Xq*a+%y~aIKxkiL|2YdcX)w?AH`R2q@jHrI6M<)$E8cTCJW!Wzt8c(xqmANagy)Ux7jxC_p{Vm*D>3uD#uQTSybF@7fFfp7Atua|jZdXEj%<g{ph-4MmrHCn@sGZtu?u09Mztr#*XDz{h@`q~%iu=${@s<P=NJgNwt0^MgoqJ)`d`3%nWI~8r5o0%udVhS9?xJ6q%|i}Zi4O!W2)GJf}CnplBO$l4;Vl~gUTK3TRovo04ceFXbBIk9sXgUKjF0h0K9HZ2j`Vb(2R*@bV|oOW}jwg5_XVcGM_nZf(I6Y6v^s*kmTPpVyF3#MDqd?s%l2Z9Dv7>Y-`NeRWrlh{c)==pw0BR+3m<eijcj|$$Ag<h*l=kF`FET4d2_7QjVNr2pc%09j8}#!fgvb5sg?YBD?jAw;OD`eD%lI;O(=L>%bMYXC4WdF6l2hTgy4{SK8qX(^MVZVGSFH<zO$lTVV^wqH;hg*k>>6(NPhyOfgv4fr9k&0^#?|lM^I4@e}rf=<NqaS&0GtzFnK!tU)-QXtaw!%_*-HGyQA%SES|OQk}eA))FUI%=48T8lFn{#KeC)Hg~IzeB3J-r<eN{WrPBp<{!2RB+3s_IU8tXR9C6%$H-(t<5S-&K{BHB(NFLJ0*yZXDJCd^@ZgxojOjb}{bILkvcAuJelGI2qO~~G^NQUbx7d?|ZznUb)9MvOf~JUd7op<k`h?k+#Mkg`Ai^UeeCDl~4!r}bF;)~Y&0kK08Tms}DHZ*UFo$OUN7QvJxytO|2Vy}qVM)$8vja@dIXwOKS<HV|<C=2W7+U&5OKN{u<`a_8kARN6vU!mQh9fuzg>F6a7DQ_<$kAu{H(q)79yVU~C;t(1kd3w%{EW{;C}8Y2rFy>oo<<6d`~S717$d{8RP?UoIadW*A=Pz1UrCHX8>I8dke^G?y`9N*Y7<S`=Qj;SbZ$R8R8ZN<g~zQsqk3BSN>{bvTJb41oF24&7?T$;oAvLXBRx(FxzDd=w`N%`D1E6(oei<Wc9hB6YTe%W)Fa>tbYSSP7kYf-b=eZoFdfRxdoY3)F}~K0>(whZM`44_hWK>7yEqE#={6yFf0OnWr?WcD1rNjPQbI}7M!Njv^ST1xRFk(_fdGAguy24_#f7<knLI*%G{vJ|7#%Nu>|WI+!btOzU_myZ*sgZXa~NiI^sr9w#MVE+XE-EjNpO~M7}rU~`Yq1XNY}8phzjsHIV9yEj$Qg+quYTcAEV;zi$AnXLGGAJNjo3V`Z0O9>_^$g(v}y|*-6Q%<yCfSGq)=KtjEy!zzqFUzEw0d5}%dIy<@n~)r?4YR74M<lCAsqYc)-1fL{S}wkXI5Zf9!kCQ*UZHdmelw;oVZz<*G`KuuZ8QQ{w6sXzPza(@j0FDHDS7^C=~X8d3Pt<BdkgKOUJ^RYF#fKxYiyk<e+m3;iGLT!+QdY_@=V6{oIm2P?6t9+rT>@k!_Y^pXM@i^%zgpW9F5H-AiexRej%`@~N+y*1ZLQM6Z2i8{AS2%q|FcG1hXwR-OW^S@WC6Sx}qNys5>P6*i9blWyAw*JhZVawGP0L5#KPv;-_^d2H9kMKg_XmwtlmF5YyG*{oO+TVdLa9xMqfm+GHNf0KRHi9xnGOp_{i8=#^yAB(YIm`|vTO{@<5$`-{VPA*d@2g(q$%&u=GE-zNMhdp0pRveiC8j3$N6JV+E!@BJ|sGk&ymlf60>^@x1oe%c-RV$#!=SRrhq<c*CGC%lStA{r<mnIB<YAP8k#KR>|%)E(fNXW<+SM)Pa%%s&!n@EOm!pO-gn7+rodwkzOWMGW=ioS(cS+9#`8hf{dk)$Pcqv2=+!~152J||F^V772g<|_<Gj*8HG|j5Vz+WZS0A`3>?1Xlfc&dW*cR4FuXwm3l&3$vD1)B`2x~NiRirs19MNTOR+w7Hxyx=BggAj;_;h)-xYyOfU^p-In_rMK!9+yuSa|c~hAFWLxn#X0?Qwqp_C%!9eAczzC`G6?D-fUQ;+FU9BP(}**Wc$xf5wbF*dPg7zT!?0eLd~n>T_<8B56`f!x1sTo!oTsI=}0|uxs!=&Kom*8yrXy{jbP;s71sHXzs#zwf80Uo=qg~Wnm0F2uQv2OCcSg=T+y!%8yOo%A0<ZkD&6ssoC-v@doyE)1yq~ltktyD%x8rK8Y%oombygmO$v=4GgW6az8DoNA@mcgl@NIZtK2rr%db%^W^2`$8vY9=bS<+VhE*58%vJkM+nOBTQ$UV!7>gZuhv?u1Q&y|mnr)gyr|SG?f?t~{CyQ()o{d^zo1k;da!$kIBxP#pI`9wq(vSYN)k?j+SU(8tqlyg+tSShCD2%D;DaiZ+7H9q+~m)2nR(eLyQV5_AE~!sWh0b~73PoKvcVQ`zT0N#Ehj0uH0(Lr3sXAfv-<^@M#i~xHX40MH16$SiI`@*bz$+2?_p@2DJ-s%1rP^cMKKY4T<W!_X;Rn~1VJ$;S6%zxe0D)zIlvdG2$nf4`#O)mDxXv7s67ipeH*m>nnEA%?+ot*4V;|RBYv{E#y<*_eKxRPbh&{0v0e;k_!`MeyvKOp^(KBDZkVdv5&i@G$=L=FcadOA(w?`pmh~AN+v6<u6*HEf83}AbN`kigz`*oQ?pTjhtnjm=H{x7sU)B4PHSBrTHs8fkln$@^Stwlpy5kEoBd9;wow;hW5N>OaS^6bCi$3#5?ds+Ttm0Y)<|i3GfL#FKe%#-?a$J6v#%|<%lqSs2_9HQ45OKpQMao9G<Hrx&#EA%7vqv0-YsCY?|2(E?A=Z!8J;L#=<ySLUZlKRqEg$^QivBqimI*F*Z$t9NmF`}-Kw1_2CV3O<?Xwu-&tYmc+9Rp*?WToZ+6W=6dQJ+bYd#ywoPX?A?4Pno=nIdQT|(*d9z>?uUr+}(Zy@xutMX(j#Md|zLfOm)mbbSCX2H{X0*0yi^lrHufirpxSr`;pDK&&H$XOrbNN!lMvyVUTcK3wp(<(JgnKJNGC1L%&?B6n8QS+4wt!Jg_Jr*-#ZZ8D>8EL|ds$+3Or6P3Igbas#T21K)VK96^6SzcYSOwwmn9*b;0MLE!ucJc0Ks=5$4<=pL!qra;J^7QuiF55d9sAY~LLB*RsDSS^t1c14?mTu4POrsMDDN>((Y^;<GO244H-<^tj{yT7h@nn03$XX*Mg7MEi@gkD^N{H#FvlDNN@by<^xfwXd6>-j`ko~+?<=YuAmVnjG6PzXi!#JHVMq<bkf|}}Wx9l|04P53$#;ArO@(yk{xiKJ!I<AaM;ah(3MsLBnefx+@Dcpxu?l!9enK>aKPoHfcHftkdM&R1nHC``m#$quD-mtilL6pcizh*L&xd&fSzgBeer?Xf?#iQ&?w49%>W>Gar-AfGVqcbPp?j0cKNyl&kca?4p7#Ku^cuwb#B8u1f&~S(LVi!o&z=LUt@B~^7N!~Q%_p7}DlQuzyTd#y;eSJAQXhHKTbBQ7&dlf-R*ebQ*lP0J=BeFt@FT3}7L)kz0N5xOmz{uVJC?H`Cvhr;eJD0Ff-v_~hZFr1!{Rq<={bhZ-UNoIuD)c!&NdTGGb6YE9Y$bDM8>0K%V$BmgK1|4GJgXlYlTo^;uMS#0mBBo56glBsfj5fIc2EBRc(-B+JTEW@T2mkmsk>z5UUrR2E%+nWCn$z=O_EC^M7`hISvB!eyBb>xm=NRZ+X5m--`{2vT6wH94x5}Sr~T1eSwFO6}8}Nl;lo^DRe#<Sa!d$`mmK%+0&nbj%E+bkoj;k$XdLKMrZ3Uvl}Q0ZsGIeFoj!4fU#TE$&Y1V>tmmhrl5YZf@KU2{D#@ZP5tc%KXG_~@0Xw%7{}S<YQ16VNxMyM_OKwl*bIW4)nm%NbjhsQ{!@)L4PKc0`Ea5~x9%pbV?Z4Kv)5nwoSx=}FB~2f=$)1CNr^_V^f7z&Pu6us1epTjQIWf8%zmH+X#fsaR2CxCpSwl-CjOW9H{!42$8Imy)>hI%vqw(o7MbVLLcye1c4q84iJsX>wsaI97gM~_g}mM=ol2>o;lOJ4_*C`e+^Ag~v41ryJwe0ghNn~)ikn8DyM)<)l+(_N<+DOP(hTD8d+@h5v2|IR#5e7svSVwzJ|sGZZpn{jIv-6cxd#hQ+b~iw^X%!2bfYCGy`~Xhve&g5Y?(>s55HvfS#8kq_&W!caDM=YU1Jo~$lk`Qj$oh_3)tsmOpW3p%!3?*xAq0{PoT;0bY}zGAne!k`2f~-4j_SD!!Gzdc+f!8R~e|@?QaBqI(?jIa&Z5uiD{1`{n_v*B=c$SMw9c(EM<C2@4;pyTco_mhXR=BMvhFSTz824mVBKr1-{7jPWyP0feO}biSQ$Z2i)@q-7=UF9M42?<=A7;UnSjO(=(?YA{7>yReVw>e!R)6S#bxaOK&H^C5u64LL3cF2=vMy|JMO9Z1XB#!os2l=X*hnFMc-_m%8)H(Q(fARO4&j;DjvAjrp&<O)#3hcz)MZkBg$f=n7KsFY%Go{1u*m7EFmkilMetd{hvi??uQ4*<oD<hOmJHqGbs7R@FP4;bf_~raUiKN1@uOIiHV)fvr~k#g(=e+S$VDJ5$gF@}^#PpC+{MNGqER%{1;aZIxccH`e-l!~29@jew8+@-p$oZidMT+8mbeZ9>J>-pf_gIJ8GJ?j2)?yWhg<!#{-&vqHDNnWm`TyG72ix8qo+*T}R~#OzMdtIS)Da2yF_iMEZ#)SsB7fiya~;K;fpCAlc>*H<p?9zSKVhXZX4bqNdd@-XkRIkP{HDY&!paGgr_KInHpY;c5}CiziF_hp!bQwfFp_DWnSFHxtlC6rLw@3t+!`S!M2Iz+U3Rj2MxT!L6DlS?D^yFnY2GM`>T%((cdf8_$?1zDP_hr)!Bol0%6q+R)-%Wr)jl==hvGoHQe07;oHFr(6)Z@ENj*>t!xo?pk^s8Ig$m3ytJws~{=3z`WW$`p;2>@lJ~1AxDso|Tv~HntFFOQ|qRXT2z4cn_eFF(ZWXnPb1Qm}~iM?JYO3FH*ArVfoBXcWI9ENFlO_s*<+_bWl4^d<o5g8t&6?BUy5W41&D%S516h1T@=Xv3YFbXK4XZA~tg3iu?$2J*y8)O~em0{BUND5S(qHXGyO9e8Hn_mY(WUM#~5OQe^+%T-ga3ORM+%E@W1=-9k6^z3nfAPqfQ405DF|@6Kb|p^$&3^y~;tPr<p>ztBSj>-)BIu8D#*+^&b=L?dNC_A_wsPAD%<#n0>VL-L*g^@bplu$t^vTx-!nnUl#MyOmht>D}(Ztr<BDJ~OWQq1DmYnUZh^)r>9q$HJ>tu!>_iY=b>Q4n8c|0ukx4*L{Jf<KKAa9itZ?9-+E2xeGnVR!!XARycGM|Kh4c6i6Iy$fCGo6?;(QkBj<tY%1}r_FG=n_lNwl1MhB5yLwKuW~T5Nv20sf!h1AVA0s40BVOjqZ3V>yXASz2YCPS<sBNjn`O+UbGqrDH#&<Z{)rbyioejb7%5}-sBIBmHp(*Rf`@UW77}@W?iVr-wVpDJ$kE~%vJPj-&gb8F(Shi~2%96`A2Ib6zveFaOnX>eMd-$-nxLuf}E<+Xh;VC!^@v~g>Z~Ei<o{~T#R(=Zr$w*IM#Op^GX$~-%tua(JC=%|dyY^v%cwHnsbLcnWjc@z<m1R|+Z1i<hX@AhjjOrRhI&U8R38vVrf0<d9O%%<H(k!8Woy@4H5eEYc#G*2>$vv{ykEamBF}2bog$g6q<I@*RH(+W*MjKn>-us$%oPl5AMu-2D$Rq<V3BkX(N}6x_eBn~{deK02=l((;B`S_yKI#E4QwNzN@=#YoHAKvjzj6lw4$W2RR;?5AJY?Zxu>B3YH`CL9r(bpO$O3AP{GHdx&61QD(gKT~vnFLBy1M-IaN~Wj?WaV|GTR!H7{Z1%q*|{vKI0v4EI0Rz8rEE)liZL_uC5mpo5slTu!EbYJbh(P%njU1rttsb%3I^&JQ!oA*QFU`{e2b@jI`07i#j|0jsFj`j*ih9fJb8eCVTSH>`Euctvr$}Fz4O|&?#9xGcV?4{5s4RXE?b?&k3cI072gWkH2%AJCqdk-zjGwy)=ISr~(Pv3=owlJThl}nWS`Z&%Zy5Q&qU|lb6?$`UD$_e$7qSo(!Ydg^uNN7SY8&g~#RA2`VYL;ONy|!JnB>f>(9Np8v_ebN8uzL$OQ22S}dRKF5uhdJKxL`azodm3>E@_}$VD_m1u)IQO!v67s5Tp8~KYt5#F4YP3VMJN#7E>@c%X1yK5z**{E`T!)Tip=z;SknR_t@DiUX5CWy1xC3lyT&tpl;)3M#FO?7l8!lVBYqAW(j!E-%0AU-D54jP*G-3Bw+Yo(bOWVX^i#ROupH18q4IN)PB!BzIyHL(GbIh(9w3D9%)BO7PXjK2F!I}Ww7Ywn8^yZr+O+s^cDwJAW<Zv3S5BzvbZiE1}Z2nBb2XjeTeV5t^W#w-Ve@EAt6`^mr7o#5zu?%&JH-Na+G0j{Zlbp9o3y%%`6Ws1~eN(fhyH<wh4{_0q$t4vAXew?mgNzvEMb>9&keUK}UP;|rS4QZ6Z4T8kPxVF68x!_D;C!oh&cPPxPoA3YXZJV^YLly`#&(H7q~IYnpgH=t_}bXac>l#lAYl?sWw(Zogt17gRPp0p>bbeC<+dDg_0Oc+{7?8HNQ8$$+yDbW`UOALFX%=LNWlsT+Hya>-lyX_Tq(l#R@fDwZh6-U{nQ8jB1RpF`IOHJjJIT!^=6Pn_I^~Bxf}OlkM#4$1AC={do5C7NY2J!Mhu|T!Msg>3;B1ECcl54nCW47DsPBGfgIDdGH^R96(!b|K?r0&8HLfz{BGYOW^X^#u{HdzDcxR|f)0V#*?*&-sIQhl?I-~}aY+{2`JzmF#R?R6X`auDqY)d{TLWtyBVj*)O@b&@MIBK-d=RWM@cmcby#&SFbWrRX)^n~`*hr;cZgqIabyoeE3Gc14+F8<S%|^j7xp@H`TG!~Q6MWUCm2NkZQ;dcYYS&6_0sV>jm@_i@v>lCV>q#CcPQBHd@ymRV2zZ)s2m?a*Gw~q@jRI-mucv45CWrJO8ats6<DYr=Sy^gJ6Tin5fO1k|O!qf=3F{Mnr*WYuGVzd$)w`GaF$I2F>0cgR9BSV#<~4_{0PCi60hpP@5?IG*Y4bn45-@A?_2Gru7p;xsB(s;90M7AUpL~oojlQ+Z_nUU=2FT4u67U~LwWTTBK1KV)_v^efohcn!OIy~$bh6hnQNO1rrMA&d18RQ$1{t)BJcc6ybK@MD9K5V(VKX4?Q&-6AQr48;589L?_v~`dJa$Xfm9}@LZwV;Ps-*?fwGrF6RldU^f5!YAGDfc^Mh!X+q_}$vus<__ue~*}=?oULuNg!@(wz}Um7XwC@f5fko;RN;koVqZ^MKfYU;kS9wsf~A{0P0{K=!HNq5|f%Ckrbry!HoS)eXSj`}1wZ4sYDQnlnA7>1Z~7pY9H1;e89(u+XvaMiK8@pWI{s%)Z6OI^HB83s5cSwG_cPq+!XU^jzmnx#3~7MThI7UWMi<hDVA^tz2E<{4Xlc|BeI-u_L30nr#*b5p5x!dfDbZ2?iyQh1jqQB^)~Sc>{S3>LDUH2M#@|m`5uPZ|nq}L?JHJ{!x`OC0)F^vMBMU<Qp7C%{;|5gY=(CmxN8Qwvq4EnXNR#+C(#3uS&ju@TfwMYaazfC^BE%v0=M@1SY+DkmF(jJeGpm<e3t;#u1Be>-OKrI~*$T-4X3b#XU^>M4RsT+f?dX)L6+~Pl`1*nvuT@7Ly;3)MZpF1wN$Xu7$(#YgocAU`^{Cyr}(HIx1Z*8l6Hy^0Kn^ANR{aMVWH^w5YL7%a25;`Ee_0=KNI?N4~BQ0hS~T(H+0X%9UhXa^kChyr5Ap&SDz;h(dX=Eeo>}yOU${CZAUP@i$b=*ipOsp~mv&dh(xAO!?&%W{*zri2KH*l_|_-|7T~ZUenoFRf2I%ptLwbWI93Ysfu>>`uD=yTB=okocC#E8ic^E2@8`SrR;u6(j%$$WCVhkNKW*~{kQtBP&z&W#bK6aY4wNujDOpjUb0hlv2x?b_~x=jU2c+LKH`(4jx>E*sEUIWt1Ru$Ed^=K<7R_xMus4Qh*j=a<wUT8IphOi--jCLCk;w(TVf;QN}K!OJNg~|;%fSlDD%wq7nHSC`^E-JTU34!`TZyxINGIZZY<OxUKfRWDfcFauBU|IcQ;W~_tnkESXKEXi_*;JiXq&BN)~xzB>Z=`Wpmv&;;-Fx!8<>hAKp7B-X;pvRwXdn!#MBmFQW*{0v8*c&chamZWM2)_E5*nPQCdpB|>O2QzZliuX}Dx(xH`?(%if4saUSzZ`x}clj8nsBM${7SfJP1-zoWBp4x2odPM)mB=)m>L0<OgH6rQX6$A~OY<}_p%7x@)_duwLRzWffH(>$862T`rOlBp|W!kU+B>{DO74wzk&wA`;m9**%AmA-BEd(?Q3+G_{^kCN=w1?~~l?qv+X<ZF<BLyg*y=`+!&D)La`uv`%cxP22ABj=8L(iA5Qh-~6NeS6)7hB?};jhG3nXh$wg@pFhcHJ+c60SpvS4C{*hNLiFq9#9;tPIff?>7fCQ2ydvfwR*_sFoW`XkwCg@syAvYllXCI>_Egb6IjXv_{m%=j#4@R){Wc@JN@{)O_;Nei+W|NCeowQj7W=@O7O4F?-g<K9DRDx;N!8o9mP<UBmnF#1)e%!PA`v#(&JLQ?BB0E4RA#7BZ)-)sENF{zABI?J&N35dgmMCsEw5R{ykOS)9UtX5Q_`Ks*?EBXrU%+kpB|(P4KK%*dD#2ntE<3(*Ne%ZTs@H%hwU@NEU4$ff@Rha<^ZeEujW1gZPlV(88mQEr~QO{?rL&Tl2}JHmKj>))YoWn4~4r+oH+Eh?qVPvwgd#f{P($EJ?v3L(0*-*8kFY_-PYi-UvkOPh!=Y<>a$O)|%}g)en>p|M{ce^vM=R+;jAIhz*@j0gKZb_Y)_nrT{N^1i+r|K<0KB2R?ETXV+Y1LtEj^m3L_>aUw7RX1FPhiP?XOQ`!%q5pOd$Tz*@^Or#cPW{DjL#S*v`W2~M`ZTO3>&nab(VCvgR-k)5J8?^cLK}sYRA1mAE#br1{EPvlqd?q38FC2ZY%NTAhx-ndKwIJRe}__Cz8xMp%0I3rPyyM*{Ycn#7Bm*%*H;Qzy?={c%Ft1=29@>$O)}7^WG`++^6S@VHJF!QsOuz9g<`tNB_UP%!=(C&8DaN8{+?B9F?WH##3sA@98(Qcg4O;JwXjEqXzPN|Efp1({Gi71Y+=jm9xiSQ0wBhC5esT@sq~7+L|LAPDsmON95i4X!x?4;4DvS~`)?+lFJor^Ty6bo((|0LK>8U=&FXu_(j<mRL@qU`+^n~7pN<6tBmzH_hQYw5^IV_t!L+u#_ob#6<(X*K?sURaO8Sha=HOfpi}v*Av-ih!(<;v6$xJCgA$#VYZBytxpHj(VrF3aob|AfAvb0#Y(J2?lzb(3rS~BI@@AUcnG{P5k&|UBCwCW@F%k#~b*BV2=z7S)z@t^tq(;L294aD%)?pdG;|7H1DMHfnO<rQAXBMKmLR#`gQK5`&s=7=X)>A@mrJ3*X{QV30(B<k8KeKWK8Z0kKAy#a8Cg;-dK`8N2sClZC*mP<UduUowl=XdZbIX7xe`4q?p3ii>77=1;+(>})OYKLBYp7+yc5G+y!B?p5L0BvmSMv1dXN0L}w8elm8_{-D&*ve{v|2bzrS!#Do5!$AsoDu1yUh$~DdwW4SJ3!>O(9!VYJAbG|Oj`A-D0rdkt5o#K2geqMh<1~+Fsqgg(^4|rql9weo1oebj*M<bllu?wW1U2wYUz|R%Knu~8osfAa?JuL1hfkVQ*sg<1!^E5LZDZ`2HACrReyfJ#+H+FlK-24-Vh&MNLkJUNyeLkbb|qe-;_b5!`VUpYq(ZT$E#q7g2u5=FkH2*o#duIK;{mc)*t<JsE%cKsYQ;hBpx5beeV&uZzpWH>}}kfus5*6LHn}O?u$Q?ht8r*4rN$cQ4T=Uf0PqwPZ2S+k?_0N3vhr`J%;9Np%RSXhXGx>K)8pptQql-0?U*(U@aOAW&6nx%9}wbBdn8=HHo&$=qfo@bx?W{p((k~?keYem;O8^xID0!=D3HP7Dvkq3;l}dg@umBX^c*~0Fn8@3qUaA8|)269*Ra<x3nbb*FWYfVwW?$!E=t=C-b7o`dW*+_nfl!J#u|Sw7uQG#V)77L-7VdA$^i{PWB=Rdm#Ik`aNx&+k&p&%@Smh?0=#J1@z^E7UMwsU-ANpAX+)Vjw7g4UIa~{xqkOdh`lPpjr^gt?p!dJ{Oi9e&wBPJM+bbr#T(*?3c;d+gn$%Y;P@XXMA*Qm;jVVzkwHp$C}Eu9if9>@UsCkg1{3Bqld;~4;37^udzkEQ&Bg!}BfZCFi~nVI#QRFPMq^P|*3Pqhi{yZc^rv|Y^5a~gnivcK-wPmsz-Kl!?<a%y%@)pNT0l$#jU6|lNC|mOnbm+`uld&e?#p+d=w;O<5OdD|E19~U33#u_sG##^yk%g5LfvrH`mU!loG&2E*9k85L|dmyr(O-hYfd~)SRl1R`PfEKhA|~jh0snOVA)kc6tLzLFmhH3zK;4+9Dg=3mo}eYmg6nxkleLy&?Lt%`S+uc@Ro!Jyf!3=pfHIf#6)YLtYTU`Fu?{fp2D>1LQ(C}X8Q{70``8qOQ1Rn+!&B1<6rjrA!@7qS^6i0DTh?1R;$h)7#hTA0@rG_B`{Hn{&Xuj>e`hecnL)g#%fq3O5*B#LlbMhcTiAK7Xk?=NbS*eI76Z2cSzduBXl0XJ3TAq$$y<n&Q>wgXNNQXr{0m)xaoT6!~oQCUxMAa{IL=pRLzp=b-|r&cNYwtTGHDA@xFl|h;1)u&~ZG<7l%XR=Z5l|10QoPPfUAMGEn|N1RZ}eXbXogQxZ-pm0j|!^Tm$YHuPR@nq%{{Z(1Nx=6lu>I4R(l_<SncRY%Dpog(0A+DN-ffR8aPd01RS0hfLm*_P-q^kF8f{>GlziE>-V_5l%y6qviYb3XbgMCStjZ^_Xq<@Ao$a~liV*;_lZg~`d#NdntjN$7rlizIdG;0tG7&<C;ar8EPuh^?|n^{L^_sJZ4Zvv*n&`HRFvNmi?;t9@2$O5xCNx+eh^7Cp(cTOu~q=-x?|Z<+pd{dIbw^%JPS>}6|u5lI5@Z3!TQUrFTSNu=nd<nL7v@ns|P|FrP#ghysIB#UC0Oz`Tx%I6Lv7_Wstuyl~^2hzZZD3hdoGaRLNZT+S}&&auOb|B-+21y$z{3A?wij84`CS;S^JgyXu!}AiO?0x;GL|Q36lqW_kZxU$XMW-aCO*H%TaAh^hBLcpm<m`t5xi4HR1&ptgzMfBPJuF7*iD?<rxDlAq?65^SlRream=w7j1^k)Z7WNQ-<=C5~Ln;x8?p<3tPSwz653Em*Cp1!2w8WwY_-^LHR}k`96G2pvyD*D=r>W7zszynEPGIVpb-{CDpoA9k4038rsOcxTI2q^4`_GXcI;{OR>Y1JuFNq8}4?|6*KPEPcp_uCjUBMsK#R}|ew=&lcPZPwkOls=NO_i@maH8{!KiF4?DsB}_xjBn!y^;Y`@Vm@9%uxRA9^mGZNjZ!{d3P;3{v)Tn@m%%yMqJDSVA{y?-KMDD$1nN?ebNeU=csO#lP4~WIjPm@0tPqIdf)Sm(0D}$%(+%luA&!UYIKBX{@86jre<#jg0G)I_{sahe`+?{h}F+I74%q_#ZRV=7{1}1#~k?X7C2@|IUvqaW;8Ef1s`QV<7W6+GfvUuTC^zWfrmGOuNyLTz5Ffqw{u=N86WfQKSp#YCu}(%wJaBwyyc(pV33wv@$kW*1_I9Gh#*VBuqnMkx5_b|uae;U#1zu1bZn)1hUV}V03o)HWMI%nXwmqerSGhbB*IM*oX+mR9W9P#GL7Zup{>skmt6=W&iig0S@#Z;WQ?R}Eb;@WtCMRpoF}q}aAk0(&W-{gDMq?yD*aC}pg7&|FVJT}uKWl1#1n@WWB(ZQMrrdeF#yhup_dHHca@s$cP5}(Lb!e9ys~7q5t}$o9<9=5@oTFswl^Bf3zHjZ(cjzRuaLv)v;~dhyspve`n&vh9EK02fQ2-qC4L4<YgFsiZDC_OL8k%7*&o1U!9;;5D^yl<Sl6Z&GhFnUVvoGCM?M7>F!WAK;<Kg>g?3R8`c9IW)CU+flGE6~Q5rW@T^f7g*)KNUZTl=Z$gP*t-b<5b3NOiI(<2JX!70IiLV&#0*4Wq?IL46o4#c2cWhZ6oo)sC2l5}Gg?5B<PL>p+1Z!Jrh%KuK{UEc4qm*eUf`-RkIl5lem5F>SUw!)4O%O>rzD6+>*6J65f(E$`;vlW*a2{mx=8zc$R7h|*!`@yId&Y{_u+zWgVlL(~TL-~L8?8_k;4K16k5o>y;H5CzBMR*!9<BH5(MGYwS(N7g31*%el^TAL)4xU%?TQDd9CvqJ;!0N&iJbIa!Yx!jZNn*TkNj`RC_Ho~Je{RfIgV5&ea`>JBmsk6NIqf|O`H4?tVU<~kRKs0V!0T4HSsS*|g{lfbs8IFu?4DF(YD_eyh9d8+W2%ad>VKe2PRxQsxejewsQ%$qcw@5GW0RN0mdm*sp%`=V6-Ekkr29K}T5yt}&W918HSm#?&78z9vymaFVJ*$9VPR-RA;`R?Xph?@0~Mb?f<@QjNDb&5gp%|(EORrW<!oyPnq98I1h=C~&A(uY+-WLwge+FwYeN}I)L%<Z4c{@uJaNAlTesQmD(Cuj&4m26Xh-L2V;c1$7e7XFiK4OxC(bi+{6{%gV<8MX?~5*V-QvUqoan-%Az~^W+!sp^dRJ9XV>=9N5?IT}n`b|INRC=eG0o(Z&~1I)`=@=8We!X;FLnw~@AcNet>wi9bof8ce*3g6NULlV^%_<QFuzCvs;;YQaVE$N#-uYml&=NqT6Ns^RZap{1Q?*(YW1yRP-!mFXaeZmuK0LW+5l+W*n~ZTFQ+G`1}?|Ht+HIB`cs1;F&SvYyv^T2dUC6pT_f?nKjt&ZaCpg9cf#$9Am)aFoEl00_CX@wc!%%U@JM82wJo;qm>Q92P9u(+z$lOeik^vYaeq8e1eFi57!#<CxLS&oY3!m!a1;#~E<%$(IL7EV|7raPo_gC%)jrE@A)LEG6?CVgCaiNAqA{#Gd{+0HA{TVJ4P~1$94!7wZ-MexV3~Brd-E>USC-7LH%0Yvn{+t&RFi#KeBI5yKLWqyfui0|#AE7FZ=9d~GlB~EepR)BbZ=HrUZ(x7KdG>gBUtF^--jJ6cvQwl|B0S7hm5L0is<3uXomcG<$ls0vj`jgyiqVW2Bb3wPyxkSb$QdBUhl?w_?S09R6L<h<YH<5Qec+dQ>a*|g1O%&a;Bjyz-mQy#`@oA-Mps@VheJqrN3&Xx??eVg^1K%G&XV;_(qU_ZWQ(nVCQt1tD?@oWW{jW2Y*Z=5qX(vTjw=VacVaX=P1T&^2R-pRzJONHn{&LSURB2#$Ub3xp<b4<H|a6^rP@ui0C?4K^ZBgn0a6OrpnVfq(JPa<!H*cv5y#&-mD|80);2M{N)mou2^odsst`8xbRbYqXOb=|IR%?RZiPr%`u=)K~S|dRqH)l5lHL61Ul4l1?GdGWw5<rM#J|{;S<;91Xi;7s;OzS9vs%yP@c24_`l(j1;*HtLGR1bq4#^%RT%zv@Of%?F7-$bC0s`cRnX+4@DN+p1a~~!APi0mILGT?s3#WVKG|3&r_9jWVa-GRz4X`)n-X=(Bo+_~sQA^amm4Jn6ue2aECmSt3t^)e{AeJjBTK1!+Q<M@gtBu|UDp7C+d0kr@JQUq;KMW@qe7a15{idG@)b8K!gC|+;$x1y9Q6lXA4E+1EQ8^B)iQMF-sfZ1)?aI~^wWA|T2QDeH=kOc$lT0dQ~Wk*@bT1V!9@b8{Ur=+=v~8{+nT7?+$julWCsMMW1E}2*`E+vuk!WBGhk8RGx!F#qurt+h@+%`zJ>5rZ$e#=E}D6&1_a#ahu3HAl`tk(Sr)t3K>GLsONAG()SkiS*Ly5Td(A5hV(;+Qpm(=+aoXhnsyg3sJ@sG~V-fT=5p6yT_xGzVc5=TM<3?L)rw<Q~@33TOG!dlHatT9Iv)ftlmz;lu)>HN8r3ZW3<OkD4{HvU4UJx<p8H1P@1LES!pep^3LWAq+zKBK=CKCN+iwVg4umq!k>Mn!!S^Vo-lQ0|GHG1ji?O~Kr+~jdDx&qj#9y{nFQ`vHJfl`tor5^EBar_r_aGBpSVQ0HpI<s;QoBo>X2_Z=HXQ*Dko0e|v;50nNUp6va=9D5Cr7YB0R9<X;brK&k26SIbs9p=(+M-~z&qew7$)Len7dT`JVN#4HQK|L#@~v#TZbLf<qf_VZRez<3vhr~quU^|m*26dIYRo|gTFaTi@s!KQ?oT>&KbCNGA?D7oU$@+7hDDWIa-I{rHfe;^Di_P97^<(fd~1fm)Y+on_(3W-Sv=QY-L00`Yk1^^(6UlA`*I|y2k(219Zn0bXOI_fe60FRoP@W&iMmU~KB<@8SrdovmlZMT-)8%^5`JmUjG8BRIzXy$B$RFQ*8qfI_^Tob95ZDRE2I#)-TjkrsipKw;St5CT)y7zgi}#z8vn}eY<n{9U6G-?5A@;n28Dtzm;R9VpdM9*9t~(^vi)&bDOtw%Q1Bf*zQ*>a8izq;iZ(<j8~YkR^17k^CvQ|P%1?n|=UiRN4{Aa_ENmXKo~8F02Vqvl^MzmLw@!U%#T~dI<$J|?eL9LFl~`q5DgGzLPmq%^<!}2%bcn4XVSQx0QeV8_OKr0afZ2n$K50J#6A{;K0oIaJa0taW=xJLHNb*wF;Dc^ZgvBeY=X@z|nA!-(HVQs2J<Gmq=QEB!p=JFo_Mr)2Wd@Ca>jLF-HL=(X`sn1;G9KV7%K@caMeLlKyw9T~dppC=y}qh2Vtyh<etv9pEAYdRzS>iYY!Ueg{K9UprypE^X<}iKKWN09W?6HA{brvW?iVg4u?cH$WPTzWS}}iFMu>E0mz9<8!~fU~GIHuDFxX{JGGEUU=VCwX9rvy$8;*JzGAg0pib9JiebQV*9qEr-Sng~kSXq$}lQn7T$4_8R%~{EPUAQW^2IVQED5bTZHq-#XF8w72UzV`%B1CD|-o>bUMo{@F#R3Nr*L4Bfh@@mNN$v|54B$(DzbcpZcHscwjX)-LlJYB*53jVowq|W2e0o)~EggRQB8pd$Z~~Y+yes2Lw9^*~s(>bgn{RVvu@Dm>+pSS$F4rgWg$sx-sOp5Y`Ljrr>B_7ZB@luy1*Ap?Z9L)R+$QV^efvOcze+nsOweQdNa<aw$(%7))aeA?8y@ozL}TMPI#^!x#^s)hd#Q=zD@2+01DUi!eu4AXe?^mn!t#eMJnv1WY%cszFKMnSnB8hTB5W5ylD8dfK}{t$3p}bWMz+QE=>WK}#`)DgNl7FgGPZ<a?s;4V2F!lj?Q7F7B_sQPCx$9g$$xUSC~GP44R_@>!yUu6|4dhCRi&~(@xbF5aM{0H(`r@F_v>Uv(#7HnMp*cj7obnwb^5!#2<g=uLy*cl(XJoiyCxo)y!}TxKgl;SL$={_#Ak(BT=%;yTA__=6Ujpgqy(vHWN~Aj9l||>ER8nBDc)3_?As}*%E*ofjAA64LUzE|Q~FdbZ0G!-4aQ&xLb89pMZ<kfhmRYsM~{!icZ5fIe8kCFVkT-P+#-}YVF0d?C;{K5-C;+eSjUa|%FONn(T<w4&6nVaa3LE!@f+hTLv9Ef32TK|{DfZl$Cz-D{*?1fsgXWw!pQ10!a$C$jQdz75C?ekw*zx{hT89B6X^OwTv|Q5@N<Q@UI3QiHc#H98RA`XVN;#p=J|PB+S0;}yNrXo;eRDlO&{bUbey<=HM#Y>?vM^E@Q^sMHP|1&<o``jBIfp=yBn)KCLVrkN2r#GtiErtAZYp>JEW)_c)-kse!}S-WpKsqtWzbvTF?si-=w{&?~i<o&J!5c6f5W@7YYU3iHW!FahE{0#aq5^0eu<Df=isT^bRQpLV@^Y&JPBzhsa<s>D}!Os^sJ2{_(P?KTESlyj)nqfAtoDL2mp%16pdR+Vt6>B8qv<4{lw1Mji-?lN0VIAxTOhD&wavy@{j|ODUKc%uA7bC2_WL5w`8SUYN_7j+IHr7i-w_n6_Z~MbMvWtiJa~=sL926)qdV`iiQpK^dK{zzoD3^8xwVWjl{QH{f=%p-@F|#TLM{+39l7-h?|N$s$O0_T{|7c<5Pn_i9TXlF0ZeYbebAHYya1+S*ddeZ|(z-E84!|8bUyh&#9xzwhU#9x@G2`=SMt4<Ibzuurp+EAK}k@->Lf{Epq*{i$j2J*r*%DceLTL*voDRBaGRSV(^$;&!vR<zJUJiJ;&|FKN%)>0+MwQ78j5srhQAf*LePX2O&C^hbJ`lGf%jb55I7w$4?JRKUlMq=uFLoDX)o*Y9Nzp+7+4Tc@x8iXi&oVUl$^05mr7A?V*nxWGWv%(g=MuR<YiNX$Iaa@UeB&U~$f!_bKk7IA(7(%uxM?{1n@nLHJ}KfRvb?0RvaR87)Wq%74#@Si+r1eNAa|3=&fXj)uCiZLo}ERHR^1w~~$2IU#@tPKuSLgNb%h|6@tk=cBKvgzovM8UE<hJXH>v0US|T1vM@Vxccfw^(6`34Q)HYiUc95f+N9@VhW|L#QwKy8(<rmy?u|b2)~4-Od3zi49BozlUeEK>JhGZ)pzDMHv||P>_X9&G2}kUET!j%}*_fd;L(ro`q$7{`Gd_h<h{RTT9eWJn3~Ch&!dZ{c2q)(gRK(_z8l01Gn76IqspJ25x_kv1cf(Ob+nfyGtlR(#}u#9=nc3#xIQM8G9UJBwm9#$?_lN<jUS3EHG-fR~VHK9*jmFy{m0eFC<ydE>jCyMVngXg#$eyj@b`Ke%UM!k_2^^-y=d})$W2Xl1cN6O*LFE+bto}N6{tTh;=gitGm@T3;MjFyL#pfLT5AG;vr6h!8)JKF4m}Y51Nh60PA9d$xZRiOpcjgn-z`#nX|Lv){FVPRIFxFk!>kR`P?er?~m2uz)&AHas6?2g*0_KAAjo1C@@3P(uKyRH&M$%+f*AA`^+;uto$j%!*s5wSbEw3xt8f1mPqWP$#*(g5*3+1wBH#<hD}!8Yfz1*_(l}ZkeQYGZ=6tS8_Dl2m{^Z1Ls?(a7>IR-9OT;jvz6`$o&%ogbM2vVUu!xDR6mS_>NEvhinj=Ud;5kbh7BPKlGX(1R*Ah|G{y+rw=p5|pLeSx4o_Ec%YAO}z*keMNELl`GJ-r&Sc+>7!RFPZ76R(NPV`o@Ser8iS<YFq&p(S_0w%Q$KY6(<23{lJw=sW&F8}f~>aKGvIKZE8LH3^(DK+DCS&&-j{y9lrZXS+Zd`^0%S~h2&VpnjUrq-yYg5=M#C^;Na0mK$>h<T9fwf1Zj*3AZ7=Ez}<GQLwj1`Tqfw#dAHvO7#C#=M6Eui2CZ1;Z2xT_n>GotQ}Jd$H^Sx)W+IxmAH$75xdmIJ)r3r<qLq0aWTz79F`OjQU+%uQ+n+)I#PCu^FRsuqrF~-vMG9C@}$S-2NNbwvCF1ArIwsi0c1%I*V;*nI#Ng5Cb&G5O)a<Ga$ITT>arcYwd5Iy-Awts`u%VZfE#Qf%T7dJ`aw0FLxP3l(^6k3D7e0X04ZyI&s3!3h$gcICp5p86UoOqJ5Wj3vMN3jqjvu(ZA++?djrhE541Pe5*L9zp{<4K~-g;Qut4O7KnJZn28tK^SDA2y8c<yaqC83#jZI2F8+T%+Ph$pSj3FTLt^*1_ibVDEd(BfmCL_L5azgz+NKWntK>Z=xXG47LYo~#Td2-cYt*CDt!9^s7J5ER<HP(nkU5U10y(AbBz#7A;PWw(BXrWdY#O*P)}{p3^iM$=KO1TOqOhQ9l{rCv-AxSbF%W?1CRBzF^BJ@?-+v~7OvJSv0YyT`Afh%>xLoJLzh((G;C0|3&~oU)J{duDtl^o5o805~;Q4i!*XeqJ^KSuNrNE^|*e-w37U=xhiSFsTEPc+xalVE09VTr~c9z=ujCkY^39gNHo4t8~QW7*wfhXipxR>=o2DuIa^9-GY^DC}){QnXgzbg7W{N7jo?kz->QJT?Q7ZkLnsXFJza|`u0;?=f@t5T*?YPK@-^We|yNkxGc)R{D;O0`I(t|qhd?gmqRVvZ+OoMVywu2&f%Gw0mRzfPt2Wojq{BgwrpTe39AzyR$h$UAN-U=|C>8a5H|4b|E;Q+YO~43Q(%SXKSlV=C=zy$(IjFWBFfdxaWGH8CxiCd*CAQFImdVf2@%Xi4sD#1_!%(?TeWnI&M)(({s2{1MUo;$q$naP>hpEa%jhm9f?#3AHssjA*gh)_)i!pg|aa7l9Dl+?2ZY+d;o{OUJ4$m#+RdX-}2I!m>gidGv8o>%3vs0b8kh-Qx87!KGIBR)nc+4(#jeS7t&5qo1DmlqlrcD{hj7iBZFv$mJvL6azr$XXn-aeg0B4L0|$8^4C68^&nWyZ~%J1x7?LtR;=~<J!+s&v0UOF8hF>sT|R^J_6+mh+y!oqb#vkgKXSH@OFsGR=RrpKgXf>Q+EDTY%9cTdpc?nHocsQltd08-lc7DRSv5r`*F|=XdtI#V4@bkMo7iXS>&y`^6?3iq1W*@zo^f*rY(9JHe19|sex7yJ;OOIfP^Zm1z{*(n%Deh~umuS6_}8u3@^oFW*RH1|Z-w|EKYJFfPmGY&RRGC6eErM#Ex0hes?)HnmB;%3COX{X6tjg)^?RRAkS8lok+KDy-~F~X!7GRpk;;b~s;Kr4dQ>#Q8f?nkEBXffa2$(mx-b+(lJA18C2-@>gXcw=@bo?L|3+?eLzeF4qx!#(BGHQ%(O$Xo$IaI$_H=ghWxLm#ajV6u0j+kY^T)#e-l(q!A&yYKE<itQfjk(>j`XR_d5a*I6EB9`pkOrn>fjQ2pJnw@&+;f=ZKHspj+!aDVTsp^dP3xQVtu)J;;T35yMLMl2A#j0h-To?MvZN$G}j8l&H-x8Xnjk~gZJ{*c(dO+1ECk81IGMyLT~JBFZV?tXLm<bZH}%o)&h$tHPhzvpzT=VL9X3QBl~(TGX8Gv?*=yKsM;rbtYBQ{7lqc5_m}D-jON#`s-s|IlbOZ&e)aF_wnhEC7_&9irw}Z(T)#V%*r4_puXBqoOA(x=cg}L`EAWJ-Z=vV_n)m-^kr0<}fg9k71w2c)JqPjo=*x&2|9<?!up01F+<6fYL~E$ye`(h6qEO8+8RCUJh*8;bqjn&Wnl|GU#5J3Y$QS+n&U$Y4z1?_!(9_&{*Jiw=e{A>|L8L%;$FR<(QSANRfLp;opQ7P3_*M&l&|ZJ>J%}DB<#Xn)nlGCWw{4{#H2b^EzxhQwNocSj`|QRJGmV|+|L#55vW>GYNNn8sQl#hnU=xm52>`VROzA)S^jMzfq#;SDHl^z6SOWzDB1(*s^>@7*Yi!JTX<(;PDPWj~;)6uL*>a@AnU85nb%gm#LH8-fo(fInIWV8owjUYZCq)7#?okI`<Nt_$x86`EjK-AiJEl69A`<6p!ANbcWL*n0HEEJYv<xh23N=IGL6gtvEF>eW1ncI<AIhm0P;t^hb-S|VY(jB-(2yZpvO?8_sl}5sEGQ3hkFrNieUi=QApQg<E!SQWmeL#CmCYwX;aV+HRZq_xqY9eXV!;sP!~HRv`Ohp&i8_AgbF{Yt<v0!Rd0F0*b2e*DTb^X!CF_^xsl0*v3|L|sx&@yOrEJq*4}Dr~M2A-d3Ngg6sUrS>$S%pm(niPCu;g8R<ADDbFiKy-N72=UZIR%<iEWY~_c?i89$UMP+O*fb53JRQrny)5Vt-ys+>68jF&e?wvFn<^dVRfKCLePxGZq&S8YLmhBl0JBT8m%uSNZLTbUKJ~>Es^IU;I@NhroneQ>GK32UekfzE2n?OY#X|G#Iz`CGcVX2CLcn4nB-4@6^qqPefm|d1kJI&$S(JF!&q)_pUBV!BhWw<>Frk=ar2bEIKufttqu6Y(Vt=Hc#I74kSuTorMVJey_AwhyglJ9oPVy!aqPgc$MXdkPb@l##SK1?iLaoT3Or)#)(RVyV@cA)dx=Ugo`kM*NYp$Eht(C<<Le<|34A<?RN%Uq@Vl=Snv(QgyxE*{fSkI=%2WJAg!Xj*$fAXd8C+7_~r{}w0|l{Hlq5*UvX+2$lrOOl4i)<RJFEk%VLb(WTV#_q+8RIMTWqJMHZ6Q+h&z3i;zu6rMP~N3!4syo+^k_ee<ANoN0)5Fm`#abKy7UP;%ysDw6Ykaif35MFW%f{|)QN$WJXB7_;9Nz;W(u=tePpKFTpUjiJ*9GoX0JE4*<?dN?#pr5j*&HYhFe1FLG7J3;fO&tJEEg2f|QjES%70xF$^{7r(G$QY43F~WR&!#Dk`o7owdjaR$q(+J|c0jRh#S2KI3Co!6t?^v==ZkaS*doQ9KT}!;Az9m^Bb?4Fyk-zRj0~uc4RkC;!QpmqYl{l>#=_B4laC`c=XSS1MzfAl^UD<2dt5Y$hE|H60HxY(*%R9g-%neM0&9L6$@f*~~W;C?A_J`Inu(T$$r15n>=tVt)+8ObG1uHy})E_NbrQ75<z#1I}PXc7pIRs{e0S&04p=bo;2y=N?7Mfe(GoSocPLaCjVsEzOw--8?g_7)nd9J+ek6G^BL~%Wt4NvXc!C#HE+f$?yPeL5RBH~;AFp+Gyv}7IE`;G^erQsojaADF;?Ez8MgR8g4tc_^)e)Z5wI*mu=Ri<b^u{3*TC9doiUgs3Xg>><@$~=E5=pCPzSA!BY#?N;3TSl*asihdl54G-UIpS@~_N>@CIT!m5yYBlCu<(;n;=4gdnw!0u;!A9(+QT~D_*<*!&}5V8i^TUPUGp6NHSy*WHsa&8BF!v5${J<?uQ_O=>9B21I7KQ8<b+Q{VM}PlS$8Kk!qHe*-h8uQpLPFbfg~r#k<6!TSNPW?5rG%3+!n57!Ta9{{VSQeHg9EnPO~OQS=L3}YlBNf;8$RR!>9bcz^;@7^@zC3bT#71Z9=zR$WdyUPWR)@WQkw^EH7Hov+`_FIeX0F6<7G3bdc9J$H<@LgbJJ{g(J}MA0*!>EJQ!pI)!VWI{_klG$3$Mje3-q$W5`D&m)CP$ApE^TLmqltmFV-%#sxStY9f?eoQy^t9fk<sOgF8rM1NWs1f~nMee})#|PbY*GE_J_wveETr)D}>&YUCxS^|Dv-K4cQ@&FzNo@!C{cxkCvuy}cOM2lg-e6t>O4=B|8R+=`{oVP{okWfC{nwUf3oML3vvfVeaRYP}bc<_KU-Klo3j8T~KCY)7{zNxzSfEzVS}Ot%JtvCKf}w+?WnUgbr%w}$WR0d78jh+%hEX)tT<KgW4we1@wE=eS`Pmjz%emf@@&hM#0o!^*5kKWA8>Ke0sefeGWg=?9{ArYClgf7Q$Q<9zV({H%?$_*Us+PIWB|i#1#a2tZe5lUU4xTLfSF|^ruft8ql7YWDFabTp!nI!{-iIx>;d4!QDlclTGPN0<r~*H>x}6uN-CpO7Xec1Uy_ZgiRx%*x8V%26Z<Q%!5stXUoYFb`D?9$C3-F+sEaL0DezF(lpN8zv5VQQSkh3ak+FtX)-;v$uBIGRn`YsI^@>Eh?A-q4@H%y}P?gdfwS4$n_Ak2emw2s9Qub^uVAhx0N54&O6Qz*z%+wSJpWQ<=0qsnOm^hO8B#o%=P<nnBs17gsgo6A4%iy$ci_UeS$KS@;MhHVYFsEZ`4R$vOfzZK%5aBxdGxn@#{|D6ZM1QAs-4B@5#D$4b+G|>9=7i{{B?J-(yx3B;4BkEV9ik*Bo4UBYdu{*WY23}*78c6qQ@aUBAs*jGWO@lgs5BtFL!(@k3DscJB3se2s^55}<hV_=eiNn?kLuj5&I8M~Aa5%!eMH6ca&Y{{P;tKUFfvC3kY=VK&B)NA!9udFlJ8?V@4a><}HycyzlhCBPV}pUFe~M|gGH+tH?hM9e>W7C1UJ)1Gd)yH1`|hkND(T0+@jC)s2~^nf=Ucm`pyWMmi<MmY%iDas6rPLGJ1B$;8Z8=#X!!aa+YAO~*8VegQU%=~b-$`2gkEdA+gy?z4MPwSc=GitpwbSnAdLsr@$*Rcu|7X+=KNpl0Z-8{-ef}?i6qiFp*Cnn>_rG{#_+P~s30q+r(IBg;tXxSRaLHGe5iZrOQ`spqoIy%7lA(S`>}Hh@Y=`<U|C|1KyKNo@2BCRQTH}fMo%m3JLsUEexlBBIDUPMJ|{w`OErXS8US}D<u3}e>4RgjvRWb(BI#2JAFDh47(GMPM%x?!$go!v!!alF7A8;M`n)t8yJBJe_P+y!$qO34(V30#RJMzzkuln@DoeL2?Z3$=zl!*4xQ;kB<y@>PWM&%4V18Ps9ED@wBaZU`*(vV!pa5HNZ*VHHCQ`zJo(#nu8*=z!6mL&DwKsaPP4xYHsyoG)bP-PX<?h`3a5ZH7o5$p75vX?3Pmv_>`%87e60rOpar;ud%L?~dNe+<>W0QV`3};$lvncs=62m!Q^26BD=_7jX1;_APzajX=8)@T;1FMD_oNc-$oqxqeimlASUM$ohkEUID#H<=L_vJ76sc$%8$`DcHJ?s}KQmR8zS{BDgrx;CRgz^?$NAgA-&vAKj8v*)xx80eD7y5OiA?U|Rz=(g><05`&y5S4bKfvH2c|s6`L)Z>0<rR_{ral>xOc^3Ww@v&tplt-g)2X?nzrVa}5b~mO7yED2Iv6Yrf;`{a5JlMl2m2Wbf(!UV{X03kUTGyJ(?<e(4QqitOeGny@j1QU{gj-g-d@%t;rF@{)dw3s$!Fvag`MsVcSA_7Wodf78bXR6;s?7n_c7HE9DJ{yggKz6aV$jt9>s15X_oedR@aT2ylQ#6ljkr`Ag>m$e2T$(5;3KH@5)OywPD?(BcM@-@9gpzTSUyvY4nz7RP|oZv`Oyb;<^Dq%bz|2VKs8sKa}&%QXvf>n!}@bDerh`Pxh=L>rrWYc$kbar#6FQ7VH2}pJRW&lFYPWCu&X<_HK4?{H^_JS>MLiY19TxbSaD2S7uW@n>khO2!BDuMGc<c8N(t({C7^pL7y55A3+WpG}htvJOHupa#g#|ziaG<{M&HkPnZg4mVeSjRTErQAoz$8Xdnwmw^kw(OZ6FbPMi`aV&e8MFC4#;nb8x101zQ{H5G+yT~gSkwmi3q(@S=JN9jHT;JFZ}ruz8}tfeNU=@%rx?_ebufkwz={#%n3Tn;o33l^JT!{w23zdW1P{wy$g%vX%mMkWl7JV#XkAfx+(e;+onVw(Au2)YFLvL?LMwHQ~hH?|RX7c_@|)B=fLj;*Kz%SU6=9rn;iXL*4vuPIrx8Z%w5oD%&TaPJY&WT7k1ne{%lVjdq<LWb!i{&tr3K74o8Wws&6f~9dDrDm9oiHrKFp7FoR{jVMMnw~}v;?Q)q?2YzDl;`bE==#VYd-uqHib+?#a2Y9T*OWv2GdN(K7l9tDD6M20#n;3mg75C%A+W`?jdBag_Mm>8kF`^3frcPveCf-*Os=m1tntWE2L@{>fA`wAeZ2j|@h{-d)%<&~LGI1d`Mvw2g5Q_wxik5}zqu2OB0Bdd9sqdus$$oN5_AFLDHT`%>)V=1wB*nP)%aqLs$SWS+P4Cv@Pfjsxf^-KM1}pAYXtDkg%xhCqMT(^$Uh;Xj5Hb|I>ZZcInooUQ52nPE~;Q`FkG4!Ge7z=Nol^5^;OOqDv}*i&OU(=oqBGV9i-f90$-`eJ>lH3KOqh04#5xBnqsN-TSX)UiEZbb67b1V9pmv>*BlF#+54{5gc6cYjlkD6BQ?}560fHRaoJM8uW&T8q#67?#su?B8Q+W=J|!q@%m3PkxL3+rTsz7&{Lz2N5xv55(<>?Iy8hbAT9(~u4Cq>?BDN#H74!o*tD#)aogQ$hFWP_MjNV^EBk4nO*-7PtS)?Ln(&u8qxB(gd8raUBHSd6mL*#VK1)TefhY}F>Iukozr|NH3*KBvdSbiI>UfVeoKHD9<hjFR9V#<EztM6_t*>iV4h*0L(i|f%}2B82GWeOq|^PggZ?6AY{)Bnn_rs5qYp$o)41>K0R7tF|n^Bib1SI26L3g`y4!PCQ{U_&JHDvvm?V@+a>b}*%h^1taw#LH7wM44#rShpNvcw+yZTYLvO=~>RP))4-P(+U;|_Pg`y#69eTa{#~KuqiE;ugFxEY5Vw@Vpj2lv3L-^T(s<Zmp$vG0-_kX;a%P@>(_Uoub_Ta3Rz<A_fN*GH<X{1t^Ym+PR)F63qU-YK|@fTd0Ac&x%*O?&JvjVk4ujk)|4>6d_G@gxihWrWOP)3iJ>>x#rc_ENlYpBC`HT0-|nGO-lYB2F%^Ny_xW({Qde8A-uHsiAG>S1w5McY2gbYbcroVqt%dn)ybc=b+NY$df4{q^+j4*7ID?qbuJFro<DUOPusksMwb^siYM>qq{u-{29_t9zL=T^}86+>cg6AnXm2!ippzfxeUbkHJ!HG;?w_Wa3Z?l2OL7YMiFCXbZD~zPc23bhMHM|7$8{97JLlCk!V0kV1IsE4>e5P(#p7$~HI;%j`!iZQ0n601z^vnqJ8|<itEfZlK%iZi*q9ZP~aPg|3orM@Mlm*-%u*kmnXgz7nI9U!3?EJYk3ZziLlCI>>2Ub|n%0tDaTspWyiN1kR67Sl{YWsUNY%VP{v`y;Ayq;PvYP;V!G^)VkHsJX8Q=5DeFN9wm#rMOGzU1Dk_xnl+uU#<%<1c6?{v6ZqL7`CfBeAAj%K*apds%fWdMbVHm5<~gUmvo~AFZ9CcZ*lz?lGPLWTZ|Q0xF!7GcYX-`R`t?)zND9r-i?v_umww*}7;bQ?h^EFSB|~0-=?8xK6dyKE-4PDrAN}FPf9&(pHjY!Fco~<8|dLj$-x3iz!OnR-ug#B~)^KE2sw9$GMw47s_y=7;)%~JD{!jt#aXCwwt8T%@IeBUXoI&>|wxuYEp&!25T%+W^~{Wf(jSZ_0<-}(~J5}4hCDml^;C4AG!uJjSiu2C)YX+nGw5V%VWCE=+kOqAZvMe{5{H3vrn#7IYs)<7ya$zw7{PeV}eoil)OZ40F5_zPdCgNi4^chag8!FDmWn&13l6-Uo}nLR;@&jD-m+0%%WZh__o-<Z8x8SBlM@)tr!L)!P6##L8MWEVY1IgU;e$jI5Y>m<=HV9pn2fS3Wrk0NDvgj<ynD#tn7nX6G>&f)8twMo!<hEXBP}^^Z=YD&}}mF{xZ<NQH3oJl0Xszc=c5mzfQ#bKEB+&&1>b-uy)cm-45~iE4L(QgJvj<HftQ$c^bmj!+D~fSMgr<rueQ96aK17y9>tr^{LM)`%iJ>|C-}lk#l4Lb-iop+n+HRvdHjHR)_)!V-A_{$DK@L+7H!&bNw?;*~-{B`59C?3wQ;DIic`EQB10gkG6Iq<x+%{pCJdvO{AQu{r;x6x!(?Me~;928CZmts?!RqsoevIF4KF7@Gw6uxEa;ve$9@87U6s`KaAP2?)YdS3-;$t4msY4TxPl+3N=gH%I^~r?fq?x69bI!uN1KyM#p1Nws)I%Px;)z0avt9?q|GipG<e$jZGVV$*AM-Gqmk4($<Mag~`&)Oxxt@XefSnYZJ+9-F9D-n!uqZDSz_rY}oVT?EiHDa%z9)@z9%tXYd|>y#%*IQn(=puic+cM5H4a$<|0%lY&;{-9|Ja4aoH61HowySO$4E0Wtb~<X<p;O9nREdSl6Eo}X7&W^?j4_JlwDr=_%QiUcxmmk>%Fkl}VMcz$Uz!c%d*XuJ4I29{)GcV0hIq`86<+qFM-y>OI*s^s>^hOII4jgfc+#kF<-{CVGObh5jQ{neaN;tnDXif`#f*q~ia(`e7oV;tLR?^T4f))3n;!nrkQOY98a{U|TEY*E6Cl0_w4imKRRfTPY1)WLEt&=70JjTTPO(k>-p_xg_-{n32V<t+W6%xN@*M^du!%IEF7m8f4pwV0@L-zFf?l;}9eq#tj4juY9_{P-A%RQ|+;BST^tb7B*^&)y;PtINSD49rk{W#Ib9SN9PWR{a4}U$$GnFu8L_vw=cLoyoKrJ$oPY{UBxTX;hWkL-y$|yv8Ay`oW()70~xnjQ5LKl|*m*JAT6y0k&F36UfeY(JssTZ@NInG(Rqby%-?-b1Oh!p-sWEX8cy<Y;iT5&T^keGwi(jcv(YPHzdc-0gocJNjjk~8xrI`krdZ4VA}99UEDhUDQ%>mzQXL+81=V+B9ED-Z|I6f9v{#A(wzIMGTZy;^!w83j-1mN=KG6-2CeW`Jr(PqXn!cTQNOFKK<GPm@}zO;PmHD_#ysFWvhwmi+T=e&XqC&qW8!98B-=TztaC6giAh0>G*!#&s7`)R?K`{(Zto7E3X>LzPZoU$$kvRtXjCc|B-j(M;v2oMe?_P47(f+zTu29(y`APUV#UV`&p#bVKw5F9bmQj2VCJ=h7081EK;>fw@qVGJ<ZzO|TN3df=Q<QL*7+4w=6%&gsasStnWh5aObT1wj+jmbxv@n$81(3X^8{oq5W>It7Wk;=iX&rNbXx=b>w-C6`i*oJzI5AFu_-?bl(HYc*!fzMVpX<j3?0+K=7D51$Xa4+l2!J5PJGqMjz3S6NJ&dfxM<sc%&2_Fze747ek%BTkJvp2rt2JF5Z4D=%q`WmX{Id8CY5gb+csbZ%E|q(#rgPekU(ie{<i-$=lSxNT99359ymEu+X_ZbKG~P;xE%AGQsw`!`&(&6q7`mFvCfjQU*GU<al3kCk3YDq(m+*29d<k_omW458Y3Q=#QDofZqnq)0Ak*c1!ohghvm6t5g4bEe9lmlPXSmK3(o8;_;(9st2WD;sd1xLev|`_#TF^XL7Rg$EjvWvf7ySLBbfYws{@pqZ-RWR8utdmj<N>j_g@#E2?SE|ni(efn@4=I!wjuuOs?>vA^wW?c%T^`6QTQKA=s;+OyZDUYo(GyOa*-*8s0i_Gz}2iZYrmVM9}U&Azu#DQf*gWvh}Np5+P6#fLi$0WRmIOq*b5GMzWS@m;wB+mXiR?Agbm0wm!z8V(fXCAXo$R()G&O5rg@w>Z2y&)6oGzwLTVZ8XNd@a*SeSpP<y&E!?}+vQSi6q<~QmDSxUH%{H`weNgB9{YN4yp1jZmR-)cs{r>eADPe7tiodIgWz0`lFbr#Xdx4i5`3)~doT#!|QOI(q8H4*EpO)k3bi3KmtL(c(0TT<{w|f<S5CvsSG1`CGgDGZY_N8j1?#uXtTIbYzulV}8)QWcgN(Vso(98wDi^zW$n)bW2W|@T@nkBy9C;wt(K8Kc2IVEr|ehat=c{1}8rXEB?iJ-9cUjp#?UG}drgr&?f(h3#$i6_OkP+oE`=*!tc!g@eC*ZkFw<W3rIXu@kgPtZ@<OZw<Een&$U5<9niy_?UiepnBcTnf)D(z`8Wp#0wg-cDKE-d2rowC;PLIKeB1ZbQBD0RL~qL#btlK~Ec07KX~&bOC+nghrJE7^QInWpK(c#in&9C=O$kQ(+LMHEKvsH87*f@#NJ1CPDNJWwX?O=O6;sq(6M_`QB*TpRBKK9`$tvzzvg1K5|(snm7rj^l?CSzt_n~24UC^W8L7A<$$@|B7J>>Ed>-)cC%Sff=@)@wEvgZ3_$zRg|9KEO?`gKvY?jTy*<Cv4E+<DLXu9yl}WwXnpA9uu7~*YLkSVH;{-q>6l3U~NV#QiFQtSO=d9&yuY;jfg?u`Q$!W-cp1n4zuem+~`SX#=mox5cNT3rPiIE>9pJ7u&x-XuibgxMS(LA2fy9~4RIxVOzg1&4P3PT4}wmpa)_0^T(*Mb(jvS;dB$km2c`q!41T9n80^5^Lqg#PhA8IEY$80Ndo)IOf@A<0_S${TNu9Cv~N1eHMr&LpUBcE$Q3-^w3;TcLWlf_FEVo2^K#eGO)Js0|Mf7018gqABSegYjut6jt=~h#DR3tJs;suo6conQ}Tvsx;Qvf{Rmh`wl$V*D&%jfyzbfrkWTB)>a9TA=pAsI`(5mqTBRDpB(eV^7+009jK-d<;B0E7QTbkGksH!W>w?IFRZC8@QWjGF?44Dj}$z6{RCB8zxcQs`E>|a%<`6J$Hxgz6uEVI*nOy-sYEjmjbg2>V*;gpuKub>B12r~r?dtUK4nz4U>bKBMFviLJm6<_My4rrkDc;Hf)P108~5X^-IN$FX`!}^s4-7d5CIkGH_#a~qP+*4H0gEF`-CJk>`~%hE$5BO&dy8xh!hm!djMS~;%}ZROYCP=Pn*(RLX?w}HBkU@`fnWYMX~4(_etjIw)k=J*`_0!XufP*j&Dd=#7o7|=M6%_h~lcw(tmx8(;Tl$Bui-^+$jArkM$*@)CBzbD#V{?Fx>CdUJbK1UUX8WYW9_D%Q(+t&3A^97(t*qrof)_UlpAjcwGDaBRU3I$0Ddng7G!}f{1cJEb~d}ahm&T;K*;+B26-#4WnJs;Md{fiX|J?`x|~~fJQfz1wU^jm2+Pt!)SiRZZ91^`Vm$x618vH`Dj`M{m_J$Mb54GP5-D7lWRfT^?K+tCT1`3YaNiq#w)qVmodXs)Hh+-^y#t07PeCg+E7o)u~qtTXJqKQwV$k1Z4Jy0zNQ*bk!eyL%?3AS%GPiO+=hSU0(N^w4R0b3{Q=!2sKN!a$pRxmTHhQT?JEX{oUp{%Vvm!WoLEl$eQ^7Ggm~paJ;BWu2^r)EW4Lg89m`a@`ui`laY~elw2tUY{wXG54EcBcM1Zj7j_AAb^PnU0oUgc--FltuLZ~P1VS`wvay{q>v!j>NP%Du}zPZ3n>O-g2s<>CrQV00NU-z_WiuESon_i6gS)M-~=;R*}tW3@v#rn`0A3f8;Z@=5C4=k(ES04%j2#Sji2W3kMgn;XkOi2qwI~pV}{46qSo>yi>BumX~Gd%<{zy7GsM!oFCW6SLRrOF5ap`mUjMjK%MD-S_CSCc0t;jyZdf$L*O7{u}`btjuB@l$cbhF1W9iML7LHR<><57hjE*pqQ|j^^)9L|K2@hY%(b`=+hI(f-Z@K?WjnnQFhcwi%O|!vSl-^K0eWErlF&vRMlZ0yX0f3G-T$r1(n3i0=Gw9MaE(*to_PUFp}zCLx&C>_OxY_k7+j6C)`3P5FU;hY1s7U|HFDzm=p*&uE_203wmyHDcvnSX{%j|K#sGxvrZ#D=%I^kks<jQQLTxx-gAp0?Ar0H(DSuqlw2v?1MFHhhcnep*Jv)$Y0HwArp<FET7j-S$YB=R3Qm`&GfjOGImoxJNd}`t-DWwM>QJd9_mtbJpnZ!Xm?_wf(r;1orZ4Q{Kk_Al;qII4{|SD(kavrGEU&n2ZpMfx-GU5hDIQ?7`2*?JM=OioTL9Y&iT8yy+XFqOG7kF<l-G>(C#PdH!Ns^%M|<7-=`7hdqZD5$98^wS5uKOGsLX3b*3v4{AGGRb0@r7{emO)spM0gKKo@W(KX4OD<_a(65f)5Qsc()=Odh|zdw<;P9u9>)Xx#fn3#iQu<{EHP+gVEh+YZ-iK2PZnHzNVfc{7L67T8?U_DW@Nu-YcHs(r8s3{Nc2XPnbYHlr{yq$*>^@#gtdupR=g7<%tWwP&ORj{=4sXTp#h~KY@7bGiRs9Hnx481~k*;mT_i8I!f1$^X*4(8(Fza(2QB<YNllcGrB_VEiIM}-UH=-pN;ZB8EY`@&7ccavB9pcC^RxtjS$utsfQ2Uo9l(0i3Z9kSgw!@kPQ{Tpbd4E`%BPH_>zo<v1W<Te5qZ@De7;ZsgF=x?-Qmy99|LC?I-iRK>ldF`CKw~z;YxEz1?I1FAitbv!G-!^0nH?H&Srw<4XFMj)H>{2}ilm_xE+W{pf5a957u`ls5{S-UDtoZywcavdAW*c&PrGwZT!6)1(%{Ck|B6?ZWegX;}T*^U@GZZNVXh2ihVz9TcE~avH|21!jfCN1+3}wH2Pn#*axv4(Y&UOc9KWro5V6QCIIF!L)7+DT490y!+v}qdGsMl;|OO50P=`#`=jyzx3KE2G?R_y&0p`kQ)ZuVag$-1<U(L-+@Qp&pj2*(>nX#aL!n}9%ba9d;Yt^k|3vV7d33Iz#MUg8DhR%lsr!Cd$!NX!%73fz`BDQaeCw^Jv~k8r#&f!+3BH8GtaV-27hEOa}h9+qJ8{=K)MiJkT}LvFkM@~_axj)_kj{vluu+T`$28PKV94ESacd%f1vPXMj34WP5n^7EX9oYvt`qMp>P@UIMKYqvF@lix2WebKjyh-wS>Rb+FJdAvwe{5J&VJ1z=Ed_y{I#qvbo4ehEQ-XEtA_X<7p*u^Ls<L#R=u^X*TcyO6Udl)X;8=eY(`wIPLnUzv2M#Iq}{TP~De`(Ab=np?xuasrl{C>GE{TAm0a)WitLMvd36WW^va}3PS`m&l|xM1_*dpH#LGEiLYP&@Hcy_~wN5`U+hD7A%c$}aOXyP_PBY{+_D(2R9YHDLfN`WkF3mw`ghu?>x9^U|#JBZU>G-<D_0I;C<Q(uG;5xbj(qb%dOG|6ENo>_?0zDw+O`7hjg3wE2fs-nTt4J7&cUc2llgpgM{1MSP(clef~ffbhciqLpYMz0~!(-W3+k>ow+3EU91AF;7h0A}PfO2)Ml26nwXn768}6KObn3CFY5$DQ@5VsXmP5>EtYsL>l)Q4qTy^Us_AmG5;GT{{tKtgkPPUZov-Vy0LlfE+h?;u}T)Gb)<z<3!?t4xtNJ)i>L*{$NU=*^2QCi=0|3GHbeQ~^c#$B-FK>VD)>=H>@gv9ByA#9p>L@ES?j_?)H!v#mwDeRlx7%lS1P$bcASG_i^j~x&cioM4{D`97D9L4-)Rj0`CUvE&`?AT9H9#kIZl{v?wXZ`SHi8hd!pE<wtIkVqY~PC>cvGZ5D!O~4xFXT6}o*ll34|+5veY3aYcj1&->AEUCFC4fA~8hA?SmUP5!lk(^NffyGnM@MO>mL3K=i}AZ@)JrE{&}%N4H?gSxQuro+)C02oPp+@0NiwdbU_mN21gGE6ta`M)4w`t1kCxC`U|ZX<uGH2{aN8enR@Z5tkgHRaaxk*g#lv{I1(*h+x#uh<amV7HZuhEXL^4&|=(pmVopN2ON3q|>hrZ0n|*u+Ir%46H4c^ePOp{+sdBpbTw-``%43B25-r*Xp8?GsW+#zV@uOu#WfDGTMIw|4GKEHKLJtTH<L4l><8XW8l-5?b~$z$~rK)mFFqo95+FFkCZ3!<b3}vAYzE9YM9b(eq^j_o+nYog^9n>2eOE(Ozn>g2g1;>@>-rAX2Q@+qnebOiZ|spvD=>BS!!xPi7e-6fSJ5vnjiA$jk_V3?rci<?}%j1^4hdNCFM~DBYBA=lZa>}fX@B$QSq@0HccI6lxH$p!Z0B2jT6L&!1a&X1=M=hGOn?bk&m6NZ%rY-+CR&0F>}u9xwvdu+4|4j!mp<8IgC6O;>)z;vPq43r$}y0=v+qk=EH!jN6+yZuT@bAG`uddE7_TZ!wH#OhPswL5B#63$eOL+{5mxYYtdA3=RRLp%Jxiu@9I=Apekyoxd-Pp(H3+sY`iE)m`;<woL2w-*fh^YNiiz{sxcTi^S!vY%Jx#Zj}h;b;kM}7XsQEzntzTj23UZ6x{tsfxjWo9_tz9<4RS4gkA(iHK{4N!z5qE#(FjotJ6ciRAeLgGjJWenc`fIHSSSia-l6OUNEKyNx(Ydq4W}>cO%SQ;VfNnzupE$H#>V)AColhQv;jvmmrym<EYl12B4M&rsk$>pC`@TaY^!oXl%pBlRkHF5-fM4OqLOcqe7nlCR)?=eh*bu?|0ET^>2<M8e3cccFLmq{<gr+~e<U)Zi3`^46o3&`rb^S2s})a*B%4LIK^w)WJy3R6ys_&_o-$&9BG$nQP=E@-%+z)+W2DJpkKsjVAiUS1w8Vsmmx3?m@1R@X|3YH|GoVbZtaLa#Ce_ji>WKJr!dSX1_xE8YFY1^hecjOpUMB*oCnoaG!_<%MkBU`o;(!Fv_z2vnLi}_R5Y&HO|E+X>u0!g(Gm<}QH0Wi=ev^fCh9^i(g!do<*8u0V1q^B|@%h#~xz?}0ixxYIgG6E^sG5CA`I)nZoXq$T2FC<hi7qz6^>%i{^hx3(qo0m*pc?l3qeeM4jH-;0>{Uxp<GfbS)pg0Y5!G$L;x7lH*P1H8!B^Clvq+k<qzKfto!qIaa_GU2v4H-sy+&jZp8_#CWh2X;aMt^m{@AdkhQBi=(k^_)>-Co7$Z`pG8X_OQ!9FTBNvK1zO&rvO+jRXMUPABO9})(HXPl)N@%=Ed)3g)sN|NNHi@kJqpu;CztRv1iUlYgBC8z&uHq`6>l5Dh~f-nWos-OF`yPzVP`b;ThiVD>eP(Yt@2yIpzdZp>Qu>mhTP2bSMR;f|ELRwYeAIy*~=_6i*^5y88h@ciEjG2Cvzj#GIfF#-yfiG6ac6a`CQBL`g5kxKla~s3pXxo1DuK=bBe2E-D4c=VVRzmoVjqcLaUG05sfIgAnx3U;d{G3F8y`OE53jNyQz5G2&xMdc>g(BQ1vjWRYZZB5x$H7CM-+w6%<BSG@Ru3t;Hi6XP=E<kMimmpwxXDzwnP1ns6o}{*Ve<2a(yW(*;kBcViOS_G5E<V81$?s^6YJ1xinEdaMRM^cKVA>neo-<Jl6rUCupcD&eHOe)Q{5j+1-aa{CDp+;<3i`qN@e#vna-i=OLaq1>3g1m;twwHS<xS|hX2O)>#`$)@S!mP&W6nHh#Y;PPKo~zLVy~5hMWDwH#+8`?>u=%`rDx}`T*FJv$pX8aw*=pnALUW!OTly<7=kX9eEdjgzc9oK=p4tgJJ$2a)Dk?ytx$5GvmF$j4`pV$AJc}+q=5tw9X&Dk9`auGe(!?=Eb%)Y3yCo?)=`XjcWFAj))@JCzPfpvB+G@>0Ft6x%<tnzmAF&PQr%Avps%l!q3f;1`nKQ_8*Tc;X$S;;D4|V9U<QXk)v$}TGtpNJ(&EXgJZORy$*v{zf(0o1v1=nrpAeGZwDYT0Jvpzl;1y;o2^C&f{!Tc-@#KJXx^ykM8~0XnCjj4AB6JYC6Rs~1!j4JUT-gxT_Th1;D_O!(e!&tmN=*r^3C8L8QiGKhK}1vf<b6&H^|tZX7}?&CqZK8JVM*K%QvtmRaxK4^#+G`QBi$YLG}W^ImzgmWbD2aHWv@98PiC^YJ6`^^(=c#qCzdhpqQ4GY7MS8aoPrez#H_&KgropT|xjj1}a_Pb%P3lQI0Gx)>nC+5<Wnit{*Kiz^Wln$1{HlypwAOl`->*L_fJ%02)1i$d_?GSJp1*7f!vnBfqVDaYy)}`|$7J=kENLhNPD?YQ7#nfPEj*gj{SpYv_?E#8oQ}V>?6}8iT()%mT+DsC@m4PjQ`LhL6%&Qq@J@6R%Tqzp7pj0z#KLmqE4jlO^T9tG0~kjRiwx+(ub;;InOJ#RVZ|gr&0a>9-DN%lcvJ@go=xBI+7*y&X|9$lP2#!n8*$hH6i@Nh8z)a=yZ#q(c@C8k=v2xiTRQt$(@39H3$S<e*kIfDeQBjbj99nI*xL>nrnggrd2~MeBjR;<{_ta2)TtO1sMU{M8lMsynOk=33}70o6oU@22x>f*QJkILi1SN3QwL-4e5GVQUoPb*9<NtA;LqX@rkp`q^kDhF@g0#r;4BOk*V=;ZB1~K?F~(#~hP_*VdS4zen09JTomhe=*2q#|OaxyV%1<_}btF{4F48$}R#=ta}>|$P%sd000EJXJ5T??tGU&Q?Rr@lxw^Mw#f#Uyrb#*m?4P=7cDR}Hfujx+tJ@jR$<4aJ6}0ERqH{`6q>hVLib1bZn+{mZv%E_Uxs=XufmJEvHv3I3`8byT)&F7L_L^C_#ACqN}P4K3M=w7qC&L*fEy%rRM6H$D*t`0#0}IoRspN&Fh5`fBQ(svOi$}na4Bj}KF9)qd5k!EJ#n?Gyw!l5GFY>v5^OHgMx%5N+TQCE#_b%$UWf9W)JBXlU;PoU_l!b;rmg<H%pUZ-A(d;)A|eDD{gW{bc#WsxA2yYGtNi`0DE-q8c=`SZ&Q{3QuF2u93K<p<Q(^9cu!J92XqhY~0CdPhK|EXw(5}m+hFX+IN>N<OW^@TQZFai+PU~;d-j9!!wnh3#nBeiCY_F)9T}Sg@G%5)wS|;c{9Q;jctF#T=A9y9B_9^^zv@qUehV+YTEQb4CxR!du4n%m~*VB`as#$fdto5(_{1q2%l$YSPxTj}(RvmQu_tWs3U<G!Zc#2Wmpe%+<p#@suce+z0WNA1J2spF*?hl?>;U}nIk<W>MR4FH9aqnv2QX+@|`=W*<YyU1Mh5Q`rFPRu#%I8hIN|q$)Qkp}*gj*7gejxM^HpesOhH)PpU?1ALFX$sNU*?hON>le63Gj<de6dB1+yw8GOfEd<K>Yr&jo5tupeM!Q9B4J|*wlr?5rDrQmU{Mt9lu!<&t4KfZqwFqLhDLKgZUy>D6R>;B6Y<K<~kjvWI@WC(n{JGAH*;Er1Gr)Hv}W$)WgD0{_h4h?tk6Ad5_~-mLK^4`xG4Y6cka443QMIMRinJ`%3M5z8rz#B2wZeZlaW(fE)FPVb}$9p*<KFhT(csDD>2{3*C+OVBq)A=s&Vh-y`Rf%)OVSL`sUte6QSg!-@AIB=WB3p5=GWJ@>}Qt~W<DbAeBkLCf9F2R%k&s)fuVy<Zb6k*<-Mz3kLdoSf;<<fflv;kC2uF1r~Vah5jhmX=6~rR1K<NGW<wI1NLS3yH;WF`p$yiBX0Nm|YuI)V(>~FGO`SD^Z(d0q@r>z20X`Gp!Wcb+OKyT`t)X)7ut78QR{mdzO=?>6|kY_l03?VQA^OL}-O$dNezBM%hMf+pI4RlQDp%+at>bYsGEaQ=;529p|OK*3UMw*}OZScBx}xf2^tkbI1=2yHU!>bb>jQj}uGFG#72dsWhf7OXKRZ@}`tekVNC?j)zBWCT~(Koi@{C!bq|$eZ(j70gPdKb`l>S39dJ7+0*U<Uu{~MQEp34C;NPLDD~zha0y5r*q1KRnxv0ZYoG6S*PB9bw{k}MSnahpxYnIky2rv;s%J^2K^9w7H&trqo3(YWdfF-zcSXB#oR;S7tbMHR=WItdW<5tX^VLbVd30&JyJ@6EDJ|^Dp4m@PVr@n5q|87~XU9Y~sc#QbW2G>2vc0g{%@n?H%n7|xrpFG&DZQRV7J~aNs`-R69dM28Fm+s&8ACFSSt6TRwM@Hx>@TwO-J)G|93orVExJQjm(4*km9Zt2kV=PSOLr(-98jCw8t-=*u_RA(y4&H*0b8;Y({6Dt&Fb3eq*BL~hTG=U1k5)9&GiQ&5ByzA5zS=Vp{j=oWf|jkYGhK!MSqqP#=TT3S!vtFX{|BcXI7)R+}IZJ89hu5cEeI~1sv%dL+;lr0Z^deq=O?VIGwF$DwV;eBCV|YL^`nCbn6(+u|0Lh-4;Gn7Y*KU`>n0H#p(7cSs&N3cBVK;bNa}sEt=(OeUNsUT!&LD_2zmpblR<znx5^pOsd(Qub5mQ!d1dhx2Z&v%^JN<cRW7s^-1+m$d}|UrE}dzs-7L^Dq2CF^z`hplwc(@WlEXZFuzOlwHZ}R*6iHYRP!`v3Wa@#X&coXe&l3a>NiYwTb_{t<Q(@bb5S$&xi!xn0Pv?B2OrptQB~|ukBLEjuBz>F{eY7MPcjrOY@A8nrn*_H)8FWPp0jEjYrE&xW`~(FGcC=GQmvj{G#5>-HsZK#pQ)TK-jT^plZCl|_{z0=F45dH*7R;g46GVo)A5a4DUXfjNNlx??xbu_Tl1nx^Tt@Ddu4&26Xsw#%^eNAWT)mrI$2HZ3W70jP5TKx*RN>(+91deoG<FMbFlGF7ogw~TR$c{DbArSm#D9{dVUYwc7d9gdb<{}7e_T_GPVZAYQM3r%k)G{Ru>I&!)Iy-QYGeQzBd{#N+l=TEv$v|Mz81Eg((rB+pRNQEhJ^4lo#o|+dF8}@vz))CjgEs4G-gldfb}1YTxP)Mp>p)S<~H3-p%Ysb*BXs6P0mt!%>>mZ9dh_;0ncTJ63<3OQc<TTH@!-Zdg3+^mOyZj43tSxaekRt1zZ|3WU%_%f<<fOY9nH!PfDena!<_)#{4cw<q%)Zfug>`bcM{GJ)&G;dH9+k5*m7kCQ5!FHJZgQ+9&O?3qrXwhw{{sYau{Dv-xTn*gvhWocr&AZYyoZyJfcS!&NK{Wjms);ja<JlCw()4&Un6l(`B)KCt1FO6$^TAdV35uk}yrk+nt3cSIzk3wy;Y1WOtlnO42OBJ#Q7FcRvMpu(eH)&eiU59GV(hHkP^(uY0;F9ACQxr|XXe|;JlQf{OxL0wulTW8jQ|TI6N$wS!BWIA><{Fi<QYb6=VQGWc=WQ*MYXzalvE1%w#yU55s_V(Vz9?-9N2_J?K#^67>Vg{gWqGho3VCu$BofmSw@(0;wUY;eS4V?1Pwm;^n5-@KjYh-Fjy8CnHpFg0Z_<6In#y<O8WU&>dr$$M_dJ7hY<5m1x>c&4*v@Aa$35gmBO{?N#;K#**%_<KY$#;LP03C0yTQR&was>OpW2VzVs~1^%d|n`8M!!OYFwfy^Flk5%CPF1UTDGLjU#!a*~;F`4SU)Bph9GwGS9NZk~+tEGvOpki{m;^kPCX49vf*fov|o;-IbKg0VgJomERNTMSEhVT8$Jd0PL?;^7}O1w&$DdDzgHLyJ|E}X*jk+0guMj-CorsW-MNqP_sIDEH#daU0F2pz_J!*Wn++UPB(hGV-?r^L66k)E!<sC@upRy%fjX;j_~oO$S0^|wpAFmlby|^HdSY)l{@_@<FZmT^fgVkSWv#?8XI-q9!Ya|;T&D-SSndYRTw6QY|b@tNpJO}(x7VziFzx;mWFh;Fy51+4z;LdXhJKkQY*=kq=8;Kl$m+H!*{mT4Hw`*mZ$q^w>s<)e6wh8a+%g)GFp&IKi8=?^R<OavJ-;aB*bZcY&VZ7g)dhCXxtT@oUK%g&Q3^nTB*|9<qSE2@3+*3q(@eHN=;dFZ4yJ$=man(+Za*okPtgfn(C}XT^O_}iE}FCVN}LlDmkwesN`s$(@Aok;H-`!0KCyTwyQaFd*sqaG0`uyH>FOoxZ?BFUP|}ei8XO2#!5*|R+R?XYX^!+Rd$tp-R`9FN2<+EbGf-)EUsC-B_5M}tzXv!$s!kgwOiO0>w~tFEr~mtt`Y0@c<m1DKD^$@IMUTt67MG1VTGU7G>#s-nk^hUdwqW(jNkxUm7N{;eO=+rV|Od?sXpDsht71A;`_US&d{~|ac<1UTe_rHsBGn^H5!>k#wx1|&B|xtML(JOeluGgv!bHx^_}Yi?oSRJE}foMnw@rImk2nJ=r(pZ?KBGXoaIvo&L|Ie30ElPjQvPi2$_bamuso?cwz9y$m|bO+;A}L0YBk5V}KB*1#5F?vrVQnbKTLgSV$K3wkaj4ifsYkzNu%3OkhNMU6M@qhrN8FPo&s&E-QB{McL`hhjTWu=<Cit)whegx!TG0^Mk(a^yC39&WYxvv+8fE3V>qyVP<1)4kdkhNU@uF-=5Xxql0er)>f*Z<)<edXy-*TJINHOwoqgz8=gO=kF>sU^;Ex|GLvL|Cbi{CIbjsKoHbGBjX~BZi1QVt)@P2MmgJS2XxEFS!ob)M*Q*94nPgLv%Itzy2FJ$6A%jG)M#`15<ZjavC3zzj%9T2WyRD?2nGXn|z_hEH(@PDu3yzyMI<h0QnNd&BsbrekYsFf+ZuiKQldmMSIhPvg_Nc*YK&e&m{c2S(3)4e?e+;_HCtb6j*G+|4+4Oq2Qgu0h7#(_hI!R6{c~{hjZKJ^zB`4Wp6|&Jy7cI>w(qn5fR<%R3#tPi7uPE!X!4bJ_Cuxezs#V0fDbuRWRINSV2VSGn6P=u+0l%WH^ct?Yt`yu>wKi?7Mv3XnqKApYU<mI6B^PzR+37ZIKE2m~GhxWAqaWIK9ZWA<tyal=Tf=hzvNEMwo2?Ectx#L9%7^Ol6#TC3_(qSZr_vd5l51`yoiA+~iJr{W`jXW&M`fYaNhe3Wl0L64HbN&+o8wN3bk#K5v-GK(vCN#s&-Lno9Lu{^ug*C1pr#B;(;dD`$!abgbme9Vz1z(;^J}`uR1-&+>Qkvj&2bKlTaky3OH3xEiM$;*9KOh#xgMifi;8UmKYrb)^&4tV9ozFxr;+Y#hXc8%7bPi;myFs`E0^T$s$Aa9&gVqBgH>X*ry8BCHq)f>ep*+zX}L_*#tz@a@wSpK<X6ntNKUQX-f<Ewf=Lb!=7vg*Yg8>m*rc%2<aMW&2db|&ls1Qa|3G&WqukIb_j;+oG&XXyRu}44&B>Nmi`k4wSm|tzs#Y}4wJM{cs!0W%RI4o6&bOo)*IHMFbSuf{T83FW3hm^)?(A`RraNCI4+FcTWyey<JWK?^%Btx!Uzi1^vC!x(`bPkgU9FO;wP%wdv*)<k-VxN+FsCLO>oHke9CW_E9`92{c}V0B^P-UDY+h@2)j`c^CAX6bL#2S5R;$(%c(YSv6SMMwS5j@JQFrYio0#dhCNirZloCr26}43-#`Uo+Hq9E*R~pi|!ghv2w^whrR8y?dQ$x{b`F49-TjYzpQ!Q4KgeugN)%jqZ85T;D70&W2U0hM^a-%M%6xt~T2SX>UTFD*NN^Lx4glfLgF9XM>Uu%k>w^{Po8t?mun!V{Ile=u2bj4{iJ2)na`&OA(s#1!Xh~jbF<W@p0+vzz|cR$!_V|!3CW(Mg9Wa2O#oV>=Y>84xRTxyUii-Yz$muMG9eLk69o9p$Vgs-NZ^tLCa`D07SuiAaBQ?54+V%#v8N`J3T>U}O(ne3(HPVEx#9PB<boKJIQu6pcMm1Lz`Ed;yW8H!=Dim^)-Yi`1Av<np5J+^?I?9Hbv-6oUuH0iEpxH<-wV=&M%YgH+Z%Ka^svi94mUQPq{7$$`IrdcSGO`<p8?MB(!G$f|Kb;c<=Ed)_c+-X(pBE>XwI!@7Jdf2FziE>wP*LjxXh$NBVk2Ri}4jH!0Hr+{M(JEGC`dFMy=#GG^lXY*}IGBqAnOIxHBe5Ay&C$BD>36iF-t5cu#36`CA2WKAlGn^8pX)AUEkP3^Q6pE?ePah)%l%lcPFsCS>58+u+sh`0I@9mhrj4SUF1VVRXBUmhS}c(Bm87gkYoVDLC#f#Wii%iYxRaHYNl$~2z7BxWKor|9N9L2`l_A##sm|P52(2+t%p)aTuk`uD7D)E6Mh(+sHl+&|(HT@*x}06Bd`CMZcII9$sOvqv{aP={M}S;<X{iMiVKcXz6a#xzqzhwZQL1c<i)4FPHXDtjZ4XP?uC$&N=Si!c$q1<`wJLO`)MCvEwwldK_)IC&`EIkjJr3Q~f;Jj+E3en`#JDAw3V9}x+VuA9T&cQZd1D3~I4(F;ZcuG>tmOKT-V`gTD%lrT`Ak*BkDW|nGGdv|s?s%_oiQh;9ZJM|dU*z~h}tKr;yBq)*60B_+=#iUG)a_prL1^l59z!#PFYl~<W_6J9=^?LrBsU%)V(zwOWCg7n~{?RUhkyVz5J?Lv3dX(v$+PdGZPGL0$OLR{frsb=+>&5CrY9$=8KJXCo3eVbh(wI@}2I+O(&<-&Qv{Y+H#Y~oz5PV>t^Gy&^I$ONfvhOq_E&@DamJ&W~P#n?4(pU4D$6wf>avYhFja__%<yyQtKw(7A<Nvna!)+k#<Z9+|aO!no;J*yO!Ol;knVq=GoOc*zInPn`zf{%yO$zvnPopmn=$M!tCre1t-Hb(*0I~85J{GW0fGYLTc9>9A$%XYHBjyYnsVznd~LH7QN07RjxVE6i!;_t>Jc*U#v#$4A96Os~aR(I)+u%XJcUOfl+g_EyYS4HCFERr&+@llFVjr+p~PCek^S_eGTrgvhHZr?rI%5CH3GRHO@5U?xCZv*ZV2A>X_*)Q*Kimj<q_iwJm0+0b6Lz1enW4X>|3R3yfK<v0ofhq>wKc7=8*QvpU$Ws)jSF7P32`Tb6b^zNwFER%MW^wK^)m_miZt-j2FCDNUu<iL|X4izDH7`-7FS+w~kgP)sh9*qE-n;1>*?9%=P4MeYktJ)LT`IRbb-+1|EfsOqT6DA^S?N-TQoMSe~@)Tq@att#1LoP>BR7pNSsP*Pqg4Qtu8tLe%Hx7ku<Hcg-G6<gUDU1w2GZj1O}mmITPy(#6)Jn$K+1j)|a-I1reD<Lydnd+fbZLxcxyz|rclx3A-iDU}fd@jS(Gj3->n`^Pe&6$zab|oQGTbL8zXz>BM-6rVj%-B%tLB1&OopF`T$zxNalJZs_3|hi&+iF{~TeV90`cz14jx=A+ZzL;49?B*?J<=ps-SnpU1@5{=W<6|9^EtgdC#as0rvcPxio;;{pd+ow)owKFPwMWvsLs>v18o=R>5h@=&aB^GXBOKcwQ(x4Uc>7o$>T(NP;-^(I43R)cW9Nx-GWF+W36`>kzK_(OzL!_Syq_t7N4gC+CJT6&bI7odN<|G(sX=K)y<;W>$z&DulJHNp01jiBrBLDwnt<)c$OJgcbiJHST1k#vH|@1c_!Z?Tk95M8R<;2F1SK3Gdc?Nfx!>+JVj8YhOs*tku;ajZlu&?xb9GuOy4k^c{kN<ubFkJhvWN-Gg14g3X#uqnf@ZTIriNGp;gCJ=dj`H^tig6&PPqE?KTcQ`EYQ}(k#I^-9wjNP#b%Ha7&#apvsj<b0Taz4Q`m_v-6oe?eF=j%CZxO-I1juEe=(DkZ6`19q$hkyJCLE5%O>(PQ~(kGh+Y%n@!wYh0&(`h?NdhjjUG2?0A%Jn~eb@Z6!Hy<wQ|rYb&DPud2IE+fL4U-GX57Y$c(NW=DIqZtaH2S<_@zZg$`3EO>J|F9X4BbH~2S@)?I<Y`0h`5l5c1*3BecQrONan>c2xv@#TnWJ3+m?Qk)t)}w5Ss#v(N*%yh5*%nq=XVFsZq&nA0U?R5#&QY2aJ>S%fgQMo%Vb-GEV_8X!^V@!<lvnn(W2u(6YdNyH?~XQ_I@_4tNmoDcBexnr&J9^C3)a@8NP?-dDvOIXrM%jim71=VDto(;oX|63&@_yCS2vDsO{fo?0+Aff+jw%!wFG-o?(uu=xKpiGBD2D`TD83{=E!Ve+{&!!UBL?ebjf%=Z<e#`7Nu^Tx=Jbh?x0n*tiD<#dy933+-8#LO~&qZ_&vE24{2vaW?N#rL*i<N!w0kUx|+_dfyZT=LVrTFjRiiN4D2m6JkUy?9Blbw5F$|*r3|54CFYP%_quztkdukrLLw_2t6k3wa~s2I0EjrH+5K@`C^LIj!PVhG&MO;oNRd)=pEWZUG02hnp;lsDLCXN&W@7awZlm9y_Q&-^U_>%zs!(0zsI@CFN;f$i>g!`=Q5yh-L>!NG)+tWwYeA#Zi9Xfs4%6u)3$V<j&eUdydYfjr?n0`j$HzWy4}^`iD4M-ON}XoRVrIW_RKl6sfesW}D|X&WcjyAnn0$Vwqy$mx9dTn)U#+E`JHXqNv#B<#+}Lf*ww-i!Ym)SIrP%3oS*qFeFukLsg<5WAS6R_2F6t?5k-}w*n63vsLDs94;Bb6enTUs>)y?d1j!hVczH(F(;&?GRbSCz=t6R!oU$GXmInURs`6}Pam6c6p+*~QMNoO-U7OExLp~~gMq-Uhe{=BsqrY5cZlxQ61;#^=hN-GHIuVs5)Xl12CVxXovqvH&BdSar^_01WDr_Dq|BviA+iJ3t;GwG5=Uag2V0Cfkz7}%WK)l!GOm;pZPkRxhtvy(0krU?r_N+Qc|rbV+bYX_Nh^Yx)f9Huo=mUMXWM}yB=OjTBeO<^dMDl2^A<g_f^vggGHFXWYknN)~uiJH=_VYNEV(oA~Z?lAM5LpOP<V`Zw_-FVo?cM3`Cgpi(9lfedH6=?b5u&KavR3kwh^ybY$Bfs0xh4iu8UyLfNQYO(@nfg)N)5lSzEVtJ+t`8LJN>8SH`N7O^`<-!T-In?-O_E4qJ)Mau$D&MYTJKcr`03L0(T-9{d!~+Z#C%AMHMTEN8G%nzr9`tuXR`;jWle^CmFjgkdT$k+`rhJ`q+KAp1DYIHI@x`f%4<dL*hx+LRoy8ZGNy}H!Iyk}X72!U4GcbTf2#9lC(Es-R5>e9r9*Noc6o}hs)pzk8wA}m7DN{}S_i4^&Sta1Zkr;ze1hFEQ=Af|tyoWH^UYP06Xt_yuiiI~ER*V#w30YWJEY66gZr3L^-klESUCE4E~GkQqOfSDgu<4?nOR?)&N#*vY<bb1b=|6-SBe1sjRgfCWwq-1khk<4M<s=$<xoZ3V&=PU7SATxyv<07ZL4Qx$@O~C2s{yToR!+C@pJsE`>*~48x1Fo-V-J(ICi&a^sp7fZf*Vk0W-CvZKkk0Q8F#fIADy*VFnLB^WZIS5=qBQC3gb(sAG4)GMFM}X?qpZnS-n`-2LNMg;J?I?u?ejLa8<GEz6Ao_KZ!tgBJRj1g`ROG+b6CnK$EK`Gx4hY+0O-Dnn2-MPfh32%Mz+UtfLo6~_zy2$u}YYPM=EB~{Sw){Me0T}6JvRtJkWA23;C89DUi9((gsjFVXFt!Wt#;Qx0|h#CrSF%QdUoiR*)i7LVNmhdshSj^q2oqJSVw@vYR$;z6_FD+)hWGu@t&xIc1Jy4*dS&~rZ9f{=|ps~1D)!;4LP_g%MR<aIDiHkqMP9E31br%P8TLzEsG0njIE(D2}xuwI%Hh-Gp18Shb#UJ8hb*qA^jdJ|{0re65i>sh;{0WZM>p({jKHoH4!453?5U<%_vBxHFTs1E94ll=_UTp}Kv31Z6epTP$4O7z8Fad%`4{=aBE`YD$x9B^3^}%O>rOyK<Bk)UBQ*<y8)w)B2c*4NyqU8p^y+uaPpAG)ev{!dV{O#9YC!c=&v)G^h^v}L_as18KE+M>w?LVM`_m7~Wq~FD{$N2r*Cj!Ucg%=Q&!6d=|0L8-lq-qu>sn}io5w!IP>SDZX@>sA+aewTr!7~<rVqb42h;mWpJ$>UO0K1?FK4Cq^60twSI$*j$KHx7<m|5{MnlyL>Xar{t%Xw1|R^*xES&icX#T;*$?tgOP+Q>Wf^gbY)#KEzGGD}WlZ3Pnfyv9W|bWEv%Cmy5!<aU*ieE4<R@JUEGpwK<PCfE-bf+%P*#~aUgC*nZXzE(K*$-5VL1-AaylaqJ%iTE;}c(q_4o$v0${XZ&OFn~LtJwQqGd1To91MdQbxzx7kn^*WxupZElyy5Vkx{aF{l8+=L6{Z`!Ai0Q<7>>g%N#T>Krm{THrx@dC5{GF(0QQDtN$MIr<d_3!!5i%(>cF%ZMSq5^!P<|2-R=+<3-Ie*{72lIA1QBsG++Lx{v-NFL!ah4V3KEV9!ViCJM!}VYb1!FA;;d`e^{awevdl+uzYXZ688vyP@q$hci%qc-hFsHO1`}TT=0A+#G$3ZCX$Z%8~_*pYxQf@|5^r3K4I@KrXZP`pcx8d-NA>Z&a=-k6ELgFnX&s1U;F3-{S)FPutZp+3|jHV>n~aC9Vm$2b&!ntZ{f<LS8X`0(_?><mu*ix{d6kk>nl{S3SORGKvjjF4mI0gVRuMAKftL*S{&93WIA&eo=0S>-kTx=9xsvTdvXff^2(ls=2lrxZsEA^eU<=vMtPRB$0B^+=-zqH_YzPcU~vRsb{`j#4$beKSNI{mk3XDVHGlwBs_g;*YxfvqVvNCxlEXipCgDGLgp3JHg>e^;3^4u>QYE*`M<ySCK+}DtI2a>`w8EnTtRLX3M_z@B>+U|Vu%<0r&)#I9<?xJ>ugrKu0;Y;v!d@Ou-_RHzmH+~v)}vb4C#~16uc!p<?zN`w|CeX9Z2sh*3`PPrU<fqpNYmtsVQ63?XPkv?#gG352=!L{^xc2ZF_DolNPTSm>APRD{z@{Irbz4((cumX?L&A#zEy(HeFO8#M3{XT4q3J?^KU&X<NbsHDFlwdWMy83)$V^v{`eB1y*#&_{qY-21~Uqn(E`Tnw6HfhFvO>@yW1QG{{ekuNWA$Rum|J^8ED+Q`=3COHlN=*kFaI<1!!plbD&Z7YrTs!<xkIlcmLB21&s)Ngjxbi2|t?vfq36vSxxri-+QxGMd{Obe{OrLC~BX+{eM}^`uKmV*y_`F{|3<E<9}7x@%zhRFzVsX8}`zaj{Hxr!0_cn5Rx-(C0y&e(5*#_bd4D3r8%voPv8Dp!qktyRj*g{V(^eaz~C^3Wy0mXyNf5|4_N%`ujBV<sPGdU8Cn(i9pIzj`=hDLk_BtrqbZ;={yX#jdkh#Z!ta0ihrj*w-G2lk#eMqruhl@lfO!2{hZFc$*W-t{?fs?hy3kD@{`C3G2QRaME+Ue_fkfKFoR7bXs(S3xcmD~q#6SEkrhNMDH*7@UgMUzuocJ6{^`*x2G2BI&=uEDr8&#txLSNGvF0J1%(4`2CMeE*&I2QV6KZZYU6DM5nWo8QCLUcYCeR^Q^E^b@Gn;cjugV$w-<u96o(EACt75A(z@3OpZVRwPvDKea|dL9NqPXcs-M*2|cR=p41q4#?NZHV{rC`+qH9)3jX2{d^o+Ra(FJm&lTFF$?v3)W}NU$fX*{Xb#x1T<}+DIh0;p((Ic54gLxAiMiLvAX+xP`djfJP*Y30s6#{W!~O4-VZNefOls?u_DiIP3VjXlFBi%3>>om%?CK~1bEDwETi*C)b10&4aDx=;&1ZI8=>%~`tE&(`f&fX`Q!f;*?(XNAL;YD1BUflM_Bp}DsS&Q(BuTvI^MUp_`640+w;a9cpkw}aCY|>8t2x+p3s|b#NWfgeu&!gsMmjn1P?d89QQ$X@8OhQw&BS1doJJ?TW_e^U^M`wmyqr6ZtE@~;8g45e^!82`t<E@4v<R$#)P#$#821<H3sy&h5QRo^#3Si;M3=2%z}DEuf6X8>-m1PZ9uQ<R10_o79*(unBVanfJz*II-qml6jvFb3~tlRC)Kbr95%Wg(9g~W4&@RCuz2q7H0|L1IY4yk4U<gI9|!z(T?}e^zrbg7Md{PGf2CrUXFtHtv%n(baS|)+&NCQ9fG!khNzSjmw-j}MUNp!BK1qCX2Lsg%X)US1uRcxZ;gzYL0t(MTArF5q5d=Q?<nm0C|3>Fk4mhpn$lBd~n4VX!1A@UJBdVeh%IC&(C1gH}07hM(BP}`uT=f^@EQmkO>+}kD-T#vZR?bUriOc~B<Uf8%aOKPe;d*`uqQbBuP~E_*hfxHCPq#d;o0w#o7!2IPp|Y6C^IY=G-B7|GPc{JdV(|(vxEAl3fzzOU{eK?KmF5TQ9;S!SA?S0s-Fu*wSw_`V$!`h1eF1aT1Apl}-#`oRYzFhXNP4~A@}^4dZl|(rcT0u#lJ1rp)kdX!8EFcbkI{AcfW{NdIr{!4FF&6eyIB^p<T9AJ8SxyW!EPNu105*cD3j`j1Q;NG3ZkIk688W7%YTO;27r`*sa&AW#04%*U{Q1xZkBk&PV|Ld&A&qG=^F`pF~Ff|mwPgE04#E6iM;0ZeIIRs47Gp&F2Fz^f9)$dpw%=0m?hYj{P9-`=D<GKXbY)O3#cv&jO)KvMa=y4-R~I8XCg2SPX#@I_kZ|X23v~~63~nB;Gnfn-~H9Wf69uQ#PZLQs@vdY3AFqR6(F)8{(I7&e!1s39`_aK)f*yyfpC@_ivI(zl;KuOQ{(~A5#o#j#fatKn3kr)01kM(+}Rpn#U8Msg<56VDbSVs4<R&*6s{j@M~h|f3al`w(A`mGIV?;n4{@JO)+oyFdj&7oK@8vMRJ*5&sD|GuFP~=S#j{C(vQzQ<r!#jxzoH&bG)bM>15o^?__jZN_je3h(qE`ST<|4_4Mi(oj-C793I*Gq;~w$j7fa;F<2_RteVGbgdX^sx3}cjke*YJM1AWW~jq(<7?9TyUG8lxG;tz0;f#mx8W-o}Yp=s9AVD>)u3Gva{7xa60`~Etf{ox&U=iB{DPZx~fKFqzrE=DXsTA;^gh#v2PzL6;ozIgM$?$OizaF6c!EiC&ksC34ZUR6^w09jGvkH%WoR(J6qqbTtG!<Iih%Z#$(7)*cCL-<jFju$}jFr3PJ0rPP4Ft+Zu{`OrM&7ko-`KwYwA`gA;vt#v$m0_gCCuk~<e6XJ*{iOv(fS`n=8H{nS8C;+Z+Q?-?k((suN0z}S6duOzDyqf9?H179Z!84YqNHaTlZTP@yMXk2K)rV-GYZ)Rik3HxlcYzYWboheVfg@6^X=&5oyTqA3Ks8L&q6#J;>P~Wo4{3A9K2{xE(71-Ap-r6$ft=%ooXnyfkz$ksw?Q1q^W^hjK*<lB@qXW!nFb7{C`OCpLop#e(zTop%{N5Af66B0#d;iLu7q|B!wm!7}7g0C<;qFc;0yg`NEO`tN3mX<dswW6$M^bpT7I|aCpC9FW3Su7w}Vg_u+2ob+NqnLTmti89*7`!S)}Bd%p`rd{F!;_2ChF4=V(^98_5GhQHG+p<R`b-3i8XhXb|}p^-uy6?o+F2mAqrVnJuo>3PkD?a~D`o?)H0Ua>dCyPtUDJoC=k+Ru3C{CSQbm?8$uHw~Q&Pj;e~H;K76Vtx#mXh>EG2EU-NA-jG82N(s~{rLAtL1NfHodKre5unMK+vR~bm#PL<<kWxQuAlk)XYmKmJA6XVY!x84Eil?)h3^K{PXOc>>SM@2M@NKce$(7}ym@jSe2azT8wRRgm+%X);f)V2axhlV1PZL8Bn}S<ZqM8vMtS#94nG_F(*|~6@IP;~>wa>`OIACuqvrEx9jZWnMhMDlAAhBKQhC}FS$+EU??4~^BC>#wm=_e=!wtRm81;uk3=;qN=Q^;V-~Hy?xcc!|ho50+B#`<4cge?<@*n=z1_JQyKb(VkehmZS*!AOyouUK|a6c<D>KeG=X9bF|$ZNzo?;?kU)yGQK%>e=&avLZ8*y}9-NxH$m@e_Ldam4Q<D#7n1x+(Q?>!-E8)xjB11>2K1UGwmsVHBS|K}T_EX+E$%!KyRF49hGEil8tG9Q}-LKVrU~P2;}iN_s9s5JpK8zMczw2gooUl2iHp5+=qV2J_RK?p}$(`9ANTU?@523G;)6I%As1oPmmk%J5CCME?ZyHu@zKtR)YqY?u~CkX}Rr(*#UX0GZ53;Prb>IB0^mo>#yQW~j$ihVp~qNZyy#L1kE9j=Iy%vM?N0Mkg{xf}E%c;A7vev-AdgTl8rFG;OTI@3E0j4u4zg%!i>3KZtI@Ji#>YM8*_h@Z1~7-6~EWhPKWdLmu#w)$<8MkSQ47m%xm{!lFpOaR6(KM*Q}PAm2TB9|`j5-2=qZ_g}q+LSBo>`<q(|;FXgoD_7HtUk2qb^!BT}#sFZy5CVpEZ}QenSK)i>(D>JCWR1>Y0qa7yz7%8hRjo%50118t>^?N_zl4JIAEd{tK!L{@XKqDC2Pn$_2Ou{?15J5ja0rsP3K2kqb=`-r;K4|~QU5!7@fWM~d|UP}{bW#=3;_`2t0Gs+AJy;w;>uTh!Bva;{h#Hv5JLDuH#@=^FFM=4Ek?_FnKBdj6E{<Bpigl#p$5EoIf*72&7O&_H(b)+vY7h&pF>~@IT$JS5K^^1{z?LK0gC+BYJ_)x63p=TzeKgSAOGRx%z0eqpr0r=%LqY)Ypmrfze2AC<BZ?^9Sfbme}q6I^?>;^!N}|*{zw3=E`9_fL4?2vpOYh)3_!_m!7s0OfIa>OlVSAB_J;imR`G4J@#(w2l(3KAoPbMYSrG*H4Ik)=fgmu9-hcLmFy)U!8=nI;VVD5K><!8u{wD(>ryhO)5(y&<Rs`tbw|+iHnCfAK;UNj%Lps5ba8AexZus~yaRYa}fOw+T;d5J8kbz!=pWeh`A-6cZ$ld_qB0t7%x;xMs8`dkkN#U)WTQvd}x!CpjDn#|z*D4I~{NWoY>&D0bjClCle|U<8mnMc`zz9{mV6d+M&_>4g<L_7z<yinpW3ltV5DQ(l0gO=@0V<#iVW8Vz#*g0sY#^!PWpUv7jzR$?Z#xNDQvZP$D7Qp_HU7~;9CO(O@Q!O>-Mvi-MwWfqg)4tqH2sM6Y+3e)2756<!H?enf<V9#dr4))MzDJ@7%$I6l%gK`&tmsi{D2r81tD%M{H3z^>>l2^dBo6ORNCA5&`x3UTkPcp_c`nt`|N(BFZ&Oe7wGoCf|_WbXBm~GyR-Y{_3-ct3!}1;rKr^#*r@*TUv}zP>Epla)S?Sj4D-TM>>)C~TP3|Q!IF`&M~ZfB3*d-g)Ua%KJnD@{%W9)tx&O*{H~dm7z`_dec@#kFVbEJZaV*nbnLtYbfkSH6e2gfN8`Aq65a@P6xX#bFWchldZP*<TN)<HRhoI3L`*Gz;savj;{c<;24pbxW>Y8DBJh#-)y#Gh(M{hPSXvi;P;jq~GJ6ce_eFxRsrM_JAP(9$Xy@5U(C=&7X0y^LS5hDBYKK><<&fWuxllgnE-W=f2!h5aWOs<;fdFgW;3f*5ML3oRN;ivcySyVw48Dyw}3>p-8SiZV}>b*3<^7y+K=Y5Yyw1pA-@#AR-v3n?@p{<HA3;8WwvCesOB5WjH;Fgocd-LWE7EvVNLG1n_Abr|KILD&>Q9NM8l~NaCeqfq}f$4JuG#2)v03j~p(=i{_n9wsj2dO>Y4+7PYG_kOo0oEITK&iC;knS&_HTL|B;ZL`SVDd80T1aO6x^Mj|Z!qFrgzsS>ZX1d{BMI=Uzi19;(44D)(|)H$D!*bDqbM0^jI%y_L<c^A2Oio1_7oPRCa~C^^?`AOYiswilJwg+Wws+`4%?Eu=uE>pBs?wPEPwp<A@Kf!+@aHU7!WrPP{2W+r3Y%sSCbB60B^NXp4eGLL&*gI`glIl348qYiL_CB8Ei6uk^OsbW6xvxOTLV7BjmW-{ypTY7!f<K#W{Bf%qT+t@IE)JMaH5YJm@s!!^bXtcsSJXIBq)ew{!45pI{ifk&x$g=w;-E^hacZh;)}hfmajHB4T?T5QtrKmltz9uRD~wu;G3sYwkrebEEweFTwUt84Jtno+26nC@DV}0q24wov{%N1G*>}kYGr_o|$mJ<o$=h4HUKg5*^g@&N9M~T38s)lR!z&w`Jpp+1Q)Q^83GFe8?f*NOC&+-#-b$*$~<L&ZUSVd={L(W%#bo7QDVl6+{Gzozp8m!|>6}Aupfjl#6g$w^v2tGve^ahyqMuc*d@>MbSGCsD_izPQh7p{uc`vA~1h94gz20d)>+feTKt$p_Dg>%S^CnPoMz&6)ABZoBt{DHZTH9@1=h#^cq>81t?-=PIP#oa1@ZAk3sv80?DhN-hP%>>^&4Vf3)`>qQTv>R7O=x5F7-edOG-fiV#A0@n;x1Xcu{p;)VB7R|#e^0u2x?7&>4bJ7o~VV?#dO%$Ef^>>&7sKO?$l%*Qb>TmdF5dVy?g_3{5gK?7iR!?x0s(Et^KB~U_`^rG{}Ks`Oc{D^1o=@OP*g75d?WR|np9C^aSYbd298K}tHi7c@f6IlQ`{H8;@?fz)rMy#5EfT{rDDJpPz3MG`<Av~htprb(N{x0%A{6Z3UIVAWmk{g7&d&z|hD-mx+bn)YV_3YgXpq!IT9pDz9QI;07g2&ZhC#N_alEI+Be?Lb0r(>56gvYv<{^YCpfMxukAQbuk$vEZa5_|#Q_{;DbpL~&rH5`q;muKa*{X_gJRP)NKdfB7|Pa?%QP1OwFs-0|3^ra6fZd;@ffNfVwBWPp>jY`M2HK(^5Q&S%~ThYyv!}ACuc@k?up5|54296P9vXb<SHZ>lQd#qZ|<b7~HIEK!O#r%6Ht`V(A*|7I`W;AGdu3kt{r_0;%3YS8=UdU)c6BT&{A4F;kyv2%u+^FTN(iblSor9h)FP7@_sPuAezvygApojcKwLt&GZpP4}faZ%D_5nlywa%6?=7%;ztoy=5yl9StY}xIRL;(d@njoI?`AP_7oNELTA6OBdi-Y;7aM?cNW`)jXK&RLawnLM_=Ao}>gU1l<1O$i#hN^Js(Jp4x$v(%3{Nf|1zWsRdHDgDL`dt0=IZj8D_F7zB@$vcH6_3NVCZA>P7a}&bPv8Ac!e9WGH?8pW(e5b>Dj1Uc!}c*W+k#of@Q@f%K12U%qDvz9H(3Cs24jGxuBkwUYpcxz7K|R^b0m}Kfh;*84R_hvS-U|Zp1%o^Z!Z$+T*M##v;RA+-)^aC^!a5y9S|dl#e98&_BBD>nC~LnmLxy2ntmYfu3LD(%H2+P5Z;pj`UrWhXA^SP-QfanV<(~plZ?FswSq6NSdY-4{l*@l$%x&wAbyD-Xg0zOU9F5t^-^Ore`PDE3`ql7{+d>|gyY0muu4=Yf?zV_dh{0URRhL{vj=PlNNe8t?1`GYaEcb1hJC)`QPVE!4K2nLKU>d)r98JPWSbO5wc&0O7>)FjWs1c-&O$PcF)GFwE6Fk#<AAo+O;OS@@3t#+YXs;V^Y(Gz5jM$!7v!MmD_FamK65hUW%(9wZD_V`K7Mtw7)hkJz_=M(MlFWUQU(@jFY;h)4kO7B)p`47!K(Q+O;{Bmv%M(6shC@D1J27VK@b;y4I;xRO~X$odW?`Fz}c5r+$RIfJ^3r(5&%$oD+mfzXQ0bpw?}?^r+gGY2hI-+1H<x5bsaT$klUAy@^VsWk1NYT<x#L@Sz*A+-36xN^*$rWJ{SP>ZeUstQ09Mk9e(tZD*kn_B?LbI%>&wsc)*qq0J`3#-ejm#{rkt*sgL`w{#bMp9q!o|yXFr+#%{gf*9Sy}r;*V#WzUZYnD2VjK9afnVkiTFNbG_ggfD313~g?;@Pm*}lx#1<o`3NI?)euG_*|3ZPcRxOlt2(TjrU@y{>Cm6FB^y(ltUQD4FvSjuZ{-@!u*URhAcXM1Aftk&bZLV&IaHLcljecsqxn_6rlbcV}n6^n<N3f?qjckt1qh*LR}~9;8(nlMFr#<Z=G?Lm!;;<3Z=&XH^o{)%r_P9eQJG(y$rXmaKdZ2>wCeiFGg3MaQT?bcl6M&CGSW8La+c!EMe}13oIFH`2&LmJc}7(=&i@L-u&eQyts!qfS==~R`VhdEKHU_Ddy}0`F6~N62<#1AtMNFBI*EG4tP}>OodLOY#VIcz*t~iS3IB}kP!~ERX^9kV|jl8&Ty@YI_Y`euL$~lMc9*9@hrqVIej{>=D8T6!gG{%k>z-fuE{0xeZE@$b6L-@Kfm?+FClh~y}N~puOl2$0{n9X(9sdT45N{Xdj&;*2610KjaG{CIjRwT6fJI|OYl&!SO^coDEvP^NdL8ZrP@D(?XfQa_g)e((%WIShk7^q;HSVsp`)&`pT$1w9$YQcwV&|A9fcq4DPZ5jRk+$ChG|(>R^@BeBQ)Az^v)BQAAjZFsq}Nq({87fNk7*aZgYl>Q1m=ttb{75Yv$nPf+sOJ>m=q)A&C`aIbz_Df`mKL&oIWSnL!Gpg03En6#K&T)^HVgzyMx<f%yvg0VX6{Fih@Wuj?rikDhl|*Ja)4>fy$nT9EozkKqKOPouNBzWKr*Y_wP;l6qbcn0p?&*8w8=;A#f+9_2d6ZZ<_jY9nTXL%dm}2+-`-ghk+gj~h*bmpvg0-ruY+Vhn(IPnaA<q9CE)#w_$^x#EG726WZU+8!64(=Yw1h_EkI@jEmbJ5t5(jS(#VrJCWR>!&>N(@htVgz-quQb5gU(uddREoTO$1Dx*%!9t>T@&~;X1JAQTBIcbu;6g)0@)QN^C=B4EkY&J{zJk0N2=H*r^R>|p^n?#={JWOm{a$BVc`KD5Xb|OY_%ei^-Gy!JC8yuE^)K4{b5l2m`Q^KNu$J#chNHXDZQ+O);;mKWT9&gP@^ZlcO2HOkG(T*{E-HjKLS8L$;pD)Z^}fVB{&Np$eL<S72kKAPk|C}AB|QIXX7cy2B;QYVBFE%km!a=3M^Vl5--PqO`U3O&{cPwhlNmUhp1rw|jQjB$4Gb9mKo;(wm8?N?88wz)Y$Sh}ar_=e@%tOY8v%*X0sULh;)jJJK7(%lNK|u5LI>0HNN)Zy@*g>Kaj5{VPwpWDc}YcdXf}NM_x6FlmolGUPi(xA191D2vs)#@+U@z~oUgsb;JUVpvm)V2*9#d+jJ#M#807kM82A1b9W)a^0)x6@R7jq0|0;B>0JXMMc-4L(FZydW2C!M|Ifnfh%aYMET=1Cvu-@ol!v@`JS3tRPV^ArLLLR4sKT?k*5jFWY8zcNgvgBnxZa5G7;t(0>U-AO)s8&zc86~k<5ByNqAAfc5u1LD5mU_g7=++kn%=U2cl8U@6A-fqVkPZq!s;cXx`g?e17CJZ=KDc{PD+6i)jp4b^P^!*5Lf&-;7qLz(`-stSGXhHmw=~fytUYO8mdib2Rdmn76y9}0cpokc<sY%O<N$8HL%)VF6F*vnfXC2z8H~n{l0pB`f?+t;yetZqs>B%FmlOpnG~m~8&*=*agLSF6Iy}n-<LDKYH`W)cLx9zxC7`^@yl!1A3;`CV;DD|S?9K&Tkqk0ClAdRfgxfKH&s=tz@eWBE4C?gmROg&R2=~uns;7*62z7ng0$8awx}jI`Zx;d;FUx>cqHUA66?oqn5?U{bbOqW+d~@9_STo?dBT8Q!F#t<NA8x$>3sZxC07J##9TXQY!BPyj(gk0VP!_;iY<c6dJRo(jWOt%{@W8nZh=G##PT#ho4Kz#=(?ty>cz?r+7c(K@!my$QxES8>dD#zGfFff+(gVW58>}=$aCr6|-ar0Z<+8bKWR_S3@QZeN3L^)*1olTcV0YdJ>9QF>UkJLd$(RE4EpQH_!jse&qfNofAsA!JTNlp(b^A7`0(keT4m?;3fa3+}Q<N_oKsW$A-(I|hY6b>#+3WEEig`gFZ#&~cyQZ?y*QtxwNMX2`Wdo{7jEt@9^+k#Nqkmc}`kaC)!n+{p;sqc|_~`h>Tk@n)(V3V(oiN5vA>#w_+J5@(?=MQ9lymT>2Q1MB_2A`ozXN>dT|NL-=H(VB{|HWKuMX}iU7f`V%BPVPNur#{TZyR`#WSaq@h_DC3-D4>6B>!1;&V|e=NU84LjmUduNf~+aZxNES=}4KzG(S0emY2=h@8NLsxET3=tVsuRPW^&%|#`6L+Tlmu;|3bO;mPK@AA?$M5gcw!;A71l(vt*wGiy_T#2OUhkMZ8G+fId^*}~<vhIL%UbF%h-rE=g+-vPMWBUX|4jm|la*@OaK&xvCn6~WQo{0Y1#YG#L$6zD(bcu)>$#4Lm>dXuY4|`u&XRt&gU=_Z(&?#@iFeymG<z09VFIKAm;cp6931HxV+lhTaR^;_5ooIv6fSM3{|5=~z0~WiebNBu;UfzfMa8&K&j-My>@h@ZHd7Q&nS667qT6MIE@zsrxpb&%p`4jdY-f;1Ah${cjM*KQB@86K>QPL{}Z*_@<+6mp52Ac!pi{J82yoS6HUA5tP$=Lf4y<rhAnF@P<rhvaq93XQA7z_`SgUNZz7W}QjTYshtyYY9rLZ^SfpoZs@plw#@)x1B=0iHh$pP)R)*x?z&>yu`o_bFHt-IV%-&gjE5aemDkpyVlx6!TCx$^$2tIF1MZhyKo9jQZk+5MqD5v2@ID1l>M<HK|PS+S>}edY=v6qhz7fOT}_QF?0>uaxbaZW%8%4AS}OrPvDpH_V)*uFye5UxCnrIEIdPk_@a6qwg}fFzo?#pAbqrE>WgafKBy1Zq)zk%$bQK|WPgJaaM5fPMu3)#EH4>^^ly<2E+2P7^fwA*(MZ)B>`cHlQxHzS@iHHpA*9^tkd=4+Pe>~8mr8oq6orezg<2ytyM!0&-4L<xlK2E*!Q5qSeWI#~aDBK^>I*8JV1KwG_4$ha!ba<*KVOfD_yFO`aLHD{2e>i&>;-*zg!XR~giFVGkpIS8xOPWPTZUI7tf%0LF(=G_qX1kd1p)sXFX0mHPU!ze0k|9%bOCO>gA_MBKVS*{fLrw;bxo9j0mgshJtUwXsYe^=#Eml9i!!MjWgrm)#{lRp_ePOCTC30{6k#n5$r!yTJp2~Y@Wus!;UZ+93mEkf((U0Qsc;eaM{BQ(P=Ud^dCECl60z;|xyf*m45Iz@k+^UfNZZ$ru!PG(8o#!e7%rPXui5J*(~$Bn-y#z(30L9fRb1ghBx1@?v^V@R<-NSVk0e}(3Qbe>;5C4NHwc`DYrq=JUJhs$6u&N-Innu6I<{BxgNJ1HBJ}s5YQ6}j`_azO-#55*B?Af`1=sXlr6ynB(SXOEE>HS>Nf5hqaR<-YLwdv}=$N{NJcFwY4m5HNXdKm!CSds2bK>VaIS`}+^YgJC%9Qm+9?dE7%3bZNg_D0?y<6cj`{8PMR~N#2U504tUwzu*4=W95x(3W2G;H0vIhwE4^R5UaqK3TA@F-roN%cl+0%-1SWiaRt-eK>pgU+MN+#i?7*I6z<0H_WggfFV_+2v~$X0-nX#w+33W8eP_-BI@V=!M(=e>W2i+W'
# GUI layer: backend runs in its own namespace, without changing global stdin/stdout.
import base64, zlib, types, sys, os, threading, traceback, json, re, unicodedata, subprocess, shlex
from pathlib import Path
try:
    from PyQt5.QtCore import Qt, QThread, pyqtSignal, QSettings, QTimer, QUrl, QSize
    from PyQt5.QtGui import QFont, QDesktopServices, QIntValidator, QIcon, QPixmap, QPainter, QSyntaxHighlighter, QTextCharFormat, QFontMetrics
    from PyQt5.QtCore import QByteArray
    from PyQt5.QtSvg import QSvgRenderer
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
        QHBoxLayout, QGridLayout, QFrame, QLabel, QPushButton, QTabWidget,
        QScrollArea, QLineEdit, QSpinBox, QComboBox, QPlainTextEdit, QDialog,
        QDialogButtonBox, QFileDialog, QMessageBox, QFormLayout, QProgressBar,
        QSplitter, QCheckBox, QTabBar, QSizeGrip)
    import lz4.block, requests
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError as exc:
    message = f'Thiếu thư viện: {exc}\nChạy: python -m pip install PyQt5 lz4 requests cryptography'
    print(message)
    if sys.platform == 'win32':
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, message, 'Township Studio', 0x10)
    raise SystemExit(2)

BACKEND = types.ModuleType('township_studio_core')
BACKEND.__file__ = str(Path(__file__).resolve())
sys.modules[BACKEND.__name__] = BACKEND
exec(compile(zlib.decompress(base64.b85decode(ENGINE_DATA)).decode('utf-8'),
             BACKEND.__file__ + ':engine', 'exec'), BACKEND.__dict__)
B = BACKEND

# FetchCity version handling: only use values observed in LocalInfo or entered by user.
def gui_version_pair(xml):
    metadata, _ = B.parse_localinfo_metadata(xml)
    return metadata.get('version', '').strip(), metadata.get('fver', '').strip()

def gui_device_version_pair():
    import tempfile, uuid
    B.check_device()
    remote = '/data/local/tmp/tsstudio_version_' + uuid.uuid4().hex + '.bin'
    try:
        B.root_shell('cp ' + B.shell_quote(B.REMOTE_LOCALINFO) + ' ' + B.shell_quote(remote) +
                     ' && chmod 0644 ' + B.shell_quote(remote))
        with tempfile.TemporaryDirectory(prefix='tsstudio_version_') as folder:
            local = Path(folder) / 'LocalInfo.xml'
            B.adb('pull', remote, str(local), timeout=120)
            return gui_version_pair(B.decode_save(local.read_bytes()))
    finally:
        B.root_shell('rm -f ' + B.shell_quote(remote), check=False)

def gui_valid_version_pair(bver, fver):
    return bool(re.fullmatch(r'\d+(?:\.\d+){1,3}', bver) and re.fullmatch(r'\d+', fver))

_GUI_FETCH_CITY_ORIGINAL = B.fetch_city_live

def gui_fetch_city_live(city_id, bver, fver, city_ver=0, out_dir=None):
    bver, fver = str(bver).strip(), str(fver).strip()
    if not gui_valid_version_pair(bver, fver):
        raise B.SaveToolError('FetchCity cần bver/fver hợp lệ. Mở game đã cập nhật, đóng game rồi kết nối ADB tải lại save/LocalInfo; hoặc nhập đúng phiên bản thủ công.')
    B.print(f'FetchCity: bver={bver}, fver={fver}')
    try:
        return _GUI_FETCH_CITY_ORIGINAL(city_id, bver, fver, city_ver, out_dir)
    except B.SaveToolError as exc:
        if 'old_version' not in str(exc):
            raise
        B.print('Máy chủ từ chối phiên bản cũ; đang đọc lại LocalInfo trên thiết bị...')
        try:
            fresh_bver, fresh_fver = gui_device_version_pair()
        except Exception as refresh_error:
            raise B.SaveToolError(f'FetchCity old_version (bver={bver}, fver={fver}). Không đọc được phiên bản mới qua ADB: {refresh_error}. Cập nhật Township, mở game đến thành phố, đóng game rồi kết nối ADB tải lại save. Chưa áp dụng clone.') from exc
        if not gui_valid_version_pair(fresh_bver, fresh_fver) or (fresh_bver, fresh_fver) == (bver, fver):
            raise B.SaveToolError(f'FetchCity old_version (bver={bver}, fver={fver}); LocalInfo trên thiết bị chưa có phiên bản khác hợp lệ. Cập nhật Township, mở game đến thành phố, đóng game rồi kết nối ADB tải lại save. Chưa áp dụng clone.') from exc
        B.print(f'Thử lại FetchCity một lần với phiên bản từ thiết bị: bver={fresh_bver}, fver={fresh_fver}')
        try:
            return _GUI_FETCH_CITY_ORIGINAL(city_id, fresh_bver, fresh_fver, city_ver, out_dir)
        except B.SaveToolError as retry_error:
            if 'old_version' not in str(retry_error):
                raise
            raise B.SaveToolError(f'Máy chủ vẫn báo old_version với bver={fresh_bver}, fver={fresh_fver}. Cần phiên bản Township được máy chủ hỗ trợ và LocalInfo mới. Chưa áp dụng clone.') from retry_error

B.fetch_city_live = gui_fetch_city_live


# Theme preferences only affect Qt presentation; saves and device settings are untouched.
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QColor

THEME_FIELDS=[('background','Nền ứng dụng'),('surface','Nền thẻ / ô nhập'),('text','Chữ chính'),('primary','Màu chủ đạo'),('secondary','Nút / tiêu đề bảng'),('accent','Màu nhấn'),('hover','Khi rê chuột'),('selection','Mục đang chọn')]
THEMES={
 'pastel':('Pastel Aurora · xanh tím, hồng đào',dict(zip([k for k,_ in THEME_FIELDS],['#F5F7FD','#FFFFFF','#20264B','#6C7EE1','#92B9E3','#C688EB','#FBA2D0','#FFC4A4']))),
 'ocean':('Ocean Breeze · xanh biển thanh lịch',dict(zip([k for k,_ in THEME_FIELDS],['#F0F7FC','#FFFFFF','#183047','#2563EB','#BADDF2','#14B8A6','#D4F4F0','#CDE6FF']))),
 'forest':('Jade Garden · xanh ngọc dịu mắt',dict(zip([k for k,_ in THEME_FIELDS],['#F1F8F4','#FFFFFF','#17382E','#18866B','#BDE3D1','#D9AE57','#E8D6A7','#C9EDE1']))),
 'midnight':('Midnight Violet · nền tối, tím điện',dict(zip([k for k,_ in THEME_FIELDS],['#101426','#1B223A','#E9EDFF','#A78BFA','#354266','#56CFE1','#574B7A','#423568']))),
 'graphite':('Graphite Neon · nền than, xanh cyan',dict(zip([k for k,_ in THEME_FIELDS],['#141C23','#202D37','#EAF4FA','#22D3EE','#334955','#FBAD66','#3A6070','#1E5967']))),
 'rose':('Rose Quartz · hồng thạch anh',dict(zip([k for k,_ in THEME_FIELDS],['#FFF4F7', '#FFFFFF', '#482536', '#D75D87', '#F3CAD8', '#9C80D8', '#EADCF9', '#F8D6E2']))),
 'lavender':('Lavender Mist · tím lavender sáng',dict(zip([k for k,_ in THEME_FIELDS],['#F6F3FC', '#FFFFFF', '#342A50', '#8B6BC8', '#DED4F2', '#68B8B0', '#D6EEE9', '#E6DAF9']))),
 'sunset':('Sunset Cream · cam đào, vàng kem',dict(zip([k for k,_ in THEME_FIELDS],['#FFF8EF', '#FFFEFB', '#4A3125', '#E98B4A', '#F8D9B5', '#D66E88', '#F8CBD2', '#FFE5C5']))),
 'arctic':('Arctic Silver · bạc, xanh băng',dict(zip([k for k,_ in THEME_FIELDS],['#F2F6F9', '#FFFFFF', '#243746', '#467BA3', '#D3E2EC', '#60A8B5', '#CDEBF0', '#D9E7F1']))),
 'sakura':('Sakura Mint · hồng phấn, bạc hà',dict(zip([k for k,_ in THEME_FIELDS],['#F6FBF8', '#FFFFFF', '#294139', '#CF7F9D', '#CAE8DA', '#64AA95', '#F6DCE6', '#D5EFE2']))),
 'sandstone':('Sandstone Bronze · be cát, đồng ấm',dict(zip([k for k,_ in THEME_FIELDS],['#F8F5EF', '#FFFDFA', '#42362A', '#B18451', '#E7D9C2', '#7B9D91', '#D7E5DE', '#EDDEC4']))),
 'cyber':('Cyber Indigo · nền tối, xanh điện',dict(zip([k for k,_ in THEME_FIELDS],['#101527', '#1B2440', '#EAF0FF', '#7297FF', '#334568', '#ED88C5', '#4A426B', '#304C7A']))),
 'emerald':('Emerald Night · nền tối, ngọc lục bảo',dict(zip([k for k,_ in THEME_FIELDS],['#101F1B', '#1B3029', '#E6F7EE', '#58D6A0', '#2F5142', '#E1BB6B', '#456749', '#285D49']))),
 'burgundy':('Burgundy Velvet · nền tối, đỏ rượu vang',dict(zip([k for k,_ in THEME_FIELDS],['#24151E', '#36222F', '#FBEAF3', '#EE8CB4', '#59374C', '#C5A2EF', '#714764', '#67364F']))),
 'espresso':('Espresso Gold · nền tối, nâu cà phê',dict(zip([k for k,_ in THEME_FIELDS],['#201A16', '#302721', '#FAF0E2', '#E5B56F', '#554436', '#8CC8BA', '#65533B', '#674C30']))),
}
ACTIVE_THEME=dict(THEMES['pastel'][1])
ICON_SYMBOLS={}

def color_mix(a,b,weight):
    a=QColor(a);b=QColor(b)
    return QColor(*(round(x*(1-weight)+y*weight) for x,y in zip(a.getRgb()[:3],b.getRgb()[:3]))).name().upper()

def color_luminance(color):
    values=[v/255 for v in QColor(color).getRgb()[:3]]
    values=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in values]
    return sum(v*w for v,w in zip(values,(.2126,.7152,.0722)))

def color_contrast(a,b):
    x,y=sorted((color_luminance(a),color_luminance(b)));return (y+.05)/(x+.05)

def color_ink(background):
    dark=color_contrast(background,'#131A24');light=color_contrast(background,'#FFFFFF')
    if max(dark,light)>=4.5:return '#131A24' if dark>=light else '#FFFFFF'
    return '#000000'

def validate_theme(colors):
    if not isinstance(colors,dict) or set(colors)!={k for k,_ in THEME_FIELDS}:raise ValueError('Bộ màu thiếu thành phần.')
    if any(not isinstance(v,str) or not re.fullmatch(r'#[0-9A-Fa-f]{6}',v) for v in colors.values()):raise ValueError('Nhập mã màu dạng #RRGGBB hoặc dùng bảng chọn màu.')
    if any(color_contrast(colors['text'],colors[k])<4.5 for k in ('background','surface')):
        raise ValueError('Chữ chính chưa đủ rõ trên nền ứng dụng / nền thẻ. Chọn chữ sáng hơn với nền tối, hoặc chữ tối hơn với nền sáng.')
    return {k:v.upper() for k,v in colors.items()}

def load_theme():
    settings=QSettings('TownshipStudio','PyQt5');key=str(settings.value('theme/preset','pastel'))
    if key in THEMES:return key,dict(THEMES[key][1])
    if key=='custom':
        try:return key,validate_theme(json.loads(str(settings.value('theme/custom',''))))
        except (ValueError,TypeError):pass
    return 'pastel',dict(THEMES['pastel'][1])

def theme_style(colors):
    c=validate_theme(colors);bg=c['background'];surface=c['surface'];text=c['text'];primary=c['primary'];secondary=c['secondary'];accent=c['accent'];hover=c['hover'];selection=c['selection']
    border=color_mix(surface,text,.22);muted=color_mix(surface,text,.72);disabled=color_mix(surface,bg,.7);disabled_text=color_mix(surface,text,.52);alt=color_mix(surface,bg,.6)
    title=primary if color_contrast(primary,bg)>=4.5 else text
    # Compute ink independently for every colored control, including custom colors.
    return f'''
QWidget {{background:{bg};color:{text};font-family:"Segoe UI";font-size:13px;}}
QMainWindow,QDialog {{background:{bg};}}
QFrame#windowTitleBar {{background:qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 {surface},stop:1 {secondary});border:0;border-bottom:1px solid {border};}}
QLabel#windowTitle {{color:{text};font-size:14px;font-weight:600;}}
QLabel#appBadge {{background:{primary};color:{color_ink(primary)};border-radius:8px;font-size:12px;font-weight:700;}}
QPushButton#windowControl,QPushButton#windowClose {{background:transparent;color:{text};border:0;border-radius:7px;padding:0;font-size:19px;min-height:0;}}
QPushButton#windowControl:hover {{background:{hover};color:{color_ink(hover)};}}
QPushButton#windowClose:hover {{background:#DC3545;color:#FFFFFF;}}
QFrame#topNavigation {{background:{surface};border:1px solid {border};border-radius:14px;}}
QFrame#topNavigation QLabel#title {{font-size:24px;}}
QSizeGrip {{width:16px;height:16px;}}
QFrame#card,QFrame#summary {{background:{surface};border:1px solid {border};border-radius:12px;}}
QFrame#card[paletteAccent="blue"] {{border-top:3px solid {primary};}}
QFrame#card[paletteAccent="sky"] {{border-top:3px solid {secondary};}}
QFrame#card[paletteAccent="peach"] {{border-top:3px solid {selection};}}
QFrame#card[paletteAccent="pink"] {{border-top:3px solid {hover};}}
QFrame#card[paletteAccent="purple"] {{border-top:3px solid {accent};}}
QLabel {{background:transparent;}} QLabel#title {{font-size:27px;font-weight:700;color:{title};}}
QLabel#muted {{color:{muted};}} QLabel#cardTitle {{font-size:16px;font-weight:600;color:{text};}}
QPushButton {{background:{secondary};color:{color_ink(secondary)};border:1px solid {border};border-radius:7px;padding:9px 14px;font-weight:600;}}
QPushButton:hover {{background:{hover};color:{color_ink(hover)};border-color:{accent};}}
QPushButton:pressed {{background:{selection};color:{color_ink(selection)};}}
QPushButton#primary {{background:{primary};color:{color_ink(primary)};border-color:{primary};}}
QPushButton#primary:hover {{background:{hover};color:{color_ink(hover)};}}
QPushButton#primary:pressed {{background:{selection};color:{color_ink(selection)};}}
QPushButton#save {{background:{accent};color:{color_ink(accent)};border-color:{accent};}}
QPushButton#save:hover {{background:{hover};color:{color_ink(hover)};}}
QPushButton:disabled,QPushButton#primary:disabled,QPushButton#save:disabled {{background:{disabled};color:{disabled_text};border-color:{border};}}
QLineEdit,QSpinBox,QDoubleSpinBox,QComboBox {{background:{surface};color:{text};border:1px solid {border};border-radius:6px;padding:7px;min-height:19px;selection-background-color:{selection};selection-color:{color_ink(selection)};}}
QLineEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus {{border-color:{primary};}}
QLineEdit:disabled,QSpinBox:disabled,QDoubleSpinBox:disabled,QComboBox:disabled {{background:{disabled};color:{disabled_text};}}
QComboBox QAbstractItemView {{background:{surface};color:{text};border:1px solid {border};selection-background-color:{selection};selection-color:{color_ink(selection)};}}
QTabWidget::pane {{border:1px solid {border};border-radius:8px;background:{bg};}}
QTabBar::tab {{background:{surface};color:{text};padding:15px 28px;min-height:24px;margin-right:5px;border-top-left-radius:8px;border-top-right-radius:8px;}}
QTabBar::tab:hover {{background:{hover};color:{color_ink(hover)};}}
QTabBar::tab:selected {{background:{primary};color:{color_ink(primary)};font-weight:600;}}
QTabBar::tab:disabled {{background:{disabled};color:{disabled_text};}}
QTreeView::indicator,QCheckBox::indicator {{width:16px;height:16px;border:1px solid {border};border-radius:3px;background:{surface};}}
QTreeView::indicator:checked,QCheckBox::indicator:checked {{background:{primary};border-color:{text};}}
QTreeView::indicator:indeterminate,QCheckBox::indicator:indeterminate {{background:{accent};border-color:{text};}}
QTreeView::indicator:disabled,QCheckBox::indicator:disabled {{background:{disabled};border-color:{border};}}
QSpinBox::up-button,QSpinBox::down-button {{background:{secondary};width:16px;border-radius:2px;}}
QSpinBox::up-button:hover,QSpinBox::down-button:hover {{background:{hover};}}
QTreeWidget {{background:{surface};color:{text};alternate-background-color:{alt};border:1px solid {border};border-radius:7px;}}
QTreeWidget::item {{padding:6px;min-height:20px;}} QTreeWidget::item:selected {{background:{selection};color:{color_ink(selection)};}}
QTreeWidget::item:hover {{background:{hover};color:{color_ink(hover)};}} QTreeWidget::item:disabled {{color:{disabled_text};}}
QHeaderView::section {{background:{secondary};color:{color_ink(secondary)};padding:8px;border:0;border-right:1px solid {border};}}
QPlainTextEdit {{background:{surface};color:{text};border:1px solid {border};border-radius:8px;padding:8px;font-family:Consolas;font-size:12px;selection-background-color:{selection};selection-color:{color_ink(selection)};}}
QScrollArea {{border:0;}} QScrollBar:vertical {{background:{surface};width:10px;}}
QScrollBar::handle:vertical {{background:{accent};border-radius:5px;min-height:24px;}} QScrollBar::handle:vertical:hover {{background:{primary};}}
QScrollBar::add-line:vertical,QScrollBar::sub-line:vertical {{height:0;}}
QScrollBar:horizontal {{background:{surface};height:10px;}} QScrollBar::handle:horizontal {{background:{accent};border-radius:5px;min-width:24px;}}
QScrollBar::add-line:horizontal,QScrollBar::sub-line:horizontal {{width:0;}}
QProgressBar {{background:{surface};border:0;border-radius:3px;max-height:5px;}} QProgressBar::chunk {{background:{accent};border-radius:3px;}}
QCheckBox {{spacing:8px;background:transparent;}} QCheckBox:disabled {{color:{disabled_text};}}
QToolTip {{background:{selection};color:{color_ink(selection)};border:1px solid {accent};padding:6px;}}
'''

def apply_theme(colors):
    global ACTIVE_THEME
    ACTIVE_THEME=validate_theme(colors);app=QApplication.instance();app.setStyleSheet(theme_style(ACTIVE_THEME))
    for widget in app.allWidgets():
        if hasattr(widget,'_activity_highlighter'):widget._activity_highlighter.rehighlight()
        if isinstance(widget,QPushButton):
            symbol=ICON_SYMBOLS.get(widget.icon().cacheKey())
            if symbol:
                role='primary' if widget.objectName()=='primary' else 'accent' if widget.objectName()=='save' else 'secondary'
                widget.setIcon(native_icon(symbol,color_ink(ACTIVE_THEME[role])))
        elif isinstance(widget,QTabWidget):
            for i in range(widget.count()):
                symbol=ICON_SYMBOLS.get(widget.tabIcon(i).cacheKey())
                if symbol:widget.setTabIcon(i,native_icon(symbol))
        elif isinstance(widget,QLabel) and widget.property('themeIcon'):
            widget.setPixmap(native_icon(widget.property('themeIcon')).pixmap(26,26))

# Custom window chrome is shared by the main window and application dialogs.
_NativeDialog=QDialog
_NativeMainWindow=QMainWindow
_NativeMessageBox=QMessageBox
_NativeTabWidget=QTabWidget

class StudioTabBar(QTabBar):
    def __init__(self,parent=None):
        super().__init__(parent);self.setExpanding(False);self.setElideMode(Qt.ElideNone);self.setUsesScrollButtons(True)
    def tabSizeHint(self,index):
        hint=super().tabSizeHint(index);font=QFont(self.font());font.setWeight(QFont.DemiBold)
        text_width=QFontMetrics(font).horizontalAdvance(self.tabText(index))
        icon_width=self.iconSize().width()+12 if not self.tabIcon(index).isNull() else 0
        return QSize(max(hint.width(),text_width+icon_width+64,128),max(hint.height(),54))

class StudioTabWidget(_NativeTabWidget):
    def __init__(self,parent=None):
        super().__init__(parent);self.setTabBar(StudioTabBar(self));self.setElideMode(Qt.ElideNone);self.setUsesScrollButtons(True)

class StudioTitleBar(QFrame):
    def __init__(self,window):
        super().__init__(window);self.window=window;self.offset=None;self.setObjectName('windowTitleBar');self.setFixedHeight(54)
        row=QHBoxLayout(self);row.setContentsMargins(16,8,12,8);row.setSpacing(9)
        badge=QLabel('TS');badge.setObjectName('appBadge');badge.setAlignment(Qt.AlignCenter);badge.setFixedSize(32,32);badge.setAttribute(Qt.WA_TransparentForMouseEvents);row.addWidget(badge)
        self.title=QLabel(window.windowTitle() or 'Township Studio');self.title.setObjectName('windowTitle');self.title.setAttribute(Qt.WA_TransparentForMouseEvents);self.title.setMinimumWidth(0);row.addWidget(self.title,1)
        window.windowTitleChanged.connect(self.title.setText)
        self.minimum=QPushButton('−');self.maximum=QPushButton('□');self.close_button=QPushButton('×')
        for button in (self.minimum,self.maximum,self.close_button):
            button.setObjectName('windowClose' if button is self.close_button else 'windowControl');button.setFixedSize(36,32);button.setAutoDefault(False);button.setDefault(False);button.setFocusPolicy(Qt.NoFocus);row.addWidget(button)
        self.minimum.setToolTip('Thu nhỏ');self.maximum.setToolTip('Phóng to / Khôi phục');self.close_button.setToolTip('Đóng')
        self.minimum.setAccessibleName('Minimize');self.maximum.setAccessibleName('Maximize or restore');self.close_button.setAccessibleName('Close')
        self.minimum.clicked.connect(window.showMinimized);self.maximum.clicked.connect(self.toggle_maximized);self.close_button.clicked.connect(window.close)
    def toggle_maximized(self):
        if self.window.isMaximized():self.window.showNormal()
        else:self.window.showMaximized()
        self.maximum.setText('❐' if self.window.isMaximized() else '□')
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            handle=self.window.windowHandle()
            if handle is not None and hasattr(handle,'startSystemMove') and handle.startSystemMove():event.accept();return
            if not self.window.isMaximized():self.offset=event.globalPos()-self.window.frameGeometry().topLeft()
            event.accept()
        else:super().mousePressEvent(event)
    def mouseMoveEvent(self,event):
        if self.offset is not None and event.buttons() & Qt.LeftButton:self.window.move(event.globalPos()-self.offset);event.accept()
        else:super().mouseMoveEvent(event)
    def mouseReleaseEvent(self,event):self.offset=None;super().mouseReleaseEvent(event)
    def mouseDoubleClickEvent(self,event):
        if event.button()==Qt.LeftButton:self.offset=None;self.toggle_maximized();event.accept()
        else:super().mouseDoubleClickEvent(event)

class StudioChromeMixin:
    def init_chrome(self):
        self.setWindowFlag(Qt.FramelessWindowHint,True);self._studio_titlebar=None
        self._studio_grip=QSizeGrip(self);self._studio_grip.setToolTip('Kéo để đổi kích thước');self._studio_grip.resize(16,16)
    def ensure_chrome(self):
        if self._studio_titlebar is not None:return
        layout=QWidget.layout(self)
        if layout is None:return
        bar=StudioTitleBar(self);self._studio_titlebar=bar
        if isinstance(layout,QVBoxLayout):layout.insertWidget(0,bar)
        elif isinstance(layout,QGridLayout):
            columns=layout.columnCount();items=[]
            while layout.count():
                row,column,rowspan,colspan=layout.getItemPosition(0);item=layout.takeAt(0);items.append((item,row,column,rowspan,colspan))
            for item,row,column,rowspan,colspan in items:layout.addItem(item,row+1,column,rowspan,colspan,item.alignment())
            layout.addWidget(bar,0,0,1,max(1,columns))
        else:bar.deleteLater();self._studio_titlebar=None;return
        self._studio_grip.raise_()
    def showEvent(self,event):
        self.ensure_chrome();super().showEvent(event);self.position_grip()
    def resizeEvent(self,event):super().resizeEvent(event);self.position_grip()
    def position_grip(self):
        if hasattr(self,'_studio_grip'):
            self._studio_grip.move(self.width()-18,self.height()-18);self._studio_grip.setVisible(not self.isMaximized());self._studio_grip.raise_()

class StudioDialog(StudioChromeMixin,_NativeDialog):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.init_chrome()

class StudioMainWindow(_NativeMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs);self.setWindowFlag(Qt.FramelessWindowHint,True)
        self._studio_titlebar=StudioTitleBar(self);self.setMenuWidget(self._studio_titlebar)
        self._studio_grip=QSizeGrip(self);self._studio_grip.resize(16,16);self._studio_grip.setToolTip('Kéo để đổi kích thước')
    def resizeEvent(self,event):
        super().resizeEvent(event)
        if hasattr(self,'_studio_grip'):
            self._studio_grip.move(self.width()-18,self.height()-18);self._studio_grip.setVisible(not self.isMaximized());self._studio_grip.raise_()

class StudioMessageBox(StudioChromeMixin,_NativeMessageBox):
    def __init__(self,*args,**kwargs):super().__init__(*args,**kwargs);self.init_chrome()
    @classmethod
    def show_message(cls,parent,title,text,icon,buttons,defaultButton):
        dialog=cls(parent);dialog.setWindowTitle(title);dialog.setText(text);dialog.setIcon(icon);dialog.setStandardButtons(buttons)
        if defaultButton!=cls.NoButton:dialog.setDefaultButton(defaultButton)
        return dialog.exec_()
    @classmethod
    def information(cls,parent,title,text,buttons=_NativeMessageBox.Ok,defaultButton=_NativeMessageBox.NoButton):return cls.show_message(parent,title,text,cls.Information,buttons,defaultButton)
    @classmethod
    def warning(cls,parent,title,text,buttons=_NativeMessageBox.Ok,defaultButton=_NativeMessageBox.NoButton):return cls.show_message(parent,title,text,cls.Warning,buttons,defaultButton)
    @classmethod
    def critical(cls,parent,title,text,buttons=_NativeMessageBox.Ok,defaultButton=_NativeMessageBox.NoButton):return cls.show_message(parent,title,text,cls.Critical,buttons,defaultButton)
    @classmethod
    def question(cls,parent,title,text,buttons=_NativeMessageBox.Yes|_NativeMessageBox.No,defaultButton=_NativeMessageBox.NoButton):return cls.show_message(parent,title,text,cls.Question,buttons,defaultButton)

QDialog=StudioDialog
QMainWindow=StudioMainWindow
QMessageBox=StudioMessageBox
QTabWidget=StudioTabWidget

class ThemeSettingsDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent);self.setWindowTitle('Giao diện · Bộ màu');self.resize(920,660);self.original=dict(ACTIVE_THEME);self.colors=dict(ACTIVE_THEME);self.editors={};self.swatches={}
        layout=QVBoxLayout(self);heading=QLabel('Bộ màu ứng dụng');heading.setObjectName('cardTitle');layout.addWidget(heading)
        self.preset=QComboBox();self.preset.setProperty('i18nThemeList',True);self.preset.setMaxVisibleItems(10)
        for key,(name,_) in THEMES.items():self.preset.addItem(name,key)
        self.preset.addItem('Tùy chỉnh · chọn màu của bạn','custom');self.preset.setCurrentIndex(self.preset.findData(load_theme()[0]));layout.addWidget(self.preset)
        hint=QLabel('Chọn bộ màu hoặc chỉnh từng màu bằng bảng chọn / mã HEX. Xem thử không lưu; Đóng sẽ trở lại màu trước đó. Nút ADB giữ đỏ/xanh theo trạng thái kết nối.');hint.setWordWrap(True);layout.addWidget(hint)
        grid=QGridLayout();layout.addLayout(grid)
        for i,(key,label) in enumerate(THEME_FIELDS):
            row=i//2;col=(i%2)*3;grid.addWidget(QLabel(label),row,col);edit=QLineEdit(self.colors[key]);edit.setMaxLength(7);edit.setObjectName('theme_'+key);grid.addWidget(edit,row,col+1)
            button=QPushButton('Chọn màu');grid.addWidget(button,row,col+2);button.clicked.connect(lambda _,k=key:self.pick(k));edit.textEdited.connect(lambda _,k=key:self.edited(k));self.editors[key]=edit;self.swatches[key]=button
        self.preview=QFrame();self.preview.setObjectName('summary');self.preview.setMinimumHeight(230);self.preview.setMaximumHeight(270);p=QVBoxLayout(self.preview);p.setAlignment(Qt.AlignTop)
        title=QLabel('Xem trước · Township Studio');title.setObjectName('cardTitle');p.addWidget(title);p.addWidget(QLabel('Nền, chữ, nút, ô nhập và danh sách sử dụng bộ màu đã chọn.'))
        row=QHBoxLayout();example=QLineEdit('Thông tin thành phố');example.setProperty('i18nDisplayValue',True);row.addWidget(example);normal=QPushButton('Cấu hình');row.addWidget(normal);primary=QPushButton('Áp dụng');primary.setObjectName('primary');row.addWidget(primary);save=QPushButton('Ghi vào game');save.setObjectName('save');row.addWidget(save);p.addLayout(row)
        tree=QTreeWidget();tree.setHeaderLabels(['Thành phố','Level']);tree.header().setSectionResizeMode(0,QHeaderView.Stretch);tree.setProperty('i18nRowColumns',[0]);QTreeWidgetItem(tree,['Township mẫu','3']);chosen=QTreeWidgetItem(tree,['Backup đã chọn','104']);tree.setCurrentItem(chosen);tree.setMaximumHeight(95);p.addWidget(tree);layout.addWidget(self.preview,1)
        self.notice=QLabel();self.notice.setWordWrap(True);layout.addWidget(self.notice)
        row=QHBoxLayout();layout.addLayout(row)
        for text,fn in [('Về màu mặc định',self.reset),('Xem thử toàn ứng dụng',self.preview_app),('Lưu & áp dụng',self.save),('Đóng',self.reject)]:
            button=QPushButton(text);button.clicked.connect(fn);row.addWidget(button)
            if text=='Lưu & áp dụng':button.setObjectName('primary')
        self.preset.currentIndexChanged.connect(self.choose_preset);self.render_preview()
    def choose_preset(self):
        key=self.preset.currentData()
        if key in THEMES:
            self.colors=dict(THEMES[key][1])
            for k,edit in self.editors.items():edit.setText(self.colors[k])
        self.render_preview()
    def edited(self,key):
        self.colors[key]=self.editors[key].text().strip();self.preset.blockSignals(True);self.preset.setCurrentIndex(self.preset.findData('custom'));self.preset.blockSignals(False);self.render_preview()
    def pick(self,key):
        color=QColorDialog.getColor(QColor(self.colors.get(key,'#FFFFFF')),self,'Chọn '+dict(THEME_FIELDS)[key])
        if color.isValid():self.editors[key].setText(color.name().upper());self.edited(key)
    def render_preview(self):
        for key,button in self.swatches.items():
            if re.fullmatch(r'#[0-9A-Fa-f]{6}',self.colors.get(key,'')):
                swatch=QPixmap(20,20);swatch.fill(QColor(self.colors[key]));button.setIcon(QIcon(swatch))
        try:
            self.preview.setStyleSheet(theme_style(self.colors));self.notice.setText('Chữ được kiểm tra độ rõ; màu chữ trên nút và mục chọn tự điều chỉnh theo nền.')
        except ValueError as exc:self.notice.setText(str(exc))
    def reset(self):
        self.preset.setCurrentIndex(self.preset.findData('pastel'));self.choose_preset()
    def preview_app(self):
        try:apply_theme(self.colors)
        except ValueError as exc:QMessageBox.warning(self,'Bộ màu',str(exc))
    def save(self):
        try:colors=validate_theme(self.colors)
        except ValueError as exc:QMessageBox.warning(self,'Bộ màu',str(exc));return
        settings=QSettings('TownshipStudio','PyQt5');settings.setValue('theme/preset',self.preset.currentData())
        if self.preset.currentData()=='custom':settings.setValue('theme/custom',json.dumps(colors))
        settings.sync();apply_theme(colors);self.accept()
    def reject(self):apply_theme(self.original);super().reject()


STYLE=theme_style(THEMES['pastel'][1])

# Native SVG icons: independent of installed emoji fonts.
ICON_PATHS = {
 '💎':'<path d="M3 8l4-5h10l4 5-9 13z M3 8h18 M7 3l5 18 5-18"/>',
 '🪙':'<circle cx="12" cy="12" r="9"/><path d="M15 7h-4a3 3 0 000 6h2a2 2 0 010 4H8 M12 5v14"/>',
 '⭐':'<path d="M12 2l3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/>',
 '🧩':'<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
 '🏆':'<path d="M7 3h10v7a5 5 0 01-10 0z M7 5H3v3a4 4 0 004 4 M17 5h4v3a4 4 0 01-4 4 M12 15v5 M7 21h10"/>',
 '❤️':'<path d="M12 21L3 12C-1 5 7 0 12 7c5-7 13-2 9 5z"/>',
 '👤':'<circle cx="12" cy="7" r="4"/><path d="M3 22v-3a9 9 0 0118 0v3"/>',
 '⛵':'<path d="M12 2v15 M10 4L3 14h7z M14 5l7 9h-7z M2 18h20l-3 4H5z"/>',
 '⚡':'<path d="M14 2L4 14h7l-1 8 10-13h-7z"/>',
 '⛏':'<path d="M5 3c7-1 12 2 16 7L8 6z M13 7L3 22"/>',
 '📅':'<rect x="3" y="5" width="18" height="17" rx="2"/><path d="M3 10h18 M8 2v6 M16 2v6 M7 14h2 M12 14h2 M17 14h1 M7 18h2 M12 18h2"/>',
 '🔓':'<rect x="4" y="10" width="16" height="12" rx="2"/><path d="M8 10V6a4 4 0 018 0 M12 15v3"/>',
 '🗺':'<path d="M2 5l6-3 8 3 6-3v17l-6 3-8-3-6 3z M8 2v17 M16 5v17"/>',
 '🛒':'<path d="M2 3h3l3 13h11l3-10H6 M10 20h.01 M18 20h.01"/><circle cx="10" cy="20" r="1"/><circle cx="18" cy="20" r="1"/>',
 '🚂':'<rect x="6" y="2" width="12" height="17" rx="3"/><path d="M6 10h12 M9 19l-3 3 M15 19l3 3 M9 15h.01 M15 15h.01"/>',
 '🏙':'<path d="M2 22V9h7v13 M9 22V2h8v20 M17 22V12h5v10 M5 13v1 M5 17v1 M12 6h2 M12 10h2 M12 14h2 M12 18h2"/>',
 '💾':'<path d="M3 2h15l4 4v16H2V2z M6 2v7h11V2 M6 22V13h12v9 M14 4v3"/>',
 '🕘':'<circle cx="12" cy="12" r="10"/><path d="M12 5v7l5 3"/>',
 '🌱':'<path d="M12 22V10 M12 16C1 16 2 5 2 5c10 0 10 11 10 11z M12 11c0-9 10-9 10-9 0 9-10 9-10 9z"/>',
 '📂':'<path d="M2 6h8l2 3h10l-3 12H2z M2 9V3h8l2 3h8v3"/>',
 '📤':'<path d="M12 17V2 M6 8l6-6 6 6 M3 14v8h18v-8"/>',
 '⚙':'<circle cx="12" cy="12" r="4"/><path d="M12 2v3 M12 19v3 M2 12h3 M19 12h3 M5 5l2 2 M17 17l2 2 M5 19l2-2 M17 7l2-2"/>',
 '🤝':'<path d="M2 7l5-4 5 3 5-3 5 4-5 11-4 3-6-3z M7 3l5 3-4 5 3 2 4-4 6 5"/>',
 '↶':'<path d="M4 8h10a7 7 0 010 14 M4 8l5-5 M4 8l5 5"/>',
}

ICON_PATHS.update({
 '📊':'<path d="M3 22V11h4v11 M10 22V3h4v19 M17 22V7h4v15 M1 22h22"/>',
 '🌳':'<path d="M12 2l7 9h-4l6 7H3l6-7H5z M12 18v4"/>',
 '🏛':'<path d="M2 8l10-6 10 6z M4 10v9 M9 10v9 M15 10v9 M20 10v9 M2 22h20"/>',
 '🎴':'<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 6l4 6-4 6-4-6z"/>',
 '🎟':'<path d="M2 5h20v5a2 2 0 000 4v5H2v-5a2 2 0 000-4z M16 5v3 M16 11v2 M16 16v3"/>',
 '🎨':'<path d="M12 2a10 10 0 100 20h2a3 3 0 002-5 2 2 0 012-3h2a3 3 0 002-3A10 10 0 0012 2z"/><circle cx="7" cy="8" r="1"/><circle cx="12" cy="6" r="1"/><circle cx="17" cy="8" r="1"/><circle cx="6" cy="13" r="1"/>',
 '✨':'<path d="M12 2l3 7 7 3-7 3-3 7-3-7-7-3 7-3z"/>',
 '🏅':'<path d="M6 2l6 8 6-8 M3 2h5 M16 2h5"/><circle cx="12" cy="15" r="7"/><path d="M12 11v8 M9 15h6"/>',
 '🏚':'<path d="M2 10L12 2l10 8v12H2z M8 22V12h8v10 M8 12l8 10 M16 12L8 22"/>',
 '🎓':'<path d="M1 8l11-6 11 6-11 6z M5 11v7c5 4 9 4 14 0v-7 M23 8v10"/>',
 '🦁':'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="13" r="6"/><path d="M9 11h.01 M15 11h.01 M10 15l2 2 2-2 M12 17v2"/>',
 '🚀':'<path d="M7 16c0-8 8-14 15-14 0 7-6 15-14 15z M7 9H3l-2 6h6 M15 17v4l-6 2v-6 M5 19l-3 3"/><circle cx="16" cy="8" r="2"/>',
 '📦':'<path d="M2 6l10-4 10 4v14l-10 3-10-3z M2 6l10 4 10-4 M12 10v13 M7 4l10 4"/>',
 '👑':'<path d="M2 5l5 5 5-8 5 8 5-5-3 16H5z M5 17h14"/>',
 '💌':'<rect x="2" y="5" width="20" height="15" rx="2"/><path d="M2 6l10 8L22 6"/>',
 '🌆':ICON_PATHS['🏙'],
 '🩹':'<path d="M2 9l7-7 13 13-7 7z M8 8l8 8 M9 12h.01 M12 9h.01 M12 15h.01 M15 12h.01"/>',
 '💠':ICON_PATHS['💎'],
 '🛠':'<path d="M14 3a6 6 0 00-7 7L2 18l4 4 8-8a6 6 0 007-7l-4 4-4-4z"/>',
 '🔌':'<path d="M6 2v6 M18 2v6 M4 8h16v3a8 8 0 01-16 0z M12 19v3"/>',
 '🗂':ICON_PATHS['📂'], '📁':ICON_PATHS['📂'], '🧭':ICON_PATHS['🗺'],
})

ICON_PATHS.update({
 '🌐':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18 M12 3a17 17 0 0 1 0 18 17 17 0 0 1 0-18"/>',
 '☁':'<path d="M6 18a4 4 0 0 1-.4-8 6.5 6.5 0 0 1 12.7-1A4.6 4.6 0 0 1 18 18Z"/>',
 '📥':'<path d="M12 2v13 M6 9l6 6 6-6 M3 14v8h18v-8"/>',
 '📋':'<rect x="4" y="4" width="16" height="18" rx="2"/><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M8 11h8 M8 16h8"/>',
})

DEFAULT_ICON='<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M7 12h10 M12 7v10"/>'
def native_icon(symbol,color=None):
    path=ICON_PATHS.get(symbol,DEFAULT_ICON)
    svg=('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><g fill="none" stroke="'+(color or ACTIVE_THEME['text'])+'" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">'+path+'</g></svg>').encode()
    pixmap=QPixmap(48,48); pixmap.fill(Qt.transparent)
    painter=QPainter(pixmap); QSvgRenderer(QByteArray(svg)).render(painter); painter.end()
    icon=QIcon(pixmap)
    selected_svg=svg.replace(('stroke="'+(color or ACTIVE_THEME['text'])+'"').encode(),('stroke="'+color_ink(ACTIVE_THEME['primary'])+'"').encode())
    selected=QPixmap(48,48);selected.fill(Qt.transparent);painter=QPainter(selected);QSvgRenderer(QByteArray(selected_svg)).render(painter);painter.end()
    icon.addPixmap(selected,QIcon.Selected,QIcon.On);icon.addPixmap(selected,QIcon.Normal,QIcon.On)
    ICON_SYMBOLS[icon.cacheKey()]=symbol;return icon
def split_icon(text):
    bits=text.split(' ',1)
    if len(bits)==2 and unicodedata.category(bits[0][0]).startswith('S') and len(bits[0])<=4:
        return bits[0],bits[1].strip()
    return None,text
def decorate(widget):
    for button in widget.findChildren(QPushButton):
        symbol,text=split_icon(button.text())
        if symbol:
            button.setText(text);button.setIcon(native_icon(symbol))
    for label in widget.findChildren(QLabel):
        if label.objectName() not in ('title','cardTitle'):continue
        symbol,text=split_icon(label.text())
        if symbol:
            label.setText(''); row=QHBoxLayout(label);row.setContentsMargins(0,0,0,0)
            icon=QLabel();icon.setProperty('themeIcon',symbol);icon.setPixmap(native_icon(symbol).pixmap(26,26));row.addWidget(icon)
            caption=QLabel(text);caption.setObjectName(label.objectName());row.addWidget(caption,1)
    for tabs in widget.findChildren(QTabWidget):
        for index in range(tabs.count()):
            symbol,text=split_icon(tabs.tabText(index))
            if symbol:tabs.setTabText(index,text);tabs.setTabIcon(index,native_icon(symbol))

class Cancelled(Exception): pass

def format_log_value(value, indent=''):
    if isinstance(value, dict):
        lines=[]
        for key, item in value.items():
            if isinstance(item, tuple) and len(item)==2:
                lines.append(indent+str(key)+': '+str(item[0])+' → '+str(item[1]))
            elif isinstance(item, (dict, list, tuple)):
                lines.append(indent+str(key)+':')
                lines.append(format_log_value(item, indent+'  '))
            else:
                lines.append(indent+str(key)+': '+str(item))
        return '\n'.join(lines)
    if isinstance(value, (list, tuple)):
        return '\n'.join(format_log_value(item, indent) for item in value)
    return indent+str(value)

def format_log_message(args, sep=' '):
    lines=[]
    for value in args:
        text=format_log_value(value)
        parts=text.split('\n')
        structured=isinstance(value,(dict,list,tuple))
        if lines and lines[-1].rstrip().endswith(':'):
            lines[-1]=lines[-1].rstrip()+' '+parts[0]
            lines.extend(parts[1:])
        elif lines and not structured and len(parts)==1 and not text.rstrip().endswith(':'):
            lines[-1]+=sep+text
        else:
            lines.extend(parts)
    return '\n'.join(lines)

class Worker(QThread):
    output = pyqtSignal(str)
    ask = pyqtSignal(str, str)
    done = pyqtSignal(str, str)
    def __init__(self, action):
        super().__init__(); self.action = action
        self.event = threading.Event(); self.answer = None; self.cancelled = False
        self.lines = []
    def printer(self, *args, sep=' ', end='\n', **kwargs):
        if self.cancelled: raise Cancelled()
        s = format_log_message(args, sep)
        self.lines.append(s); self.lines = self.lines[-400:]
        self.output.emit(s)
    def input(self, prompt=''):
        if self.cancelled: raise Cancelled()
        self.event.clear(); self.answer = None
        self.ask.emit(str(prompt), '\n'.join(self.lines[-160:]))
        self.event.wait()
        if self.cancelled or self.answer is None: raise Cancelled()
        return self.answer
    def run(self):
        B.input = self.input; B.print = self.printer
        try:
            self.action(); self.done.emit('ok', '')
        except Cancelled:
            self.done.emit('cancel', '')
        except Exception as exc:
            self.output.emit(traceback.format_exc())
            self.done.emit('error', f'{type(exc).__name__}: {exc}')
        finally:
            B.input = lambda *_: (_ for _ in ()).throw(RuntimeError('GUI worker required'))
            B.print = print

class PromptDialog(QDialog):
    def __init__(self, title, prompt, context, parent):
        super().__init__(parent); self.setWindowTitle(title); self.resize(740, 540)
        layout = QVBoxLayout(self)
        heading = QLabel(title); heading.setObjectName('cardTitle'); layout.addWidget(heading)
        self.context = QPlainTextEdit(context); self.context.setProperty('i18nDocument',True); self.context.setReadOnly(True)
        self.context.setMaximumBlockCount(300); layout.addWidget(self.context)
        QTimer.singleShot(0, lambda: self.context.verticalScrollBar().setValue(self.context.verticalScrollBar().maximum()))
        label = QLabel(prompt or 'Nhấn Tiếp tục để quay lại'); label.setWordWrap(True); layout.addWidget(label)
        self.edit = QLineEdit(); self.edit.setPlaceholderText('Nhập giá trị hoặc lựa chọn theo hướng dẫn ở trên')
        layout.addWidget(self.edit)
        choices = []
        for line in context.splitlines():
            m = re.match(r'^\s*(\d{1,3})[.)]\s+(.+)', line)
            if m:
                if choices and int(m.group(1)) != 0 and int(m.group(1)) <= int(choices[-1][0]): choices = []
                choices.append((m.group(1), m.group(2)))
        if choices and re.search(r'chọn|stt', prompt, re.I) and not re.search(r'1,3|5-10|toa', prompt, re.I):
            combo = QComboBox(); combo.addItem('Chọn nhanh…', '')
            for value, text in choices: combo.addItem(value + ' · ' + text, value)
            combo.currentIndexChanged.connect(lambda _: self.edit.setText(combo.currentData()))
            layout.addWidget(combo)
        if re.search(r'đường dẫn|thư mục', prompt, re.I):
            row = QHBoxLayout()
            button = QPushButton('📂 Chọn file'); button.clicked.connect(self.pick_file); row.addWidget(button)
            folder = QPushButton('📁 Chọn thư mục'); folder.clicked.connect(self.pick_folder); row.addWidget(folder)
            layout.addLayout(row)
        self.confirm = bool(re.search(r'\[y/n\]|\[y/N\]|\[Y/n\]', prompt))
        if self.confirm:
            self.edit.hide()
            row = QHBoxLayout()
            yes = QPushButton('✓ Xác nhận'); yes.setObjectName('primary'); yes.clicked.connect(lambda: self.confirm_answer('y'))
            no = QPushButton('Không'); no.clicked.connect(lambda: self.confirm_answer('n'))
            row.addWidget(no); row.addWidget(yes); layout.addLayout(row)
        else:
            buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttons.button(QDialogButtonBox.Ok).setText('Tiếp tục →')
            buttons.button(QDialogButtonBox.Cancel).setText('Hủy thao tác')
            buttons.accepted.connect(self.accept); buttons.rejected.connect(self.reject); layout.addWidget(buttons)
            self.edit.returnPressed.connect(self.accept)
        self.edit.setFocus(); decorate(self)
    def confirm_answer(self, value): self.edit.setText(value); self.accept()
    def pick_file(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Chọn file', str(B.WORK_DIR), 'Tất cả (*)')
        if path: self.edit.setText(path)
    def pick_folder(self):
        path = QFileDialog.getExistingDirectory(self, 'Chọn thư mục', str(B.WORK_DIR))
        if path: self.edit.setText(path)

PROFILE = [
 ('💎','T-Cash','cash','moneyCash',0,2000000000),
 ('🪙','Coin','coin','money',0,2000000000),
 ('⭐','Level','level',None,1,1089),
 ('🧩','M3 LVL','m3',None,50,2147483647),
 ('🏆','1st Win','win',None,0,2147483647),
 ('❤️','Lives','lives',None,0,2147483647),
 ('🤝','Help','help',None,0,2147483647),
 ('🎴','Card','card',None,0,2147483647),
 ('⛵','Regatta','regata',None,0,2147483647),
 ('⚡','Expedition Energy','energy',None,0,2147483647),
 ('⛏','Mine Depth','mine',None,100,2147483647)]

GROUPS = [
 ('🔓 Unlock', [
 ('👤','Avatar','Xem, chọn, mở hoặc khóa avatar','unlock_all_avatars_prompt'),
 ('🌳','Decorations','Chọn nhóm, món và số lượng trang trí','decoration_prompt'),
 ('🗺','Land','Mở đất theo logic của bản gốc','land_prompt'),
 ('🏛','Museum','Hoàn thành bộ sưu tập bảo tàng','museum_prompt'),
 ('🃏','All Cards','Cập nhật toàn bộ thẻ','all_cards'),
 ('🎴','My Cards','Cập nhật các thẻ đang sở hữu','my_cards'),
 ('🎟','Golden Pass','Mở Golden Pass','golden_pass_prompt'),
 ('🎨','Skin','Chọn nhóm và mở skin','skin'),
 ('✨','Stickers','Chọn và mở sticker','stickers'),
 ('🏅','Profiles','Huy hiệu, danh hiệu, khung và phong cách','profile'),
 ('🏆','Achievements','Chọn thành tích cần mở','achievements')]),
 ('🛠 Tool', [
 ('🏚','Barn','Cấp kho và số lượng sản phẩm','barn_prompt'),
 ('🎟','Golden Pass Editor','Premium, score, stage và phần thưởng','golden_pass_editor_prompt'),
 ('🎓','Academi','Chỉnh bonus nâng cấp tại học viện','academy_prompt'),
 ('🦁','Zoo Card','Chỉnh thẻ động vật','zoo_cards_prompt'),
 ('🚀','Advantages','Thiết lập lợi thế và thời hạn','advantages_prompt'),
 ('🛒','Market','Chỉnh số ô chợ','market_prompt'),
 ('📦','Quantities','Chỉnh số lượng tài nguyên','quantities_prompt'),
 ('🚂','Train','Chọn tàu, toa và thông số','train_prompt'),
 ('🔐','Encode','Mã hóa XML thành file save Township','encode_file_prompt'),
 ('🔓','Decode','Giải mã file save Township thành XML','decode_file_prompt')]),
 ('👑 Premium', [
 ('⛵','Regatta Tasks','Chỉnh số nhiệm vụ MyOldTask','regatta_tasks_prompt'),
 ('💌','Send Card','Chọn người nhận và thông số gửi thẻ','send_card_prompt'),
 ('🏙','Clone City V1','Chọn donor và nội dung sao chép','clone_city_v1_prompt'),
 ('🌆','Clone City V3','Xử lý đồng thời mGameInfo và LocalInfo','clone_city_v3_prompt'),
 ('🩹','Fix Tutorial Bug','Chọn nhóm hướng dẫn cần sửa','tutorial_fix_prompt')]),
 ('💠 VIP', [
 ('💾','Backup','Sao lưu ZIP trên máy và Google Drive','backup_prompt'),
 ('🕘','History','Đọc backup trên máy hoặc Google Drive','history_prompt'),
 ('🌱','New TownCity','Tự tạo tài khoản mới LV3 / áp dụng mẫu ZIP','new_towncity_prompt')])]

# Offline interface catalog; save keys, XML, identifiers and logs are never translated.
from PyQt5.QtCore import QObject,QEvent
LANGUAGES=[('en','English'),('fr','Français'),('id','Bahasa Indonesia'),('pt','Português'),('es','Español'),('ja','日本語'),('zh','中文（简体）'),('ko','한국어'),('ru','Русский'),('tr','Türkçe'),('vi','Tiếng Việt'),('ar','العربية (مصر)')]
I18N_CODES=['en','fr','id','pt','es','ja','zh','ko','ru','tr','ar']
# First column: original UI text; subsequent columns follow I18N_CODES.
I18N_DATA='''Cấu hình|Settings|Paramètres|Pengaturan|Configurações|Configuración|設定|设置|설정|Настройки|Ayarlar|الإعدادات
Cấu hình hệ thống|System settings|Paramètres système|Pengaturan sistem|Configurações do sistema|Configuración del sistema|システム設定|系统设置|시스템 설정|Системные настройки|Sistem ayarları|إعدادات النظام
Hướng dẫn|Help|Aide|Bantuan|Ajuda|Ayuda|ヘルプ|帮助|도움말|Справка|Yardım|المساعدة
Ngôn ngữ|Language|Langue|Bahasa|Idioma|Idioma|言語|语言|언어|Язык|Dil|اللغة
Ngôn ngữ giao diện|Interface language|Langue de l’interface|Bahasa antarmuka|Idioma da interface|Idioma de la interfaz|表示言語|界面语言|인터페이스 언어|Язык интерфейса|Arayüz dili|لغة الواجهة
Áp dụng|Apply|Appliquer|Terapkan|Aplicar|Aplicar|適用|应用|적용|Применить|Uygula|تطبيق
Lưu|Save|Enregistrer|Simpan|Salvar|Guardar|保存|保存|저장|Сохранить|Kaydet|حفظ
Đóng|Close|Fermer|Tutup|Fechar|Cerrar|閉じる|关闭|닫기|Закрыть|Kapat|إغلاق
Hủy|Cancel|Annuler|Batal|Cancelar|Cancelar|キャンセル|取消|취소|Отмена|İptal|إلغاء
Có|Yes|Oui|Ya|Sim|Sí|はい|是|예|Да|Evet|نعم
Không|No|Non|Tidak|Não|No|いいえ|否|아니요|Нет|Hayır|لا
Chọn…|Browse…|Parcourir…|Telusuri…|Procurar…|Examinar…|参照…|浏览…|찾아보기…|Обзор…|Gözat…|تصفح…
Chọn file|Choose file|Choisir un fichier|Pilih file|Escolher arquivo|Elegir archivo|ファイルを選択|选择文件|파일 선택|Выбрать файл|Dosya seç|اختيار ملف
Chọn thư mục|Choose folder|Choisir un dossier|Pilih folder|Escolher pasta|Elegir carpeta|フォルダーを選択|选择文件夹|폴더 선택|Выбрать папку|Klasör seç|اختيار مجلد
Kết nối ADB|Connect ADB|Connecter ADB|Hubungkan ADB|Conectar ADB|Conectar ADB|ADBに接続|连接 ADB|ADB 연결|Подключить ADB|ADB bağlan|اتصال ADB
Kết nối lại ADB|Reconnect ADB|Reconnecter ADB|Hubungkan ulang ADB|Reconectar ADB|Reconectar ADB|ADBに再接続|重新连接 ADB|ADB 다시 연결|Переподключить ADB|ADB yeniden bağlan|إعادة اتصال ADB
Mở mGameInfo|Open mGameInfo|Ouvrir mGameInfo|Buka mGameInfo|Abrir mGameInfo|Abrir mGameInfo|mGameInfoを開く|打开 mGameInfo|mGameInfo 열기|Открыть mGameInfo|mGameInfo aç|فتح mGameInfo
Mở LocalInfo|Open LocalInfo|Ouvrir LocalInfo|Buka LocalInfo|Abrir LocalInfo|Abrir LocalInfo|LocalInfoを開く|打开 LocalInfo|LocalInfo 열기|Открыть LocalInfo|LocalInfo aç|فتح LocalInfo
Xuất file|Export file|Exporter le fichier|Ekspor file|Exportar arquivo|Exportar archivo|ファイルを出力|导出文件|파일 내보내기|Экспорт файла|Dosya dışa aktar|تصدير ملف
Ghi vào game|Write to game|Écrire dans le jeu|Tulis ke game|Gravar no jogo|Escribir en el juego|ゲームに書き込む|写入游戏|게임에 저장|Записать в игру|Oyuna yaz|حفظ في اللعبة
Hoàn tác|Undo|Annuler les modifications|Urungkan|Desfazer|Deshacer|元に戻す|撤销|실행 취소|Отменить изменения|Geri al|تراجع
Profile Statics|Profile statistics|Statistiques du profil|Statistik profil|Estatísticas do perfil|Estadísticas del perfil|プロフィール統計|档案统计|프로필 통계|Статистика профиля|Profil istatistikleri|إحصائيات الملف
Unlock|Unlock|Débloquer|Buka kunci|Desbloquear|Desbloquear|アンロック|解锁|잠금 해제|Разблокировка|Kilidi aç|فتح القفل
Tool|Tools|Outils|Alat|Ferramentas|Herramientas|ツール|工具|도구|Инструменты|Araçlar|الأدوات
Premium|Premium|Premium|Premium|Premium|Premium|プレミアム|高级|프리미엄|Премиум|Premium|بريميوم
VIP|VIP|VIP|VIP|VIP|VIP|VIP|VIP|VIP|VIP|VIP|VIP
Coin|Coins|Pièces|Koin|Moedas|Monedas|コイン|金币|코인|Монеты|Altın|العملات
Level|Level|Niveau|Level|Nível|Nivel|レベル|等级|레벨|Уровень|Seviye|المستوى
1st Win|First win|Première victoire|Kemenangan pertama|Primeira vitória|Primera victoria|初勝利|首次胜利|첫 승리|Первая победа|İlk galibiyet|أول فوز
Lives|Lives|Vies|Nyawa|Vidas|Vidas|ライフ|生命|생명|Жизни|Canlar|الحياة
Help|Help count|Nombre d’aides|Jumlah bantuan|Total de ajudas|Total de ayudas|ヘルプ数|帮助次数|도움 횟수|Количество помощи|Yardım sayısı|عدد المساعدات
Card|Cards|Cartes|Kartu|Cartas|Cartas|カード|卡片|카드|Карточки|Kartlar|البطاقات
Regatta|Regatta|Régate|Regatta|Regata|Regata|レガッタ|赛舟会|레가타|Регата|Regatta|سباق القوارب
Expedition Energy|Expedition energy|Énergie d’expédition|Energi ekspedisi|Energia de expedição|Energía de expedición|探検エネルギー|探险能量|탐험 에너지|Энергия экспедиции|Keşif enerjisi|طاقة الاستكشاف
Mine Depth|Mine depth|Profondeur de la mine|Kedalaman tambang|Profundidade da mina|Profundidad de la mina|鉱山の深さ|矿井深度|광산 깊이|Глубина шахты|Maden derinliği|عمق المنجم
Month / Year Create|Creation month / year|Mois / année de création|Bulan / tahun pembuatan|Mês / ano de criação|Mes / año de creación|作成月／年|创建月／年|생성 월 / 연도|Месяц / год создания|Oluşturma ayı / yılı|شهر / سنة الإنشاء
Avatar|Avatar|Avatar|Avatar|Avatar|Avatar|アバター|头像|아바타|Аватар|Avatar|الصورة الرمزية
Decorations|Decorations|Décorations|Dekorasi|Decorações|Decoraciones|装飾|装饰|장식|Украшения|Süslemeler|الزينة
Land|Land|Terrain|Lahan|Terreno|Terreno|土地|土地|토지|Земля|Arazi|الأرض
Museum|Museum|Musée|Museum|Museu|Museo|博物館|博物馆|박물관|Музей|Müze|المتحف
All Cards|All cards|Toutes les cartes|Semua kartu|Todas as cartas|Todas las cartas|すべてのカード|全部卡片|모든 카드|Все карточки|Tüm kartlar|كل البطاقات
My Cards|My cards|Mes cartes|Kartu saya|Minhas cartas|Mis cartas|自分のカード|我的卡片|내 카드|Мои карточки|Kartlarım|بطاقاتي
Golden Pass|Golden Pass|Pass doré|Golden Pass|Passe dourado|Pase dorado|ゴールデンパス|黄金通行证|골든 패스|Золотой пропуск|Altın Bilet|التذكرة الذهبية
Skin|Skins|Apparences|Skin|Visuais|Aspectos|スキン|皮肤|스킨|Облики|Görünümler|المظاهر
Stickers|Stickers|Autocollants|Stiker|Adesivos|Pegatinas|ステッカー|贴纸|스티커|Наклейки|Çıkartmalar|الملصقات
Profiles|Profiles|Profils|Profil|Perfis|Perfiles|プロフィール|档案|프로필|Профили|Profiller|الملفات الشخصية
Achievements|Achievements|Succès|Pencapaian|Conquistas|Logros|実績|成就|업적|Достижения|Başarılar|الإنجازات
Barn|Barn|Grange|Lumbung|Celeiro|Granero|納屋|仓库|헛간|Амбар|Ambar|المخزن
Golden Pass Editor|Golden Pass editor|Éditeur du Pass doré|Editor Golden Pass|Editor do passe dourado|Editor del pase dorado|ゴールデンパス編集|黄金通行证编辑|골든 패스 편집|Редактор золотого пропуска|Altın Bilet düzenleyici|محرر التذكرة الذهبية
Academi|Academy|Académie|Akademi|Academia|Academia|アカデミー|学院|아카데미|Академия|Akademi|الأكاديمية
Zoo Card|Zoo cards|Cartes du zoo|Kartu kebun binatang|Cartas do zoológico|Cartas del zoo|動物園カード|动物园卡片|동물원 카드|Карточки зоопарка|Hayvanat bahçesi kartları|بطاقات حديقة الحيوان
Advantages|Advantages|Avantages|Keuntungan|Vantagens|Ventajas|特典|增益|혜택|Преимущества|Avantajlar|المزايا
Market|Market|Marché|Pasar|Mercado|Mercado|市場|市场|시장|Рынок|Pazar|السوق
Quantities|Quantities|Quantités|Jumlah|Quantidades|Cantidades|数量|数量|수량|Количество|Miktarlar|الكميات
Train|Train|Train|Kereta|Trem|Tren|列車|火车|기차|Поезд|Tren|القطار
Regatta Tasks|Regatta tasks|Tâches de régate|Tugas regatta|Tarefas da regata|Tareas de regata|レガッタのタスク|赛舟会任务|레가타 과제|Задания регаты|Regatta görevleri|مهام سباق القوارب
Send Card|Send cards|Envoyer des cartes|Kirim kartu|Enviar cartas|Enviar cartas|カード送信|发送卡片|카드 보내기|Отправить карточки|Kart gönder|إرسال بطاقات
Clone City V1|Clone city V1|Cloner la ville V1|Klon kota V1|Clonar cidade V1|Clonar ciudad V1|街を複製 V1|克隆城市 V1|도시 복제 V1|Клонировать город V1|Şehir klonla V1|نسخ المدينة V1
Clone City V3|Clone city V3|Cloner la ville V3|Klon kota V3|Clonar cidade V3|Clonar ciudad V3|街を複製 V3|克隆城市 V3|도시 복제 V3|Клонировать город V3|Şehir klonla V3|نسخ المدينة V3
Fix Tutorial Bug|Fix tutorial|Corriger le tutoriel|Perbaiki tutorial|Corrigir tutorial|Corregir tutorial|チュートリアル修復|修复教程|튜토리얼 수정|Исправить обучение|Eğitimi düzelt|إصلاح البرنامج التعليمي
Backup|Backup|Sauvegarde|Cadangan|Backup|Copia de seguridad|バックアップ|备份|백업|Резервная копия|Yedekleme|نسخة احتياطية
History|History|Historique|Riwayat|Histórico|Historial|履歴|历史记录|기록|История|Geçmiş|السجل
New TownCity|New city|Nouvelle ville|Kota baru|Nova cidade|Nueva ciudad|新しい街|新城市|새 도시|Новый город|Yeni şehir|مدينة جديدة
Làm mới|Refresh|Actualiser|Segarkan|Atualizar|Actualizar|更新|刷新|새로 고침|Обновить|Yenile|تحديث
Chọn tất cả|Select all|Tout sélectionner|Pilih semua|Selecionar tudo|Seleccionar todo|すべて選択|全选|모두 선택|Выбрать всё|Tümünü seç|تحديد الكل
Bỏ chọn tất cả|Deselect all|Tout désélectionner|Batalkan semua|Desmarcar tudo|Deseleccionar todo|すべて解除|取消全选|모두 선택 해제|Снять все выделения|Tüm seçimi kaldır|إلغاء تحديد الكل
Chọn cả nhóm|Select group|Sélectionner le groupe|Pilih grup|Selecionar grupo|Seleccionar grupo|グループを選択|选择整组|그룹 선택|Выбрать группу|Grubu seç|تحديد المجموعة
Bỏ chọn nhóm|Deselect group|Désélectionner le groupe|Batalkan grup|Desmarcar grupo|Deseleccionar grupo|グループを解除|取消整组选中|그룹 선택 해제|Снять выделение группы|Grup seçimini kaldır|إلغاء تحديد المجموعة
Chọn kết quả tìm|Select search results|Sélectionner les résultats|Pilih hasil pencarian|Selecionar resultados|Seleccionar resultados|検索結果を選択|选择搜索结果|검색 결과 선택|Выбрать результаты поиска|Arama sonuçlarını seç|تحديد نتائج البحث
Tất cả nhóm|All groups|Tous les groupes|Semua grup|Todos os grupos|Todos los grupos|すべてのグループ|全部组|모든 그룹|Все группы|Tüm gruplar|كل المجموعات
Chọn tất cả đang hiện|Select all visible|Tout sélectionner dans la vue|Pilih semua yang terlihat|Selecionar todos visíveis|Seleccionar todos visibles|表示中をすべて選択|全选可见项|표시된 항목 모두 선택|Выбрать все видимые|Görünenlerin tümünü seç|تحديد كل العناصر الظاهرة
Bỏ chọn|Deselect|Désélectionner|Batalkan pilihan|Desmarcar|Deseleccionar|選択解除|取消选择|선택 해제|Снять выделение|Seçimi kaldır|إلغاء التحديد
Sửa|Edit|Modifier|Edit|Editar|Editar|編集|编辑|편집|Изменить|Düzenle|تعديل
Hiện tại|Current|Actuel|Saat ini|Atual|Actual|現在|当前|현재|Текущее|Mevcut|الحالي
Giá trị mới|New value|Nouvelle valeur|Nilai baru|Novo valor|Nuevo valor|新しい値|新值|새 값|Новое значение|Yeni değer|القيمة الجديدة
Số lượng|Quantity|Quantité|Jumlah|Quantidade|Cantidad|数量|数量|수량|Количество|Miktar|الكمية
Tên|Name|Nom|Nama|Nome|Nombre|名前|名称|이름|Название|Ad|الاسم
Trạng thái|Status|État|Status|Estado|Estado|状態|状态|상태|Состояние|Durum|الحالة
Chi tiết|Details|Détails|Detail|Detalhes|Detalles|詳細|详情|상세 정보|Подробности|Ayrıntılar|التفاصيل
Thành công|Success|Réussi|Berhasil|Sucesso|Correcto|成功|成功|성공|Успешно|Başarılı|نجاح
Lỗi|Error|Erreur|Kesalahan|Erro|Error|エラー|错误|오류|Ошибка|Hata|خطأ
Chờ|Waiting|En attente|Menunggu|Aguardando|En espera|待機中|等待中|대기 중|Ожидание|Bekliyor|في الانتظار
Dừng|Stop|Arrêter|Hentikan|Parar|Detener|停止|停止|중지|Остановить|Durdur|إيقاف
Sao chép log|Copy log|Copier le journal|Salin log|Copiar log|Copiar registro|ログをコピー|复制日志|로그 복사|Копировать журнал|Günlüğü kopyala|نسخ السجل
Xuất log|Export log|Exporter le journal|Ekspor log|Exportar log|Exportar registro|ログを出力|导出日志|로그 내보내기|Экспорт журнала|Günlüğü dışa aktar|تصدير السجل
Xóa nhật ký|Clear log|Effacer le journal|Hapus log|Limpar log|Limpiar registro|ログを消去|清空日志|로그 지우기|Очистить журнал|Günlüğü temizle|مسح السجل
NHẬT KÝ THAO TÁC|ACTIVITY LOG|JOURNAL D’ACTIVITÉ|LOG AKTIVITAS|REGISTRO DE ATIVIDADE|REGISTRO DE ACTIVIDAD|操作ログ|操作日志|작업 로그|ЖУРНАЛ ДЕЙСТВИЙ|İŞLEM GÜNLÜĞÜ|سجل العمليات
File đầu ra|Output files|Fichiers de sortie|File keluaran|Arquivos de saída|Archivos de salida|出力ファイル|输出文件|출력 파일|Выходные файлы|Çıktı dosyaları|ملفات الإخراج
Chọn ZIP|Choose ZIP files|Choisir des ZIP|Pilih ZIP|Escolher ZIP|Elegir ZIP|ZIPを選択|选择 ZIP|ZIP 선택|Выбрать ZIP|ZIP seç|اختيار ZIP
Xem thông tin|View information|Voir les informations|Lihat informasi|Ver informações|Ver información|情報を表示|查看信息|정보 보기|Просмотр информации|Bilgileri görüntüle|عرض المعلومات
Mở để chỉnh sửa|Open for editing|Ouvrir pour modifier|Buka untuk diedit|Abrir para editar|Abrir para editar|編集用に開く|打开以编辑|편집용으로 열기|Открыть для редактирования|Düzenlemek için aç|فتح للتعديل
Khôi phục vào game|Restore to game|Restaurer dans le jeu|Pulihkan ke game|Restaurar no jogo|Restaurar en el juego|ゲームに復元|恢复到游戏|게임으로 복원|Восстановить в игру|Oyuna geri yükle|استعادة إلى اللعبة
Xóa ZIP|Delete local ZIP|Supprimer le ZIP local|Hapus ZIP lokal|Excluir ZIP local|Eliminar ZIP local|ローカルZIPを削除|删除本地 ZIP|로컬 ZIP 삭제|Удалить локальный ZIP|Yerel ZIP sil|حذف ZIP المحلي
Tạo backup|Create backup|Créer une sauvegarde|Buat cadangan|Criar backup|Crear copia|バックアップを作成|创建备份|백업 만들기|Создать резервную копию|Yedek oluştur|إنشاء نسخة احتياطية
Đăng nhập Google|Sign in to Google|Se connecter à Google|Masuk ke Google|Entrar no Google|Iniciar sesión en Google|Googleにログイン|登录 Google|Google 로그인|Войти в Google|Google ile giriş yap|تسجيل الدخول إلى Google
Đăng xuất|Sign out|Se déconnecter|Keluar|Sair|Cerrar sesión|ログアウト|退出登录|로그아웃|Выйти|Çıkış yap|تسجيل الخروج
Mở thư mục Drive|Open Drive folder|Ouvrir le dossier Drive|Buka folder Drive|Abrir pasta do Drive|Abrir carpeta de Drive|Driveフォルダーを開く|打开 Drive 文件夹|Drive 폴더 열기|Открыть папку Drive|Drive klasörünü aç|فتح مجلد Drive
Cấu hình cloud|Cloud settings|Paramètres cloud|Pengaturan cloud|Configurações da nuvem|Configuración de la nube|クラウド設定|云设置|클라우드 설정|Настройки облака|Bulut ayarları|إعدادات السحابة
Lưu cấu hình|Save settings|Enregistrer les paramètres|Simpan pengaturan|Salvar configurações|Guardar configuración|設定を保存|保存设置|설정 저장|Сохранить настройки|Ayarları kaydet|حفظ الإعدادات
Tải các ZIP đã chọn|Download selected ZIPs|Télécharger les ZIP sélectionnés|Unduh ZIP terpilih|Baixar ZIP selecionados|Descargar ZIP seleccionados|選択したZIPをダウンロード|下载选中的 ZIP|선택한 ZIP 다운로드|Скачать выбранные ZIP|Seçili ZIP dosyalarını indir|تنزيل ملفات ZIP المحددة
Tải ZIP đã chọn lên Drive|Upload selected ZIPs|Envoyer les ZIP sélectionnés|Unggah ZIP terpilih|Enviar ZIP selecionados|Subir ZIP seleccionados|選択したZIPをアップロード|上传选中的 ZIP|선택한 ZIP 업로드|Загрузить выбранные ZIP|Seçili ZIP dosyalarını yükle|رفع ملفات ZIP المحددة
Sao chép kết quả|Copy results|Copier les résultats|Salin hasil|Copiar resultados|Copiar resultados|結果をコピー|复制结果|결과 복사|Копировать результаты|Sonuçları kopyala|نسخ النتائج
Giao diện · Bộ màu|Appearance · Themes|Apparence · Thèmes|Tampilan · Tema|Aparência · Temas|Apariencia · Temas|外観・テーマ|外观 · 主题|외관 · 테마|Оформление · Темы|Görünüm · Temalar|المظهر · السمات
Bộ màu ứng dụng|Application theme|Thème de l’application|Tema aplikasi|Tema do aplicativo|Tema de la aplicación|アプリのテーマ|应用主题|앱 테마|Тема приложения|Uygulama teması|سمة التطبيق
Chọn màu|Choose color|Choisir une couleur|Pilih warna|Escolher cor|Elegir color|色を選択|选择颜色|색상 선택|Выбрать цвет|Renk seç|اختيار لون
Về màu mặc định|Reset theme|Réinitialiser le thème|Atur ulang tema|Redefinir tema|Restablecer tema|テーマをリセット|重置主题|테마 초기화|Сбросить тему|Temayı sıfırla|إعادة ضبط السمة
Xem thử toàn ứng dụng|Preview application|Aperçu de l’application|Pratinjau aplikasi|Visualizar aplicativo|Vista previa de la aplicación|アプリ全体をプレビュー|预览整个应用|앱 전체 미리 보기|Предпросмотр приложения|Uygulamayı önizle|معاينة التطبيق
Lưu & áp dụng|Save and apply|Enregistrer et appliquer|Simpan dan terapkan|Salvar e aplicar|Guardar y aplicar|保存して適用|保存并应用|저장 및 적용|Сохранить и применить|Kaydet ve uygula|حفظ وتطبيق
Nền ứng dụng|Application background|Fond de l’application|Latar aplikasi|Fundo do aplicativo|Fondo de la aplicación|アプリの背景|应用背景|앱 배경|Фон приложения|Uygulama arka planı|خلفية التطبيق
Nền thẻ / ô nhập|Panel / input background|Fond des panneaux / champs|Latar panel / input|Fundo de painel / campo|Fondo de panel / campo|パネル／入力欄の背景|面板／输入框背景|패널 / 입력 배경|Фон панели / ввода|Panel / giriş arka planı|خلفية اللوحات / الإدخال
Chữ chính|Main text|Texte principal|Teks utama|Texto principal|Texto principal|メインテキスト|主要文字|기본 텍스트|Основной текст|Ana metin|النص الرئيسي
Màu chủ đạo|Primary color|Couleur principale|Warna utama|Cor principal|Color principal|メインカラー|主色|기본 색상|Основной цвет|Ana renk|اللون الأساسي
Nút / tiêu đề bảng|Buttons / table headers|Boutons / en-têtes|Tombol / judul tabel|Botões / cabeçalhos|Botones / encabezados|ボタン／表の見出し|按钮／表头|버튼 / 표 머리글|Кнопки / заголовки|Düğmeler / tablo başlıkları|الأزرار / عناوين الجداول
Màu nhấn|Accent color|Couleur d’accent|Warna aksen|Cor de destaque|Color de acento|アクセントカラー|强调色|강조 색상|Акцентный цвет|Vurgu rengi|لون التمييز
Khi rê chuột|Hover color|Couleur au survol|Warna saat disorot|Cor ao passar o mouse|Color al pasar el ratón|ホバー色|悬停颜色|마우스 오버 색상|Цвет при наведении|Üzerine gelme rengi|لون مرور المؤشر
Mục đang chọn|Selection color|Couleur de sélection|Warna pilihan|Cor da seleção|Color de selección|選択色|选中颜色|선택 색상|Цвет выделения|Seçim rengi|لون التحديد
Áp dụng vào phiên|Apply to session|Appliquer à la session|Terapkan ke sesi|Aplicar à sessão|Aplicar a la sesión|セッションに適用|应用到当前会话|세션에 적용|Применить к сеансу|Oturuma uygula|تطبيق على الجلسة
Thiết bị / serial:|Device / serial:|Appareil / numéro de série :|Perangkat / serial:|Dispositivo / serial:|Dispositivo / serie:|デバイス／シリアル:|设备／序列号：|기기 / 시리얼:|Устройство / серийный номер:|Cihaz / seri no:|الجهاز / الرقم التسلسلي:
Gói Township:|Township package:|Package Township :|Paket Township:|Pacote Township:|Paquete Township:|Townshipパッケージ:|Township 包名：|Township 패키지:|Пакет Township:|Township paketi:|حزمة Township:
Thư mục lưu backup:|Backup folder:|Dossier de sauvegarde :|Folder cadangan:|Pasta de backup:|Carpeta de copias:|バックアップフォルダー:|备份文件夹：|백업 폴더:|Папка резервных копий:|Yedek klasörü:|مجلد النسخ الاحتياطية:
Chẩn đoán ADB / save|ADB / save diagnostics|Diagnostic ADB / sauvegarde|Diagnostik ADB / save|Diagnóstico ADB / save|Diagnóstico ADB / partida|ADB／セーブ診断|ADB／存档诊断|ADB / 저장 진단|Диагностика ADB / сохранения|ADB / kayıt tanılama|تشخيص ADB / الحفظ
Tự mở Township sau khi ghi vào game thành công|Launch Township after successful write|Ouvrir Township après l’écriture réussie|Buka Township setelah berhasil menyimpan|Abrir Township após gravar com sucesso|Abrir Township tras guardar correctamente|書き込み成功後にTownshipを起動|写入成功后启动 Township|저장 성공 후 Township 실행|Запустить Township после успешной записи|Başarılı kayıttan sonra Township aç|تشغيل Township بعد الحفظ بنجاح
Chưa tải save|No save loaded|Aucune sauvegarde chargée|Save belum dimuat|Nenhum save carregado|Sin partida cargada|セーブ未読み込み|未加载存档|저장 데이터 없음|Сохранение не загружено|Kayıt yüklenmedi|لم يتم تحميل حفظ
Chưa có thay đổi|No changes|Aucune modification|Belum ada perubahan|Sem alterações|Sin cambios|変更なし|无修改|변경 없음|Без изменений|Değişiklik yok|لا توجد تغييرات
Nguồn|Source|Source|Sumber|Origem|Origen|ソース|来源|원본|Источник|Kaynak|المصدر
Nguồn backup|Backup source|Source de sauvegarde|Sumber cadangan|Origem do backup|Origen de la copia|バックアップ元|备份来源|백업 원본|Источник резервной копии|Yedek kaynağı|مصدر النسخة الاحتياطية
Thư mục lưu|Destination folder|Dossier de destination|Folder tujuan|Pasta de destino|Carpeta de destino|保存先フォルダー|保存文件夹|저장 폴더|Папка назначения|Hedef klasör|مجلد الحفظ
Thư mục backup|Backup folder|Dossier de sauvegarde|Folder cadangan|Pasta de backup|Carpeta de copias|バックアップフォルダー|备份文件夹|백업 폴더|Папка резервных копий|Yedek klasörü|مجلد النسخ الاحتياطية
Thử lại mục lỗi / chưa thực hiện|Retry failed / pending files|Réessayer les fichiers en échec / en attente|Coba lagi file gagal / tertunda|Tentar arquivos com erro / pendentes|Reintentar archivos fallidos / pendientes|失敗／未実行のファイルを再試行|重试失败／未执行文件|실패 / 대기 파일 재시도|Повторить неудачные / ожидающие файлы|Hatalı / bekleyen dosyaları yeniden dene|إعادة محاولة الملفات الفاشلة / المعلقة
Chưa thực hiện|Pending|En attente|Tertunda|Pendente|Pendiente|未実行|未执行|대기 중|Не выполнено|Bekliyor|لم يتم التنفيذ
Đang truyền|Transferring|Transfert en cours|Sedang mentransfer|Transferindo|Transfiriendo|転送中|传输中|전송 중|Передача|Aktarılıyor|جارٍ النقل
Tìm tên hoặc ID…|Search name or ID…|Chercher un nom ou ID…|Cari nama atau ID…|Pesquisar nome ou ID…|Buscar nombre o ID…|名前またはIDで検索…|搜索名称或 ID…|이름 또는 ID 검색…|Поиск по имени или ID…|Ad veya ID ara…|البحث بالاسم أو المعرف…
Ngôn ngữ giao diện phổ biến; nhật ký và mô tả chưa dịch giữ nội dung gốc. Tiếng Ai Cập: tiếng Ả Rập (Ai Cập).|Menus and common controls are translated. Logs and untranslated descriptions keep their original text. Egyptian: Arabic (Egypt).|Les menus et commandes courantes sont traduits. Les journaux et descriptions non traduites gardent leur texte d’origine. Égypte : arabe.|Menu dan kontrol umum diterjemahkan. Log dan deskripsi yang belum diterjemahkan tetap dalam bahasa asli. Mesir: Arab (Mesir).|Menus e controles comuns são traduzidos. Logs e descrições sem tradução mantêm o texto original. Egito: árabe.|Se traducen los menús y controles comunes. Los registros y las descripciones sin traducir conservan el texto original. Egipto: árabe.|メニューと共通操作を翻訳します。ログと未翻訳の説明は原文のままです。エジプト：アラビア語。|菜单和常用控件已翻译。日志和未翻译的说明保留原文。埃及语：阿拉伯语（埃及）。|메뉴와 공통 컨트롤이 번역됩니다. 로그와 미번역 설명은 원문을 유지합니다. 이집트: 아랍어.|Меню и основные элементы переведены. Журналы и непереведённые описания сохраняют исходный текст. Египет: арабский.|Menüler ve ortak kontroller çevrilir. Günlükler ve çevrilmemiş açıklamalar özgün metni korur. Mısır: Arapça.|تُترجم القوائم وعناصر التحكم الشائعة. تحتفظ السجلات والأوصاف غير المترجمة بالنص الأصلي. لغة مصر: العربية.
'''
I18N_CATALOG={}
for _line in I18N_DATA.strip().splitlines():
    _parts=_line.split('|')
    if len(_parts)!=12:raise RuntimeError('Invalid interface translation row: '+_parts[0])
    I18N_CATALOG[_parts[0]]=dict(zip(I18N_CODES,_parts[1:]))
I18N_ALIASES={'Apply':'Áp dụng','Save':'Lưu','Cancel':'Hủy','Close':'Đóng','Yes':'Có','No':'Không','OK':'Áp dụng','All Card':'All Cards','My Card':'My Cards','Chọn thư mục…':'Chọn thư mục','Tên backup':'Backup','Tên ZIP':'Tên','Dung lượng':'Số lượng','Giao diện · Bộ màu':'Giao diện · Bộ màu'}

# English UI phrases also cover dynamic activity messages. Save data is never translated.
EN_EXTRA_DATA = "FetchCity & công cụ bổ sung|FetchCity & additional tools\nKết nối và tải save qua ADB|Connect and load saves via ADB\nSave tải từ thiết bị|Save loaded from device\nĐã tải save|Save loaded\nCó thay đổi chưa lưu|Unsaved changes\nSẵn sàng · Mở save hoặc kết nối thiết bị để bắt đầu|Ready · Open a save or connect a device to begin\nTownship Studio sẵn sàng. Tất cả thay đổi được giữ trong phiên trước khi xuất hoặc ghi vào game.|Township Studio is ready. Changes stay in the working session until you export or write to the game.\nChỉnh từng giá trị → Áp dụng → Xuất file hoặc Ghi vào game. Level: 1–1089, cho phép giảm và cập nhật XP. M3 giữ giới hạn của bản gốc.|Edit a value → Apply → Export file or Write to game. Level: 1–1089, including level reduction and XP updates. M3 uses the original limits.\nXem, chọn, mở hoặc khóa avatar|View, select, unlock or lock avatars\nChọn nhóm, món và số lượng trang trí|Choose decoration groups, items and quantities\nMở đất theo logic của bản gốc|Unlock land using the original rules\nHoàn thành bộ sưu tập bảo tàng|Complete museum collections\nCập nhật toàn bộ thẻ|Update all cards\nCập nhật các thẻ đang sở hữu|Update owned cards\nMở Golden Pass|Unlock Golden Pass\nChọn nhóm và mở skin|Choose groups and unlock skins\nChọn và mở sticker|Select and unlock stickers\nHuy hiệu, danh hiệu, khung và phong cách|Badges, titles, frames and styles\nChọn thành tích cần mở|Choose achievements to unlock\nCấp kho và số lượng sản phẩm|Barn level and product quantities\nPremium, score, stage và phần thưởng|Premium, score, stages and rewards\nChỉnh bonus nâng cấp tại học viện|Edit academy upgrade bonuses\nChỉnh thẻ động vật|Edit animal cards\nThiết lập lợi thế và thời hạn|Set advantages and durations\nChỉnh số ô chợ|Edit market slots\nChỉnh số lượng tài nguyên|Edit resource quantities\nChọn tàu, toa và thông số|Choose trains, carriages and settings\nChỉnh số nhiệm vụ MyOldTask|Edit the MyOldTask task count\nChọn người nhận và thông số gửi thẻ|Choose recipients and card delivery settings\nChọn donor và nội dung sao chép|Choose a donor and the content to copy\nXử lý đồng thời mGameInfo và LocalInfo|Process mGameInfo and LocalInfo together\nChọn nhóm hướng dẫn cần sửa|Choose tutorial groups to repair\nSao lưu ZIP trên máy và Google Drive|Back up ZIP files locally and to Google Drive\nĐọc backup trên máy hoặc Google Drive|Read backups from this computer or Google Drive\nTự tạo tài khoản mới LV3 / áp dụng mẫu ZIP|Create a new level-3 account / apply a ZIP template\nBackup tự động lưu trong backups; ZIP thành phố và History dùng a_TS_Files bên trong thư mục đã chọn. Thay đổi này áp dụng cho backup mới; file cũ giữ ở vị trí cũ.|Automatic backups use backups; city ZIPs and History use a_TS_Files under the chosen folder. This setting applies to new backups; existing files stay in their original locations.\nMuMu: nhập serial như 127.0.0.1:7555. Thiết bị cần kết nối ADB và có quyền root.|MuMu: enter a serial such as 127.0.0.1:7555. The device needs an ADB connection and root access.\nĐiền ADB, serial và tên gói hợp lệ.|Enter valid ADB, device serial and package settings.\nChọn thư mục lưu backup|Choose the backup folder\nKhông thể ghi backup vào thư mục này|Cannot write backups to this folder\nĐã sao chép nhật ký vào clipboard.|Log copied to clipboard.\nXuất nhật ký|Export log\nKhông xuất được nhật ký|Cannot export log\nĐã xuất nhật ký|Log exported\nĐang thực hiện|Running\nHoàn tất|Completed\nThao tác gặp lỗi|Operation failed\nĐã hủy thao tác|Operation cancelled\nKhông thực hiện được|Operation could not be completed\nThay đổi chưa lưu|Unsaved changes\nMở save mới sẽ bỏ các thay đổi chưa lưu. Tiếp tục?|Opening another save discards unsaved changes. Continue?\nMở save trước khi xuất.|Open a save before exporting.\nChọn thư mục xuất|Choose an export folder\nFile đầu ra đã tồn tại. Ghi đè?|The output file already exists. Overwrite it?\nGhi đè file|Overwrite file\nĐã encode, decode kiểm tra và xuất|Encoded, decoded for verification and exported\nXuất save đã xác minh|Export verified save\nĐang thao tác|Operation in progress\nĐợi thao tác hoàn tất; nếu đang nhập dữ liệu, chọn Hủy trong hộp thoại.|Wait for the operation to finish. To stop an input request, choose Cancel in its dialog.\nThoát và bỏ thay đổi chưa lưu?|Exit and discard unsaved changes?\nXem giá trị hiện tại|View current values\nDanh sách bạn bè|Friends list\nChọn bạn bè|Select friends\nFetchCity bạn bè|Fetch a friend's city\nXem donor|Inspect donor\nQuét City ID trong XML|Scan City IDs in XML\nSửa Var bất kỳ|Edit any Var\nSửa thuộc tính tag|Edit tag attributes\nKhôi phục backup local|Restore local backup\nCác công cụ bổ sung cũng sử dụng bảng danh sách và biểu mẫu.|Additional tools also use lists and forms.\nThay đổi chỉ áp dụng vào phiên. Dùng Xuất file hoặc Ghi vào game để lưu.|Changes apply to the working session. Use Export file or Write to game to save them.\nKiểm tra dữ liệu|Validate data\nTìm tên hoặc ID|Search name or ID\nChọn / Tên|Select / Name\nChưa có trong save; không áp dụng mục này|Missing from the save; this item cannot be applied\nKết quả editor GUI|GUI editor result\nKhông có thay đổi.|No changes.\nĐã áp dụng vào XML làm việc. Chưa ghi vào game.|Applied to the working XML. Not written to the game yet.\nChi tiết|Details\nĐã cập nhật|Updated\nChưa ghi vào game.|Not written to the game yet.\nThư mục tài khoản|Account folder\nSửa đổi|Modified\nChưa kiểm tra|Not checked\nHợp lệ · LV|Valid · Level\nChọn đúng một ZIP để xem, mở, khôi phục hoặc xóa. Nhiều ZIP chỉ dùng để tải lên Drive.|Select exactly one ZIP to view, open, restore or delete. Multiple ZIPs can be uploaded to Drive.\nChọn một hoặc nhiều ZIP để tải lên.|Select one or more ZIPs to upload.\nChọn một hoặc nhiều backup trong danh sách.|Select one or more backups from the list.\nChỉ xóa ZIP trên máy; không xóa backup trên Google Drive.|Deletes the local ZIP only; the backup on Google Drive is retained.\nMở/khôi phục sẽ tạo backup phiên hiện tại trước khi thay thế hai file.|Opening or restoring creates a backup of the current session before replacing both files.\nChọn nhiều ZIP để tải lên Drive (Ctrl / Shift). Mở hoặc khôi phục vào game cần chọn đúng một ZIP.|Select multiple ZIPs to upload to Drive (Ctrl / Shift). Select exactly one ZIP to open or restore to the game.\nTạo ZIP chứa mGameInfo.xml + LocalInfo.xml + thông tin tài khoản.|Create a ZIP containing mGameInfo.xml, LocalInfo.xml and account information.\nBackup từ thiết bị sẽ đóng game trước khi đọc để hai file nhất quán.|A device backup closes the game before reading, keeping both files consistent.\nHai file hiện tại trên thiết bị|Current pair of files on the device\nHai file gốc đã tải|Original pair of loaded files\nHai file đã chỉnh sửa (encode + verify)|Edited pair of files (encode + verify)\nTải bản ZIP lên Google Drive sau khi lưu trên máy|Upload the ZIP to Google Drive after saving locally\nCấu hình Google Drive…|Google Drive settings…\nĐã backup và kiểm tra ZIP|ZIP backup created and verified\nĐang tải backup lên Google Drive…|Uploading backup to Google Drive…\nTải lên cloud chưa hoàn tất. ZIP trên máy vẫn được giữ|Cloud upload did not complete. The local ZIP is retained\nĐã tải và kiểm tra backup Google Drive|Google Drive backup uploaded and verified\nBackup thay đổi chưa lưu|Backup of unsaved changes\nBackup file gốc|Backup of original files\nBackup cặp save hiện tại trên thiết bị|Backup of the current device save pair\nĐã khôi phục backup|Backup restored\nĐã mở backup|Backup opened\nKhôi phục|Restore\nkhôi phục|restore\nmở backup|open backup\nChọn thư mục lưu|Choose the destination folder\nTải lên nhiều ZIP|Upload multiple ZIPs\nTải về nhiều ZIP|Download multiple ZIPs\nCác file được truyền lần lượt trong một đợt. File thành công được giữ lại; file lỗi có thể thử riêng. Dừng sẽ chờ file đang truyền xong.|Files are transferred sequentially in one batch. Successful files are retained; failed files can be retried individually. Stop waits for the current file to finish.\nKết quả|Result\nĐang kết nối Google Drive…|Connecting to Google Drive…\nĐã kiểm tra dung lượng và mã kiểm tra trên Drive|Size and checksum verified on Drive\nĐang dừng…|Stopping…\nĐang đợi file hiện tại xong; các file tiếp theo sẽ không truyền.|Waiting for the current file to finish; remaining files will not be transferred.\nTổng|Total\nTên thư mục trên Drive|Drive folder name\nMặc định tải lên Google Drive khi tạo Backup|Upload to Google Drive by default when creating a backup\nZIP luôn được lưu trên máy trước. History đọc các backup TS Studio đã tải lên trong My Drive. Thông tin đăng nhập lưu trong kho bảo mật hệ điều hành.|ZIP files are saved locally first. History reads backups uploaded by TS Studio to My Drive. Credentials are stored in the operating system's secure vault.\nKiểm tra / chuẩn bị thư mục|Check / prepare folder\nHướng dẫn Google Drive|Google Drive guide\nĐiền tên thư mục Google Drive.|Enter a Google Drive folder name.\nChưa kiểm tra tài khoản|Account not checked\nTài khoản đã kiểm tra|Verified account\nThư mục|Folder\nĐã chuẩn bị|Ready\nChưa chuẩn bị / cần kiểm tra|Not ready / check required\nĐã kết nối|Connected\nKết nối và thư mục sẵn sàng|Connection and folder ready\nMở thư mục Google Drive|Open Google Drive folder\nXóa phiên Google trên máy? Các ZIP trên Drive vẫn được giữ.|Remove the Google session from this computer? ZIPs on Drive are retained.\nĐăng xuất Google Drive|Sign out of Google Drive\nSao chép hướng dẫn|Copy instructions\nMở Google Cloud Console|Open Google Cloud Console\nChọn nhiều backup bằng Ctrl / Shift hoặc Chọn tất cả đang hiện. File tải về được kiểm tra ZIP và mã kiểm tra trước khi mở hoặc khôi phục.|Select backups using Ctrl / Shift or Select all visible. Downloaded files pass ZIP and checksum checks before opening or restoring.\nTìm tên ZIP / City ID / level…|Search ZIP name / City ID / level…\nNgày sửa (UTC)|Modified (UTC)\nBấm Làm mới để đọc Google Drive.|Click Refresh to read Google Drive.\nĐọc History Google Drive|Read Google Drive history\nbackup trên Google Drive.|backups on Google Drive.\nTải và kiểm tra backup|Download and verify backup\nĐã dừng trước khi thực hiện|Stopped before starting\nThao tác chưa hoàn tất. Kiểm tra mạng / cấu hình rồi thử lại mục này.|The operation did not complete. Check network and settings, then retry this item.\nKhông kết nối được Google Drive; kiểm tra cấu hình và thử lại.|Cannot connect to Google Drive; check settings and retry.\nChọn file OAuth JSON hợp lệ, loại Desktop app. Xem Hướng dẫn Google Drive.|Choose a valid Desktop app OAuth JSON file. See the Google Drive guide.\nCần cài thư viện cloud|Cloud dependencies required\nKhông mở được kho bảo mật hệ điều hành. Trên Windows, kiểm tra Windows Credential Manager; Linux cần Secret Service / KWallet. Không lưu token dạng văn bản.|Cannot open the operating system's secure vault. On Windows, check Credential Manager; Linux requires Secret Service / KWallet. Tokens are not stored as plain text.\nKhông lưu được thông tin đăng nhập vào kho bảo mật hệ điều hành.|Cannot store credentials in the operating system's secure vault.\nĐăng nhập thành công. Bạn có thể đóng tab này và quay lại TS Studio.|Sign-in completed. You can close this tab and return to TS Studio.\nĐăng nhập chưa hoàn tất hoặc Google từ chối. Kiểm tra OAuth Desktop app, Test users và quyền Drive; thử lại trong 180 giây. Không có mật khẩu/token nào được ghi vào log.|Sign-in did not complete or Google denied access. Check the Desktop app OAuth client, Test users and Drive permission; retry within 180 seconds. Passwords and tokens are not logged.\nChưa đăng nhập Google Drive với OAuth client này. Mở Cấu hình → Google Drive → Đăng nhập Google.|Not signed in with this OAuth client. Open Settings → Google Drive → Sign in to Google.\nPhiên Google Drive hết hạn, bị thu hồi hoặc mất mạng. Kiểm tra mạng và đăng nhập lại trong Cấu hình.|The Google Drive session expired, was revoked or lost its connection. Check the network and sign in again in Settings.\nKhông xóa được phiên đăng nhập trong kho bảo mật.|Cannot remove the session from the secure vault.\nGoogle Drive chưa kết nối.|Google Drive is not connected.\nĐịa chỉ Google Drive không hợp lệ.|Invalid Google Drive address.\nKhông kết nối được Google Drive. Kiểm tra mạng; backup trên máy vẫn được giữ.|Cannot connect to Google Drive. Check the network; local backups are retained.\nDrive đang giới hạn yêu cầu; thử lại sau.|Drive is rate limiting requests; try again later.\nFile/thư mục không còn tồn tại hoặc OAuth client này không có quyền.|The file/folder no longer exists or this OAuth client lacks access.\nKiểm tra Google Drive API, quyền truy cập và dung lượng Drive.|Check Google Drive API, access permissions and storage space.\nĐăng nhập Google lại trong Cấu hình.|Sign in to Google again in Settings.\nThử lại sau; backup trên máy vẫn được giữ.|Retry later; local backups are retained.\nGoogle Drive trả về dữ liệu không hợp lệ.|Google Drive returned invalid data.\nID file/thư mục cloud không hợp lệ.|Invalid cloud file/folder ID.\nDrive chưa trả đủ kết quả. Thử Làm mới lại.|Drive returned incomplete results. Refresh again.\nDrive trả trang kết quả trùng; thử lại.|Drive returned a duplicate result page; retry.\nTên thư mục Google Drive cần từ 1 đến 150 ký tự.|The Google Drive folder name must contain 1–150 characters.\nMã kiểm tra backup tải về không khớp; không khôi phục.|Downloaded backup checksum mismatch; restoration is blocked.\nBackup cloud thiếu mã kiểm tra hoặc dung lượng vượt giới hạn.|The cloud backup lacks checksums or exceeds the size limit.\nFile cloud tải về vượt dung lượng đã công bố.|The download exceeds its declared size.\nTải backup bị gián đoạn. Chưa tạo file ZIP trên máy; hãy thử lại.|The backup download was interrupted. No local ZIP was created; retry.\nFile không phải backup thuộc thư mục TS Studio đang chọn.|This file is not a backup in the selected TS Studio folder.\nThao tác cloud chưa hoàn tất. Kiểm tra cấu hình và thử lại; các file trên máy vẫn được giữ.|The cloud operation did not complete. Check settings and retry; local files are retained.\nVui lòng đợi. Đăng nhập Google có thời gian chờ tối đa 180 giây.|Please wait. Google sign-in has a maximum wait of 180 seconds.\nMở đất; xóa các đối tượng expandBuy theo logic bản gốc.|Unlock land; remove expandBuy objects using the original rules.\nHoàn thành các cổ vật theo danh sách trong file gốc.|Complete artifacts using the original catalog.\nMở Golden Pass trong save đang chỉnh sửa.|Unlock Golden Pass in the working save.\nCập nhật toàn bộ thẻ theo logic gốc.|Update all cards using the original rules.\nChỉ cập nhật những thẻ đang sở hữu.|Update owned cards only.\nNhấn Áp dụng để thực hiện chức năng này.|Click Apply to run this action.\nBiển tên thành phố|City name signs\nĐồ trang trí thường|Standard decorations\nDanh mục lấy từ file gốc. Chọn từng món, cả nhóm hoặc toàn bộ; số lượng đặt lại trong kho. Biển tên luôn là 1.|The catalog comes from the original file. Select individual items, groups or all items; quantities are reset in storage. City signs always have quantity 1.\nSố lượng mỗi món|Quantity per item\nCác món Merge / Expedition có mẫu hoàn thành sẽ được hoàn thành theo TSVIP. Tên hiển thị là ID gốc khi chưa có bảng tên dịch.|Merge / Expedition items with completion templates use the TSVIP completion rules. Original IDs are shown when translated names are unavailable.\nChưa có cờ|No flag\nĐã khóa|Locked\nĐã mở|Unlocked\nChọn avatar cần mở hoặc khóa. Không nhập số thứ tự.|Select avatars to unlock or lock directly.\nKhóa avatar đã chọn|Lock selected avatars\nMở avatar đã chọn|Unlock selected avatars\nThao tác|Action\nChưa có cờ mở|No unlock flag\nĐã mở / áp dụng|Unlocked / applied\nChọn từng mục, cả nhóm hoặc toàn bộ danh mục.|Select individual items, groups or the entire catalog.\nTrong mỗi nhóm được chọn, danh sách Profile sẽ được THAY bằng lựa chọn mới theo logic TSVIP.|For each selected group, the Profile list is REPLACED with the new selection using TSVIP rules.\nGiá trị cho các mục đã chọn|Value for selected items\nĐặt cho mục đã chọn|Set selected items\nSửa cấp kho hoặc sản phẩm. Tab Sản phẩm chỉ áp dụng các dòng đã chọn có số lượng mới khác hiện tại.|Edit barn level or products. The Products tab applies only selected rows whose new quantities differ from the current values.\nSức chứa cơ bản|Base capacity\nSản phẩm|Products\nSố lượng cho các dòng đã chọn|Quantity for selected rows\nNhà máy|Factories\nTàu hỏa|Trains\nĐảo|Islands\nTab Cấp / Bonus: chọn nhà máy, tàu hoặc đảo. Tab Ô sản xuất: chỉnh số ô cho nhà máy đã có trong save.|Level / Bonus tab: select factories, trains or islands. Factory slots tab: edit slots for factories already present in the save.\nÔ sản xuất nhà máy|Factory production slots\nSố ô cho nhà máy đã chọn|Slots for selected factories\nxp/money/shelf dùng cho Factory/Train; products dùng cho Island. timeBonus: tối đa 100 ở Factory/Train, 101 ở Island.|xp/money/shelf apply to Factory/Train; products applies to Island. Maximum timeBonus: 100 for Factory/Train and 101 for Island.\ntimeBonus 101 chỉ áp dụng cho Đảo.|timeBonus 101 applies only to Islands.\nChưa có chuồng|No enclosure\nHoàn thành thẻ của các loài được chọn (30 mảnh, status=3). Chuồng chưa có trong save sẽ bị vô hiệu hóa.|Complete cards for selected species (30 pieces, status=3). Enclosures missing from the save are disabled.\nĐộng vật|Animals\nĐánh dấu bonus cần sửa; giá trị 0 tắt bonus. Các giá trị đề xuất lấy từ TSVIP.|Check bonuses to edit; 0 disables a bonus. Suggested values come from TSVIP.\nMine x2 · số ngày|Mine x2 · days\nChọn bonus hoặc bật sửa Mine x2.|Select a bonus or enable Mine x2 editing.\nBooster / Lab / Mỏ / Quặng|Booster / Lab / Mine / Ore\nSửa số lượng từng mục trong cột Giá trị mới, hoặc đặt cùng một giá trị cho các mục đã chọn.|Edit quantities in the New value column, or set a shared value for selected items.\nCần một Object citymarket có slotsCount.|A citymarket Object with slotsCount is required.\nChỉnh số ô chợ: 1–9999.|Edit market slots: 1–9999.\nSố ô chợ|Market slots\nChọn Stage ở FreeRoad / PremiumRoad. Bật Sửa ở các thông số cần cập nhật; ô không bật được giữ nguyên.|Choose a Stage in FreeRoad / PremiumRoad. Enable Edit for fields to update; unchecked fields stay unchanged.\nStages & thông số|Stages & settings\nSubReward của ST_Chest|ST_Chest SubReward\nChưa có Reward|No Reward\nChọn số ô sản xuất từ 2 đến 7. Chỉ sửa nhà máy đã có dữ liệu hợp lệ; mục thiếu hoặc trùng dữ liệu bị vô hiệu hóa.|Choose 2–7 production slots. Only factories with valid data can be edited; missing or duplicate entries are disabled.\nChưa có dữ liệu nhà máy|No factory data\nCó nhiều Object / thuộc tính JSON cùng ID|Multiple Objects / JSON attributes share this ID\nThiếu slotsCount hoặc ngoài phạm vi hỗ trợ 2–7|Missing slotsCount or outside the supported range of 2–7\nJSON trùng khóa|Duplicate JSON keys\nChọn ít nhất một nhà máy có số ô thay đổi.|Select at least one factory with a changed slot count.\nSố ô sản xuất phải từ 2 đến 7.|Production slots must be between 2 and 7.\nChưa có Object nhà máy hợp lệ trong save.|The save contains no valid factory Object.\nXác minh ô sản xuất thất bại|Factory slot verification failed\nChọn ít nhất một nhà máy có số ô mới khác hiện tại.|Select at least one factory whose new slot count differs from its current value.\nĐọc được|Read\nSẽ áp dụng|Will apply\nnhà máy đã sửa|factories edited\nsố ô|slot count\nTải nguồn để xem các phần có thể sao chép, rồi chọn những phần muốn áp dụng.|Load the source to see which sections can be copied, then select the sections to apply.\nTải nguồn và xem danh sách|Load source and view sections\nĐổi nguồn / tải lại…|Change source / reload…\nChưa tải nguồn.|Source not loaded.\nDanh sách các phần sẽ xuất hiện sau khi tải nguồn.|Available sections appear after the source is loaded.\nLấy Level + XP từ donor và đồng bộ LocalInfo (cho phép giảm LV)|Copy donor Level + XP and synchronize LocalInfo (allows level reduction)\nGiữ City ID và thông tin tài khoản hiện tại. Muốn giữ LV/XP: bỏ chọn lấy Level và không chọn Stats. Stats vẫn lấy LV/XP như V1 trước đây.|Keep the current City ID and account identity. To keep Level/XP, uncheck Copy Level and do not select Stats. Stats copies Level/XP as in the original V1 behavior.\nThu gọn nguồn|Collapse source\nNguồn đã đổi. Nhấn Tải nguồn để cập nhật danh sách.|The source changed. Click Load source to update the section list.\nNguồn bố cục|Layout source\nĐang tải nguồn…|Loading source…\nĐã hủy tải nguồn.|Source loading cancelled.\nKhông tải được nguồn|Cannot load source\nĐợi tải nguồn hoàn tất.|Wait for the source to finish loading.\nTải nguồn trước khi áp dụng.|Load the source before applying.\nChọn Stats cùng AirScore / AirInfo, hoặc bỏ chọn AirScore.|Select Stats with AirScore / AirInfo, or uncheck AirScore.\nĐang tải nguồn|Loading source\nĐợi yêu cầu tải nguồn hoàn tất trước khi đóng.|Wait for source loading to finish before closing.\nBố cục thành phố|City layout\nSở thú / Bảo tàng|Zoo / Museum\nTrang trí / Hồ sơ|Decorations / Profiles\nThống kê / Tùy chọn|Statistics / Options\nĐất và công trình thành phố|City land and buildings\nĐảo / IslandsInfo|Islands / IslandsInfo\nBảo tàng / ArtInfo|Museum / ArtInfo\nPhong cách|Styles\nXóa CCSecret|Remove CCSecret\nBackup ZIP thành phố|City backup ZIP\nBạn bè từ LocalInfo|Friends from LocalInfo\nDonor đã tải|Loaded donor\nFile XML/save trên máy|Local XML/save file\nBạn bè|Friends\nChọn file donor tồn tại.|Choose an existing donor file.\nChọn/nhập City ID hợp lệ.|Select or enter a valid City ID.\nĐiền bver và fver.|Enter bver and fver.\nChưa có donor. Chọn file hoặc FetchCity.|No donor is loaded. Choose a file or use FetchCity.\nFetchCity thành công|FetchCity succeeded\nClone V1 làm thay đổi trường cần giữ|Clone V1 changed a protected field\nPhiên bản nguồn|Source version\nchưa xác định|unknown\nChọn ít nhất một mục Clone V1 hợp lệ.|Select at least one valid Clone V1 section.\nNguồn không đủ dữ liệu|The source lacks required data\nSave hiện tại thiếu City ID; chưa áp dụng Clone V1.|The current save lacks a City ID; Clone V1 was not applied.\nAirScore / AirInfo hiện dùng cùng Stats trong V1. Chọn thêm Stats hoặc bỏ chọn AirScore.|AirScore / AirInfo requires Stats in V1. Select Stats or uncheck AirScore.\nCặp save V3 chuẩn bị|Prepared V3 save pair\nCặp save LV3 chuẩn bị|Prepared level-3 save pair\nCặp save encode trước ghi|Encoded save pair before writing\nĐọc lại từ thiết bị trước mở game|Device readback before launching the game\nLV kết quả|Resulting level\nLV trước|Previous level\nLV nguồn|Source level\nĐã chuẩn bị cặp mGameInfo + LocalInfo|mGameInfo + LocalInfo pair prepared\nToàn bộ donor mGameInfo|Complete donor mGameInfo\nGiữ cityId/gameId/token/thiết bị của tài khoản hiện tại|Keep the current account cityId/gameId/token/device\nTạo lại LocalInfo, xóa danh sách bạn/clan cũ|Rebuild LocalInfo and remove the previous friends/clan lists\nReset Regata/team/clan của donor|Reset donor Regata/team/clan\nGiữ PromoCode của target|Keep target PromoCode\nĐã ghi cặp save|Save pair written\nGhi thành công. Backup|Write completed. Backup\nBackup thiết bị|Device backup\nĐã gửi lệnh mở Township trên giả lập|Township launch command sent to the emulator\nPhiên bản save V3: hiện tại|V3 save version: current\nPhiên bản Township đang cài trên thiết bị|Township version installed on device\nCảnh báo|Warning\nKhông xác định|Cannot determine\nLevel giữa mGameInfo và LocalInfo không khớp; giữ game đóng để kiểm tra.|Levels in mGameInfo and LocalInfo do not match; keep the game closed for inspection.\nClone đổi LV cần tải cả mGameInfo và LocalInfo qua ADB.|Level-changing clones require both mGameInfo and LocalInfo loaded via ADB.\nLocalInfo chưa đồng bộ LV; không áp dụng clone.|LocalInfo level is not synchronized; clone was not applied.\nChưa có đủ City ID, Game ID và token.|City ID, Game ID or token is missing.\nĐịnh danh giữa hai file chưa khớp.|The identities in the two files do not match.\nDừng quét|Stop scan\nDừng tạo mới|Stop new-city creation\nĐang đợi request hiện tại kết thúc…|Waiting for the current request to finish…\nNew TownCity · tự động LV3|New TownCity · automatic level 3\nChờ định danh mới|Waiting for a new identity\nĐã nhận diện và bấm Agree của Township.|Township Agree button detected and clicked.\nĐã bấm vị trí Agree do bạn cấu hình.|Clicked the configured Agree position.\nTài khoản mới không còn ở LV1–3; chưa áp dụng mẫu.|The new account is no longer at level 1–3; the template was not applied.\nMẫu phải ở LV3.|The template must be at level 3.\nGhép mẫu làm thay đổi định danh.|Applying the template changed the identity.\nTất cả (*)|All files (*)\nChọn nguồn|Choose source\nMở save hoặc kết nối ADB trước khi Apply.|Open a save or connect ADB before applying.\nChọn ít nhất một mục.|Select at least one item.\nTùy chỉnh|Custom\nXem trước · Township Studio|Preview · Township Studio\nNền, chữ, nút, ô nhập và danh sách sử dụng bộ màu đã chọn.|Backgrounds, text, buttons, fields and lists use the selected theme.\nChọn bộ màu hoặc chỉnh từng màu bằng bảng chọn / mã HEX. Xem thử không lưu; Đóng sẽ trở lại màu trước đó. Nút ADB giữ đỏ/xanh theo trạng thái kết nối.|Choose a theme or edit colors using the picker / HEX values. Preview does not save; Close restores the previous theme. ADB keeps its red/green connection indicators.\nChữ được kiểm tra độ rõ; màu chữ trên nút và mục chọn tự điều chỉnh theo nền.|Text contrast is checked; button and selection text colors adapt to their backgrounds.\nBộ màu thiếu thành phần.|The theme is missing required colors.\nNhập mã màu dạng #RRGGBB hoặc dùng bảng chọn màu.|Enter a #RRGGBB color or use the color picker.\nChữ chính chưa đủ rõ trên nền ứng dụng / nền thẻ. Chọn chữ sáng hơn với nền tối, hoặc chữ tối hơn với nền sáng.|Main text has insufficient contrast against the application / panel background. Use lighter text on dark backgrounds or darker text on light backgrounds.\nThành phố|City\nThông tin thành phố|City information\nBackup đã chọn|Selected backup\nNgôn ngữ giao diện phổ biến; nhật ký và mô tả chưa dịch giữ nội dung gốc. Tiếng Ai Cập: tiếng Ả Rập (Ai Cập).|Choose the interface language. English includes additional captions and activity messages. Other languages use the available catalog and English fallback. Egyptian means Arabic (Egypt).\nChưa nhận|Not received\nĐã nhận|Received\nThay danh sách SubReward của ST_Chest (để danh sách trống sẽ xóa)|Replace ST_Chest SubReward list (an empty list removes it)\n+ Thêm SubReward|+ Add SubReward\nXóa dòng đã chọn|Delete selected row\nBật ít nhất một ô Sửa.|Enable at least one Edit checkbox.\nSave đang mở chưa có dữ liệu toa tàu theo định dạng editor hỗ trợ.|The current save has no carriage data in a supported format.\nChọn khối Trains|Select a Trains block\nMở nhóm đã chọn|Open selected group\nSave chứa nhiều nhóm dữ liệu tàu. Chọn nhóm thuộc thành phố đang chỉnh sửa; chương trình chỉ cập nhật nhóm được chọn.|The save contains multiple train groups. Choose the group belonging to the city being edited; only that group will be updated.\nDữ liệu toa hiện có|Existing carriage data\nNhóm / đường dẫn XML|Group / XML path\nSố dòng tàu|Number of train rows\nChọn một nhóm trong bảng.|Select a group in the table.\nNếu chưa xác định được nhóm cần sửa, dùng Lưu chẩn đoán Train để gửi đường dẫn XML cho người hỗ trợ.|If unsure which group to edit, use Save Train diagnostics to provide the XML paths to support.\nLưu chẩn đoán Train|Save Train diagnostics\nCó nhiều khối Trains; cần xác định nhóm đang dùng.|Multiple Trains blocks exist; identify the active group.\nChọn toa ở một hoặc nhiều tàu. Các ô không bật Sửa được giữ nguyên; productDone=0 đặt lại trạng thái toa theo TSVIP.|Select carriages from one or more trains. Unchecked fields remain unchanged; productDone=0 resets carriage state using TSVIP rules.\nBật Sửa ít nhất một thông số toa tàu.|Enable Edit for at least one carriage field.\nTrain · chưa có dữ liệu toa tàu|Train · no carriage data\nTải lại save qua ADB|Reload saves via ADB\nĐã lưu chẩn đoán|Diagnostics saved\nChẩn đoán Train|Train diagnostics\nTrain chỉnh toa tàu hiện có. Nâng cấp cấp tàu dùng Tool → Academi → Tàu hỏa.|Train edits existing carriages. To upgrade train levels, use Tools → Academy → Trains.\nSố MyOldTask hiện tại|Current MyOldTask count\nSố nhiệm vụ mới|New task count\nĐặt lại danh sách nhiệm vụ đã hoàn thành; 150 điểm/mục, ưu tiên Match3 theo TSVIP.|Reset completed tasks; 150 points per item, prioritizing Match3 using TSVIP rules.\nMục tiêu|Target\nPhiên bản|Version\nChọn một hoặc nhiều nhóm hướng dẫn cần sửa.|Choose one or more tutorial groups to repair.\nNhóm tutorial|Tutorial groups\nPhiên save đã thay đổi; mở lại Clone V1 để tải đúng dữ liệu.|The save session changed; reopen Clone V1 to load the correct data.\nchưa có|missing\nClone đổi LV cần LocalInfo; kết nối ADB tải lại cả hai file.|Level-changing clones require LocalInfo; reconnect ADB and reload both files.\nThiếu container gốc để kiểm tra Clone V1; kết nối ADB lại.|The original container is missing for Clone V1 verification; reconnect ADB.\nClone V1 encode/decode mGameInfo không khớp; chưa áp dụng.|Clone V1 mGameInfo encode/decode mismatch; changes were not applied.\nClone V1 encode/decode LocalInfo không khớp; chưa áp dụng.|Clone V1 LocalInfo encode/decode mismatch; changes were not applied.\nBackup phiên trước Clone V1|Session backup before Clone V1\nBackup XML trước Clone V1|XML backup before Clone V1\nKhông khôi phục được file làm việc|Cannot restore the working file\nĐã chuẩn bị cả mGameInfo và LocalInfo; khi ghi sẽ ghi cặp save.|mGameInfo and LocalInfo are both prepared; both will be written together.\nĐã áp dụng vào XML làm việc. LocalInfo giữ nguyên.|Applied to the working XML. LocalInfo is unchanged.\nClone V3 cần LocalInfo của tài khoản hiện tại.|Clone V3 requires LocalInfo from the current account.\nChọn nguồn donor. FetchCity chạy khi áp dụng nếu chọn City ID hoặc bạn bè.|Choose a donor source. FetchCity runs on Apply if a City ID or friend is selected.\nGiữ AirScore / AirInfo của donor|Keep donor AirScore / AirInfo\nXóa CCSecret của donor|Remove donor CCSecret\nV3 thay toàn bộ donor mGameInfo và dựng lại LocalInfo; giữ cityId/gameId/token/thiết bị hiện tại, reset clan/bạn bè/regatta. Phải xuất hoặc ghi cả hai file cùng nhau.|V3 replaces mGameInfo with the donor save and rebuilds LocalInfo; it preserves current cityId/gameId/token/device and resets clan/friends/regatta. Export or write both files together.\nClone V3 chưa lấy đúng LV nguồn; không áp dụng.|Clone V3 did not copy the source level correctly; changes were not applied.\nChọn thư mục lưu.|Choose a destination folder.\nTải lên Drive chưa hoàn tất; kiểm tra mạng và cấu hình rồi thử lại từ History.|Drive upload did not complete; check the network and settings, then retry from History.\nLọc tên file / tên tài khoản / City ID / level…|Filter filename / account name / City ID / level…\nChọn các backup ZIP|Choose backup ZIP files\nĐã chọn|Selected\nZIP. Bấm Tải ZIP đã chọn lên Drive để tải cả đợt.|ZIPs. Click Upload selected ZIPs to upload the batch.\nThay cặp save|Replace save pair\nBackup phiên hiện tại rồi thay toàn bộ hai file bằng ZIP đã chọn|Back up the current session and replace both files with the selected ZIP\nvà ghi vào game?|and write to the game?\nXóa|Delete\nKhông xóa được|Cannot delete\nĐã tải và kiểm tra|Downloaded and verified\nZIP. Chọn một ZIP để xem thông tin hoặc khôi phục.|ZIPs. Select one ZIP to inspect or restore.\nTài khoản trên thiết bị khác phiên đã tải; kết nối lại ADB trước khi tạo mới.|The device account differs from the loaded session; reconnect ADB before creating a new account.\nMẫu LV3 khác phiên bản save hiện tại. Chọn ZIP cùng phiên bản trước khi reset.|The level-3 template version differs from the current save. Choose a matching ZIP before resetting.\nBackup tài khoản trước thao tác|Account backup before this operation\nBước 1/4: ghi mẫu reset New TownCity. Game sẽ tạo định danh mới khi khởi động.|Step 1/4: write the New TownCity reset template. The game will create a new identity on launch.\nĐã ghi mẫu reset; backup|Reset template written; backup\nTiếp tục từ tài khoản đã reset; không ghi mẫu reset lần nữa.|Continue from the reset account; do not write the reset template again.\nBước 2/4: mở Township và chờ City ID mới.|Step 2/4: launch Township and wait for a new City ID.\nĐịnh danh đổi khi đóng game; chưa ghép mẫu. Kết nối lại ADB rồi tiếp tục.|The identity changed when closing the game; the template was not applied. Reconnect ADB and continue.\nBackup định danh mới trước LV3|Backup of the new identity before level 3\nBước 3/4: ghép mẫu LV3, giữ City ID / Game ID / token / thiết bị.|Step 3/4: apply the level-3 template, preserving City ID / Game ID / token / device.\nĐã có City ID mới|New City ID obtained\nZIP LV3 đã chuẩn bị|Level-3 ZIP prepared\nĐã ghi và xác minh cặp save LV3. Backup ghi|Level-3 save pair written and verified. Write backup\nBước 4/4: mở Township để kiểm tra LV3 và tutorial.|Step 4/4: launch Township to check level 3 and the tutorial.\nHoàn tất chuẩn bị tài khoản LV3. City ID|Level-3 account preparation completed. City ID\nKiểm tra kết quả trong game; bản ghi đã xác minh trước khi mở game.|Check the result in the game; the save was verified before launching.\nTạo mới LV3: backup → reset → mở game / Agree → đợi định danh mới → ghép mẫu LV3 → ghi và mở game. Thao tác này ghi trực tiếp vào game.|Create level 3: backup → reset → launch game / Agree → wait for a new identity → apply the level-3 template → write and launch. This action writes directly to the game.\nChế độ|Mode\nMẫu TSVIP có sẵn (chuẩn bị như trước)|Built-in TSVIP template (prepare only)\nZIP thành phố của bạn (chuẩn bị như trước)|Your city ZIP (prepare only)\nTiếp tục LV3 sau reset / chờ Agree|Continue level 3 after reset / waiting for Agree\nTự tạo tài khoản mới LV3|Automatically create a level-3 account\nZIP mẫu LV3 / ZIP thành phố|Level-3 template ZIP / city ZIP\nĐể trống ZIP ở chế độ LV3 sẽ dùng mẫu 39.0.2 đã thử thành công. Có thể chọn mẫu LV3 khác cùng phiên bản. Không dùng ID của mẫu làm ID tài khoản mới.|Leave the ZIP field empty in level-3 mode to use the tested 39.0.2 template. You can choose another level-3 template with a matching version. The template's ID is not used as the new account ID.\nThời gian chờ định danh|Identity wait timeout\nTự nhận diện và bấm Agree bằng ADB|Automatically detect and click Agree via ADB\nDùng tọa độ Agree đã xác định nếu không đọc được chữ (tùy chọn)|Use configured Agree coordinates if text detection fails (optional)\nTiếp tục và ghi LV3|Continue and write level 3\nTạo mới và ghi vào game|Create new account and write to game\nTạo mới sẽ thay tài khoản hiện tại; backup được lưu trước khi reset. Hết thời gian chờ: dùng chế độ Tiếp tục để tránh reset lại. Với các chế độ chuẩn bị, vẫn cần bấm Ghi vào game như trước.|Creating a new account replaces the current one; a backup is saved before resetting. If the timeout expires, use Continue to avoid resetting again. Prepare-only modes still require Write to game.\nChọn mẫu LV3.|Choose a level-3 template.\nChọn ZIP thành phố.|Choose a city ZIP.\nĐã chuẩn bị New TownCity|New TownCity prepared\nChọn người nhận và card; các request được gửi qua SendBox API. Master AES key cần lấy từ phiên TSVIP hợp lệ.|Choose recipients and cards; requests use the SendBox API. Obtain the Master AES key from a valid TSVIP session.\nKhông tự gửi lại khi timeout; kiểm tra hộp thư trong game trước khi thao tác lại. Token và master key không được lưu vào báo cáo.|No automatic resend on timeout; check the in-game mailbox before retrying. Tokens and master keys are excluded from reports.\nTên sender|Sender name\nsendCounter bắt đầu|Starting sendCounter\nCity ID bổ sung, phân cách bằng dấu phẩy|Additional City IDs, separated by commas\nNgười nhận|Recipients\nChọn ít nhất một người nhận.|Select at least one recipient.\nMaster AES key phải là hex hợp lệ.|The Master AES key must be valid hexadecimal.\nMaster AES key phải dài 16, 24 hoặc 32 byte.|The Master AES key must be 16, 24 or 32 bytes long.\nBáo cáo|Report\nĐang có cặp save chưa lưu. Xuất/ghi hoặc hoàn tác trước.|An unsaved save pair is pending. Export/write it or undo first.\nĐã đọc LocalInfo|LocalInfo loaded\nbạn bè|friends\nKhông tìm thấy màn hình khởi động cho|Cannot find a launch activity for\nThiếu LocalInfo gốc; kết nối ADB tải lại cặp save.|Original LocalInfo is missing; reconnect ADB and reload both files.\nSave hiện tại trước ghi|Current save before writing\nLocalInfo hiện tại trước ghi|Current LocalInfo before writing\nTài khoản trên thiết bị đã đổi hoặc thiếu cityId/gameId. Không ghi kết quả clone; kết nối lại ADB trên đúng tài khoản.|The device account changed or cityId/gameId is missing. Clone output was not written; reconnect ADB on the correct account.\nSave đã thay đổi từ lúc kết nối; đã backup cặp save mới|The save changed since connection; the new save pair was backed up\nĐã cập nhật bản gốc để đối chiếu; giữ nguyên cặp save clone đang chờ ghi.|The original baseline was updated; the pending cloned save pair is unchanged.\nKhông có thay đổi để ghi.|No changes to write.\nSave thay đổi ngay sau ghi; chưa mở game. Kiểm tra backup và kết nối lại ADB.|The save changed immediately after writing; the game was not launched. Check backups and reconnect ADB.\nSave đã ghi thành công, nhưng không mở được Township|The save was written, but Township could not be launched\nMở save trước.|Open a save first.\nKhông có thay đổi chưa lưu.|No unsaved changes.\nEncode + verify, tạo backup rồi ghi|Encode + verify, create a backup, then write\ncả mGameInfo và LocalInfo|both mGameInfo and LocalInfo\nvào thiết bị đã cấu hình?|to the configured device?\nBỏ toàn bộ thay đổi chưa lưu?|Discard all unsaved changes?\nĐã hoàn tác phiên về save gốc.|The session was reset to the original save.\nHướng dẫn TS Studio|TS Studio help\nBạn bè / FetchCity|Friends / FetchCity\nXem donor hiện tại|View current donor\nCông cụ|Tools\nMở LocalInfo trước để có danh sách bạn bè.|Open LocalInfo first to load the friends list.\nFetchCity lưu donor, chưa thay đổi save tài khoản hiện tại.|FetchCity saves the donor; the current account save is unchanged.\nFetchCity người đã chọn|Fetch selected friend's city\nTìm tên hoặc City ID|Search name or City ID\nTìm và chọn bạn bè; chọn tải donor hoặc chỉ lưu lựa chọn.|Find and select a friend; fetch the donor or save the selection only.\nNhóm|Group\nChọn bạn bè, chưa Fetch|Select friend without fetching\nChọn một người trong bảng.|Select a person in the table.\nĐã chọn bạn bè|Friend selected\nChỉ tải donor|Fetch donor only\nNhập City ID để tải donor; có thể clone layout ngay vào save đã mở.|Enter a City ID to fetch the donor; the layout can be cloned into the open save immediately.\nSau khi tải|After fetching\nLấy Level + XP từ donor (cho phép giảm LV)|Copy donor Level + XP (allows level reduction)\nCity ID phải có 3–64 ký tự chữ, số, _ hoặc -.|City ID must contain 3–64 letters, digits, _ or -.\nĐã tải donor|Donor loaded\nChưa có donor.|No donor loaded.\nDonor hiện tại|Current donor\nChọn nguồn donor và phần layout cần sao chép.|Choose the donor source and layout sections to copy.\nChọn friend_city / friend_honor XML|Choose friend_city / friend_honor XML\nCity ID liên quan|Related City IDs\nTìm thấy|Found\nMở LocalInfo có bạn bè trước.|Open LocalInfo containing friends first.\nBắt đầu quét|Start scan\nQuét mạng bạn bè, lọc trùng City ID và tìm tài khoản theo level.|Scan the friend network, deduplicate City IDs and find accounts by level.\nRandom · xáo trộn|Random · shuffled\nGiới hạn FetchCity|FetchCity limit\nKiểu quét|Scan mode\nNghỉ giữa request (giây)|Request interval (seconds)\nSố tài khoản mục tiêu|Target account count\nĐiều kiện level (>100, >=150, 100-200)|Level condition (>100, >=150, 100-200)\nĐộ sâu|Depth\nKết quả được lưu theo từng bước trong workspace_simple/friend_network. Bấm Dừng quét để dừng sau request đang chạy.|Results are saved incrementally in workspace_simple/friend_network. Click Stop scan to stop after the current request.\nGiới hạn FetchCity phải ≥ số tài khoản mục tiêu.|The FetchCity limit must be ≥ the target account count.\nFriend Network yêu cầu tham số ngoài cấu hình GUI.|Friend Network requires parameters beyond the GUI settings.\n+ Thuộc tính|+ Attribute\nThuộc tính|Attribute\nXóa dòng|Delete row\nGiá trị|Value\nTên thuộc tính không hợp lệ.|Invalid attribute name.\nThuộc tính bị trùng|Duplicate attribute\nThêm ít nhất một thuộc tính.|Add at least one attribute.\nChọn Var, tải thuộc tính rồi sửa trực tiếp từng dòng. Không cho thay name của Var.|Choose a Var, load its attributes and edit rows directly. The Var name cannot be changed.\nTên Var|Var name\nTải thuộc tính|Load attributes\nKhông được đổi name của Var.|The Var name cannot be changed.\nCông cụ XML chuyên sâu: điều kiện tìm tag dùng key=value, phân cách dấu phẩy. Thuộc tính cập nhật sửa trực tiếp trong bảng.|Advanced XML tools: specify tag filters as comma-separated key=value pairs. Edit updated attributes directly in the table.\nTên tag|Tag name\nĐiều kiện tìm|Search filter\nTên tag không hợp lệ.|Invalid tag name.\nCần ít nhất một thuộc tính tìm tag.|At least one tag filter attribute is required.\nKhông sửa thuộc tính đang dùng để tìm tag.|Cannot change an attribute used in the tag filter.\nChưa có backup local *.mGameInfo. Backup cặp ZIP nằm trong tab VIP → History.|No local *.mGameInfo backup exists. ZIP pair backups are available under VIP → History.\nChọn backup mGameInfo cần ghi vào thiết bị.|Choose the mGameInfo backup to write to the device.\nĐã khôi phục. Kết nối/tải save lại trước khi chỉnh sửa tiếp.|Restored. Reconnect/reload saves before editing further.\nTùy chỉnh · chọn màu của bạn|Custom · choose your own colors\nSao chép toàn bộ nhật ký đang hiển thị|Copy the entire displayed log\nLưu nhật ký đang hiển thị thành file TXT UTF-8|Save the displayed log as a UTF-8 TXT file\nMở|Open\nCập nhật|Update\nNhật ký (*.txt);;Tất cả (*)|Log (*.txt);;All files (*)\nthiếu|missing\nChọn ADB|Choose ADB\nChẩn đoán|Diagnostics\nGiữ đầy đủ các công cụ còn lại của file gốc. Thao tác và danh sách lựa chọn mở bằng hộp thoại.|Includes the remaining tools from the original file. Actions and selections open in dialogs.\nThư mục cloud đã bị thay đổi. Trong Cấu hình, chọn lại tên thư mục và chuẩn bị thư mục mới.|The cloud folder has changed. Select its name again in Settings and prepare a new folder.\nDrive không trả địa chỉ tải lên; ZIP trên máy vẫn được giữ.|Drive did not return an upload URL; the local ZIP is retained.\nBản cloud chưa qua kiểm tra dung lượng / mã kiểm tra; không coi là backup thành công. Giữ ZIP trên máy và kiểm tra Drive.|The cloud copy failed size/checksum verification and is not considered a successful backup. Keep the local ZIP and check Drive.\nKiểm tra Google Drive|Check Google Drive\nChọn ít nhất một mục trong danh sách.|Select at least one list entry.\nmục có thể áp dụng|applicable entries\nNguyên liệu biển|Sea ingredients\nNguyên liệu nông trại|Farm ingredients\nVật liệu / Dụng cụ|Materials / Tools\nSắp xếp trong từng nhóm:|Sort within each group:\nSố lượng hiện tại: cao → thấp|Current quantity: high → low\nSố lượng hiện tại: thấp → cao|Current quantity: low → high\nChọn ít nhất một dòng có số lượng mới khác hiện tại.|Select at least one row whose new quantity differs from the current value.\nĐã sửa|Edited\nĐã dừng chẩn đoán.|Diagnostics stopped.\nGói đã chọn|Selected package\nThiết bị|Device\nThiết bị chưa sẵn sàng. Kiểm tra serial và kết nối ADB.|The device is not ready. Check the serial and ADB connection.\nChưa xác nhận được package; kiểm tra tên gói.|Package not confirmed; check the package name.\nĐã cài|Installed\nQuyền root: chưa xác nhận được UID 0. Bật root trong giả lập và cấp quyền cho ADB.|Root access: UID 0 not confirmed. Enable root in the emulator and grant ADB access.\nKhông thể kiểm tra save riêng của game.|Cannot inspect the game's private save files.\nQuyền root: OK (UID 0)|Root access: OK (UID 0)\nThư mục: tồn tại|Folder: exists\nThư mục: thiếu|Folder: missing\nkhông đọc được|unreadable\nđọc được|readable\nKhông nhận được kết quả kiểm tra.|No diagnostic results received.\nLệnh kiểm tra gặp lỗi; xem kết quả bên trên.|The diagnostic command failed; see the output above.\nHoàn tất. Hai đường dẫn có thể trỏ cùng thư mục. Báo cáo chỉ kiểm tra quyền và thông tin file, chưa kiểm tra nội dung mã hóa của save.|Completed. Both paths may refer to the same folder. The report checks permissions and file information, not the encoded save contents.\nLệnh ADB quá thời gian 10 giây. Kiểm tra kết nối hoặc hộp thoại cấp quyền root trong giả lập.|The ADB command exceeded 10 seconds. Check the connection or the emulator's root permission dialog.\nChẩn đoán gặp lỗi|Diagnostic error\nDùng thông số đang nhập trong Cấu hình. Kiểm tra ADB, quyền root và cặp file save.|Uses the values entered in Settings. Checks ADB, root access and both save files.\nDừng chẩn đoán|Stop diagnostics\nXuất báo cáo…|Export report…\nXuất chẩn đoán|Export diagnostics\nÔ sản xuất sau sửa|Production slots after editing\nMột tag Train chứa hai thuộc tính JSON toa tàu; cần kiểm tra save trước khi sửa.|A Train tag has two car JSON attributes; inspect the save before editing.\nCó nhiều khối Trains chứa dữ liệu toa tàu; chọn rõ một khối trong GUI để chỉnh sửa.|Multiple Trains blocks contain car data; select a specific block in the GUI to edit.\nKhối Trains đã chọn không hợp lệ; mở lại Train.|The selected Trains block is invalid; reopen Train.\nSTT tàu không hợp lệ|Invalid train index\nđể sao chép Level/XP.|to copy Level/XP.\nDonor cần đúng một trường|The donor must contain exactly one field\nbị trùng.|is duplicated.\nTarget có trường|The target has a field\nthất bại.|failed.\nCần đúng một PushNotifDeviceInfo trong LocalInfo để đồng bộ LV; tải lại cặp save qua ADB.|LocalInfo must contain exactly one PushNotifDeviceInfo to synchronize the level; reload both saves via ADB.\nClone: LocalInfo đồng bộ LV|Clone: LocalInfo level synchronized\nkhông áp dụng V3.|V3 was not applied.\nTrường định danh trùng|Duplicate identity field\nKhông xác định Global để giữ|Cannot locate Global to preserve\nkhông áp dụng.|not applied.\nV3 làm thay đổi định danh|V3 changed the identity\nV3 không giữ đúng|V3 did not correctly preserve\nV3 LocalInfo thiết bị hiện tại|V3 current device LocalInfo\nV3 giữ định danh thiết bị|V3 preserves device identity\nV3 giữ định danh tài khoản và thiết bị hiện tại:|V3 preserves the current account and device identity:\nCảnh báo: không xác định được phiên bản save; vẫn tiếp tục V3 với các kiểm tra XML và cặp save.|Warning: save version unknown; V3 continues with XML and save-pair checks.\nCảnh báo: chưa đọc được phiên bản game qua ADB:|Warning: could not read the game version via ADB:\nmới hơn save hiện tại|newer than the current save\nvẫn tiếp tục Clone V3. Game có thể không chấp nhận save này.|continuing Clone V3. The game may reject this save.\nVẫn tiếp tục Clone V3.|Continuing Clone V3.\nCảnh báo: chưa xác định được phiên bản game đang cài; donor|Warning: installed game version unknown; donor\nmới hơn game đang cài|newer than the installed game\nVẫn tiếp tục clone; game có thể không chấp nhận save này.|Continuing clone; the game may reject this save.\nGame đang cài không cũ hơn donor; cho phép V3 dù XML gốc còn ghi phiên bản cũ. Không sửa nhãn phiên bản XML.|The installed game is not older than the donor; V3 is allowed even though the original XML has an older version label. XML version labels are preserved.\nLocalInfo thiết bị|Device LocalInfo\nmGameInfo thiết bị|Device mGameInfo\nMẫu LV3 khác phiên bản tài khoản mới; chọn mẫu cùng phiên bản. Chưa ghi LV3.|The level-3 template and new account have different versions; choose a matching template. Level 3 has not been written.\nEncode/decode mẫu LV3 không khớp.|The level-3 template failed encode/decode verification.\nchưa có save mới|no new save yet\ngame vẫn ghi định danh cũ hoặc mẫu reset|the game still has the old identity or reset template\nđang chờ cặp save hợp lệ|waiting for a valid save pair\ngiây. Nếu Agree không nhận diện được, bấm Agree trong giả lập; chương trình sẽ tự tiếp tục.|seconds. If Agree is not detected, press Agree in the emulator; the program will continue automatically.\nChờ định danh mới: còn khoảng|Waiting for a new identity: approximately\nHết thời gian chờ định danh mới|Timed out waiting for a new identity\nChưa ghép LV3. Mở game, bấm Agree nếu cần rồi dùng chế độ tiếp tục; không reset lần nữa.|Level 3 has not been merged. Open the game, press Agree if needed, then use Continue mode; do not reset again.\nDanh hiệu|Titles\nHuy hiệu|Badges\nNguồn Clone V1 cần có phần tử root.|The Clone V1 source must have a root element.\nChưa có tên|Unnamed\nKhối root bị trùng|Duplicate root block\nSave hiện tại|Current save\nCó đất + công trình|Land and buildings available\nNguồn thiếu TownGround hoặc Buildings|Source is missing TownGround or Buildings\nNguồn thiếu Zoo hoặc ZooInfo cần thiết|Source is missing the required Zoo or ZooInfo\nTrường hồ sơ bị trùng|Duplicate profile field\nThiếu dữ liệu nguồn hoặc vị trí hồ sơ đích|Missing source data or target profile location\nCó Global và bộ Level/XP|Global and Level/XP fields available\nNguồn thiếu Global hoặc Level/XP|Source is missing Global or Level/XP\nDùng cùng Stats theo xử lý V1 hiện tại|Used with Stats in the current V1 process\nNguồn thiếu dữ liệu AirScore / AirInfo|Source is missing AirScore / AirInfo\nCó cờ Avatar|Avatar flags available\nNguồn chưa có cờ Avatar|Source has no Avatar flags\nXóa CCSecret trong tài khoản hiện tại|Remove CCSecret from the current account\nCần kiểm tra kết quả trong game.|Check the result in the game.\nhiện tại|current\nLevel/XP từ donor|Level/XP from donor\nchưa áp dụng.|not applied yet.\nFile mẫu vượt giới hạn 32 MB.|Template exceeds the 32 MB limit.\nDữ liệu nguồn|Source data\nCấp kho|Barn level\nBarn · cấp kho|Barn · level\nBarn · sản phẩm|Barn · products\nCấp / Bonus|Level / Bonus\nAcademi · ô sản xuất nhà máy|Academy · factory production slots\ntrạng thái|status\nThời gian boost|Boost duration\nBật sửa Reward type = ST_Chest khi thay SubReward.|Enable editing Reward type = ST_Chest when changing SubReward.\nKhối|Block\ncờ cần sửa|flags to change\nHistory: mGameInfo hiện tại|History: current mGameInfo\nHistory: LocalInfo hiện tại|History: current LocalInfo\ngiây|seconds\nGửi card qua API|Send cards via API\nGửi card|Send cards\nGửi|Send\nDừng gửi|Stop sending\nLocalInfo thiếu bver/fver.|LocalInfo is missing bver/fver.\nNội dung|Content\ndấu vết City ID.|City ID references.\nBằng chứng|Evidence\nQuan hệ|Relationship\nSequential · theo thứ tự|Sequential · in order\nvào thiết bị?|to the device?\nFetchCity cần bver/fver hợp lệ. Mở game đã cập nhật, đóng game rồi kết nối ADB tải lại save/LocalInfo; hoặc nhập đúng phiên bản thủ công.|FetchCity requires valid bver/fver values. Open the updated game, close it and reload save/LocalInfo via ADB, or enter the correct version manually.\nMáy chủ từ chối phiên bản cũ; đang đọc lại LocalInfo trên thiết bị...|Server rejected the old version; reloading LocalInfo from the device...\nKhông đọc được phiên bản mới qua ADB|Could not read the new version via ADB\nCập nhật Township, mở game đến thành phố, đóng game rồi kết nối ADB tải lại save. Chưa áp dụng clone.|Update Township, open your city, close the game and reload saves via ADB. Clone has not been applied.\nLocalInfo trên thiết bị chưa có phiên bản khác hợp lệ.|Device LocalInfo has no other valid version.\nThử lại FetchCity một lần với phiên bản từ thiết bị: bver=|Retrying FetchCity once with the device version: bver=\nCần phiên bản Township được máy chủ hỗ trợ và LocalInfo mới. Chưa áp dụng clone.|A server-supported Township version and fresh LocalInfo are required. Clone has not been applied.\nMáy chủ vẫn báo old_version với bver=|Server still reports old_version with bver=\nTownship mẫu|Sample Township\nBộ màu|Color theme\nChọn|Choose\nNhấn Tiếp tục để quay lại|Press Continue to return\nNhập giá trị hoặc lựa chọn theo hướng dẫn ở trên|Enter a value or choice following the instructions above\nChọn nhanh…|Quick selection…\nXác nhận|Confirm\nTiếp tục|Continue\nVịt Cướp Biển|Pirate Duck\nBò Cướp Biển|Pirate Cow\nHeo Cướp Biển|Pirate Pig\nCừu Cocktail|Cocktail Sheep\nBò Nhảy Múa|Dancing Cow\nOng Nhạc Sĩ|Musician Bee\nVẹt Cao Bồi|Cowboy Parrot\nHeo Cao Bồi|Cowboy Pig\nHải Ly Cao Bồi|Cowboy Beaver\nGà Tây Phù Thủy|Witch Turkey\nOng Sành Điệu|Stylish Bee\nCừu Điên|Crazy Sheep\nBò Hoa|Flower Cow\nHeo Nông Dân|Farmer Pig\nVịt Cà Rốt|Carrot Duck\nOng Giáng Sinh|Christmas Bee\nCừu Mùa Đông|Winter Sheep\nGà Trượt Băng|Ice-skating Chicken\nBò Phi Hành Gia|Astronaut Cow\nHeo Tên Lửa|Rocket Pig\nGà Đầu Bếp|Chef Chicken\nChim Tình Yêu|Love Bird\nOng Bọ Rùa|Ladybug Bee\nCừu Nhạc Sĩ|Musician Sheep\nHải Ly Thần Đèn|Genie Beaver\nGà Phục Sinh|Easter Chicken\nOng Phục Sinh|Easter Bee\nBò Rocker|Rocker Cow\nHải Ly Trống|Drummer Beaver\nHeo Lái Thuyền|Boating Pig\nCừu Hang Động|Cave Sheep\nBò Lửa Trại|Campfire Cow\nOng Mùa Hè|Summer Bee\nGà Thư Giãn|Relaxing Chicken\nHeo Hula|Hula Pig\nBò Điện Ảnh|Movie Cow\nGà Phi Công|Pilot Chicken\nVịt Halloween|Halloween Duck\nOng Phù Thủy|Witch Bee\nHải Ly Pháp Sư|Wizard Beaver\nBò Giáng Sinh|Christmas Cow\nCá Rồng|Dragon Fish\nCừu Hồng|Pink Sheep\nGà Cổ Vũ|Cheerleader Chicken\nCừu Thỏ|Bunny Sheep\nHeo Phi Hành Gia|Astronaut Pig\nOng Tiên|Fairy Bee\nCừu Sấm Sét|Thunder Sheep\nCừu Thám Tử|Detective Sheep\nGà Cao Bồi|Cowboy Chicken\nBò Đầu Bếp|Chef Cow\nBò Ma Cà Rồng|Vampire Cow\nCừu Cung Thủ|Archer Sheep\nGà Nhảy Múa|Dancing Chicken\nBò Trượt Tuyết|Skiing Cow\nCừu Lễ Hội|Festival Sheep\nHeo Trung Hoa|Chinese Pig\nVịt Yêu Tinh|Elf Duck\nBò Phục Sinh|Easter Cow\nGà Rocker|Rocker Chicken\nGà Đánh Hạc|Crane-fighting Chicken\nĐặc Vụ Bí Mật|Secret Agent\nCừu Hiệp Sĩ|Knight Sheep\nCừu Atlantis|Atlantis Sheep\nCừu Mexico|Mexican Sheep\nGà Đi Nghỉ|Vacation Chicken\nBò Ý|Italian Cow\nCừu Xiếc|Circus Sheep\nGà Pháp Sư|Wizard Chicken\nCừu Ai Cập|Egyptian Sheep\nCừu Giáng Sinh|Christmas Sheep\nBò Mùa Đông|Winter Cow\nGà Trung Hoa|Chinese Chicken\nBò Ca Sĩ|Singer Cow\nCừu Công Chúa|Princess Sheep\nCừu Quà Tặng|Gift Sheep\nBò Tình Yêu|Love Cow\nGà|Chicken\nHeo Hoa|Flower Pig\nHải Ly Giận Dữ|Angry Beaver\nVịt Tự Sướng|Selfie Duck\nChim Xanh|Blue Bird\nHeo Thời Trang|Fashion Pig\nCừu Rapper|Rapper Sheep\nVịt Ma Cà Rồng|Vampire Duck\nBò Frankenstein|Frankenstein Cow\nGà Mùa Đông|Winter Chicken\nVịt Giáng Sinh|Christmas Duck\nHải Ly Trung Hoa|Chinese Beaver\nHải Ly DJ|DJ Beaver\nCừu Sao|Star Sheep\nVịt Phong Cách|Stylish Duck\nHeo Hawaii|Hawaiian Pig\nHải Ly Đi Nghỉ|Vacation Beaver\nGà Choáng|Dizzy Chicken\nVịt Buồn|Sad Duck\nĐôi Vịt Yêu|Duck Couple\nHải Ly Thiên Thần|Angel Beaver\n"
EN_TRANSLATIONS={key:values['en'] for key,values in I18N_CATALOG.items()}
for _row in EN_EXTRA_DATA.strip().splitlines():
    _key,_value=_row.split('|',1);EN_TRANSLATIONS[_key]=_value
EN_TRANSLATIONS['Mở save / LocalInfo hoặc kết nối ADB trước.\n\nDecorations và các danh mục: đánh dấu từng mục, chọn cả nhóm hoặc tất cả, tìm theo tên/ID.\nCác bảng số lượng: chỉnh từng dòng hoặc đặt chung cho mục đã chọn.\nÔ Sửa chỉ bật những thông số cần thay đổi.\nÁp dụng giữ thay đổi trong phiên; Xuất file hoặc Ghi vào game để lưu.\n\nTên ID lấy từ file gốc; chưa có ảnh hay tên dịch cho toàn bộ danh mục. Clone V3 / New TownCity / History dùng cả hai file. New TownCity tự động LV3: backup, reset, mở game, chờ ID mới và ghi mẫu; không cần bấm Ghi vào game lần nữa. Nếu chờ Agree quá lâu, bấm Agree trên giả lập hoặc cấu hình vị trí Agree. Chế độ Tiếp tục không reset lại. Encode kiểm tra không đảm bảo server chấp nhận nội dung.\nCông cụ XML chuyên sâu dùng biểu mẫu; điều kiện tìm tag vẫn nhập theo cú pháp key=value.']='Open a save / LocalInfo or connect via ADB first.\n\nDecorations and other catalogs: select individual entries, a group, or all entries; search by name/ID.\nQuantity tables: edit each row or apply a common value to selected entries.\nEnable Edit only for fields you want to change.\nApply keeps changes in the working session; export or write to the game to save.\n\nIDs come from the original files; images and translated names are not available for every catalog. Clone V3 / New TownCity / History use both save files. Automatic level-3 New TownCity backs up, resets, opens the game, waits for a new ID and writes the template; no second Write to game action is required. If Agree takes too long, press Agree in the emulator or configure its position. Continue mode does not reset again. Encode verification cannot guarantee server acceptance.\nAdvanced XML tools use forms; tag search filters use key=value syntax.'
EN_TRANSLATIONS.update({'Google Drive — thiết lập lần đầu\n\n1. Cài thư viện cloud (các chức năng cũ vẫn chạy khi chưa cài):\n   python -m pip install google-auth-oauthlib keyring\n2. Mở console.cloud.google.com, tạo/chọn dự án và bật Google Drive API.\n3. Trong Google Auth Platform, cấu hình Audience / Branding; nếu ứng dụng ở chế độ Testing, thêm email của bạn vào Test users.\n4. Tạo OAuth client loại Desktop app, tải file JSON về máy.\n5. Chọn JSON ở cửa sổ này, đặt tên thư mục rồi bấm Đăng nhập Google. Cho phép quyền truy cập trong trình duyệt.\n6. Bấm Kiểm tra / chuẩn bị thư mục. TS Studio tạo thư mục riêng trong My Drive.\n\nBackup: luôn tạo và kiểm tra ZIP trên máy trước; đánh dấu tải lên Google Drive khi cần. Nếu mạng lỗi, ZIP trên máy vẫn được giữ. Tùy chọn mặc định chỉ áp dụng khi bạn bấm chức năng Backup, không tự tải các backup nội bộ lên cloud.\nHistory: chọn nhiều ZIP bằng Ctrl / Shift hoặc Chọn tất cả đang hiện để tải lên cả đợt.\nHistory → Google Drive: chọn nhiều backup rồi bấm Tải các ZIP đã chọn; sau đó chọn đúng một ZIP để dùng Xem thông tin, Mở để chỉnh sửa hoặc Khôi phục vào game. Cửa sổ truyền file có tiến độ theo số file, kết quả từng file, Dừng và Thử lại mục lỗi / chưa thực hiện. Dừng chờ file hiện tại xong; file đã thành công không bị truyền lại khi bấm Thử lại.\n\nPhạm vi: My Drive cá nhân; hiển thị backup do TS Studio tải lên bằng cùng OAuth client và tài khoản. Chưa duyệt ZIP có sẵn ở mọi thư mục Drive, chưa hỗ trợ Shared drives. Giữ lại JSON / OAuth client để tiếp tục đọc các backup đã tải lên ở máy khác.\nĐăng xuất xóa thông tin đăng nhập trên máy, không xóa backup trên Drive. Token lưu trong kho bảo mật của hệ điều hành, không nằm trong QSettings, ZIP hoặc log. Không nhập mật khẩu Google vào TS Studio.\nThư mục và file trên Drive giữ quyền mặc định riêng tư; TS Studio không tạo liên kết công khai. Chia sẻ hay xóa file trực tiếp trên Drive do bạn quyết định.\nNếu quyền hết hạn hoặc bị thu hồi, đăng nhập lại. OAuth đang ở chế độ Testing có thể yêu cầu đăng nhập lại định kỳ.\n': "Google Drive — first-time setup\n\n1. Install the cloud libraries (existing features work without them):\n   python -m pip install google-auth-oauthlib keyring\n2. Open console.cloud.google.com, create/select a project and enable Google Drive API.\n3. Configure Audience / Branding in Google Auth Platform. If the app is in Testing mode, add your email under Test users.\n4. Create an OAuth client of type Desktop app and download its JSON file.\n5. Select that JSON here, choose a folder name and press Sign in to Google. Grant access in your browser.\n6. Press Check / prepare folder. TS Studio creates a dedicated folder in My Drive.\n\nBackup: a local ZIP is always created and verified first. Enable upload to Google Drive when needed. If the network fails, the local ZIP is retained. The default upload option applies only to the Backup feature; internal backups are not uploaded automatically.\nHistory: select multiple ZIPs with Ctrl / Shift or Select all visible to upload a batch.\nHistory → Google Drive: select backups and press Download selected ZIPs. Then select one ZIP to view information, open for editing or restore to game. The transfer dialog shows file-count progress, per-file results, Stop and Retry failed / pending files. Stop waits for the current file; Retry skips successful files.\n\nScope: personal My Drive; backups uploaded by TS Studio with the same OAuth client and account. Existing ZIPs in arbitrary Drive folders and Shared drives are not supported. Keep the JSON / OAuth client to access these backups from another computer.\nSign out removes local credentials, not Drive backups. Tokens are stored in the operating system's credential store, not QSettings, ZIPs or logs. Do not enter your Google password in TS Studio.\nDrive folders and files retain their default private permissions. TS Studio does not create public links. Sharing or deleting files directly on Drive is your choice.\nIf access expires or is revoked, sign in again. OAuth Testing mode may require periodic sign-in.\n", '1. Cấu hình đường dẫn ADB, serial và gói VN/Global.\n2. Kết nối ADB để tải cả hai file, hoặc mở mGameInfo và LocalInfo từ máy.\n3. Profile: sửa số rồi Áp dụng. Các tab khác: mở editor và chọn theo hướng dẫn.\n4. Xuất file để encode + decode kiểm tra, hoặc Ghi vào game để backup và ghi qua ADB.\n\nHủy hộp thoại dừng thao tác; thay đổi đã áp dụng trước đó vẫn giữ trong phiên.\nClone V3/New TownCity có thể thay cả hai file: phải dùng cặp mGameInfo + LocalInfo.\nCác chức năng cần master key, donor hoặc mạng giữ nguyên yêu cầu của file gốc.\nEncode kiểm tra thành công chưa đảm bảo game/server chấp nhận nội dung đã chỉnh.\nFile làm việc và backup nằm trong workspace_simple cạnh chương trình.': '1. Configure the ADB path, serial and VN/Global package.\n2. Connect via ADB to load both files, or open mGameInfo and LocalInfo from your computer.\n3. Profile: edit values and Apply. Other tabs: open an editor and follow its controls.\n4. Export to encode and verify by decoding, or Write to game to back up and write via ADB.\n\nCancel stops the action; previously applied changes stay in the session.\nClone V3 / New TownCity may replace both files: use the mGameInfo + LocalInfo pair.\nFeatures requiring a master key, donor or network retain the original requirements.\nSuccessful encoding verification cannot guarantee game/server acceptance.\nWorking files and backups are stored in workspace_simple beside the program.', 'Để chỉnh toa tàu:\n\n1. Mở Township của đúng tài khoản và kiểm tra nhà ga đã được mở.\n2. Nếu tàu đang đi, chờ ít nhất một tàu về thành phố và còn đơn hàng/toa hiện trên màn hình.\n3. Thoát game để lưu, rồi Kết nối ADB để tải lại mGameInfo mới nhất. Nếu mở file trên máy, lấy lại save mới.\n\nNếu tàu đã về nhưng vẫn gặp thông báo này, save có thể dùng cấu trúc khác. Lưu chẩn đoán Train để kiểm tra; editor sẽ không tự thêm tàu/toa mới.': 'To edit train cars:\n\n1. Open Township with the correct account and check that the train station is unlocked.\n2. If trains are travelling, wait for at least one to return with orders/cars visible.\n3. Exit the game to save, then reconnect via ADB to load the latest mGameInfo. For local files, obtain a fresh save.\n\nIf a train has returned but this message persists, the save may use a different structure. Save Train diagnostics for inspection; the editor does not create new trains/cars.'})
EN_TRANSLATIONS['FetchCity & công cụ bổ sung']='FetchCity · additional tools'
EN_TRANSLATIONS.update({'Mã hóa XML thành file save Township':'Encode XML into a Township save file','Giải mã file save Township thành XML':'Decode a Township save file into XML'})
EN_TRANSLATIONS.update({'Chỉnh Current cho từng Decor. Mục đã chọn chưa sửa riêng dùng Số lượng mỗi món khi Áp dụng.': 'Edit Current for an individual decoration. Selected rows without a manual edit use Quantity per Item when you apply.', 'Đặt số lượng cho mục đã chọn': 'Set quantity for selected', 'Số lượng riêng: 0–20 (0 xóa số lượng trong kho). Biển tên luôn là 1. Merge / Expedition được hoàn thành theo logic gốc. Các dòng không chọn giữ nguyên.': 'Manual quantities: 0–20 (0 clears the stash quantity). City signs always use 1. Merge / Expedition fragment completion follows the original behavior. Unselected rows stay unchanged.', 'Biển tên luôn áp dụng số lượng 1.': 'City signs are always applied with quantity 1.', 'Số lượng Decoration phải từ 0 đến 20. Biển tên dùng 1.': 'Decoration quantities must be from 0 to 20. City signs use 1.', 'Danh sách Decoration không hợp lệ.': 'Invalid decoration selection.', 'Số lượng Decoration phải từ 0 đến 20.': 'Decoration quantities must be from 0 to 20.', 'Xác minh số lượng Decoration thất bại': 'Decoration quantity verification failed', 'Decoration không chọn bị thay đổi': 'Unselected decoration changed'})
EN_TRANSLATIONS.update({'Mở / Tên': 'Unlocked / Name', 'Mở tất cả': 'Unlock all', 'Khóa tất cả': 'Lock all', 'Mở cả nhóm': 'Unlock group', 'Khóa cả nhóm': 'Lock group', 'Mở kết quả tìm': 'Unlock search results', 'Đã mở': 'Unlocked', 'Đã thay đổi': 'Changed', 'Tick để mở, bỏ tick để khóa. Checkbox thể hiện trạng thái hiện tại; chỉ các mục thay đổi được áp dụng khi bấm Apply.': 'Tick to unlock, untick to lock. Checkboxes show the current state; only changed items are committed when you press Apply.', 'Bỏ tick Achievement chỉ gỡ cờ mở/nhận thưởng, giữ bộ đếm tiến độ.': 'Unticking an Achievement clears its unlock/reward flag and keeps progress counters.'})
EN_TRANSLATIONS.update({'Thu nhỏ': 'Minimize', 'Phóng to / Khôi phục': 'Maximize / Restore', 'Kéo để đổi kích thước': 'Drag to resize'})
EN_TRANSLATIONS.update({'Áp dụng cho nhóm đang xem.': 'Applies to the current category.', 'All chỉ chọn dòng; None bỏ chọn; Max All chọn và đặt tối đa cho nhóm đang xem. Slots là ô kệ thưởng 0–2, khác với ô sản xuất nhà máy. Các dòng không chọn giữ nguyên.': 'All selects rows; None clears selection; Max All selects and maximizes the current category. Slots means 0–2 extra shelf slots, separate from factory production slots. Unselected rows stay unchanged.', 'Chọn ít nhất một dòng Academy.': 'Select at least one Academy row.', 'Chỉnh từng dòng trong Industries, Trains hoặc Islands. Apply dùng mức nâng cấp của mẫu TSVIP và các bonus trong bảng.': 'Edit individual rows in Industries, Trains or Islands. Apply uses the TSVIP upgrade-level templates and the bonuses shown in the table.'})
_EN_PATTERN=re.compile(r'(?<![\w])(?:'+ '|'.join(re.escape(key) for key in sorted(EN_TRANSLATIONS,key=len,reverse=True)) +r')(?![\w])')
# Paths, URLs and quoted machine identifiers retain their exact original spelling.
_EN_PROTECTED=re.compile(r'(?:[A-Za-z]:[\\/][^\n]*|https?://[^\s]+|/(?:data|workspace|sdcard|storage|tmp)/[^\n]*|[\"\'][^\"\'\n]*[\"\'])')
def english_text(source):
    if source in EN_TRANSLATIONS:return EN_TRANSLATIONS[source]
    parts=[];offset=0
    for match in _EN_PROTECTED.finditer(source):
        parts.append(_EN_PATTERN.sub(lambda m:EN_TRANSLATIONS[m[0]],source[offset:match.start()]))
        parts.append(match[0]);offset=match.end()
    parts.append(_EN_PATTERN.sub(lambda m:EN_TRANSLATIONS[m[0]],source[offset:]))
    return ''.join(parts)

# Highlight the activity log without inserting HTML or changing copied/exported text.
_LOG_WARNING=re.compile(r'\b(?:warning|warn|cảnh báo)\b',re.I)
_LOG_ERROR=re.compile(r'\b(?:error|errors|failed|failure|fatal|exception|thất bại|lỗi)\b|\b\w*(?:Error|Exception)\s*:',re.I)
_LOG_NO_ERROR=re.compile(r'\b(?:no errors?|without errors?|không có lỗi|errors?\s*[:=]?\s*0|lỗi\s*[:=]?\s*0)\b',re.I)
def activity_severity(text):
    normalized=english_text(str(text))
    if _LOG_WARNING.search(normalized):return 'warning'
    normalized=_LOG_NO_ERROR.sub('',normalized)
    if _LOG_ERROR.search(normalized) or re.search(r'\bHTTP\s+[45]\d{2}\b',normalized,re.I) or normalized.lstrip().startswith('Traceback (most recent call last):'):return 'error'
    return 'normal'

class ActivityLogHighlighter(QSyntaxHighlighter):
    def __init__(self,widget):
        super().__init__(widget.document());self.widget=widget
    def highlightBlock(self,text):
        source=getattr(self.widget,'_source_chunks',[]);index=self.currentBlock().blockNumber()
        original=source[index] if index<len(source) else text
        level=activity_severity(original);stripped=original.lstrip();self.setCurrentBlockState(0)
        if stripped.startswith('Traceback (most recent call last):'):
            level='error';self.setCurrentBlockState(1)
        elif self.previousBlockState()==1 and stripped:
            level='error'
            # Indented source/code and caret lines remain part of the traceback.
            if original[:1].isspace() or stripped.startswith('Traceback'):self.setCurrentBlockState(1)
        if level!='normal':
            dark=color_luminance(ACTIVE_THEME['surface'])<.25
            color=('#F87171' if dark else '#C62828') if level=='error' else ('#FACC15' if dark else '#A67C00')
            fmt=QTextCharFormat();fmt.setForeground(QColor(color));self.setFormat(0,len(text),fmt)

def append_activity(widget,text):
    chunks=getattr(widget,'_source_chunks',None)
    if chunks is None:chunks=[];widget._source_chunks=chunks
    chunks.extend(str(text).split('\n'));trimmed=len(chunks)>3000;del chunks[:-3000]
    if not hasattr(widget,'_activity_highlighter'):
        widget.setMaximumBlockCount(3000);widget._activity_highlighter=ActivityLogHighlighter(widget)
    app=QApplication.instance();language=app.interface_language.language if hasattr(app,'interface_language') else ui_language()
    widget.setProperty('i18nActivityLog',True);widget.setProperty('i18nRenderedLanguage',language)
    widget.appendPlainText(ui_text(str(text),language))
    if trimmed:widget._activity_highlighter.rehighlight()

def ui_language():
    value=str(QSettings('TownshipStudio','PyQt5').value('ui/language','en'));return value if value in dict(LANGUAGES) else 'en'

def ui_text(source,language):
    if not source or language=='vi':return source
    if source.startswith('? '):return '? '+ui_text(source[2:],language)
    normalized=source.replace('&','') if source.replace('&','') in I18N_ALIASES else source
    key=I18N_ALIASES.get(normalized,normalized)
    if language=='en':return english_text(key)
    if key in I18N_CATALOG:return I18N_CATALOG[key][language]
    # Missing native translations use the English catalog rather than Vietnamese.
    match=re.match(r'^(Hiện tại|Trạng thái|Lỗi|Level|History|Backup|Nguồn)(\s*[:·]\s*)(.*)$',source,re.S)
    if match:return ui_text(match[1],language)+match[2]+english_text(match[3])
    return english_text(source)

class InterfaceLanguage(QObject):
    def __init__(self,app):
        super().__init__(app);self.app=app;self.language=ui_language();self.pending=False;self.app.installEventFilter(self);self.set_direction()
    def set_direction(self):self.app.setLayoutDirection(Qt.RightToLeft if self.language=='ar' else Qt.LeftToRight)
    def set_language(self,language):
        self.language=language if language in dict(LANGUAGES) else 'en';self.set_direction();self.translate_all()
    def eventFilter(self,obj,event):
        if event.type() in (QEvent.Show,QEvent.LayoutRequest) and isinstance(obj,QWidget) and not self.pending:
            self.pending=True;QTimer.singleShot(0,self.translate_all)
        return False
    def caption(self,widget,field,get,setter):
        current=get();storage=widget.property('i18n_'+field)
        source=storage[0] if isinstance(storage,list) and len(storage)==2 and current==storage[1] else current
        translated=ui_text(source,self.language)
        widget.setProperty('i18n_'+field,[source,translated])
        if current!=translated:setter(translated)
    def translate_all(self):
        self.pending=False
        for root in self.app.topLevelWidgets():
            for widget in [root]+root.findChildren(QWidget):
                if widget.property('i18nSkip'):continue
                if isinstance(widget,(QLabel,QPushButton,QCheckBox)):
                    self.caption(widget,'text',widget.text,widget.setText)
                if isinstance(widget,QComboBox) and widget.property('i18nThemeList'):
                    for i in range(widget.count()):
                        source=widget.itemData(i)
                        if source in THEMES:widget.setItemText(i,THEMES[source][0] if self.language=='vi' else THEMES[source][0].split(' · ')[0])
                if isinstance(widget,QComboBox) and not widget.property('i18nThemeList') and not widget.isEditable():
                    blocked=widget.blockSignals(True)
                    try:
                        for i in range(widget.count()):self.caption(widget,'item'+str(i),lambda i=i:widget.itemText(i),lambda v,i=i:widget.setItemText(i,v))
                    finally:widget.blockSignals(blocked)
                if isinstance(widget,QPlainTextEdit):
                    if widget.property('i18nActivityLog') and widget.property('i18nRenderedLanguage')!=self.language:
                        widget.setPlainText('\n'.join(ui_text(line,self.language) for line in getattr(widget,'_source_chunks',[])))
                        widget.setProperty('i18nRenderedLanguage',self.language)
                        widget.verticalScrollBar().setValue(widget.verticalScrollBar().maximum())
                    elif widget.property('i18nDocument'):
                        self.caption(widget,'document',widget.toPlainText,widget.setPlainText)
                if isinstance(widget,QLineEdit):
                    widget.setLayoutDirection(Qt.LeftToRight)
                    if widget.property('i18nDisplayValue'):self.caption(widget,'value',widget.text,widget.setText)
                    self.caption(widget,'placeholder',widget.placeholderText,widget.setPlaceholderText)
                if isinstance(widget,QWidget):self.caption(widget,'tooltip',widget.toolTip,widget.setToolTip)
                if isinstance(widget,_NativeDialog):self.caption(widget,'title',widget.windowTitle,widget.setWindowTitle)
                if isinstance(widget,QTabWidget):
                    for i in range(widget.count()):self.caption(widget,'tab'+str(i),lambda i=i:widget.tabText(i),lambda v,i=i:widget.setTabText(i,v))
                if isinstance(widget,QTreeWidget):
                    header=widget.headerItem()
                    for i in range(widget.columnCount()):self.caption(widget,'header'+str(i),lambda i=i:header.text(i),lambda v,i=i:header.setText(i,v))
                    columns=widget.property('i18nRowColumns') or []
                    if columns:
                        blocked=widget.blockSignals(True)
                        try:
                            def translate_rows(item):
                                for column in columns:
                                    role=Qt.UserRole+100+column;storage=item.data(column,role);current=item.text(column)
                                    source=storage[0] if isinstance(storage,list) and len(storage)==2 and current==storage[1] else current
                                    translated=ui_text(source,self.language);item.setData(column,role,[source,translated])
                                    if current!=translated:item.setText(column,translated)
                                for j in range(item.childCount()):translate_rows(item.child(j))
                            for j in range(widget.topLevelItemCount()):translate_rows(widget.topLevelItem(j))
                        finally:widget.blockSignals(blocked)
        # Translation-induced layout events settle on the next pass without changing captions again.

class LanguageSettingsDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent);self.setWindowTitle('Ngôn ngữ giao diện');self.resize(640,350);self.original=ui_language();layout=QVBoxLayout(self)
        title=QLabel('Ngôn ngữ giao diện');title.setObjectName('cardTitle');layout.addWidget(title)
        self.combo=QComboBox();self.combo.setProperty('i18nSkip',True);self.combo.setLayoutDirection(Qt.LeftToRight)
        for code,name in LANGUAGES:self.combo.addItem(name,code)
        self.combo.setCurrentIndex(self.combo.findData(self.original));layout.addWidget(self.combo)
        hint=QLabel('Ngôn ngữ giao diện phổ biến; nhật ký và mô tả chưa dịch giữ nội dung gốc. Tiếng Ai Cập: tiếng Ả Rập (Ai Cập).');hint.setWordWrap(True);layout.addWidget(hint)
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel);buttons.button(QDialogButtonBox.Save).setText('Lưu & áp dụng');buttons.button(QDialogButtonBox.Save).setObjectName('primary');buttons.button(QDialogButtonBox.Cancel).setText('Hủy');buttons.accepted.connect(self.save);buttons.rejected.connect(self.reject);layout.addWidget(buttons)
        self.combo.currentIndexChanged.connect(self.preview)
    def preview(self):QApplication.instance().interface_language.set_language(self.combo.currentData())
    def save(self):
        code=self.combo.currentData();settings=QSettings('TownshipStudio','PyQt5');settings.setValue('ui/language',code);settings.sync();QApplication.instance().interface_language.set_language(code);self.accept()
    def reject(self):QApplication.instance().interface_language.set_language(self.original);super().reject()


class Window(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle('TS Studio • v1.39'); self.resize(1240, 920)
        self.setMinimumSize(950, 700); self.worker = None; self.current_action = ''; self.last_error = ''
        self.adb_connected=False
        self.settings = QSettings('TownshipStudio', 'PyQt5')
        B.WORK_DIR.mkdir(parents=True, exist_ok=True); B.BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        self.load_settings()
        root = QWidget(); self.setCentralWidget(root); main = QVBoxLayout(root); main.setContentsMargins(24,20,24,18); main.setSpacing(14)
        top_frame=QFrame();top_frame.setObjectName('topNavigation');top=QHBoxLayout(top_frame);top.setContentsMargins(20,16,20,16);top.setSpacing(12)
        branding = QVBoxLayout(); title = QLabel('🏙  Township Studio'); title.setObjectName('title'); branding.addWidget(title)
        sub = QLabel('SAVE EDITOR  /  FETCH CITY  /  ACCOUNT TOOLS'); sub.setObjectName('muted'); branding.addWidget(sub); top.addLayout(branding); top.addStretch()
        config = QPushButton('⚙ Cấu hình'); self.config_button=config; config.clicked.connect(self.configure); top.addWidget(config)
        help_btn = QPushButton('? Hướng dẫn'); self.help_button=help_btn; help_btn.clicked.connect(self.help); top.addWidget(help_btn); main.addWidget(top_frame)
        self.summary = QLabel(); self.summary.setObjectName('muted'); self.summary.setWordWrap(True); main.addWidget(self.summary)
        toolbar = QHBoxLayout()
        for text, action in [('🔌 Kết nối ADB',self.connect_device), ('📂 Mở mGameInfo',self.open_save), ('🗂 Mở LocalInfo',lambda:self.start(B.load_localinfo_file_prompt,'Mở LocalInfo')), ('📤 Xuất file',self.export), ('💾 Ghi vào game',lambda:self.start(B.save_to_device_prompt,'Ghi vào game')), ('↶ Hoàn tác',lambda:self.start(B.reset_changes,'Hoàn tác'))]:
            b = QPushButton(text); b.clicked.connect(action)
            if 'Kết nối ADB' in text:self.adb_button=b
            if 'Ghi vào' in text: b.setObjectName('save')
            toolbar.addWidget(b)
        self.controls = QWidget(); self.controls.setLayout(toolbar); main.addWidget(self.controls)
        self.tabs = QTabWidget(); self.profile_fields = {}; self.read_labels = {}
        self.tabs.addTab(self.make_profile(), '📊 Profile Statics')
        self.action_buttons = []
        for name, entries in GROUPS: self.tabs.addTab(self.make_cards(entries),name)
        split = QSplitter(Qt.Vertical); split.addWidget(self.tabs)
        logwrap = QWidget(); logs = QVBoxLayout(logwrap); logs.setContentsMargins(0,0,0,0)
        loghead = QHBoxLayout(); loghead.addWidget(QLabel('NHẬT KÝ THAO TÁC')); loghead.addStretch()
        extra = QPushButton('🧭 FetchCity & công cụ bổ sung'); extra.clicked.connect(self.extra); loghead.addWidget(extra)
        folder = QPushButton('📁 File đầu ra'); folder.clicked.connect(lambda:QDesktopServices.openUrl(QUrl.fromLocalFile(str(B.WORK_DIR)))); loghead.addWidget(folder)
        logs.addLayout(loghead)
        logactions = QHBoxLayout(); logactions.addStretch()
        self.copy_log_button = QPushButton('📋 Sao chép log'); self.copy_log_button.setToolTip('Sao chép toàn bộ nhật ký đang hiển thị'); self.copy_log_button.clicked.connect(self.copy_log); logactions.addWidget(self.copy_log_button)
        self.export_log_button = QPushButton('💾 Xuất log'); self.export_log_button.setToolTip('Lưu nhật ký đang hiển thị thành file TXT UTF-8'); self.export_log_button.clicked.connect(self.export_log); logactions.addWidget(self.export_log_button)
        clear = QPushButton('Xóa nhật ký'); clear.clicked.connect(self.clear_log); logactions.addWidget(clear)
        logs.addLayout(logactions); self.log = QPlainTextEdit(); self.log.setReadOnly(True); self.log.setMaximumBlockCount(3000); logs.addWidget(self.log)
        split.addWidget(logwrap); split.setSizes([560,190]); main.addWidget(split,1)
        self.progress = QProgressBar(); self.progress.setRange(0,1); self.progress.setValue(0); self.progress.setTextVisible(False); main.addWidget(self.progress)
        self.status = QLabel('Sẵn sàng · Mở save hoặc kết nối thiết bị để bắt đầu'); self.status.setObjectName('muted'); main.addWidget(self.status)
        self.refresh(); decorate(self); self.append('Township Studio sẵn sàng. Tất cả thay đổi được giữ trong phiên trước khi xuất hoặc ghi vào game.')
    def scroll(self, content):
        scroll = QScrollArea(); scroll.setWidgetResizable(True); scroll.setWidget(content); return scroll
    def make_profile(self):
        content = QWidget(); grid = QGridLayout(content); grid.setContentsMargins(16,16,16,16); grid.setSpacing(12)
        for index,(icon,label,key,var,minimum,maximum) in enumerate(PROFILE):
            card = QFrame(); card.setObjectName('card'); card.setProperty('paletteAccent',('blue','sky','peach','pink','purple')[index%5]); lay = QVBoxLayout(card)
            title = QLabel(icon+'  '+label); title.setObjectName('cardTitle'); lay.addWidget(title)
            current = QLabel('Hiện tại: —'); current.setObjectName('muted'); lay.addWidget(current); self.read_labels[key] = current
            row = QHBoxLayout(); spin = QSpinBox(); spin.setRange(minimum,maximum); spin.setValue(minimum); row.addWidget(spin,1)
            button = QPushButton('Áp dụng'); button.setObjectName('primary'); button.clicked.connect(lambda _,k=key:self.apply_profile(k)); row.addWidget(button); lay.addLayout(row)
            self.profile_fields[key] = spin; grid.addWidget(card,index//3,index%3)
        datecard = QFrame(); datecard.setObjectName('card'); datecard.setProperty('paletteAccent','peach'); lay = QVBoxLayout(datecard)
        title = QLabel('📅  Month / Year Create'); title.setObjectName('cardTitle'); lay.addWidget(title)
        current = QLabel('Hiện tại: —'); current.setObjectName('muted'); lay.addWidget(current); self.read_labels['date'] = current
        row = QHBoxLayout(); self.month = QSpinBox(); self.month.setRange(1,12); self.year = QSpinBox(); self.year.setRange(1970,2100); self.year.setValue(2026)
        row.addWidget(self.month); row.addWidget(self.year); button = QPushButton('Áp dụng'); button.setObjectName('primary'); button.clicked.connect(lambda:self.apply_profile('date')); row.addWidget(button); lay.addLayout(row); grid.addWidget(datecard,3,2)
        hint = QLabel('Chỉnh từng giá trị → Áp dụng → Xuất file hoặc Ghi vào game. Level: 1–1089, cho phép giảm và cập nhật XP. M3 giữ giới hạn của bản gốc.'); hint.setWordWrap(True); hint.setObjectName('muted'); grid.addWidget(hint,4,0,1,3)
        grid.setRowStretch(5,1)
        return self.scroll(content)
    def make_cards(self, entries):
        content = QWidget(); grid = QGridLayout(content); grid.setContentsMargins(16,16,16,16); grid.setSpacing(14)
        for i,(icon,name,desc,function) in enumerate(entries):
            card = QFrame(); card.setObjectName('card'); card.setProperty('paletteAccent',('blue','sky','peach','pink','purple')[i%5]); lay = QVBoxLayout(card); lay.setContentsMargins(18,16,18,16)
            title = QLabel(icon+'  '+name); title.setObjectName('cardTitle'); lay.addWidget(title)
            subtitle = QLabel(desc); subtitle.setObjectName('muted'); subtitle.setWordWrap(True); lay.addWidget(subtitle,1)
            b = QPushButton('Mở '+name+'  →'); b.clicked.connect(lambda _,fn=function,n=name:self.start(self.resolve(fn),n)); lay.addWidget(b)
            self.action_buttons.append(b); grid.addWidget(card,i//3,i%3)
        for col in range(3): grid.setColumnStretch(col,1)
        grid.setRowStretch((len(entries)+2)//3,1); return self.scroll(content)
    def resolve(self, function):
        if function == 'all_cards': return lambda:B.cards_prompt(True)
        if function == 'my_cards': return lambda:B.cards_prompt(False)
        if function in ('skin','stickers','profile','achievements'): return lambda:B.unlock_catalog_prompt(function)
        return getattr(B,function)
    def read_profile(self,key,xml):
        var = next((x[3] for x in PROFILE if x[2]==key),None)
        if var: return int(B.read_var(xml,var)['v'])
        readers={'level':B.read_township_level,'m3':B.read_match3_level,'win':B.read_first_win,'lives':B.read_lives,'mine':B.read_mine_depth}
        if key in readers: return readers[key](xml)
        return next((v for v in B.read_profile_stat(xml,key).values() if v is not None),None)
    def refresh(self):
        s = B.SESSION
        self.summary.setText(f'{"● Đã tải save" if s.loaded else "○ Chưa tải save"}   •   {"Có thay đổi chưa lưu" if s.changed else "Chưa có thay đổi"}   •   {B.DEVICE_ID}   •   {B.PACKAGE_NAME}\nNguồn: {s.source_label or "—"}')
        self.tabs.widget(0).setEnabled(s.loaded)
        for key,spin in self.profile_fields.items():
            value = None
            if s.loaded:
                try: value = self.read_profile(key,s.current_xml)
                except (ValueError,B.SaveToolError,KeyError): pass
            self.read_labels[key].setText('Hiện tại: '+(str(value) if value is not None else '—'))
            if value is not None: spin.setValue(value)
        text = '—'
        if s.loaded:
            try:
                from datetime import datetime
                dt=datetime.fromtimestamp(int(B.read_var(s.current_xml,'gameStartDate')['v']),B.UTC_PLUS_7)
                text=dt.strftime('%m/%Y'); self.month.setValue(dt.month); self.year.setValue(dt.year)
            except (ValueError,B.SaveToolError,KeyError,OSError,OverflowError): pass
        self.read_labels['date'].setText('Hiện tại: '+text)
        self.update_connection_controls()
    def update_connection_controls(self):
        connected=self.adb_connected
        busy=self.worker is not None
        self.adb_button.setText('Kết nối lại ADB' if connected else 'Kết nối ADB')
        color='#26715A' if connected else '#B83749'
        hover='#328668' if connected else '#CC435B'
        self.adb_button.setStyleSheet('QPushButton {background:'+color+';color:white;border:1px solid '+color+';} QPushButton:hover {background:'+hover+';}')
        self.controls.setEnabled(not busy)
        self.tabs.setEnabled(connected and not busy)
        allowed=(self.adb_button,self.config_button,self.help_button,self.copy_log_button,self.export_log_button)
        for button in self.centralWidget().findChildren(QPushButton):
            if button not in allowed:button.setEnabled(connected and not busy)
        self.adb_button.setEnabled(not busy)

    def apply_profile(self,key):
        value = self.profile_fields[key].value() if key!='date' else (self.year.value(),self.month.value())
        def action():
            B.SESSION.require_loaded(); xml=B.SESSION.current_xml
            var = next((x[3] for x in PROFILE if x[2]==key),None)
            if var: result=B.set_integer_var(xml,var,value,0,2000000000)
            elif key=='date': result=B.set_game_start_month(xml,*value)
            elif key in ('help','card','regata','energy'): result=B.set_profile_stat(xml,key,value)
            else:
                setters={'level':B.set_township_level,'m3':B.set_match3_level,'win':B.set_first_win,'lives':B.set_lives,'mine':B.set_mine_depth}
                result=B.set_township_level(xml,value,allow_decrease=True) if key=='level' else setters[key](xml,value)
            B.validate_xml_document(result[0],'Profile'); B.SESSION.apply_xml(result[0]); B.print(f'Đã cập nhật {key}: {value}. Chưa ghi vào game.'); B.print('Chi tiết:',result[1])
        self.start(action,'Cập nhật '+key)
    def copy_log(self):
        QApplication.clipboard().setText(self.log.toPlainText())
        if self.worker is None:self.status.setText('Đã sao chép nhật ký vào clipboard.')
    def export_log(self):
        from datetime import datetime
        suggested = B.WORK_DIR / ('TS_Studio_log_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'.txt')
        destination,_ = QFileDialog.getSaveFileName(self,'Xuất nhật ký',str(suggested),'Nhật ký (*.txt);;Tất cả (*)')
        if not destination:return
        path = Path(destination)
        try:
            path.write_text(self.log.toPlainText(),encoding='utf-8')
        except OSError as exc:
            QMessageBox.warning(self,'Không xuất được nhật ký',str(exc)); return
        if self.worker is None:self.status.setText('Đã xuất nhật ký: '+str(path))
    def clear_log(self):
        self.log._source_chunks=[];self.log.clear()
    def append(self,text):
        append_activity(self.log,text); self.log.verticalScrollBar().setValue(self.log.verticalScrollBar().maximum())
    def start(self,action,name):
        if self.worker is not None: return
        self.current_action=name; self.last_error=''; self.append('\n━━ '+name+' ━━')
        self.worker=Worker(action); self.worker.output.connect(self.append); self.worker.ask.connect(self.answer_prompt); self.worker.done.connect(self.action_done); self.worker.finished.connect(self.thread_finished)
        self.controls.setEnabled(False); self.tabs.setEnabled(False); self.progress.setRange(0,0); self.status.setText('Đang thực hiện: '+name); self.worker.start()
    def answer_prompt(self,prompt,context):
        dialog=PromptDialog(self.current_action,prompt,context,self)
        ok=dialog.exec_()==QDialog.Accepted
        self.worker.answer=dialog.edit.text() if ok else None
        if not ok: self.worker.cancelled=True
        self.worker.event.set()
    def action_done(self,result,error):
        if self.current_action=='Kết nối và tải save qua ADB':
            self.adb_connected=result=='ok' and B.SESSION.loaded
        if self.current_action=='New TownCity · tự động LV3' and result!='ok':
            self.adb_connected=False
        self.last_error=error
        self.status.setText({'ok':'Hoàn tất','cancel':'Đã hủy thao tác','error':'Thao tác gặp lỗi'}[result]+' · '+self.current_action)
        if error: self.append('Lỗi: '+error)
    def thread_finished(self):
        worker=self.worker; self.worker=None; worker.deleteLater()
        self.controls.setEnabled(True); self.tabs.setEnabled(True); self.progress.setRange(0,1); self.progress.setValue(1); self.refresh()
        if self.last_error: QMessageBox.warning(self,'Không thực hiện được',self.last_error)
    def allow_replace(self):
        if not B.SESSION.changed: return True
        return QMessageBox.question(self,'Thay đổi chưa lưu','Mở save mới sẽ bỏ các thay đổi chưa lưu. Tiếp tục?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes
    def connect_device(self):
        if self.allow_replace():
            self.adb_connected=False;self.update_connection_controls()
            def action():
                B.SESSION.load_device()
                level=B.read_township_level(B.SESSION.current_xml);local_level=B._clone_tag_attrs(B.SESSION.localinfo_xml,'PushNotifDeviceInfo').get('lvl','thiếu')
                B.print(f'Save tải từ thiết bị: mGameInfo.levelup={level}; LocalInfo.PushNotifDeviceInfo.lvl={local_level}')
            self.start(action,'Kết nối và tải save qua ADB')
    def open_save(self):
        if not self.allow_replace(): return
        path,_=QFileDialog.getOpenFileName(self,'Mở mGameInfo',str(Path.home()),'Save (*.xml *.mGameInfo);;Tất cả (*)')
        if path: self.start(lambda:B.SESSION.load_local(Path(path)),'Mở mGameInfo')
    def export(self):
        if not B.SESSION.loaded: QMessageBox.information(self,'Xuất file','Mở save trước khi xuất.'); return
        destination=QFileDialog.getExistingDirectory(self,'Chọn thư mục xuất',str(B.WORK_DIR))
        if not destination: return
        files=['mGameInfo.xml']+(['LocalInfo.xml'] if B.SESSION.pending_localinfo_xml is not None else [])
        if any((Path(destination)/name).exists() for name in files):
            if QMessageBox.question(self,'Ghi đè file','File đầu ra đã tồn tại. Ghi đè?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:return
        def action():
            encoded=B.SESSION.encode_verify(); local=B.encode_pending_localinfo() if B.SESSION.pending_localinfo_xml is not None else None
            B.atomic_write(Path(destination)/'mGameInfo.xml',encoded)
            if local is not None: B.atomic_write(Path(destination)/'LocalInfo.xml',local)
            B.print('Đã encode, decode kiểm tra và xuất: '+destination)
        self.start(action,'Xuất save đã xác minh')
    def load_settings(self):
        B.ADB_PATH=Path(self.settings.value('adb',str(B.ADB_PATH)))
        B.DEVICE_ID=self.settings.value('device',B.DEVICE_ID)
        B.PACKAGE_NAME=self.settings.value('package',B.PACKAGE_NAME)
        self.auto_launch_game=str(self.settings.value('auto_launch_game','false')).lower() in ('true','1')
        backup_root=Path(self.settings.value('backup_root',str(B.WORK_DIR))).expanduser().resolve()
        B.BACKUP_DIR=backup_root/'backups'
        B.ACCOUNT_BACKUP_DIR=backup_root/'a_TS_Files'
        B.REMOTE_SAVE=f'/data/data/{B.PACKAGE_NAME}/saves/mGameInfo.xml'
        B.REMOTE_LOCALINFO=f'/data/data/{B.PACKAGE_NAME}/saves/LocalInfo.xml'
    def configure(self):
        if self.worker is not None:return
        old_device=(str(B.ADB_PATH),B.DEVICE_ID,B.PACKAGE_NAME)
        dialog=QDialog(self); dialog.setWindowTitle('Cấu hình hệ thống'); dialog.resize(720,350); layout=QVBoxLayout(dialog); form=QFormLayout()
        adb=QLineEdit(str(B.ADB_PATH)); device=QLineEdit(B.DEVICE_ID); package=QComboBox(); package.setEditable(True); package.addItems(['com.playrix.township.vn','com.playrix.township']); package.setCurrentText(B.PACKAGE_NAME)
        row=QHBoxLayout(); row.addWidget(adb); pick=QPushButton('Chọn…'); row.addWidget(pick)
        def choose():
            path,_=QFileDialog.getOpenFileName(dialog,'Chọn ADB','','ADB (adb.exe adb);;Tất cả (*)')
            if path:adb.setText(path)
        pick.clicked.connect(choose); form.addRow('ADB:',row); form.addRow('Thiết bị / serial:',device); form.addRow('Gói Township:',package)
        backup=QLineEdit(str(B.BACKUP_DIR.parent));backup.setObjectName('backup_root');backup_row=QHBoxLayout();backup_row.addWidget(backup,1);backup_pick=QPushButton('Chọn thư mục…');backup_row.addWidget(backup_pick)
        def choose_backup():
            path=QFileDialog.getExistingDirectory(dialog,'Chọn thư mục lưu backup',backup.text())
            if path:backup.setText(path)
        backup_pick.clicked.connect(choose_backup);form.addRow('Thư mục lưu backup:',backup_row);layout.addLayout(form)
        auto_launch=QCheckBox('Tự mở Township sau khi ghi vào game thành công');auto_launch.setObjectName('auto_launch_game');auto_launch.setChecked(self.auto_launch_game);layout.addWidget(auto_launch)
        backup_hint=QLabel('Backup tự động lưu trong backups; ZIP thành phố và History dùng a_TS_Files bên trong thư mục đã chọn. Thay đổi này áp dụng cho backup mới; file cũ giữ ở vị trí cũ.');backup_hint.setWordWrap(True);layout.addWidget(backup_hint)
        hint=QLabel('MuMu: nhập serial như 127.0.0.1:7555. Thiết bị cần kết nối ADB và có quyền root.'); hint.setWordWrap(True); layout.addWidget(hint)
        diagnose=QPushButton('Chẩn đoán ADB / save');diagnose.setIcon(native_icon('🛠'));layout.addWidget(diagnose)
        def open_diagnostics():
            config=(adb.text().strip(),device.text().strip(),package.currentText().strip())
            if not config[0] or not config[1] or not re.fullmatch(r'[A-Za-z][\w]*(?:\.[A-Za-z][\w]*)+',config[2]):
                QMessageBox.warning(dialog,'Chẩn đoán','Điền ADB, serial và tên gói hợp lệ.');return
            SaveDiagnosticDialog(config,dialog).exec_()
        diagnose.clicked.connect(open_diagnostics)
        language=QPushButton('Ngôn ngữ');language.setIcon(native_icon('🌐'));language.clicked.connect(lambda:LanguageSettingsDialog(dialog).exec_());layout.addWidget(language)
        appearance=QPushButton('Giao diện · Bộ màu');appearance.setIcon(native_icon('🎨'));appearance.clicked.connect(lambda:ThemeSettingsDialog(dialog).exec_());layout.addWidget(appearance)
        cloud=QPushButton('Cloud · Google Drive');cloud.setIcon(native_icon('☁'));cloud.clicked.connect(lambda:GoogleDriveSettingsDialog(dialog).exec_());layout.addWidget(cloud)
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel); buttons.accepted.connect(dialog.accept); buttons.rejected.connect(dialog.reject); layout.addWidget(buttons)
        if dialog.exec_()==QDialog.Accepted:
            if not adb.text().strip() or not device.text().strip() or not re.fullmatch(r'[A-Za-z][\w]*(?:\.[A-Za-z][\w]*)+',package.currentText().strip()):
                QMessageBox.warning(self,'Cấu hình','Điền ADB, serial và tên gói hợp lệ.');return
            if not backup.text().strip():
                QMessageBox.warning(self,'Cấu hình','Chọn thư mục lưu backup.');return
            try:
                import tempfile
                backup_root=Path(backup.text().strip()).expanduser().resolve();backup_root.mkdir(parents=True,exist_ok=True)
                for folder in (backup_root/'backups',backup_root/'a_TS_Files'):
                    folder.mkdir(parents=True,exist_ok=True)
                    with tempfile.TemporaryFile(dir=folder) as check_file:check_file.write(b'TS Studio backup check')
            except OSError as exc:
                QMessageBox.warning(self,'Cấu hình','Không thể ghi backup vào thư mục này: '+str(exc));return
            self.settings.setValue('auto_launch_game',auto_launch.isChecked())
            self.settings.setValue('backup_root',str(backup_root))
            self.settings.setValue('adb',adb.text().strip()); self.settings.setValue('device',device.text().strip()); self.settings.setValue('package',package.currentText().strip()); self.settings.sync(); self.load_settings(); B.ROOT_PREFIX=None
            if old_device!=(str(B.ADB_PATH),B.DEVICE_ID,B.PACKAGE_NAME):self.adb_connected=False
            self.refresh()
    def extra(self):
        if self.worker is not None:return
        entries=[('Xem giá trị hiện tại',B.show_known_values),('Danh sách bạn bè',B.list_friends_prompt),('Chọn bạn bè',B.select_friend_prompt),('FetchCity bạn bè',B.fetch_selected_friend_prompt),('Manual City ID → Fetch + Clone',B.fetch_manual_cityid_prompt),('Xem donor',B.inspect_current_donor_prompt),('Clone City / Zoo / Stash / All',B.clone_current_donor_prompt),('Quét City ID trong XML',B.inspect_network_ids_prompt),('Friend Network',B.crawl_friend_network_prompt),('Sửa Var bất kỳ',B.edit_any_var_prompt),('Sửa thuộc tính tag',B.edit_any_tag_prompt),('Khôi phục backup local',B.restore_backup_prompt)]
        dialog=QDialog(self); dialog.setWindowTitle('FetchCity & công cụ bổ sung'); dialog.resize(680,200); layout=QVBoxLayout(dialog); combo=QComboBox()
        for name,_ in entries: combo.addItem(name)
        layout.addWidget(combo); hint=QLabel('Giữ đầy đủ các công cụ còn lại của file gốc. Thao tác và danh sách lựa chọn mở bằng hộp thoại.'); hint.setWordWrap(True); layout.addWidget(hint)
        buttons=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel); buttons.accepted.connect(dialog.accept); buttons.rejected.connect(dialog.reject); layout.addWidget(buttons)
        if dialog.exec_()==QDialog.Accepted:
            name,fn=entries[combo.currentIndex()]; self.start(fn,name)
    def help(self):
        QMessageBox.information(self,'Hướng dẫn Township Studio',
          '1. Cấu hình đường dẫn ADB, serial và gói VN/Global.\n'
          '2. Kết nối ADB để tải cả hai file, hoặc mở mGameInfo và LocalInfo từ máy.\n'
          '3. Profile: sửa số rồi Áp dụng. Các tab khác: mở editor và chọn theo hướng dẫn.\n'
          '4. Xuất file để encode + decode kiểm tra, hoặc Ghi vào game để backup và ghi qua ADB.\n\n'
          'Hủy hộp thoại dừng thao tác; thay đổi đã áp dụng trước đó vẫn giữ trong phiên.\n'
          'Clone V3/New TownCity có thể thay cả hai file: phải dùng cặp mGameInfo + LocalInfo.\n'
          'Các chức năng cần master key, donor hoặc mạng giữ nguyên yêu cầu của file gốc.\n'
          'Encode kiểm tra thành công chưa đảm bảo game/server chấp nhận nội dung đã chỉnh.\n'
          'File làm việc và backup nằm trong workspace_simple cạnh chương trình.')
    def closeEvent(self,event):
        if self.worker is not None:
            QMessageBox.information(self,'Đang thao tác','Đợi thao tác hoàn tất; nếu đang nhập dữ liệu, chọn Hủy trong hộp thoại.'); event.ignore();return
        if B.SESSION.changed and QMessageBox.question(self,'Thay đổi chưa lưu','Thoát và bỏ thay đổi chưa lưu?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:
            event.ignore();return
        event.accept()

from PyQt5.QtWidgets import (QTreeWidget, QTreeWidgetItem, QAbstractItemView,
    QHeaderView, QDoubleSpinBox, QStackedWidget, QInputDialog)
from datetime import datetime

# Google Drive backup transport (v1.39). No changes to the embedded save engine.
import hashlib
import uuid
from urllib.parse import urlparse

CLOUD_SCOPE='https://www.googleapis.com/auth/drive.file'
CLOUD_INSTALL='python -m pip install google-auth-oauthlib keyring'
CLOUD_HELP='''Google Drive — thiết lập lần đầu

1. Cài thư viện cloud (các chức năng cũ vẫn chạy khi chưa cài):
   python -m pip install google-auth-oauthlib keyring
2. Mở console.cloud.google.com, tạo/chọn dự án và bật Google Drive API.
3. Trong Google Auth Platform, cấu hình Audience / Branding; nếu ứng dụng ở chế độ Testing, thêm email của bạn vào Test users.
4. Tạo OAuth client loại Desktop app, tải file JSON về máy.
5. Chọn JSON ở cửa sổ này, đặt tên thư mục rồi bấm Đăng nhập Google. Cho phép quyền truy cập trong trình duyệt.
6. Bấm Kiểm tra / chuẩn bị thư mục. TS Studio tạo thư mục riêng trong My Drive.

Backup: luôn tạo và kiểm tra ZIP trên máy trước; đánh dấu tải lên Google Drive khi cần. Nếu mạng lỗi, ZIP trên máy vẫn được giữ. Tùy chọn mặc định chỉ áp dụng khi bạn bấm chức năng Backup, không tự tải các backup nội bộ lên cloud.
History: chọn nhiều ZIP bằng Ctrl / Shift hoặc Chọn tất cả đang hiện để tải lên cả đợt.
History → Google Drive: chọn nhiều backup rồi bấm Tải các ZIP đã chọn; sau đó chọn đúng một ZIP để dùng Xem thông tin, Mở để chỉnh sửa hoặc Khôi phục vào game. Cửa sổ truyền file có tiến độ theo số file, kết quả từng file, Dừng và Thử lại mục lỗi / chưa thực hiện. Dừng chờ file hiện tại xong; file đã thành công không bị truyền lại khi bấm Thử lại.

Phạm vi: My Drive cá nhân; hiển thị backup do TS Studio tải lên bằng cùng OAuth client và tài khoản. Chưa duyệt ZIP có sẵn ở mọi thư mục Drive, chưa hỗ trợ Shared drives. Giữ lại JSON / OAuth client để tiếp tục đọc các backup đã tải lên ở máy khác.
Đăng xuất xóa thông tin đăng nhập trên máy, không xóa backup trên Drive. Token lưu trong kho bảo mật của hệ điều hành, không nằm trong QSettings, ZIP hoặc log. Không nhập mật khẩu Google vào TS Studio.
Thư mục và file trên Drive giữ quyền mặc định riêng tư; TS Studio không tạo liên kết công khai. Chia sẻ hay xóa file trực tiếp trên Drive do bạn quyết định.
Nếu quyền hết hạn hoặc bị thu hồi, đăng nhập lại. OAuth đang ở chế độ Testing có thể yêu cầu đăng nhập lại định kỳ.
'''

class CloudError(B.SaveToolError):pass

class GoogleDriveBackup:
    API='https://www.googleapis.com/drive/v3'
    FIELDS='id,name,size,modifiedTime,md5Checksum,appProperties,parents,mimeType,trashed'
    SERVICE='TownshipStudio.GoogleDrive'
    def __init__(self,config=None):
        self.settings=QSettings('TownshipStudio','PyQt5')
        self.config=config or self.configuration()
        self.session=None;self.credentials=None;self.vault=None;self.key=None
    @staticmethod
    def configuration():
        s=QSettings('TownshipStudio','PyQt5')
        return {'client':str(s.value('cloud/drive/client','')),'folder_name':str(s.value('cloud/drive/folder_name','TS Studio Backups')),'folder_id':str(s.value('cloud/drive/folder_id',''))}
    @staticmethod
    def auto_upload():return str(QSettings('TownshipStudio','PyQt5').value('cloud/drive/auto_upload','false')).lower() in ('1','true')
    def client_config(self):
        try:
            p=Path(self.config['client'])
            if not self.config['client'] or not p.is_file() or p.stat().st_size>1024*1024:raise ValueError()
            data=json.loads(p.read_text(encoding='utf-8-sig'));c=data['installed']
            if not isinstance(c,dict):raise ValueError()
            if (not str(c.get('client_id','')).endswith('.apps.googleusercontent.com') or not c.get('client_secret') or
                c.get('auth_uri') not in ('https://accounts.google.com/o/oauth2/auth','https://accounts.google.com/o/oauth2/v2/auth') or
                c.get('token_uri')!='https://oauth2.googleapis.com/token'):raise ValueError()
            return {'installed':c}
        except (OSError,ValueError,KeyError,TypeError):raise CloudError('Chọn file OAuth JSON hợp lệ, loại Desktop app. Xem Hướng dẫn Google Drive.') from None
    def setup_vault(self):
        c=self.client_config()
        try:
            import keyring
            backend=keyring.get_keyring()
            secure=('keyring.backends.Windows','keyring.backends.macOS','keyring.backends.SecretService','keyring.backends.libsecret','keyring.backends.kwallet')
            if not type(backend).__module__.startswith(secure):
                from keyring.backend import get_all_keyring
                choices=[b for b in get_all_keyring() if type(b).__module__.startswith(secure) and b.priority>0]
                if not choices:raise RuntimeError()
                backend=max(choices,key=lambda b:b.priority)
            if backend.priority<=0:raise RuntimeError()
            self.vault=backend;self.key=hashlib.sha256(c['installed']['client_id'].encode()).hexdigest()
        except ImportError:raise CloudError('Cần cài thư viện cloud: '+CLOUD_INSTALL) from None
        except Exception:raise CloudError('Không mở được kho bảo mật hệ điều hành. Trên Windows, kiểm tra Windows Credential Manager; Linux cần Secret Service / KWallet. Không lưu token dạng văn bản.') from None
        return c
    def save_credentials(self):
        try:self.vault.set_password(self.SERVICE,self.key,self.credentials.to_json())
        except Exception:raise CloudError('Không lưu được thông tin đăng nhập vào kho bảo mật hệ điều hành.') from None
    def connect(self,login=False):
        c=self.setup_vault()
        try:
            from google.oauth2.credentials import Credentials
            from google.auth.transport.requests import Request,AuthorizedSession
            from google_auth_oauthlib.flow import InstalledAppFlow
        except ImportError:raise CloudError('Cần cài thư viện cloud: '+CLOUD_INSTALL) from None
        if login:
            try:
                flow=InstalledAppFlow.from_client_config(c,[CLOUD_SCOPE],autogenerate_code_verifier=True)
                token_request=flow.oauth2session.request
                def bounded_token_request(*args,**kwargs):
                    kwargs.setdefault('timeout',(10,30));return token_request(*args,**kwargs)
                flow.oauth2session.request=bounded_token_request
                self.credentials=flow.run_local_server(host='127.0.0.1',port=0,open_browser=True,timeout_seconds=180,
                    authorization_prompt_message='',success_message='Đăng nhập thành công. Bạn có thể đóng tab này và quay lại TS Studio.',
                    access_type='offline',prompt='consent select_account')
                if not self.credentials.refresh_token:raise ValueError()
            except Exception:raise CloudError('Đăng nhập chưa hoàn tất hoặc Google từ chối. Kiểm tra OAuth Desktop app, Test users và quyền Drive; thử lại trong 180 giây. Không có mật khẩu/token nào được ghi vào log.') from None
            self.save_credentials();self.settings.remove('cloud/drive/folder_id');self.config['folder_id']=''
        else:
            try:
                raw=self.vault.get_password(self.SERVICE,self.key)
                if not raw:raise ValueError()
                stored=json.loads(raw)
                if stored.get('client_id')!=c['installed']['client_id'] or stored.get('token_uri')!='https://oauth2.googleapis.com/token':raise ValueError()
                self.credentials=Credentials.from_authorized_user_info(stored,[CLOUD_SCOPE])
            except Exception:raise CloudError('Chưa đăng nhập Google Drive với OAuth client này. Mở Cấu hình → Google Drive → Đăng nhập Google.') from None
            if not self.credentials.valid:
                try:self.credentials.refresh(Request());self.save_credentials()
                except Exception:raise CloudError('Phiên Google Drive hết hạn, bị thu hồi hoặc mất mạng. Kiểm tra mạng và đăng nhập lại trong Cấu hình.') from None
        self.session=AuthorizedSession(self.credentials,refresh_timeout=30)
        return self
    def disconnect(self):
        self.setup_vault()
        try:
            if self.vault.get_password(self.SERVICE,self.key):self.vault.delete_password(self.SERVICE,self.key)
        except Exception:raise CloudError('Không xóa được phiên đăng nhập trong kho bảo mật.') from None
        self.settings.remove('cloud/drive/folder_id');self.settings.remove('cloud/drive/account');self.settings.sync()
    def close(self):
        if self.session:self.session.close()
    def request(self,method,url,**kwargs):
        if not self.session:raise CloudError('Google Drive chưa kết nối.')
        if urlparse(url).scheme!='https' or urlparse(url).hostname!='www.googleapis.com':raise CloudError('Địa chỉ Google Drive không hợp lệ.')
        try:
            response=self.session.request(method,url,timeout=(10,60),allow_redirects=False,**kwargs)
        except Exception:raise CloudError('Không kết nối được Google Drive. Kiểm tra mạng; backup trên máy vẫn được giữ.') from None
        try:self.save_credentials()
        except Exception:response.close();raise
        if response.status_code not in (200,201):
            status=response.status_code;response.close()
            hints={401:'Đăng nhập Google lại trong Cấu hình.',403:'Kiểm tra Google Drive API, quyền truy cập và dung lượng Drive.',404:'File/thư mục không còn tồn tại hoặc OAuth client này không có quyền.',429:'Drive đang giới hạn yêu cầu; thử lại sau.'}
            raise CloudError(f'Google Drive HTTP {status}. '+hints.get(status,'Thử lại sau; backup trên máy vẫn được giữ.'))
        return response
    def json_request(self,method,url,**kwargs):
        r=self.request(method,url,**kwargs)
        try:return r.json()
        except ValueError:raise CloudError('Google Drive trả về dữ liệu không hợp lệ.') from None
        finally:r.close()
    @staticmethod
    def file_id(value):
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,200}',str(value)):raise CloudError('ID file/thư mục cloud không hợp lệ.')
        return str(value)
    @staticmethod
    def query_text(value):return str(value).replace('\\','\\\\').replace("'","\\'")
    def list_query(self,q,fields):
        files=[];page=None;seen=set()
        while True:
            params={'q':q,'spaces':'drive','pageSize':100,'fields':'nextPageToken,incompleteSearch,files('+fields+')','orderBy':'modifiedTime desc'}
            if page:params['pageToken']=page
            data=self.json_request('GET',self.API+'/files',params=params)
            if data.get('incompleteSearch'):raise CloudError('Drive chưa trả đủ kết quả. Thử Làm mới lại.')
            files.extend(data.get('files',[]));page=data.get('nextPageToken')
            if not page:return files
            if page in seen:raise CloudError('Drive trả trang kết quả trùng; thử lại.')
            seen.add(page)
    def folder(self,create=False):
        folder_id=self.config.get('folder_id','')
        if folder_id:
            data=self.json_request('GET',self.API+'/files/'+self.file_id(folder_id),params={'fields':self.FIELDS})
            if data.get('trashed') or data.get('mimeType')!='application/vnd.google-apps.folder' or data.get('appProperties',{}).get('ts_kind')!='root':
                raise CloudError('Thư mục cloud đã bị thay đổi. Trong Cấu hình, chọn lại tên thư mục và chuẩn bị thư mục mới.')
            return folder_id
        name=self.config.get('folder_name','').strip()
        if not name or len(name)>150:raise CloudError('Tên thư mục Google Drive cần từ 1 đến 150 ký tự.')
        found=self.list_query("trashed = false and mimeType = 'application/vnd.google-apps.folder' and name = '"+self.query_text(name)+"' and appProperties has { key='ts_kind' and value='root' }",self.FIELDS)
        if found:folder_id=self.file_id(found[0]['id'])
        elif create:
            data=self.json_request('POST',self.API+'/files',params={'fields':self.FIELDS},json={'name':name,'mimeType':'application/vnd.google-apps.folder','appProperties':{'ts_kind':'root'}})
            folder_id=self.file_id(data['id'])
        else:return None
        self.config['folder_id']=folder_id;self.settings.setValue('cloud/drive/folder_id',folder_id);self.settings.sync();return folder_id
    def check(self):
        user=self.json_request('GET',self.API+'/about',params={'fields':'user(displayName,emailAddress),storageQuota(limit,usage)'})
        account=user.get('user',{}).get('emailAddress') or user.get('user',{}).get('displayName','Google Drive')
        folder_id=self.folder(True);self.settings.setValue('cloud/drive/account',account);self.settings.sync()
        return {'account':account,'folder_id':folder_id,'quota':user.get('storageQuota',{})}
    def list_backups(self):
        folder=self.folder(False)
        if not folder:return []
        return self.list_query("trashed = false and '"+self.file_id(folder)+"' in parents and mimeType = 'application/zip' and appProperties has { key='ts_kind' and value='backup' }",self.FIELDS)
    def upload(self,path):
        path=Path(path);raw=path.read_bytes() if path.is_file() and path.stat().st_size<=2*B.BACKUP_MAX_BYTES else b''
        _,_,meta,_=B.read_account_backup_bytes(raw)
        sha=hashlib.sha256(raw).hexdigest();md5=hashlib.md5(raw,usedforsecurity=False).hexdigest();folder=self.folder(True)
        props={'ts_kind':'backup','ts_sha256':sha,'ts_version':'1.25','ts_city':str(meta.get('city_id',''))[:100],'ts_level':str(meta.get('level',''))[:100]}
        payload={'name':path.name,'mimeType':'application/zip','parents':[folder],'appProperties':props}
        # One bounded ZIP upload per request; local file remains the durable retry source.
        r=self.request('POST','https://www.googleapis.com/upload/drive/v3/files',params={'uploadType':'resumable','fields':self.FIELDS},json=payload,
            headers={'X-Upload-Content-Type':'application/zip','X-Upload-Content-Length':str(len(raw))})
        location=r.headers.get('Location','');r.close()
        if not location:raise CloudError('Drive không trả địa chỉ tải lên; ZIP trên máy vẫn được giữ.')
        data=self.json_request('PUT',location,data=raw,headers={'Content-Type':'application/zip','Content-Length':str(len(raw))})
        if int(data.get('size',-1))!=len(raw) or data.get('md5Checksum')!=md5 or data.get('appProperties',{}).get('ts_sha256')!=sha:
            raise CloudError('Bản cloud chưa qua kiểm tra dung lượng / mã kiểm tra; không coi là backup thành công. Giữ ZIP trên máy và kiểm tra Drive.')
        return data
    def download(self,item,directory):
        file_id=self.file_id(item['id'])
        data=self.json_request('GET',self.API+'/files/'+file_id,params={'fields':self.FIELDS})
        folder=self.folder(False)
        if (not folder or folder not in data.get('parents',[]) or data.get('trashed') or data.get('mimeType')!='application/zip' or data.get('appProperties',{}).get('ts_kind')!='backup'):
            raise CloudError('File không phải backup thuộc thư mục TS Studio đang chọn.')
        size=int(data.get('size',0));sha=data.get('appProperties',{}).get('ts_sha256','');md5=data.get('md5Checksum','')
        if not 0<size<=2*B.BACKUP_MAX_BYTES or not re.fullmatch('[a-f0-9]{64}',sha) or not re.fullmatch('[a-f0-9]{32}',md5):raise CloudError('Backup cloud thiếu mã kiểm tra hoặc dung lượng vượt giới hạn.')
        r=self.request('GET',self.API+'/files/'+file_id,params={'alt':'media'},stream=True)
        raw=bytearray()
        try:
            for chunk in r.iter_content(256*1024):
                raw.extend(chunk)
                if len(raw)>size or len(raw)>2*B.BACKUP_MAX_BYTES:raise CloudError('File cloud tải về vượt dung lượng đã công bố.')
        except CloudError:raise
        except Exception:raise CloudError('Tải backup bị gián đoạn. Chưa tạo file ZIP trên máy; hãy thử lại.') from None
        finally:r.close()
        raw=bytes(raw)
        if len(raw)!=size or hashlib.sha256(raw).hexdigest()!=sha or hashlib.md5(raw,usedforsecurity=False).hexdigest()!=md5:raise CloudError('Mã kiểm tra backup tải về không khớp; không khôi phục.')
        B.read_account_backup_bytes(raw)
        directory=Path(directory)/'GoogleDrive';directory.mkdir(parents=True,exist_ok=True)
        # Never trust the remote filename as a filesystem path; never overwrite a local backup.
        name=re.sub(r'[^\w.\-]+','_',str(data.get('name','backup'))).strip('._')[:130] or 'backup'
        if name.lower().endswith('.zip'):name=name[:-4]
        target=directory/(name+'_'+uuid.uuid4().hex[:12]+'.zip');B.atomic_write(target,raw)
        return target

def drive_operation(operation,config=None,login=False):
    client=GoogleDriveBackup(config)
    try:
        client.connect(login);return operation(client)
    finally:client.close()

class CloudJob(QThread):
    result=pyqtSignal(object);error=pyqtSignal(str)
    def __init__(self,action,parent):super().__init__(parent);self.action=action
    def run(self):
        try:self.result.emit(self.action())
        except (B.SaveToolError,OSError,ValueError) as exc:self.error.emit(str(exc))
        except Exception:self.error.emit('Thao tác cloud chưa hoàn tất. Kiểm tra cấu hình và thử lại; các file trên máy vẫn được giữ.')

class CloudWaitDialog(QDialog):
    def __init__(self,title,action,parent):
        super().__init__(parent);self.setWindowTitle(title);self.resize(540,160);self.value=None;self.failure=None
        layout=QVBoxLayout(self);label=QLabel(title+'…\nVui lòng đợi. Đăng nhập Google có thời gian chờ tối đa 180 giây.');label.setWordWrap(True);layout.addWidget(label)
        progress=QProgressBar();progress.setRange(0,0);layout.addWidget(progress)
        self.job=CloudJob(action,self);self.job.result.connect(self.received);self.job.error.connect(self.failed);self.job.finished.connect(self.completed)
        QTimer.singleShot(0,self.job.start)
    def received(self,value):self.value=value
    def failed(self,message):self.failure=message
    def completed(self):
        if self.failure:QDialog.reject(self)
        else:QDialog.accept(self)
    def reject(self):
        if not self.job.isRunning() and self.job.isFinished():super().reject()
    def closeEvent(self,event):
        if self.job.isRunning() or not self.job.isFinished():event.ignore()
        else:event.accept()
    @staticmethod
    def perform(parent,title,action):
        dialog=CloudWaitDialog(title,action,parent);result=dialog.exec_()
        if dialog.failure:QMessageBox.warning(parent,title,dialog.failure)
        return (result==QDialog.Accepted,dialog.value)

# A single connection serves a bounded queue: each ZIP is checked independently.
class CloudBatchWorker(QThread):
    started_item=pyqtSignal(int)
    item_result=pyqtSignal(int,str,object)
    def __init__(self,mode,tasks,directory,parent):
        super().__init__(parent);self.mode=mode;self.tasks=list(tasks);self.directory=directory
    def run(self):
        client=GoogleDriveBackup()
        try:
            if not self.isInterruptionRequested():client.connect()
            for index,item in self.tasks:
                if self.isInterruptionRequested():
                    self.item_result.emit(index,'pending','Đã dừng trước khi thực hiện');continue
                self.started_item.emit(index)
                try:
                    value=client.upload(item) if self.mode=='upload' else client.download(item,self.directory)
                    self.item_result.emit(index,'ok',value)
                except (B.SaveToolError,OSError,ValueError) as exc:self.item_result.emit(index,'error',str(exc))
                except Exception:self.item_result.emit(index,'error','Thao tác chưa hoàn tất. Kiểm tra mạng / cấu hình rồi thử lại mục này.')
        except Exception as exc:
            message=str(exc) if isinstance(exc,(B.SaveToolError,OSError,ValueError)) else 'Không kết nối được Google Drive; kiểm tra cấu hình và thử lại.'
            for index,_ in self.tasks:self.item_result.emit(index,'pending' if self.isInterruptionRequested() else 'error',message)
        finally:client.close()

class CloudBatchDialog(QDialog):
    def __init__(self,parent,mode,items,directory=None):
        super().__init__(parent);self.setWindowTitle('Google Drive · '+('Tải lên nhiều ZIP' if mode=='upload' else 'Tải về nhiều ZIP'));self.resize(960,640)
        self.mode=mode;self.items=list(items);self.directory=directory;self.worker=None;self.launch_pending=True;self.states=['pending']*len(self.items);self.values={};self.details={};self.attempt_done=0
        layout=QVBoxLayout(self);heading=QLabel(self.windowTitle());heading.setObjectName('cardTitle');layout.addWidget(heading)
        hint=QLabel('Các file được truyền lần lượt trong một đợt. File thành công được giữ lại; file lỗi có thể thử riêng. Dừng sẽ chờ file đang truyền xong.');hint.setWordWrap(True);layout.addWidget(hint)
        self.progress=QProgressBar();self.progress.setRange(0,len(self.items));layout.addWidget(self.progress)
        self.tree=QTreeWidget();self.tree.setHeaderLabels(['Tên ZIP','Kết quả','Chi tiết']);self.tree.setProperty('i18nRowColumns',[1,2]);self.tree.header().setSectionResizeMode(0,QHeaderView.Stretch);self.tree.header().setSectionResizeMode(2,QHeaderView.Stretch);layout.addWidget(self.tree,1)
        self.rows=[]
        for item in self.items:
            name=Path(item).name if mode=='upload' else str(item.get('name','Backup'))
            self.rows.append(QTreeWidgetItem(self.tree,[name,'Chờ','']))
        self.status=QLabel();self.status.setWordWrap(True);layout.addWidget(self.status)
        row=QHBoxLayout();layout.addLayout(row);self.stop=QPushButton('Dừng');self.stop.clicked.connect(self.stop_batch);row.addWidget(self.stop)
        self.retry=QPushButton('Thử lại mục lỗi / chưa thực hiện');self.retry.clicked.connect(self.start_batch);row.addWidget(self.retry)
        copy=QPushButton('Sao chép kết quả');copy.clicked.connect(self.copy_results);row.addWidget(copy)
        self.close_button=QPushButton('Đóng');self.close_button.clicked.connect(self.reject);row.addWidget(self.close_button)
        self.stop.setEnabled(False);self.retry.setEnabled(False);self.close_button.setEnabled(False);self.update_summary();QTimer.singleShot(0,self.start_batch)
    def start_batch(self):
        self.launch_pending=False
        if self.worker is not None:return
        tasks=[(i,item) for i,item in enumerate(self.items) if self.states[i]!='ok']
        if not tasks:self.close_button.setEnabled(True);return
        self.attempt_done=0;self.progress.setRange(0,len(tasks));self.progress.setValue(0)
        for i,_ in tasks:self.states[i]='pending';self.rows[i].setText(1,'Chờ');self.rows[i].setText(2,'');self.details.pop(i,None)
        self.retry.setEnabled(False);self.close_button.setEnabled(False);self.stop.setEnabled(True);self.stop.setText('Dừng');self.status.setText('Đang kết nối Google Drive…')
        self.worker=CloudBatchWorker(self.mode,tasks,self.directory,self);self.worker.started_item.connect(self.started_item);self.worker.item_result.connect(self.item_result);self.worker.finished.connect(self.finished);self.worker.start()
    def started_item(self,index):
        self.rows[index].setText(1,'Đang truyền');self.tree.scrollToItem(self.rows[index]);self.status.setText('Đang truyền: '+self.rows[index].text(0))
    def item_result(self,index,state,value):
        self.states[index]=state;self.attempt_done+=1;self.progress.setValue(self.attempt_done)
        self.rows[index].setText(1,{'ok':'Thành công','error':'Lỗi','pending':'Chưa thực hiện'}[state])
        if state=='ok':
            self.values[index]=value
            detail=str(value) if self.mode=='download' else 'Đã kiểm tra dung lượng và mã kiểm tra trên Drive'
        else:detail=str(value)
        self.details[index]=detail;self.rows[index].setText(2,detail);self.rows[index].setToolTip(2,detail);self.update_summary()
    def update_summary(self):
        self.status.setText(f'Tổng {len(self.items)} · Thành công {self.states.count("ok")} · Lỗi {self.states.count("error")} · Chưa thực hiện {self.states.count("pending")}')
    def finished(self):
        worker=self.worker;self.worker=None;worker.deleteLater();self.stop.setEnabled(False);self.retry.setEnabled(any(s!='ok' for s in self.states));self.close_button.setEnabled(True);self.update_summary()
    def stop_batch(self):
        if self.worker is not None:
            self.worker.requestInterruption();self.stop.setEnabled(False);self.stop.setText('Đang dừng…');self.status.setText('Đang đợi file hiện tại xong; các file tiếp theo sẽ không truyền.')
    def reject(self):
        if self.worker is not None or self.launch_pending:self.stop_batch();return
        super().reject()
    def closeEvent(self,event):
        if self.worker is not None or self.launch_pending:self.stop_batch();event.ignore()
        else:super().closeEvent(event)
    def copy_results(self):
        lines=[self.windowTitle()]
        for row in self.rows:lines.append(' | '.join(row.text(i) for i in range(3)))
        QApplication.clipboard().setText('\n'.join(lines))
    @staticmethod
    def perform(parent,mode,items,directory=None):
        dialog=CloudBatchDialog(parent,mode,items,directory);dialog.exec_()
        return [dialog.values[i] for i in range(len(dialog.items)) if dialog.states[i]=='ok']

def cloud_select_visible(tree):
    tree.clearSelection()
    for i in range(tree.topLevelItemCount()):
        item=tree.topLevelItem(i)
        if not item.isHidden():item.setSelected(True)

def cloud_selected_items(tree):return [item for item in tree.selectedItems() if not item.isHidden()]


class GoogleDriveSettingsDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent);self.setWindowTitle('Cloud · Google Drive');self.resize(780,530)
        self.settings=QSettings('TownshipStudio','PyQt5');layout=QVBoxLayout(self);layout.setSpacing(14)
        title=QLabel('Google Drive · Backup & History');title.setObjectName('cardTitle');layout.addWidget(title)
        form=QFormLayout();layout.addLayout(form)
        self.client=path_field(form,'OAuth Desktop JSON',str(self.settings.value('cloud/drive/client','')))
        self.folder=QLineEdit(str(self.settings.value('cloud/drive/folder_name','TS Studio Backups')));self.folder.setMaxLength(150);form.addRow('Tên thư mục trên Drive',self.folder)
        self.auto=QCheckBox('Mặc định tải lên Google Drive khi tạo Backup');self.auto.setChecked(GoogleDriveBackup.auto_upload());layout.addWidget(self.auto)
        self.status=QLabel();self.status.setWordWrap(True);layout.addWidget(self.status)
        hint=QLabel('ZIP luôn được lưu trên máy trước. History đọc các backup TS Studio đã tải lên trong My Drive. Thông tin đăng nhập lưu trong kho bảo mật hệ điều hành.');hint.setWordWrap(True);layout.addWidget(hint)
        row=QHBoxLayout();layout.addLayout(row)
        for label,callback in [('Đăng nhập Google',self.login),('Kiểm tra / chuẩn bị thư mục',self.check),('Mở thư mục Drive',self.open_folder),('Đăng xuất',self.logout)]:
            button=QPushButton(label);button.clicked.connect(callback);row.addWidget(button)
        help_button=QPushButton('Hướng dẫn Google Drive');help_button.clicked.connect(self.help);layout.addWidget(help_button)
        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Close);buttons.button(QDialogButtonBox.Save).setText('Lưu cấu hình');buttons.button(QDialogButtonBox.Save).setObjectName('primary');buttons.button(QDialogButtonBox.Close).setText('Đóng');buttons.accepted.connect(self.save_and_close);buttons.rejected.connect(self.reject);layout.addWidget(buttons);self.update_status()
    def persist(self):
        name=self.folder.text().strip();path=self.client.text().strip()
        if not name:raise CloudError('Điền tên thư mục Google Drive.')
        config={'client':path,'folder_name':name,'folder_id':str(self.settings.value('cloud/drive/folder_id',''))}
        if path:GoogleDriveBackup(config).client_config()
        if path!=str(self.settings.value('cloud/drive/client','')) or name!=str(self.settings.value('cloud/drive/folder_name','TS Studio Backups')):
            self.settings.remove('cloud/drive/folder_id')
        if path!=str(self.settings.value('cloud/drive/client','')):self.settings.remove('cloud/drive/account')
        self.settings.setValue('cloud/drive/client',path);self.settings.setValue('cloud/drive/folder_name',name);self.settings.setValue('cloud/drive/auto_upload',self.auto.isChecked());self.settings.sync()
        return GoogleDriveBackup.configuration()
    def update_status(self):
        self.settings.sync();account=str(self.settings.value('cloud/drive/account','Chưa kiểm tra tài khoản'));folder=str(self.settings.value('cloud/drive/folder_id',''))
        self.status.setText('Tài khoản đã kiểm tra: '+account+'\nThư mục: '+('Đã chuẩn bị' if folder else 'Chưa chuẩn bị / cần kiểm tra'))
    def job(self,title,fn,login=False):
        try:config=self.persist()
        except B.SaveToolError as exc:QMessageBox.warning(self,'Google Drive',str(exc));return False,None
        result=CloudWaitDialog.perform(self,title,lambda:drive_operation(fn,config,login));self.update_status();return result
    def login(self):
        ok,value=self.job('Đăng nhập Google',lambda c:c.check(),True)
        if ok:QMessageBox.information(self,'Google Drive','Đã kết nối: '+value['account'])
    def check(self):
        ok,value=self.job('Kiểm tra Google Drive',lambda c:c.check())
        if ok:QMessageBox.information(self,'Google Drive','Kết nối và thư mục sẵn sàng: '+value['account'])
    def open_folder(self):
        ok,value=self.job('Mở thư mục Google Drive',lambda c:c.folder(True))
        if ok:QDesktopServices.openUrl(QUrl('https://drive.google.com/drive/folders/'+GoogleDriveBackup.file_id(value)))
    def logout(self):
        try:config=self.persist()
        except B.SaveToolError as exc:QMessageBox.warning(self,'Google Drive',str(exc));return
        if QMessageBox.question(self,'Đăng xuất','Xóa phiên Google trên máy? Các ZIP trên Drive vẫn được giữ.',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:return
        def action():
            c=GoogleDriveBackup(config)
            try:c.disconnect()
            finally:c.close()
        CloudWaitDialog.perform(self,'Đăng xuất Google Drive',action);self.update_status()
    def save_and_close(self):
        try:self.persist();self.accept()
        except B.SaveToolError as exc:QMessageBox.warning(self,'Google Drive',str(exc))
    def help(self):
        dialog=QDialog(self);dialog.setWindowTitle('Hướng dẫn Google Drive');dialog.resize(820,650);layout=QVBoxLayout(dialog)
        text=QPlainTextEdit();text.setReadOnly(True);text.setPlainText(CLOUD_HELP);text.setProperty('i18nDocument',True);layout.addWidget(text)
        row=QHBoxLayout();copy=QPushButton('Sao chép hướng dẫn');copy.clicked.connect(lambda:QApplication.clipboard().setText(text.toPlainText()));row.addWidget(copy)
        console=QPushButton('Mở Google Cloud Console');console.clicked.connect(lambda:QDesktopServices.openUrl(QUrl('https://console.cloud.google.com/')));row.addWidget(console)
        close=QPushButton('Đóng');close.clicked.connect(dialog.accept);row.addWidget(close);layout.addLayout(row);dialog.exec_()

class GoogleDriveHistoryDialog(QDialog):
    def __init__(self,parent,directory):
        super().__init__(parent);self.setWindowTitle('History · Google Drive');self.resize(1000,650);self.directory=directory;self.downloaded=None;self.downloaded_paths=[]
        layout=QVBoxLayout(self);hint=QLabel('Chọn nhiều backup bằng Ctrl / Shift hoặc Chọn tất cả đang hiện. File tải về được kiểm tra ZIP và mã kiểm tra trước khi mở hoặc khôi phục.');hint.setWordWrap(True);layout.addWidget(hint)
        self.search=QLineEdit();self.search.setPlaceholderText('Tìm tên ZIP / City ID / level…');layout.addWidget(self.search)
        self.tree=QTreeWidget();self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection);self.tree.setHeaderLabels(['Tên ZIP','City ID','LV','Dung lượng','Ngày sửa (UTC)']);self.tree.header().setSectionResizeMode(0,QHeaderView.Stretch);layout.addWidget(self.tree,1)
        self.status=QLabel('Bấm Làm mới để đọc Google Drive.');self.status.setWordWrap(True);layout.addWidget(self.status)
        row=QHBoxLayout();layout.addLayout(row)
        for label,callback in [('Cấu hình cloud',self.configure),('Làm mới',self.refresh),('Chọn tất cả đang hiện',lambda:cloud_select_visible(self.tree)),('Bỏ chọn',self.tree.clearSelection),('Tải các ZIP đã chọn',self.download),('Đóng',self.reject)]:
            button=QPushButton(label);button.clicked.connect(callback);row.addWidget(button)
        self.search.textChanged.connect(self.filter);self.tree.itemDoubleClicked.connect(lambda *_:self.download())
    def configure(self):GoogleDriveSettingsDialog(self).exec_()
    def refresh(self):
        ok,files=CloudWaitDialog.perform(self,'Đọc History Google Drive',lambda:drive_operation(lambda c:c.list_backups()))
        if not ok:return
        self.tree.clear()
        for data in files:
            props=data.get('appProperties',{});size=int(data.get('size',0))
            item=QTreeWidgetItem(self.tree,[str(data.get('name','')),props.get('ts_city',''),props.get('ts_level',''),f'{size/1024/1024:.2f} MB',str(data.get('modifiedTime','')).replace('T',' ').replace('Z','')]);item.setData(0,Qt.UserRole,data)
        self.status.setText(f'{len(files)} backup trên Google Drive.');self.filter()
    def filter(self):
        word=self.search.text().strip().casefold()
        for i in range(self.tree.topLevelItemCount()):
            item=self.tree.topLevelItem(i);item.setHidden(bool(word and word not in ' '.join(item.text(j) for j in range(5)).casefold()))
    def download(self):
        selected=cloud_selected_items(self.tree)
        if not selected:QMessageBox.information(self,'Google Drive','Chọn một hoặc nhiều backup trong danh sách.');return
        values=CloudBatchDialog.perform(self,'download',[item.data(0,Qt.UserRole) for item in selected],self.directory)
        if values:
            self.downloaded_paths.extend(values);self.downloaded=self.downloaded_paths[0];self.accept()



class NativeDialog(QDialog):
    def __init__(self, title, parent, description='', apply_text='Áp dụng vào phiên'):
        super().__init__(parent); self.setWindowTitle(title); self.resize(960,700)
        self.layout=QVBoxLayout(self); self.layout.setSpacing(12)
        heading=QLabel(title);heading.setObjectName('cardTitle');self.layout.addWidget(heading)
        if description:
            hint=QLabel(description);hint.setWordWrap(True);hint.setObjectName('muted');self.layout.addWidget(hint)
        self.body=QVBoxLayout();self.layout.addLayout(self.body,1)
        self.footer=QLabel('Thay đổi chỉ áp dụng vào phiên. Dùng Xuất file hoặc Ghi vào game để lưu.');self.footer.setWordWrap(True);self.footer.setObjectName('muted');self.layout.addWidget(self.footer)
        self.buttons=QDialogButtonBox(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)
        self.buttons.button(QDialogButtonBox.Apply).setText(apply_text);self.buttons.button(QDialogButtonBox.Apply).setObjectName('primary')
        self.buttons.button(QDialogButtonBox.Cancel).setText('Đóng');self.buttons.rejected.connect(self.reject)
        self.validator=None;self.buttons.button(QDialogButtonBox.Apply).clicked.connect(self.accept_checked);self.layout.addWidget(self.buttons)
    def accept_checked(self):
        try:
            if self.validator:self.validator()
            self.accept()
        except (ValueError,B.SaveToolError) as exc:QMessageBox.warning(self,'Kiểm tra dữ liệu',str(exc))
    def form(self):
        form=QFormLayout();form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow);self.body.addLayout(form);return form

class ItemPicker(QWidget):
    """Grouped, searchable checked lists; selection always uses stable IDs, never row numbers."""
    def __init__(self, groups, parent=None, labels=None, current=None, values=False, limits=(0,2147483647), defaults=None, disabled=None, row_class=QTreeWidgetItem, hide_id=False):
        super().__init__(parent);self.rows={};self.groups={};self.spinboxes={};self.current=current or {};self.disabled=set(disabled or [])
        self.catalog=groups;labels=labels or {};defaults=defaults or {}
        layout=QVBoxLayout(self);layout.setContentsMargins(0,0,0,0)
        toolbar=QHBoxLayout();self.search=QLineEdit();self.search.setPlaceholderText('Tìm tên hoặc ID…');toolbar.addWidget(self.search,1)
        self.group_filter=QComboBox();self.group_filter.addItem('Tất cả nhóm',None)
        for group,items in groups.items():self.group_filter.addItem(group,group)
        toolbar.addWidget(self.group_filter);layout.addLayout(toolbar)
        commands=QHBoxLayout()
        for name,callback in [('Chọn tất cả',lambda:self.check_all(True)),('Bỏ chọn tất cả',lambda:self.check_all(False)),('Chọn cả nhóm',lambda:self.check_group(True)),('Bỏ chọn nhóm',lambda:self.check_group(False)),('Chọn kết quả tìm',lambda:self.check_visible())]:
            button=QPushButton(name);button.clicked.connect(callback);commands.addWidget(button)
        layout.addLayout(commands)
        self.tree=QTreeWidget();self.tree.setHeaderLabels(['Chọn / Tên','ID','Hiện tại']+(['Giá trị mới'] if values else []));self.tree.setProperty('i18nRowColumns',[0,2]);self.tree.setAlternatingRowColors(True);self.tree.setRootIsDecorated(True);self.tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree.header().setSectionResizeMode(0,QHeaderView.Stretch);self.tree.header().setSectionResizeMode(1,QHeaderView.Interactive);self.tree.setColumnWidth(1,240);self.tree.header().setSectionResizeMode(2,QHeaderView.Interactive);self.tree.setColumnWidth(2,200)
        self.tree.setColumnHidden(1,hide_id)
        if values:self.tree.header().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        for group,items in groups.items():
            parentitem=QTreeWidgetItem(self.tree,[f'{group} ({len(items)})','','']);parentitem.setFlags(parentitem.flags()|Qt.ItemIsUserCheckable|Qt.ItemIsAutoTristate);parentitem.setCheckState(0,Qt.Unchecked);self.groups[group]=parentitem
            for raw in items:
                item_id=str(raw);key=(group,item_id);label=labels.get(key,labels.get(item_id,item_id))
                item=row_class(parentitem,[str(label),item_id,str(self.current.get(key,self.current.get(item_id,'—')))])
                item.setToolTip(0,str(label));item.setToolTip(1,item_id);item.setToolTip(2,item.text(2));item.setData(0,Qt.UserRole,key);item.setFlags(item.flags()|Qt.ItemIsUserCheckable);item.setCheckState(0,Qt.Unchecked);self.rows[key]=item
                if item_id in self.disabled or key in self.disabled:
                    item.setDisabled(True);item.setToolTip(0,'Chưa có trong save; không áp dụng mục này')
                if values:
                    spin=QSpinBox();spin.setRange(*limits);spin.setValue(int(defaults.get(key,defaults.get(item_id,0))));self.tree.setItemWidget(item,3,spin);self.spinboxes[key]=spin
                    spin.valueChanged.connect(lambda _,it=item:it.setCheckState(0,Qt.Checked))
            parentitem.setExpanded(True)
        layout.addWidget(self.tree,1);self.counter=QLabel();self.counter.setObjectName('muted');layout.addWidget(self.counter)
        self.tree.itemChanged.connect(self.update_count);self.search.textChanged.connect(self.filter);self.group_filter.currentIndexChanged.connect(self.filter);self.update_count()
    def selected(self):return {group:[item_id for (g,item_id),item in self.rows.items() if g==group and not item.isDisabled() and item.checkState(0)==Qt.Checked] for group in self.groups}
    def ids(self):return list(dict.fromkeys(v for values in self.selected().values() for v in values))
    def values(self):return {item_id:self.spinboxes[key].value() for key,item in self.rows.items() for item_id in [key[1]] if key in self.spinboxes and item.checkState(0)==Qt.Checked and not item.isDisabled()}
    def require(self):
        if not self.ids():raise B.SaveToolError('Chọn ít nhất một mục trong danh sách.')
    def update_count(self,*_):self.counter.setText(f'Đã chọn: {sum(len(v) for v in self.selected().values())} / {sum(not item.isDisabled() for item in self.rows.values())} mục có thể áp dụng')
    def check_all(self,state):
        self.tree.blockSignals(True)
        for item in self.rows.values():
            if not item.isDisabled():item.setCheckState(0,Qt.Checked if state else Qt.Unchecked)
        self.tree.blockSignals(False);self.update_count()
    def active_group(self):
        group=self.group_filter.currentData()
        if group:return group
        item=self.tree.currentItem()
        if item:
            if item.parent():return item.data(0,Qt.UserRole)[0]
            for group,parent in self.groups.items():
                if parent is item:return group
        return next(iter(self.groups),None)
    def check_group(self,state):
        group=self.active_group()
        for (g,_),item in self.rows.items():
            if g==group and not item.isDisabled():item.setCheckState(0,Qt.Checked if state else Qt.Unchecked)
        self.update_count()
    def check_visible(self):
        for item in self.rows.values():
            if not item.isDisabled() and not item.isHidden() and not item.parent().isHidden():item.setCheckState(0,Qt.Checked)
        self.update_count()
    def filter(self,*_):
        word=self.search.text().strip().casefold();group=self.group_filter.currentData()
        for g,parent in self.groups.items():
            visible=False
            for index in range(parent.childCount()):
                item=parent.child(index);match=(not group or group==g) and (not word or word in (item.text(0)+' '+item.text(1)).casefold());item.setHidden(not match);visible|=match
            parent.setHidden(not visible)
    def set_all_values(self,value):
        for key,spin in self.spinboxes.items():
            if self.rows[key].checkState(0)==Qt.Checked and not self.rows[key].isDisabled():spin.setValue(value)

class UnlockStatePicker(ItemPicker):
    """Checkboxes are desired unlock states; only differences are committed."""
    state_changed=pyqtSignal()
    def __init__(self,groups,states,labels=None,disabled=None):
        self.initial_states={key:bool(value) for key,value in states.items()}
        super().__init__(groups,labels=labels,disabled=disabled,hide_id=True)
        self.tree.setColumnHidden(2,True);self.tree.headerItem().setText(0,'Mở / Tên')
        commands={'Chọn tất cả':'Mở tất cả','Bỏ chọn tất cả':'Khóa tất cả','Chọn cả nhóm':'Mở cả nhóm','Bỏ chọn nhóm':'Khóa cả nhóm','Chọn kết quả tìm':'Mở kết quả tìm'}
        for button in self.findChildren(QPushButton):
            if button.text() in commands:button.setText(commands[button.text()])
        blocked=self.tree.blockSignals(True)
        try:
            for key,item in self.rows.items():item.setCheckState(0,Qt.Checked if self.initial_states.get(key,False) else Qt.Unchecked)
        finally:self.tree.blockSignals(blocked)
        self.update_count()
    def changes(self):
        return {key:item.checkState(0)==Qt.Checked for key,item in self.rows.items()
                if not item.isDisabled() and (item.checkState(0)==Qt.Checked)!=self.initial_states.get(key,False)}
    def update_count(self,*_):
        opened=sum(item.checkState(0)==Qt.Checked for item in self.rows.values() if not item.isDisabled())
        total=sum(not item.isDisabled() for item in self.rows.values())
        self.counter.setText(f'Đã mở: {opened} / {total} · Đã thay đổi: {len(self.changes())}')
        self.state_changed.emit()

def gui_catalog_list_field(xml,name,profile=False):
    pattern=rb'<DataElem\b[^>]*>' if profile else rb'<(?:Var|DataElem)\b[^>]*>'
    matches=[m for m in re.finditer(pattern,xml) if B.parse_attributes(m.group(0)).get('name')==name]
    if len(matches)>1:raise B.SaveToolError('Duplicate unlock field: '+name)
    if not matches:return None,[]
    attrs=B.parse_attributes(matches[0].group(0));value=attrs.get('value',attrs.get('v',''))
    return matches[0],[v for v in B.html.unescape(value).split(',') if v]

def gui_write_profile_state(xml,field,values):
    match,_=gui_catalog_list_field(xml,field,True);value=','.join(values)
    if match:
        tag=B.replace_attribute(match.group(0),'value',value);tag=B.replace_attribute(tag,'type','string')
        return xml[:match.start()]+tag+xml[match.end():]
    anchors=[m for m in re.finditer(rb'<DataElem\b[^>]*>',xml) if B.parse_attributes(m.group(0)).get('name')=='UnlockedAvatars']
    if len(anchors)!=1:raise B.SaveToolError('Cannot locate UnlockedAvatars to insert '+field)
    tag=f'<DataElem name="{field}" type="string" value="{B.xml_escape_attribute(value)}"/>'.encode()
    return xml[:anchors[0].start()]+tag+b'\n'+xml[anchors[0].start():]

def gui_set_avatar_states(xml,changes):
    if any(type(value) is not bool for value in changes.values()):raise B.SaveToolError('Invalid avatar state.')
    updated=xml
    for unlocked in (True,False):
        ids=[key for key,value in changes.items() if value is unlocked]
        if ids:updated,_=B.set_avatar_unlocks(updated,ids,unlocked)
    verified=B.avatar_states(updated)
    if any(verified[key]['state'] is not value for key,value in changes.items()):raise B.SaveToolError('Avatar state verification failed.')
    return updated,{'opened':sum(changes.values()),'locked':sum(not v for v in changes.values())}

def gui_set_catalog_states(xml,kind,changes):
    catalogs={'skin':B.TSVIP_SKINS,'stickers':B.TSVIP_STICKERS,'profile':B.TSVIP_PROFILE,'achievements':{'Achievements':tuple(B.TSVIP_ACHIEVEMENTS)}}
    if kind not in catalogs:raise B.SaveToolError('Unknown unlock catalog.')
    catalog=catalogs[kind]
    for group,items in changes.items():
        if group not in catalog or not set(items)<=set(catalog[group]) or any(type(v) is not bool for v in items.values()):raise B.SaveToolError('Invalid unlock state selection.')
    B.validate_xml_document(xml,'Unlock states');updated=xml
    if kind=='skin':
        root=B.validate_xml_document(xml,'Skin states')
        if len(root.findall('Skins'))>1:raise B.SaveToolError('Duplicate Skins blocks.')
        for group,items in changes.items():
            if sum(node.get('id')==group for node in root.findall('Skins/type'))>1:raise B.SaveToolError('Duplicate Skin group: '+group)
        opened={group:[key for key,value in items.items() if value] for group,items in changes.items()}
        opened={group:ids for group,ids in opened.items() if ids}
        if opened:updated,_=B.unlock_skins(updated,opened)
        match=B._decor_block(updated,'Skins')
        if match:
            block=match.group(0)
            for group,items in changes.items():
                removed={key for key,value in items.items() if not value}
                if not removed:continue
                matches=[m for m in re.finditer(rb'<type\b[^>]*>',block) if B.parse_attributes(m.group(0)).get('id')==group]
                if matches:
                    node=matches[0];attrs=B.parse_attributes(node.group(0));available=[v for v in B.html.unescape(attrs.get('available','')).split('|') if v and v not in removed]
                    tag=B.replace_attribute(node.group(0),'available','|'.join(available)+('|' if available else ''))
                    block=block[:node.start()]+tag+block[node.end():]
            updated=B._decor_replace_block(updated,'Skins',block)
    elif kind=='stickers':
        _,values=gui_catalog_list_field(updated,'UnlockedChatEmoji')
        wanted=dict(keyvalue for items in changes.values() for keyvalue in items.items())
        values=[key for key in values if wanted.get(key,True)]
        for key,value in wanted.items():
            if value and key not in values:values.append(key)
        value=''.join(f',{key},' for key in values)
        updated=B._m3_upsert_field(updated,'UnlockedChatEmoji',value,'s','Global')
    elif kind=='profile':
        for field,items in changes.items():
            _,values=gui_catalog_list_field(updated,field,True)
            values=[key for key in values if items.get(key,True)]
            for key,value in items.items():
                if value and key not in values:values.append(key)
            # glow includes the companion style used by the original unlock handler.
            if field=='UnlockedStyles' and 'glow' in items:
                if items['glow'] and 'animatedUnderwaterViolet' not in values:values.append('animatedUnderwaterViolet')
                elif not items['glow']:values=[key for key in values if key!='animatedUnderwaterViolet']
            updated=gui_write_profile_state(updated,field,values)
    else:
        items=changes.get('Achievements',{});opened=[key for key,value in items.items() if value]
        if opened:updated,_=B.unlock_achievements(updated,opened)
        for key,value in items.items():
            if not value:updated=B._m3_upsert_field(updated,'AchReward_'+key,'0','i','Global')
    B.validate_xml_document(updated,'Unlock states after editing')
    for group,items in changes.items():
        states=B.unlock_catalog_states(updated,kind,group,items)
        if any(states[key] is not value for key,value in items.items()):raise B.SaveToolError('Unlock state verification failed: '+group)
    values=[value for items in changes.values() for value in items.values()]
    return updated,{'opened':sum(values),'locked':sum(not v for v in values)}

def bind_unlock_apply(dialog,picker):
    button=dialog.buttons.button(QDialogButtonBox.Apply)
    picker.state_changed.connect(lambda:button.setEnabled(bool(picker.changes())))
    button.setEnabled(bool(picker.changes()))

class DecorationPicker(ItemPicker):
    """Current quantities are editable; unedited selections use the bulk quantity."""
    def __init__(self,groups,current,parent=None):
        super().__init__(groups,parent,current=current,hide_id=True)
        self.quantity_editors={};self.manual_quantities={}
        for key,item in self.rows.items():
            existing=int(current.get(key[1],0));spin=QSpinBox();spin.setRange(0,max(20,existing));spin.setValue(existing)
            self.tree.setItemWidget(item,2,spin);self.quantity_editors[key]=spin
            if key[1] in B.DECORATION_GROUPS['sign']:
                spin.setReadOnly(True);spin.setButtonSymbols(QSpinBox.NoButtons);spin.setToolTip('Biển tên luôn áp dụng số lượng 1.')
            else:spin.valueChanged.connect(lambda value,k=key:self.edit_quantity(k,value))
    def edit_quantity(self,key,value):
        self.manual_quantities[key]=value;self.rows[key].setCheckState(0,Qt.Checked);self.update_count()
    def set_selected_quantity(self,value):
        for key,item in self.rows.items():
            if not item.isDisabled() and item.checkState(0)==Qt.Checked:
                quantity=1 if key[1] in B.DECORATION_GROUPS['sign'] else value
                spin=self.quantity_editors[key];blocked=spin.blockSignals(True);spin.setValue(quantity);spin.blockSignals(blocked)
                self.manual_quantities[key]=quantity
    def quantities(self,bulk_quantity):
        self.require()
        quantities={key[1]:(1 if key[1] in B.DECORATION_GROUPS['sign'] else self.manual_quantities.get(key,bulk_quantity))
                    for key,item in self.rows.items() if not item.isDisabled() and item.checkState(0)==Qt.Checked}
        if any(type(value) is not int or not 0<=value<=20 for value in quantities.values()):
            raise B.SaveToolError('Số lượng Decoration phải từ 0 đến 20. Biển tên dùng 1.')
        return quantities

def gui_set_decoration_quantities(xml,quantities):
    """Reuse the original fragment/sign handling for positive quantities, verify zeros separately."""
    known=set().union(*B.DECORATION_GROUPS.values())
    if not quantities or not set(quantities)<=known:raise B.SaveToolError('Danh sách Decoration không hợp lệ.')
    if any(type(value) is not int or not 0<=value<=20 for value in quantities.values()):raise B.SaveToolError('Số lượng Decoration phải từ 0 đến 20.')
    quantities={key:1 if key in B.DECORATION_GROUPS['sign'] else value for key,value in quantities.items()}
    original=B.decoration_inventory(xml);updated=xml;reports=[]
    for quantity in sorted(set(quantities.values())-{0}):
        selected=[key for key,value in quantities.items() if value==quantity]
        updated,report=B.set_decorations(updated,selected,quantity);reports.append(report)
    zero_ids={key for key,value in quantities.items() if value==0}
    if zero_ids:
        match=B._decor_block(updated,'BuildingsStash')
        if match:
            stash=match.group(0)
            def zero_count(item):
                key=B.html.unescape(B.parse_attributes(item.group(0)).get('id',''))
                return B.replace_attribute(item.group(0),'count','0') if key in zero_ids else item.group(0)
            stash=re.sub(rb'<Building\b[^>]*>',zero_count,stash)
            updated=B._decor_replace_block(updated,'BuildingsStash',stash)
    verified=B.decoration_inventory(updated)
    for key,value in quantities.items():
        if verified.get(key,0)!=value:raise B.SaveToolError('Decoration quantity verification failed: '+key)
    for key,value in original.items():
        if key not in quantities and verified.get(key)!=value:raise B.SaveToolError('Unselected decoration changed: '+key)
    return updated,{'selected':len(quantities),'quantities':quantities,'groups':reports}

ACADEMY_FIELDS={
    'Factory':(('timeBonus','Time',100),('moneyBonus','Coin',100),('xpBonus','XP',100),('shelfBonus','Slots',2)),
    'Train':(('timeBonus','Time',100),('moneyBonus','Coin',100),('xpBonus','XP',100)),
    'Island':(('timeBonus','Time',101),('products','Products',100))}
ACADEMY_NAMES={'bagfactory': 'Bag Factory', 'bakery': 'Bakery', 'bouquetfactory': 'Bouquet Factory', 'cakefactory': 'Cake Factory', 'candyfactory': 'Candy Factory', 'chipsfactory': 'Chips Factory', 'chocolatefactory': 'Chocolate Factory', 'clothingfactory': 'Clothing Factory', 'coffeefactory': 'Coffee Factory', 'cottonfactory': 'Cotton Factory', 'dollfactory': 'Doll Factory', 'drinksfactory': 'Drinks Factory', 'factory_music_instruments': 'Music Instruments', 'fastfoodfactory': 'Fast Food Factory', 'featherfactory': 'Feather Factory', 'frenchrestaurant': 'French Restaurant', 'furniturefactory': 'Furniture Factory', 'gardeningfactory': 'Gardening Factory', 'holidayfactory': 'Holiday Factory', 'hotdogfactory': 'Hotdog Factory', 'housewaresfactory': 'Housewares Factory', 'icecreamfactory': 'Ice Cream Factory', 'italyfoodfactory': 'Italy Food Factory', 'jamfactory': 'Jam Factory', 'jewelryfactory': 'Jewelry Factory', 'kitchenwarefactory': 'Kitchenware Factory', 'mexfoodfactory': 'Mexican Food Factory', 'milkfactory': 'Milk Factory', 'mill': 'Mill', 'paperfactory': 'Paper Factory', 'petfactory': 'Pet Factory', 'roasterfactory': 'Roaster Factory', 'scentfactory': 'Scent Factory', 'semifinishedfactory': 'Semi-Finished Factory', 'shoefactory': 'Shoe Factory', 'spongefactory': 'Sponge Factory', 'stationeryfactory': 'Stationery Factory', 'sugarfactory': 'Sugar Factory', 'sushifactory': 'Sushi Factory', 'tea_factory': 'Tea Factory', 'vegancafe': 'Vegan Cafe', 'wheelfactory': 'Wheel Factory'}

def gui_academy_inventory(xml):
    root=B.validate_xml_document(xml,'Academy');blocks=root.findall('Upgrade')
    if len(blocks)>1:raise B.SaveToolError('Duplicate Upgrade blocks.')
    inventory={}
    if blocks:
        for node in blocks[0]:
            if node.tag not in ACADEMY_FIELDS:continue
            key=(node.tag,node.get('id',''))
            if key in inventory:raise B.SaveToolError('Duplicate Academy row: '+str(key))
            inventory[key]=dict(node.attrib)
    return inventory

class AcademyBonusSpin(QSpinBox):
    def __init__(self,maximum,island_time=False):
        super().__init__();self.setRange(0,maximum);self.island_time=island_time;self.previous_value=0;self.setMinimumWidth(85)
        if island_time:self.setToolTip('Island Time uses 0–99 or 101; 100 is skipped.')
        self.valueChanged.connect(self.normalize)
    def normalize(self,value):
        if self.island_time and value==100:
            replacement=99 if self.previous_value>100 else 101
            self.setValue(replacement);return
        self.previous_value=value

class AcademyUpgradePage(QWidget):
    def __init__(self,xml,parent=None):
        super().__init__(parent);self.inventory=gui_academy_inventory(xml);self.rows={};self.editors={};self.edited=set();self.trees={}
        layout=QVBoxLayout(self);layout.setContentsMargins(0,0,0,0);toolbar=QHBoxLayout()
        for text,callback in [('Max All',self.max_all),('All',lambda:self.select_all(True)),('None',lambda:self.select_all(False))]:
            button=QPushButton(text);button.setToolTip('Áp dụng cho nhóm đang xem.');button.clicked.connect(callback);toolbar.addWidget(button)
        toolbar.addStretch();self.search=QLineEdit();self.search.setPlaceholderText('Tìm tên hoặc ID…');self.search.textChanged.connect(self.filter_rows);toolbar.addWidget(self.search,1);layout.addLayout(toolbar)
        self.categories=QTabWidget();layout.addWidget(self.categories,1)
        for kind,title in [('Factory','Industries'),('Train','Trains'),('Island','Islands')]:
            tree=QTreeWidget();tree.setRootIsDecorated(False);tree.setAlternatingRowColors(True);tree.setHeaderLabels(['Chọn / Tên']+[label for _,label,_ in ACADEMY_FIELDS[kind]])
            tree.setProperty('i18nRowColumns',[0]);tree.header().setStretchLastSection(False);tree.header().setSectionResizeMode(0,QHeaderView.Stretch)
            for column in range(1,tree.columnCount()):tree.header().setSectionResizeMode(column,QHeaderView.ResizeToContents)
            self.trees[kind]=tree;self.categories.addTab(tree,title)
            for item,template in B.TSVIP_ACADEMY[kind].items():
                name=ACADEMY_NAMES.get(item,item) if kind=='Factory' else ('Train '+item if kind=='Train' else 'Island '+item.lstrip('i'))
                row=QTreeWidgetItem(tree,[name]+['' for _ in ACADEMY_FIELDS[kind]]);row.setFlags(row.flags()|Qt.ItemIsUserCheckable);row.setCheckState(0,Qt.Unchecked);row.setData(0,Qt.UserRole,(kind,item));row.setToolTip(0,item);self.rows[(kind,item)]=row
                current=self.inventory.get((kind,item));invalid=False
                for column,(field,label,maximum) in enumerate(ACADEMY_FIELDS[kind],1):
                    if kind=='Factory' and field not in template:row.setText(column,'—');continue
                    raw=(current.get('probability2','0') if field=='products' else current.get(field,'0')) if current is not None else str(maximum)
                    try:
                        value=int(raw)
                        if not 0<=value<=maximum:raise ValueError(raw)
                    except (ValueError,TypeError):invalid=True;row.setToolTip(column,'Unsupported Academy value: '+str(raw));row.setText(column,str(raw));continue
                    spin=AcademyBonusSpin(maximum,kind=='Island' and field=='timeBonus');spin.setValue(value);tree.setItemWidget(row,column,spin);self.editors[(kind,item,field)]=spin
                    spin.valueChanged.connect(lambda _,key=(kind,item),f=field:self.mark_edited(key,f))
                if invalid:
                    row.setDisabled(True)
                    for (k,i,_),spin in self.editors.items():
                        if (k,i)==(kind,item):spin.setEnabled(False)
            tree.itemChanged.connect(self.update_count)
        self.categories.currentChanged.connect(self.filter_rows);self.counter=QLabel();self.counter.setObjectName('muted');layout.addWidget(self.counter)
        hint=QLabel('All chỉ chọn dòng; None bỏ chọn; Max All chọn và đặt tối đa cho nhóm đang xem. Slots là ô kệ thưởng 0–2, khác với ô sản xuất nhà máy. Các dòng không chọn giữ nguyên.');hint.setWordWrap(True);layout.addWidget(hint);self.update_count()
    def active_kind(self):return ('Factory','Train','Island')[self.categories.currentIndex()]
    def mark_edited(self,key,field):self.edited.add((*key,field));self.rows[key].setCheckState(0,Qt.Checked);self.update_count()
    def select_all(self,state):
        for (kind,_),row in self.rows.items():
            if kind==self.active_kind() and not row.isDisabled():row.setCheckState(0,Qt.Checked if state else Qt.Unchecked)
        self.update_count()
    def max_all(self):
        kind=self.active_kind()
        for (row_kind,item),row in self.rows.items():
            if row_kind!=kind or row.isDisabled():continue
            row.setCheckState(0,Qt.Checked)
            for field,_,maximum in ACADEMY_FIELDS[kind]:
                spin=self.editors.get((kind,item,field))
                if spin is not None:spin.setValue(maximum);self.edited.add((kind,item,field))
        self.update_count()
    def filter_rows(self,*_):
        word=self.search.text().strip().casefold()
        for (kind,item),row in self.rows.items():row.setHidden(bool(word) and word not in (row.text(0)+' '+item).casefold())
    def update_count(self,*_):self.counter.setText('Đã chọn: '+str(sum(row.checkState(0)==Qt.Checked and not row.isDisabled() for row in self.rows.values())))
    def selected_rows(self):
        result={}
        for (kind,item),row in self.rows.items():
            if row.isDisabled() or row.checkState(0)!=Qt.Checked:continue
            values={field:spin.value() for (k,i,field),spin in self.editors.items() if (k,i)==(kind,item)}
            dirty={field for k,i,field in self.edited if (k,i)==(kind,item)}
            result.setdefault(kind,{})[item]={'bonuses':values,'edited':dirty}
        return result
    def require(self):
        if not self.selected_rows():raise B.SaveToolError('Chọn ít nhất một dòng Academy.')

def gui_set_academy_rows(xml,selection):
    inventory=gui_academy_inventory(xml)
    if not selection or not any(selection.values()):raise B.SaveToolError('Empty Academy selection.')
    for kind,items in selection.items():
        if kind not in ACADEMY_FIELDS or not set(items)<=set(B.TSVIP_ACADEMY[kind]):raise B.SaveToolError('Invalid Academy selection.')
        allowed={field:maximum for field,_,maximum in ACADEMY_FIELDS[kind]}
        for item,data in items.items():
            values=data['bonuses']
            if not set(values)<=set(allowed) or any(type(value) is not int or not 0<=value<=allowed[field] for field,value in values.items()):raise B.SaveToolError('Invalid Academy bonus: '+item)
            if kind=='Factory' and any(field not in B.TSVIP_ACADEMY[kind][item] for field in values):raise B.SaveToolError('Unsupported Academy field: '+item)
    updated=xml
    for kind,items in selection.items():
        for item,data in items.items():
            previous=inventory.get((kind,item));updated=B.set_academy(updated,kind,[item],data['bonuses'])
            # Preserve distinct island product probabilities when Products was not edited.
            if kind=='Island' and previous is not None and 'products' not in data.get('edited',set()):
                block=B._decor_block(updated,'Upgrade').group(0)
                matches=[m for m in re.finditer(rb'<Island\b[^>]*>',block) if B.parse_attributes(m.group(0)).get('id')==item]
                if len(matches)!=1:raise B.SaveToolError('Invalid Island upgrade row: '+item)
                node=matches[0];tag=node.group(0)
                for field in ('probability2','probability3'):
                    if field in previous:tag=B.replace_attribute(tag,field,previous[field])
                    else:tag=re.sub(rb'\s+'+field.encode()+rb'\s*=\s*([\'\"])[^\'\"]*\1',b'',tag)
                block=block[:node.start()]+tag+block[node.end():];updated=B._decor_replace_block(updated,'Upgrade',block)
    verified=gui_academy_inventory(updated)
    for kind,items in selection.items():
        for item,data in items.items():
            current=verified[(kind,item)]
            for field,value in data['bonuses'].items():
                if field=='products':
                    if inventory.get((kind,item)) is not None and field not in data.get('edited',set()):continue
                    targets=('probability2','probability3')
                else:targets=(field,)
                expected=101 if kind=='Island' and field=='timeBonus' and value==100 else value
                if any(int(current.get(target,'-1'))!=expected for target in targets):raise B.SaveToolError('Academy verification failed: '+item+' / '+field)
    for key,attrs in inventory.items():
        if key[1] not in selection.get(key[0],{}) and verified.get(key)!=attrs:raise B.SaveToolError('Unselected Academy row changed: '+str(key))
    return updated,{'selected':sum(len(items) for items in selection.values())}


# Golden Pass rewards catalog and stage editor, based on TSVIP's hf2/px3 schema.
PASS_REWARD_GROUPS = {'Match-3 Boosters': ['m3Line', 'm3Bomb', 'm3RainbowBall', 'm3Mallet', 'm3HorizontalLine', 'm3VerticalLine', 'm3Reshuffle'], 'Match-3 Powers (days)': ['Match3Lives_infTime', 'Match3BombBoost_infTime', 'Match3LineBoost_infTime', 'Match3LightningBoost_infTime'], 'Pass Advantages': ['SP_BoostStorageCapacity', 'SP_BoostSpeedUpBuildings', 'SP_BoostSpeedUpHarvest', 'SP_BoostSpeedUpFarms', 'SP_BoostSpeedUpAir', 'SP_BoostTrainMats', 'SP_MarketPremium', 'SP_BoostOrderCoins', 'SP_BoostSpeedUpTrains', 'SP_ClanHelpPremium', 'SP_LoadAirPremium'], 'Materials': ['Brick', 'Glass', 'Plita', 'axe', 'powersaw', 'hammerMat', 'nailMat', 'paintRedMat', 'pick', 'TNT', 'jackhammer', 'drill'], 'Bullions': ['BronzeBullionCounter', 'SilverBullionCounter', 'GoldBullionCounter', 'PlatinumBullionCounter'], 'Card Packs': ['CardC_Pack1', 'CardC_Pack2', 'CardC_Pack3', 'CardC_Pack4', 'CardC_Pack5'], 'Coupons': ['CouponLoadTrainAirport', 'CouponHireDealer', 'CouponUpgradeFactory', 'CouponUpgradeTrain', 'CouponUpgradeIsland']}
PASS_REWARD_LABELS = {'m3Line': {'en': 'Line', 'pt': 'Linha', 'es': 'Línea', 'id': 'Garis', 'vi': 'Đường Thẳng', 'ru': 'Линия'}, 'm3Bomb': {'en': 'Bomb', 'pt': 'Bomba', 'es': 'Bomba', 'id': 'Bom', 'vi': 'Bom', 'ru': 'Бомба'}, 'm3RainbowBall': {'en': 'Rainbow Ball', 'pt': 'Bola Arco-Íris', 'es': 'Bola Arco Iris', 'id': 'Bola Pelangi', 'vi': 'Cầu Vồng', 'ru': 'Радужный шар'}, 'm3Mallet': {'en': 'Mallet', 'pt': 'Martelo', 'es': 'Martillo', 'id': 'Palu', 'vi': 'Búa', 'ru': 'Молоток'}, 'm3HorizontalLine': {'en': 'Horizontal Line', 'pt': 'Linha Horizontal', 'es': 'Línea Horizontal', 'id': 'Garis H.', 'vi': 'Ngang', 'ru': 'Горизонт. линия'}, 'm3VerticalLine': {'en': 'Vertical Line', 'pt': 'Linha Vertical', 'es': 'Línea Vertical', 'id': 'Garis V.', 'vi': 'Dọc', 'ru': 'Верт. линия'}, 'm3Reshuffle': {'en': 'Shuffle', 'pt': 'Embaralhar', 'es': 'Mezclar', 'id': 'Acak', 'vi': 'Xáo Trộn', 'ru': 'Перемешать'}, 'Match3Lives_infTime': {'en': 'Infinite Lives (days)', 'pt': 'Vidas Infinitas (dias)', 'es': 'Vidas Infinitas (días)', 'id': 'Nyawa Tak Terbatas (hari)', 'vi': 'Vô Hạn Mạng (ngày)', 'ru': 'Бесконечные жизни (дни)'}, 'Match3BombBoost_infTime': {'en': 'Infinite Bomb (days)', 'pt': 'Bomba Infinita (dias)', 'es': 'Bomba Infinita (días)', 'id': 'Bom Tak Terbatas (hari)', 'vi': 'Bom Vô Hạn (ngày)', 'ru': 'Бесконечная бомба (дни)'}, 'Match3LineBoost_infTime': {'en': 'Infinite Line (days)', 'pt': 'Linha Infinita (dias)', 'es': 'Línea Infinita (días)', 'id': 'Garis Tak Terbatas (hari)', 'vi': 'Đường Vô Hạn (ngày)', 'ru': 'Бесконечная линия (дни)'}, 'Match3LightningBoost_infTime': {'en': 'Infinite Lightning (days)', 'pt': 'Raio Infinito (dias)', 'es': 'Rayo Infinito (días)', 'id': 'Petir Tak Terbatas (hari)', 'vi': 'Sét Vô Hạn (ngày)', 'ru': 'Бесконечная молния (дни)'}, 'SP_BoostStorageCapacity': {'en': 'Storage Capacity', 'pt': 'Capacidade do Armazém', 'es': 'Capacidad de Almacén', 'id': 'Kapasitas Gudang', 'vi': 'Sức Chứa Kho', 'ru': 'Вместимость склада'}, 'SP_BoostSpeedUpBuildings': {'en': 'Speed Up Buildings', 'pt': 'Acelerar Construções', 'es': 'Acelerar Construcciones', 'id': 'Percepat Bangunan', 'vi': 'Tăng Tốc Xây Dựng', 'ru': 'Ускорить стройку'}, 'SP_BoostSpeedUpHarvest': {'en': 'Speed Up Harvest', 'pt': 'Acelerar Colheita', 'es': 'Acelerar Cosecha', 'id': 'Percepat Panen', 'vi': 'Tăng Tốc Thu Hoạch', 'ru': 'Ускорить урожай'}, 'SP_BoostSpeedUpFarms': {'en': 'Speed Up Farms', 'pt': 'Acelerar Fazendas', 'es': 'Acelerar Granjas', 'id': 'Percepat Peternakan', 'vi': 'Tăng Tốc Trang Trại', 'ru': 'Ускорить фермы'}, 'SP_BoostSpeedUpAir': {'en': 'Speed Up Airport', 'pt': 'Acelerar Aeroporto', 'es': 'Acelerar Aeropuerto', 'id': 'Percepat Bandara', 'vi': 'Tăng Tốc Sân Bay', 'ru': 'Ускорить аэропорт'}, 'SP_BoostTrainMats': {'en': 'Train Materials', 'pt': 'Materiais de Trem', 'es': 'Materiales de Tren', 'id': 'Bahan Kereta', 'vi': 'Vật Liệu Tàu', 'ru': 'Материалы поезда'}, 'SP_MarketPremium': {'en': 'Market Premium', 'pt': 'Mercado Premium', 'es': 'Mercado Premium', 'id': 'Pasar Premium', 'vi': 'Chợ Premium', 'ru': 'Премиум-рынок'}, 'SP_BoostOrderCoins': {'en': 'Order Coins', 'pt': 'Moedas de Pedido', 'es': 'Monedas de Pedido', 'id': 'Koin Pesanan', 'vi': 'Xu Đơn Hàng', 'ru': 'Монеты заказов'}, 'SP_BoostSpeedUpTrains': {'en': 'Speed Up Trains', 'pt': 'Acelerar Trens', 'es': 'Acelerar Trenes', 'id': 'Percepat Kereta', 'vi': 'Tăng Tốc Tàu', 'ru': 'Ускорить поезда'}, 'SP_ClanHelpPremium': {'en': 'Clan Help Premium', 'pt': 'Ajuda Clã Premium', 'es': 'Ayuda Clan Premium', 'id': 'Bantuan Klan Premium', 'vi': 'Hỗ Trợ Clan Premium', 'ru': 'Помощь клана Премиум'}, 'SP_LoadAirPremium': {'en': 'Airport Load Premium', 'pt': 'Carga Aeroporto Premium', 'es': 'Carga Aeropuerto Premium', 'id': 'Muat Bandara Premium', 'vi': 'Tải Sân Bay Premium', 'ru': 'Загрузка аэропорта Премиум'}, 'Brick': {'en': 'Brick'}, 'Glass': {'en': 'Glass'}, 'Plita': {'en': 'Plita'}, 'axe': {'en': 'axe'}, 'powersaw': {'en': 'powersaw'}, 'hammerMat': {'en': 'hammerMat'}, 'nailMat': {'en': 'nailMat'}, 'paintRedMat': {'en': 'paintRedMat'}, 'pick': {'en': 'pick'}, 'TNT': {'en': 'TNT'}, 'jackhammer': {'en': 'jackhammer'}, 'drill': {'en': 'drill'}, 'BronzeBullionCounter': {'en': 'Bronze Bullion', 'pt': 'Lingote de Bronze', 'es': 'Lingote de Bronce', 'id': 'Perunggu Batangan', 'vi': 'Đồng Thỏi', 'ru': 'Бронзовый слиток'}, 'SilverBullionCounter': {'en': 'Silver Bullion', 'pt': 'Lingote de Prata', 'es': 'Lingote de Plata', 'id': 'Perak Batangan', 'vi': 'Bạc Thỏi', 'ru': 'Серебряный слиток'}, 'GoldBullionCounter': {'en': 'Gold Bullion', 'pt': 'Lingote de Ouro', 'es': 'Lingote de Oro', 'id': 'Emas Batangan', 'vi': 'Vàng Thỏi', 'ru': 'Золотой слиток'}, 'PlatinumBullionCounter': {'en': 'Platinum Bullion', 'pt': 'Lingote de Platina', 'es': 'Lingote de Platino', 'id': 'Platinum Batangan', 'vi': 'Bạch Kim Thỏi', 'ru': 'Платиновый слиток'}, 'CardC_Pack1': {'en': 'Card Pack 1', 'pt': 'Pack de Cartas 1', 'es': 'Pack de Cartas 1', 'id': 'Paket Kartu 1', 'vi': 'Gói Thẻ 1', 'ru': 'Набор карт 1'}, 'CardC_Pack2': {'en': 'Card Pack 2', 'pt': 'Pack de Cartas 2', 'es': 'Pack de Cartas 2', 'id': 'Paket Kartu 2', 'vi': 'Gói Thẻ 2', 'ru': 'Набор карт 2'}, 'CardC_Pack3': {'en': 'Card Pack 3', 'pt': 'Pack de Cartas 3', 'es': 'Pack de Cartas 3', 'id': 'Paket Kartu 3', 'vi': 'Gói Thẻ 3', 'ru': 'Набор карт 3'}, 'CardC_Pack4': {'en': 'Card Pack 4', 'pt': 'Pack de Cartas 4', 'es': 'Pack de Cartas 4', 'id': 'Paket Kartu 4', 'vi': 'Gói Thẻ 4', 'ru': 'Набор карт 4'}, 'CardC_Pack5': {'en': 'Card Pack 5', 'pt': 'Pack de Cartas 5', 'es': 'Pack de Cartas 5', 'id': 'Paket Kartu 5', 'vi': 'Gói Thẻ 5', 'ru': 'Набор карт 5'}, 'CouponLoadTrainAirport': {'en': 'Train/Airport Coupon', 'pt': 'Cupom Trem/Aeroporto', 'es': 'Cupón Tren/Aeropuerto', 'id': 'Kupon Kereta/Bandara', 'vi': 'Phiếu Tàu/Sân Bay', 'ru': 'Курон Поезд/Аэропорт'}, 'CouponHireDealer': {'en': 'Hire Dealer Coupon', 'pt': 'Cupom Contratar Comerciante', 'es': 'Cupón Contratar Comerciante', 'id': 'Kupon Sewa Dealer', 'vi': 'Phiếu Thuê Thương Nhân', 'ru': 'Купон Нанять торговца'}, 'CouponUpgradeFactory': {'en': 'Upgrade Factory Coupon', 'pt': 'Cupom Melhorar Fábrica', 'es': 'Cupón Mejorar Fábrica', 'id': 'Kupon Upgrade Pabrik', 'vi': 'Phiếu Nâng Cấp Nhà Máy', 'ru': 'Купон Улучшить завод'}, 'CouponUpgradeTrain': {'en': 'Upgrade Train Coupon', 'pt': 'Cupom Melhorar Trem', 'es': 'Cupón Mejorar Trem', 'id': 'Kupon Upgrade Kereta', 'vi': 'Phiếu Nâng Cấp Tàu', 'ru': 'Купон Улучшить поезд'}, 'CouponUpgradeIsland': {'en': 'Upgrade Island Coupon', 'pt': 'Cupom Melhorar Ilha', 'es': 'Cupón Mejorar Isla', 'id': 'Kupon Upgrade Pulau', 'vi': 'Phiếu Nâng Cấp Đảo', 'ru': 'Купон Улучшить остров'}}

PASS_REWARD_GROUPS.update({'T-Cash':['cash'],'Chest':['ST_Chest']})
PASS_REWARD_LABELS.update({'cash': {'en': 'T-Cash', 'pt': 'T-Cash', 'es': 'T-Cash', 'id': 'T-Cash', 'vi': 'T-Cash', 'ru': 'T-Cash'}, 'ST_Chest': {'en': 'Chest', 'pt': 'Báu', 'es': 'Cofre', 'id': 'Peti', 'vi': 'Rương', 'ru': 'Сундук'}})
PASS_REWARD_LABELS.update({k: {'en':v} for k,v in {'Brick':'Brick','Glass':'Glass','Plita':'Slab','axe':'Axe','powersaw':'Saw','hammerMat':'Hammer','nailMat':'Nails','paintRedMat':'Paint','pick':'Pickaxe','TNT':'Dynamite','jackhammer':'Jackhammer','drill':'Drill'}.items()})
for _pass_labels in PASS_REWARD_LABELS.values():
    if 'en' in _pass_labels:I18N_CATALOG.setdefault(_pass_labels['en'],{}).update(_pass_labels)

def pass_reward_name(key):
    return PASS_REWARD_LABELS.get(key, {}).get('en', key)

def pass_stage_models(xml, road):
    rows=[]
    for index,raw in enumerate(B.golden_pass_stages(xml,road),1):
        root=B.ET.fromstring(raw);reward=root.find('Reward')
        rows.append({'index':index,'raw':raw,'given':root.get('rewardGiven')=='1',
            'type':reward.get('type','') if reward is not None else None,
            'count':int(reward.get('count','0')) if reward is not None else 0,
            'subs':[{'type':child.get('type',''),'count':int(child.get('count','0')),
                'rewardGiven':child.get('rewardGiven')=='1','raw':B.ET.tostring(child)}
                for child in reward.findall('SubReward')] if reward is not None else []})
    return rows

def pass_patch_stage(raw,before,after):
    opening_end=raw.index(b'>')+1;tag=raw[:opening_end]
    if before['given']!=after['given']:
        tag=B.replace_attribute(tag,'rewardGiven','1') if after['given'] else re.sub(rb"\s+rewardGiven\s*=\s*(['\"])[^'\"]*\1",b'',tag)
    result=tag+raw[opening_end:]
    if all(before[k]==after[k] for k in ('type','count','subs')):return result
    match=re.search(rb'<Reward\b[^>]*?/\s*>|<Reward\b[^>]*>.*?</Reward\s*>',result,re.S)
    if match is None:raise B.SaveToolError('This stage has no Reward block.')
    reward=match.group();end=reward.index(b'>')+1;tag=reward[:end]
    for key in ('type','count'):
        if before[key]!=after[key]:tag=B.replace_attribute(tag,key,str(after[key]))
    if after['type']!='ST_Chest':replacement=re.sub(rb'/\s*>$|>$',b'/>',tag)
    elif before['subs']==after['subs']:replacement=tag+reward[end:]
    else:
        # Reuse untouched children byte-for-byte, including unknown attributes.
        original=list(re.finditer(rb'<SubReward\b[^>]*?/\s*>|<SubReward\b[^>]*>.*?</SubReward\s*>',reward,re.S))
        children=[]
        for child in after['subs']:
            block=child.get('raw',b'<SubReward/>')
            origin=next((v for v in before['subs'] if v.get('raw')==child.get('raw')),None)
            if origin is not None:
                pos=before['subs'].index(origin)
                if pos<len(original):block=original[pos].group()
            for key in ('type','count'):
                if origin is None or origin[key]!=child[key]:block=B.replace_attribute(block,key,str(child[key]))
            if origin is None or origin['rewardGiven']!=child['rewardGiven']:
                block=B.replace_attribute(block,'rewardGiven','1') if child['rewardGiven'] else re.sub(rb"\s+rewardGiven\s*=\s*(['\"])[^'\"]*\1",b'',block)
            children.append(block)
        # Preserve other reward children when editing the SubReward list.
        body=reward[end:re.search(rb'</Reward\s*>$',reward).start()] if not re.search(rb'/\s*>$',tag) else b''
        body=re.sub(rb'<SubReward\b[^>]*?/\s*>|<SubReward\b[^>]*>.*?</SubReward\s*>',b'',body,flags=re.S)
        replacement=re.sub(rb'/\s*>$',b'>',tag)+body+b''.join(children)+b'</Reward>'
    return result[:match.start()]+replacement+result[match.end():]

def pass_apply_rows(xml,changes):
    for road,rows in changes.items():
        block=B._advanced_block(B._advanced_block(xml,'SeasonTicket'),road);index=0
        def patch(match):
            nonlocal index
            index+=1
            return pass_patch_stage(match.group(),*rows[index]) if index in rows else match.group()
        block=re.sub(rb'<Stage\b[^>]*/>|<Stage\b[^>]*>.*?</Stage\s*>',patch,block,flags=re.S)
        season=B._advanced_block(xml,'SeasonTicket')
        xml=B._decor_replace_block(xml,'SeasonTicket',B._decor_replace_block(season,road,block))
    return xml

class PassProductDialog(NativeDialog):
    def __init__(self,parent=None,multiple=False,current=None):
        super().__init__('Choose rewards',parent,'Select products from the list. Quantities can be edited after selection.')
        self.resize(680,620);self.multiple=multiple
        search=QLineEdit();search.setPlaceholderText('Search products');self.body.addWidget(search)
        self.tree=QTreeWidget();self.tree.setHeaderLabels(['Product','Category']);self.tree.setProperty('i18nRowColumns',[0,1]);self.tree.header().setSectionResizeMode(0,QHeaderView.Stretch);self.body.addWidget(self.tree,1)
        self.tree.setSelectionMode(QAbstractItemView.SingleSelection)
        for group,keys in PASS_REWARD_GROUPS.items():
            for key in keys:
                if multiple and key=='ST_Chest':continue
                item=QTreeWidgetItem(self.tree,[pass_reward_name(key),group]);item.setData(0,Qt.UserRole,key)
                if multiple:item.setCheckState(0,Qt.Unchecked)
                if key==current:self.tree.setCurrentItem(item)
        search.textChanged.connect(lambda text:[self.tree.topLevelItem(i).setHidden(text.casefold() not in (self.tree.topLevelItem(i).text(0)+' '+self.tree.topLevelItem(i).text(1)).casefold()) for i in range(self.tree.topLevelItemCount())])
        if not multiple:self.tree.itemDoubleClicked.connect(lambda *_:self.accept_checked())
        self.validator=lambda: self.require_products()
    def products(self):
        if self.multiple:return [self.tree.topLevelItem(i).data(0,Qt.UserRole) for i in range(self.tree.topLevelItemCount()) if self.tree.topLevelItem(i).checkState(0)==Qt.Checked]
        return [self.tree.currentItem().data(0,Qt.UserRole)] if self.tree.currentItem() else []
    def require_products(self):
        if not self.products():raise B.SaveToolError('Select at least one product.')

class PassChestDialog(NativeDialog):
    def __init__(self,items,parent=None):
        super().__init__('Chest rewards',parent,'Add several products and set the quantity and Claim state for each product.')
        self.resize(760,600);self.rows=[]
        self.tree=QTreeWidget();self.tree.setHeaderLabels(['Product','Quantity','Claim']);self.tree.setProperty('i18nRowColumns',[0]);self.tree.header().setSectionResizeMode(0,QHeaderView.Stretch);self.body.addWidget(self.tree,1)
        for item in items:self.add_row(dict(item))
        bar=QHBoxLayout();add=QPushButton('Add products');remove=QPushButton('Remove selected');bar.addWidget(add);bar.addWidget(remove);self.body.addLayout(bar)
        add.clicked.connect(self.choose_products);remove.clicked.connect(self.remove_selected)
    def add_row(self,data):
        row=QTreeWidgetItem(self.tree,[pass_reward_name(data['type'])]);row.setSizeHint(0,QSize(0,56));qty=number(data['count']);claim=QCheckBox();claim.setChecked(data['rewardGiven']);self.tree.setItemWidget(row,1,qty);self.tree.setItemWidget(row,2,claim);self.rows.append((row,data,qty,claim))
    def choose_products(self):
        dialog=PassProductDialog(self,True)
        if dialog.exec_()==QDialog.Accepted:
            for key in dialog.products():self.add_row({'type':key,'count':1,'rewardGiven':False})
    def remove_selected(self):
        row=self.tree.currentItem()
        if row is not None:
            self.rows=[entry for entry in self.rows if entry[0] is not row];self.tree.takeTopLevelItem(self.tree.indexOfTopLevelItem(row))
    def values(self):
        return [dict(data,count=qty.value(),rewardGiven=claim.isChecked()) for row,data,qty,claim in self.rows]

class PassStagePage(QWidget):
    def __init__(self,xml,road,parent=None):
        super().__init__(parent);self.road=road;self.original=pass_stage_models(xml,road);self.rows=[]
        layout=QVBoxLayout(self);self.tree=QTreeWidget();self.tree.setHeaderLabels(['Stage','Claim','Reward product','Quantity','Chest products']);self.tree.header().setSectionResizeMode(2,QHeaderView.Stretch);layout.addWidget(self.tree)
        self.tree.header().setStretchLastSection(False);self.tree.setColumnWidth(0,110);self.tree.setColumnWidth(1,80);self.tree.setColumnWidth(3,120);self.tree.setColumnWidth(4,200)
        for source in self.original:
            data=dict(source,subs=[dict(v) for v in source['subs']]);row=QTreeWidgetItem(self.tree,['Stage '+str(data['index'])]);row.setSizeHint(0,QSize(0,56));claim=QCheckBox();claim.setChecked(data['given']);product=QPushButton(pass_reward_name(data['type']) if data['type'] is not None else 'No reward');qty=number(data['count']);chest=QPushButton()
            entry={'data':data,'claim':claim,'product':product,'qty':qty,'chest':chest};self.rows.append(entry)
            product.setEnabled(data['type'] is not None);qty.setEnabled(data['type'] is not None)
            self.tree.setItemWidget(row,1,claim);self.tree.setItemWidget(row,2,product);self.tree.setItemWidget(row,3,qty);self.tree.setItemWidget(row,4,chest)
            product.clicked.connect(lambda _,e=entry:self.choose_product(e));chest.clicked.connect(lambda _,e=entry:self.edit_chest(e));self.refresh(entry)
    def refresh(self,entry):
        chest=entry['data']['type']=='ST_Chest';entry['chest'].setEnabled(chest);entry['chest'].setText(('Products: '+str(len(entry['data']['subs']))) if chest else '—');entry['product'].setText(pass_reward_name(entry['data']['type']) if entry['data']['type'] is not None else 'No reward')
    def choose_product(self,entry):
        dialog=PassProductDialog(self,current=entry['data']['type'])
        if dialog.exec_()==QDialog.Accepted:
            key=dialog.products()[0];entry['data']['type']=key;self.refresh(entry)
    def edit_chest(self,entry):
        dialog=PassChestDialog(entry['data']['subs'],self)
        if dialog.exec_()==QDialog.Accepted:entry['data']['subs']=dialog.values();self.refresh(entry)
    def changes(self):
        result={}
        for before,entry in zip(self.original,self.rows):
            after=dict(entry['data'],given=entry['claim'].isChecked(),count=entry['qty'].value())
            if after['type']!='ST_Chest':after['subs']=before['subs'] # conversion handled in the XML patch
            if any(before[k]!=after[k] for k in ('given','type','count','subs')):result[before['index']]=(before,after)
        return result


def gui_tsvip_content_checksum(payload):
    # rc0.b: 32-bit running sums (not Adler-32's modulo 65521).
    first=1;second=0
    for value in payload:
        first=(first+value)&0xFFFFFFFF
        second=(second+first)&0xFFFFFFFF
    return (((first|((second<<16)&0xFFFFFFFF))>>16)^(first&0xFFFF))&0xFFFF

def gui_encode_xml_standalone(xml,compress=True):
    import secrets
    B.validate_xml_document(xml,'Encode input XML')
    canonical=B.canonical_xml(xml);raw=canonical+b'\x00'
    if len(raw)>B.MAX_XML_SIZE:raise B.SaveToolError('XML exceeds the supported 32 MB limit.')
    payload=(B.LZ4_MAGIC+B.struct.pack('<I',len(raw))+B.lz4.block.compress(raw,mode='default',store_size=False)) if compress else raw
    total=len(payload)+B.HEADER_SIZE
    header_seed=(len(payload)^B.PAYLOAD_XOR)+(total^B.HEADER_XOR)
    if header_seed>0xFFFFFF:raise B.SaveToolError('Encoded payload exceeds the 24-bit header limit; no output written.')
    # TSVIP derives the low 16 bits from the payload and generates nonzero high bits.
    content_seed=((secrets.randbelow(65535)+1)<<16)|gui_tsvip_content_checksum(payload)
    table=B.build_hash_table(header_seed,(content_seed+4)&0xFFFFFFFF)
    encoded=bytearray(total);encoded[0]=B.FORMAT_79
    encoded[1:4]=header_seed.to_bytes(3,'little');encoded[4:8]=B.struct.pack('<I',content_seed)
    previous=0
    for index,value in enumerate(payload):
        encoded[B.HEADER_SIZE+index]=((value^table[index%B.HASH_TABLE_SIZE])+previous)&0xFF
        previous=value
    result=bytes(encoded)
    if B.decode_save(result)!=canonical:raise B.SaveToolError('Encode/decode verification failed; no output written.')
    return result

def gui_convert_save_file(source,destination,encode=False):
    source=Path(source).resolve();destination=Path(destination).resolve()
    if not source.is_file():raise B.SaveToolError('Select an existing input file.')
    if source==destination:raise B.SaveToolError('Output must be different from the input file.')
    if source.stat().st_size>B.MAX_CONTAINER_SIZE:raise B.SaveToolError('Input file exceeds the 64 MB limit.')
    data=source.read_bytes()
    if encode:result=gui_encode_xml_standalone(data)
    else:
        result=B.decode_save(data);B.validate_xml_document(result,'Decoded XML')
    if not destination.parent.is_dir():raise B.SaveToolError('The output folder does not exist.')
    B.atomic_write(destination,result)
    return destination

def barn_groups(products):
    # Explicit known raw materials; unclassified IDs remain available in Products.
    farm=set('wheat corn carrot sugarcane cotton strawberry tomat pine potato cacao rubberTree rubber silk shelk pepper rice roseSeed jasmine coffee soybean teabush mint peanut lavender cork aloeLeaves milk egg wool bacon honeycomb mushroom downFeather bigFeather apple peach watermelon plum grapes banana coconut pineapple olive lemon aloe mango1 avocado'.split())
    sea=set('fish shrimp lobster scallop pearl seaweed'.split())
    materials=set('Brick Glass Plita hammerMat nailMat paintRedMat axe powersaw pick TNT jackhammer drill clay'.split())
    groups={'Nguyên liệu nông trại':[],'Nguyên liệu biển':[],'Vật liệu / Dụng cụ':[],'Sản phẩm / Khác':[]}
    for pid in products:
        group='Nguyên liệu nông trại' if pid in farm else 'Nguyên liệu biển' if pid in sea else 'Vật liệu / Dụng cụ' if pid in materials else 'Sản phẩm / Khác'
        groups[group].append(pid)
    return {g:ids for g,ids in groups.items() if ids}

class BarnTreeItem(QTreeWidgetItem):
    def __lt__(self,other):
        a=self.data(0,Qt.UserRole+1);b=other.data(0,Qt.UserRole+1)
        return a<b if a is not None and b is not None else super().__lt__(other)

class BarnPicker(ItemPicker):
    def __init__(self,groups,current,parent=None):
        self.baseline=dict(current)
        super().__init__(groups,parent,current=current,values=True,defaults=current,row_class=BarnTreeItem)
        toolbar=QHBoxLayout();toolbar.addWidget(QLabel('Sắp xếp trong từng nhóm:'));self.sorter=QComboBox()
        for title,key in [('Tên / ID A → Z','name'),('Số lượng hiện tại: cao → thấp','qty_desc'),('Số lượng hiện tại: thấp → cao','qty_asc')]:self.sorter.addItem(title,key)
        toolbar.addWidget(self.sorter,1);self.layout().insertLayout(1,toolbar)
        self.sorter.currentIndexChanged.connect(self.sort_rows)
        for spin in self.spinboxes.values():spin.valueChanged.connect(self.update_count)
        self.sort_rows();self.update_count()
    def sort_rows(self,*_):
        mode=self.sorter.currentData()
        for key,item in self.rows.items():
            qty=self.baseline[key[1]];name=item.text(0).casefold()
            rank=(name,key[1]) if mode=='name' else ((-qty if mode=='qty_desc' else qty),name,key[1])
            item.setData(0,Qt.UserRole+1,rank)
        for parent in self.groups.values():parent.sortChildren(0,Qt.AscendingOrder)
    def changed_values(self):
        return {pid:value for pid,value in self.values().items() if value!=self.baseline[pid]}
    def require_changes(self):
        if not self.changed_values():raise B.SaveToolError('Chọn ít nhất một dòng có số lượng mới khác hiện tại.')
    def update_count(self,*_):
        selected=len(self.values());changed=len(self.changed_values())
        modified=sum(spin.value()!=self.baseline[key[1]] for key,spin in self.spinboxes.items())
        self.counter.setText(f'Đã chọn: {selected} · Đã sửa: {modified} · Sẽ áp dụng: {changed} dòng')

class SaveDiagnosticWorker(QThread):
    line=pyqtSignal(str)
    def __init__(self,config,parent=None):
        super().__init__(parent);self.config=config
    def command(self,*args):
        if self.isInterruptionRequested():raise InterruptedError('Đã dừng chẩn đoán.')
        adb,serial,_=self.config
        result=subprocess.run([adb,'-s',serial,*args],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=10,
                              creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        return result.returncode,(result.stdout+'\n'+result.stderr).strip()
    def run(self):
        try:
            adb,serial,package=self.config
            self.line.emit(f'TS Studio v1.39 · Chẩn đoán ADB / save\nThiết bị: {serial}\nGói đã chọn: {package}')
            code,state=self.command('get-state');self.line.emit('Trạng thái ADB: '+state)
            if code or state!='device':self.line.emit('Thiết bị chưa sẵn sàng. Kiểm tra serial và kết nối ADB.');return
            code,out=self.command('shell','pm path '+shlex.quote(package))
            self.line.emit('Package: '+('Đã cài' if code==0 and 'package:' in out else 'Chưa xác nhận được package; kiểm tra tên gói.'))
            code,out=self.command('shell','id -u');prefix='' if code==0 and out=='0' else None
            if prefix is None:
                for candidate in ('su 0 sh -c','su -c','su root sh -c'):
                    code,out=self.command('shell',candidate+' '+shlex.quote('id -u'))
                    if code==0 and out=='0':prefix=candidate;break
            if prefix is None:
                self.line.emit('Quyền root: chưa xác nhận được UID 0. Bật root trong giả lập và cấp quyền cho ADB.\nKhông thể kiểm tra save riêng của game.');return
            self.line.emit('Quyền root: OK (UID 0)')
            if self.isInterruptionRequested():raise InterruptedError('Đã dừng chẩn đoán.')
            for base in (f'/data/data/{package}/saves',f'/data/user/0/{package}/saves'):
                self.line.emit('\nThư mục: '+base)
                q=shlex.quote(base);commands=[f'if [ -d {q} ]; then echo "Thư mục: tồn tại"; else echo "Thư mục: thiếu"; fi']
                for filename in ('mGameInfo.xml','LocalInfo.xml'):
                    q=shlex.quote(base+'/'+filename)
                    commands.append(f'if [ -f {q} ]; then if [ -r {q} ]; then echo "{filename}: đọc được"; else echo "{filename}: không đọc được"; fi; ls -ln {q}; else echo "{filename}: thiếu"; fi')
                command='; '.join(commands)
                code,out=self.command('shell',(prefix+' '+shlex.quote(command)) if prefix else command)
                self.line.emit(out or 'Không nhận được kết quả kiểm tra.')
                if code:self.line.emit('Lệnh kiểm tra gặp lỗi; xem kết quả bên trên.')
            self.line.emit('\nHoàn tất. Hai đường dẫn có thể trỏ cùng thư mục. Báo cáo chỉ kiểm tra quyền và thông tin file, chưa kiểm tra nội dung mã hóa của save.')
        except InterruptedError as exc:self.line.emit(str(exc))
        except subprocess.TimeoutExpired:self.line.emit('Lệnh ADB quá thời gian 10 giây. Kiểm tra kết nối hoặc hộp thoại cấp quyền root trong giả lập.')
        except Exception as exc:self.line.emit('Chẩn đoán gặp lỗi: '+str(exc))

class SaveDiagnosticDialog(QDialog):
    def __init__(self,config,parent=None):
        super().__init__(parent);self.setWindowTitle('Chẩn đoán ADB / save');self.resize(900,620)
        layout=QVBoxLayout(self);hint=QLabel('Dùng thông số đang nhập trong Cấu hình. Kiểm tra ADB, quyền root và cặp file save.');hint.setWordWrap(True);layout.addWidget(hint)
        self.report=QPlainTextEdit();self.report.setReadOnly(True);layout.addWidget(self.report,1)
        row=QHBoxLayout();copy=QPushButton('Sao chép báo cáo');save=QPushButton('Xuất báo cáo…');self.close_button=QPushButton('Dừng chẩn đoán');row.addWidget(copy);row.addWidget(save);row.addStretch();row.addWidget(self.close_button);layout.addLayout(row)
        copy.clicked.connect(lambda:QApplication.clipboard().setText(self.report.toPlainText()));save.clicked.connect(self.export_report);self.close_button.clicked.connect(self.reject)
        self.worker=SaveDiagnosticWorker(config,self);self.worker.line.connect(lambda text:append_activity(self.report,text));self.worker.finished.connect(self.complete);self.worker.start()
    def complete(self):self.close_button.setText('Đóng');self.close_button.setEnabled(True)
    def export_report(self):
        path,_=QFileDialog.getSaveFileName(self,'Xuất chẩn đoán','ts_adb_diagnostic.txt','Text (*.txt)')
        if path:
            try:Path(path).write_text(self.report.toPlainText(),encoding='utf-8')
            except OSError as exc:QMessageBox.warning(self,'Xuất chẩn đoán',str(exc))
    def reject(self):
        if self.worker.isRunning():
            self.worker.requestInterruption();self.close_button.setText('Đang dừng…');self.close_button.setEnabled(False)
        else:super().reject()
    def closeEvent(self,event):
        if self.worker.isRunning():self.reject();event.ignore()
        else:super().closeEvent(event)


STICKER_VI_LABELS = {'st1': 'Vịt Cướp Biển', 'st2': 'Bò Cướp Biển', 'st3': 'Heo Cướp Biển', 'st4': 'Cừu Cocktail', 'st5': 'Bò Nhảy Múa', 'st6': 'Ong Nhạc Sĩ', 'st7': 'Vẹt Cao Bồi', 'st8': 'Heo Cao Bồi', 'st9': 'Hải Ly Cao Bồi', 'st10': 'Gà Tây Phù Thủy', 'st11': 'Ong Sành Điệu', 'st12': 'Cừu Điên', 'st13': 'Bò Hoa', 'st14': 'Heo Nông Dân', 'st15': 'Vịt Cà Rốt', 'st16': 'Ong Giáng Sinh', 'st17': 'Cừu Mùa Đông', 'st18': 'Gà Trượt Băng', 'st22': 'Bò Phi Hành Gia', 'st23': 'Heo Tên Lửa', 'st24': 'Gà Đầu Bếp', 'st25': 'Chim Tình Yêu', 'st26': 'Ong Bọ Rùa', 'st27': 'Cừu Nhạc Sĩ', 'st28': 'Hải Ly Thần Đèn', 'st29': 'Gà Phục Sinh', 'st30': 'Ong Phục Sinh', 'st31': 'Bò Rocker', 'st32': 'Hải Ly Trống', 'st34': 'Heo Lái Thuyền', 'st35': 'Cừu Hang Động', 'st36': 'Bò Lửa Trại', 'st37': 'Ong Mùa Hè', 'st38': 'Gà Thư Giãn', 'st39': 'Heo Hula', 'st40': 'Bò Điện Ảnh', 'st41': 'Gà Phi Công', 'st42': 'Vịt Halloween', 'st43': 'Ong Phù Thủy', 'st44': 'Hải Ly Pháp Sư', 'st45': 'Bò Giáng Sinh', 'st46': 'Cá Rồng', 'st47': 'Cừu Hồng', 'st48': 'Gà Cổ Vũ', 'st49': 'Cừu Thỏ', 'st50': 'Heo Phi Hành Gia', 'st51': 'Ong Tiên', 'st52': 'Cừu Sấm Sét', 'st53': 'Cừu Thám Tử', 'st54': 'Gà Cao Bồi', 'st55': 'Bò Đầu Bếp', 'st56': 'Bò Ma Cà Rồng', 'st57': 'Cừu Cung Thủ', 'st58': 'Gà Nhảy Múa', 'st59': 'Bò Trượt Tuyết', 'st60': 'Cừu Lễ Hội', 'st61': 'Heo Trung Hoa', 'st62': 'Vịt Yêu Tinh', 'st63': 'Bò Phục Sinh', 'st64': 'Gà Rocker', 'st65': 'Gà Đánh Hạc', 'st66': 'Đặc Vụ Bí Mật', 'st67': 'Cừu Hiệp Sĩ', 'st68': 'Cừu Atlantis', 'st69': 'Cừu Mexico', 'st70': 'Gà Đi Nghỉ', 'st71': 'Bò Ý', 'st72': 'Cừu Xiếc', 'st73': 'Gà Pháp Sư', 'st74': 'Cừu Ai Cập', 'st75': 'Bò Cướp Biển', 'st76': 'Cừu Giáng Sinh', 'st77': 'Bò Mùa Đông', 'st78': 'Gà Trung Hoa', 'st79': 'Bò Ca Sĩ', 'st80': 'Cừu Công Chúa', 'sp1': 'Cừu Quà Tặng', 'sp2': 'Bò Tình Yêu', 'sp4': 'Gà', 'sp5': 'Heo Hoa', 'sp6': 'Ong Sành Điệu', 'sp7': 'Bò Điện Ảnh', 'sp8': 'Hải Ly Giận Dữ', 'sp9': 'Vịt Tự Sướng', 'sp10': 'Chim Xanh', 'sp11': 'Heo Thời Trang', 'sp12': 'Cừu Rapper', 'sp13': 'Vịt Ma Cà Rồng', 'sp14': 'Hải Ly Pháp Sư', 'sp15': 'Bò Frankenstein', 'sp16': 'Cừu Mùa Đông', 'sp17': 'Bò Giáng Sinh', 'sp18': 'Gà Mùa Đông', 'sp19': 'Vịt Giáng Sinh', 'sp20': 'Heo Trung Hoa', 'sp21': 'Hải Ly Trung Hoa', 'sp22': 'Hải Ly DJ', 'sp23': 'Cừu Sao', 'sp24': 'Vịt Phong Cách', 'sp25': 'Heo Hawaii', 'sp26': 'Hải Ly Đi Nghỉ', 'sp27': 'Gà Choáng', 'v1': 'Vịt Buồn', 'v2': 'Đôi Vịt Yêu', 'v3': 'Hải Ly Thiên Thần'}

# Four additions confirmed in-game by the user after the v1.39 test.
CONFIRMED_DECORATION_FRAGMENTS = {'ExpeditionDecoration46': '<ExpeditionDecoration46 guid=""><base active="1" beenSetOnField="1"/><part1 active="1" beenSetOnField="1"/><part2 active="1" beenSetOnField="1"/><part3 active="1" beenSetOnField="1"/><part4 active="1" beenSetOnField="1"/></ExpeditionDecoration46>', 'ExpeditionDecoration47': '<ExpeditionDecoration47 guid=""><base active="1" beenSetOnField="1"/><part1 active="1" beenSetOnField="1"/><part2 active="1" beenSetOnField="1"/><part3 active="1" beenSetOnField="1"/><part4 active="1" beenSetOnField="1"/></ExpeditionDecoration47>', 'ExpeditionDecoration48': '<ExpeditionDecoration48 guid=""><base active="1" beenSetOnField="1"/><part1 active="1" beenSetOnField="1"/><part2 active="1" beenSetOnField="1"/><part3 active="1" beenSetOnField="1"/><part4 active="1" beenSetOnField="1"/></ExpeditionDecoration48>', 'ExpeditionDecoration49': '<ExpeditionDecoration49 guid=""><base active="1" beenSetOnField="1"/><part1 active="1" beenSetOnField="1"/><part2 active="1" beenSetOnField="1"/><part3 active="1" beenSetOnField="1"/><part4 active="1" beenSetOnField="1"/></ExpeditionDecoration49>'}
B.DECORATION_GROUPS = {key:tuple(ids) for key,ids in B.DECORATION_GROUPS.items()}
B.DECORATION_GROUPS['special'] += tuple(sid for sid in CONFIRMED_DECORATION_FRAGMENTS if sid not in B.DECORATION_GROUPS['special'])
B.DECORATION_FRAGMENTS = dict(B.DECORATION_FRAGMENTS,**CONFIRMED_DECORATION_FRAGMENTS)

def gui_factory_slot_inventory(xml):
    """Read only existing factory Object JSON; keep ambiguous schemas disabled."""
    B.validate_xml_document(xml,'Ô sản xuất nhà máy')
    catalog=set(B.TSVIP_ACADEMY['Factory']);found={};problems={}
    for match in re.finditer(rb'<Object\b[^>]*>',xml):
        attrs=B.parse_attributes(match.group(0))
        candidates=[]
        for attribute in ('data','v','value'):
            if attribute not in attrs:continue
            try:
                def unique_keys(pairs):
                    data={}
                    for key,value in pairs:
                        if key in data:raise ValueError('JSON trùng khóa')
                        data[key]=value
                    return data
                data=json.loads(B.html.unescape(attrs[attribute]),object_pairs_hook=unique_keys)
            except (ValueError,TypeError):continue
            if isinstance(data,dict) and isinstance(data.get('storeId'),str) and data['storeId'] in catalog:candidates.append((attribute,data))
        for attribute,data in candidates:
            sid=data['storeId'];found.setdefault(sid,[]).append((match,attribute,data))
    inventory={}
    for sid,rows in found.items():
        if len(rows)!=1:problems[sid]='Có nhiều Object / thuộc tính JSON cùng ID';continue
        match,attribute,data=rows[0];slots=data.get('slotsCount')
        if type(slots) is not int or not 2<=slots<=7:
            problems[sid]='Thiếu slotsCount hoặc ngoài phạm vi hỗ trợ 2–7';continue
        inventory[sid]=(match,attribute,data)
    return inventory,problems

def gui_set_factory_slots(xml,updates):
    if not updates:raise B.SaveToolError('Chọn ít nhất một nhà máy có số ô thay đổi.')
    inventory,problems=gui_factory_slot_inventory(xml);replacements=[]
    for sid,count in updates.items():
        if type(count) is not int or not 2<=count<=7:raise B.SaveToolError('Số ô sản xuất phải từ 2 đến 7.')
        if sid not in inventory:raise B.SaveToolError(sid+': '+problems.get(sid,'Chưa có Object nhà máy hợp lệ trong save.'))
        match,attribute,data=inventory[sid]
        if count==data['slotsCount']:continue
        newdata=dict(data);newdata['slotsCount']=count
        tag=B.replace_attribute(match.group(0),attribute,json.dumps(newdata,ensure_ascii=False,separators=(',',':')))
        replacements.append((match.start(),match.end(),tag,sid,newdata))
    result=xml
    for start,end,tag,_,_ in sorted(replacements,reverse=True):result=result[:start]+tag+result[end:]
    verified,_=gui_factory_slot_inventory(result)
    for _,_,_,sid,expected in replacements:
        if sid not in verified or verified[sid][2]!=expected:raise B.SaveToolError('Xác minh ô sản xuất thất bại: '+sid)
    B.validate_xml_document(result,'Ô sản xuất sau sửa')
    return result,{'nhà máy đã sửa':len(replacements),'số ô':{sid:expected['slotsCount'] for _,_,_,sid,expected in replacements}}

def gui_factory_slots_page(xml,parent=None):
    inventory,problems=gui_factory_slot_inventory(xml);ids=list(B.TSVIP_ACADEMY['Factory'])
    current={sid:inventory[sid][2]['slotsCount'] if sid in inventory else problems.get(sid,'Chưa có dữ liệu nhà máy') for sid in ids}
    picker=ItemPicker({'Nhà máy':ids},parent,current=current,values=True,limits=(2,7),
                      defaults={sid:inventory[sid][2]['slotsCount'] if sid in inventory else 2 for sid in ids},disabled=set(ids)-set(inventory))
    picker.setObjectName('factory_slots_picker')
    for key,spin in picker.spinboxes.items():
        if key[1] not in inventory:
            spin.setEnabled(False);picker.rows[key].setToolTip(0,str(current[key[1]]))
    def changed():return {sid:value for sid,value in picker.values().items() if sid in inventory and value!=inventory[sid][2]['slotsCount']}
    picker.slot_changes=changed
    def require():
        if not changed():raise B.SaveToolError('Chọn ít nhất một nhà máy có số ô mới khác hiện tại.')
    picker.require_slot_changes=require
    counter=QLabel();counter.setObjectName('factory_slots_count');picker.layout().addWidget(counter)
    def update(*_):counter.setText(f'Đọc được: {len(inventory)} / {len(ids)} nhà máy · Sẽ áp dụng: {len(changed())} nhà máy')
    for spin in picker.spinboxes.values():spin.valueChanged.connect(update)
    picker.tree.itemChanged.connect(update);update()
    hint=QLabel('Chọn số ô sản xuất từ 2 đến 7. Chỉ sửa nhà máy đã có dữ liệu hợp lệ; mục thiếu hoặc trùng dữ liệu bị vô hiệu hóa.');hint.setWordWrap(True);picker.layout().addWidget(hint)
    return picker


def number(value=0,minimum=0,maximum=2147483647):
    widget=QSpinBox();widget.setRange(minimum,maximum);widget.setValue(value);return widget

def text_field(value='',secret=False):
    widget=QLineEdit(str(value or ''))
    if secret:widget.setEchoMode(QLineEdit.Password)
    return widget

def optional_field(form,label,widget,checked=False):
    row=QHBoxLayout();check=QCheckBox('Sửa');check.setObjectName('edit_'+label);widget.setObjectName('value_'+label);check.setChecked(checked);widget.setEnabled(checked);check.toggled.connect(widget.setEnabled);row.addWidget(check);row.addWidget(widget,1);form.addRow(label,row);return check,widget

def remember_browse_path(key,path):
    if not key or not path:return
    settings=QSettings('TownshipStudio','PyQt5');chosen=Path(path).expanduser()
    settings.setValue(key+'/path',str(chosen));settings.setValue(key+'/browse_dir',str(chosen if chosen.is_dir() else chosen.parent));settings.sync()

def path_field(form,label,initial='',folder=False,remember_key='',save=False):
    settings=QSettings('TownshipStudio','PyQt5')
    initial=str(settings.value(remember_key+'/path',initial)) if remember_key else initial
    edit=text_field(initial);row=QHBoxLayout();row.addWidget(edit,1);browse=QPushButton('Save as…' if save else 'Chọn…');row.addWidget(browse)
    def pick():
        current=Path(edit.text()).expanduser() if edit.text().strip() else Path(initial or B.WORK_DIR)
        fallback=str(current if current.is_dir() else current.parent)
        directory=str(settings.value(remember_key+'/browse_dir',fallback)) if remember_key else edit.text()
        start=str(Path(directory)/current.name) if save and not current.is_dir() else directory
        if folder:path=QFileDialog.getExistingDirectory(edit,label,directory)
        elif save:path,_=QFileDialog.getSaveFileName(edit,label,start,'XML / Township save (*.xml);;All files (*)')
        else:path,_=QFileDialog.getOpenFileName(edit,label,directory,'Tất cả (*)')
        if path:
            if save:edit.setProperty('codecManualOutput',True)
            edit.setText(path);remember_browse_path(remember_key,path)
    browse.clicked.connect(pick);form.addRow(label,row);return edit

def selected_mapping(picker):return {k:v for k,v in picker.selected().items() if v}

def apply_result(result):
    xml=result[0] if isinstance(result,tuple) else result
    B.validate_xml_document(xml,'Kết quả editor GUI')
    if xml==B.SESSION.current_xml:B.print('Không có thay đổi.');return
    B.SESSION.apply_xml(xml)
    B.print('Đã áp dụng vào XML làm việc. Chưa ghi vào game.')
    if isinstance(result,tuple):B.print('Chi tiết:',result[1])

class DonorSource(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent);form=QFormLayout(self);form.setContentsMargins(0,0,0,0)
        self.kind=QComboBox();self.kind.addItem('Donor đã tải','loaded');self.kind.addItem('File XML/save trên máy','file');self.kind.addItem('Backup ZIP thành phố','zip');self.kind.addItem('City ID (FetchCity)','city');self.kind.addItem('Bạn bè từ LocalInfo','friend');form.addRow('Nguồn donor',self.kind)
        self.path=path_field(form,'File donor');self.city=text_field();form.addRow('City ID',self.city)
        self.friend=QComboBox()
        for friend in sorted((B.SESSION.friends or {}).values(),key=B.friend_sort_key):self.friend.addItem(f'{friend.city_name} · {friend.city_id} · LV {friend.level}',friend.city_id)
        form.addRow('Bạn bè',self.friend)
        meta=B.SESSION.localinfo_meta or {};self.bver=text_field(meta.get('version') or '');self.fver=text_field(meta.get('fver') or '');form.addRow('bver',self.bver);form.addRow('fver',self.fver)
        self.kind.currentIndexChanged.connect(self.update);self.update()
    def update(self,*_):
        kind=self.kind.currentData();self.path.setEnabled(kind in ('file','zip'));self.city.setEnabled(kind=='city');self.friend.setEnabled(kind=='friend');self.bver.setEnabled(kind in ('city','friend'));self.fver.setEnabled(kind in ('city','friend'))
    def data(self):
        kind=self.kind.currentData();city=self.friend.currentData() if kind=='friend' else self.city.text().strip()
        if kind in ('file','zip') and not Path(self.path.text()).is_file():raise B.SaveToolError('Chọn file donor tồn tại.')
        if kind in ('city','friend'):
            if not city or not re.fullmatch(r'[A-Za-z0-9_-]{3,64}',city):raise B.SaveToolError('Chọn/nhập City ID hợp lệ.')
            if not self.bver.text().strip() or not self.fver.text().strip():raise B.SaveToolError('Điền bver và fver.')
        if kind=='loaded' and B.SESSION.donor_xml is None and not B.DONOR_FILE.is_file():raise B.SaveToolError('Chưa có donor. Chọn file hoặc FetchCity.')
        return kind,self.path.text().strip(),city,self.bver.text().strip(),self.fver.text().strip()
    @staticmethod
    def load(data):
        kind,path,city,bver,fver=data
        if kind=='loaded':donor=B.SESSION.donor_xml or B.load_friend_donor(B.DONOR_FILE)
        elif kind=='file':donor=B.load_friend_donor(Path(path));B.SESSION.donor_path=Path(path)
        elif kind=='zip':
            game,local,meta,_=B.read_account_backup(Path(path));donor=B.decode_save(game);B.SESSION.donor_path=Path(path);B.print('Donor ZIP:',meta)
        else:
            donor,_,version=B.fetch_city_live(city,bver,fver,0);B.SESSION.donor_path=B.FRIENDS_DIR/city/'friend_city.xml';B.print('FetchCity thành công:',city,'cityVer:',version)
        B.SESSION.donor_xml=donor;return donor


# GUI Train reader accepts proven wagon keys in Train/Trains XML contexts.
# It does not create trains or infer unknown game schemas.
def gui_train_scan(xml,allow_multiple=False):
    B.validate_xml_document(xml,'Train save')
    tokens=re.finditer(rb'<!--.*?-->|<!\[CDATA\[.*?\]\]>|<(/?)([A-Za-z_][\w:.-]*)(?:"[^"]*"|\'[^\']*\'|[^\'">])*>',xml,re.S)
    stack=[];rows=[];summary=[]
    for match in tokens:
        if match.group(2) is None:continue
        name=match.group(2).decode();lower=name.casefold();closing=match.group(1)==b'/'
        if closing:
            if stack and stack[-1][0]==name:stack.pop()
            continue
        path='/'.join(v[0] for v in stack+[ (name,match.start()) ])
        contexts=[v for v in stack if v[0].casefold() in ('train','trains')]
        if lower in ('train','trains'):contexts.append((name,match.start()))
        attrs=B.parse_attributes(match.group(0))
        if lower in ('train','trains'):summary.append({'path':path,'offset':match.start(),'attributes':sorted(attrs),'self_closing':match.group(0).rstrip().endswith(b'/>')})
        if contexts:
            candidates=[]
            for attribute in ('v','value'):
                raw=attrs.get(attribute)
                if raw is None:continue
                try:data=json.loads(B.html.unescape(raw))
                except (ValueError,TypeError):continue
                if isinstance(data,dict) and any(f'productId_{n}' in data or f'productCount_{n}' in data for n in range(1,6)):
                    candidates.append((attribute,data))
            if len(candidates)>1:raise B.SaveToolError('Một tag Train chứa hai thuộc tính JSON toa tàu; cần kiểm tra save trước khi sửa.')
            if candidates:
                attribute,data=candidates[0]
                owner=next((v[1] for v in contexts if v[0].casefold()=='trains'),None)
                rows.append((match,data,attribute,path,owner))
        if not match.group(0).rstrip().endswith(b'/>'):stack.append((name,match.start()))
    owners={v[4] for v in rows if v[4] is not None}
    if len(owners)>1 and not allow_multiple:raise B.SaveToolError('Có nhiều khối Trains chứa dữ liệu toa tàu; chọn rõ một khối trong GUI để chỉnh sửa.')
    return (rows if allow_multiple else [v[:4] for v in rows]),summary

def gui_train_groups(xml):
    rows,summary=gui_train_scan(xml,allow_multiple=True)
    groups=[];owners={}
    by_offset={block['offset']:block for block in summary}
    for match,data,attribute,path,owner in rows:
        if owner not in owners:
            owners[owner]=len(groups)
            groups.append({'path':by_offset.get(owner,{}).get('path',path.rsplit('/',1)[0]),'rows':[]})
        groups[owners[owner]]['rows'].append((match,data,attribute,path))
    return groups,summary

def gui_train_inventory(xml,scope=None):
    groups,_=gui_train_groups(xml)
    if not groups:raise B.SaveToolError('Save đang mở chưa có dữ liệu toa tàu theo định dạng editor hỗ trợ.')
    if scope is None:
        if len(groups)>1:raise B.SaveToolError('Có nhiều khối Trains chứa dữ liệu toa tàu; chọn rõ một khối trong GUI để chỉnh sửa.')
        scope=1
    if type(scope) is not int or not 1<=scope<=len(groups):raise B.SaveToolError('Khối Trains đã chọn không hợp lệ; mở lại Train.')
    return groups[scope-1]['rows']

def gui_edit_train_wagons(xml,train_index,wagons,values,scope=None):
    rows=gui_train_inventory(xml,scope)
    if type(train_index) is not int or not 1<=train_index<=len(rows):raise B.SaveToolError('STT tàu không hợp lệ')
    match,data,attribute,path=rows[train_index-1]
    # Delegate all field/range validation and reset rules to the original editor.
    synthetic=b'<root><Trains><Object v="'+B.xml_escape_attribute(json.dumps(data)).encode()+b'"/></Trains></root>'
    edited=B.edit_train_wagons(synthetic,1,wagons,values)
    patched=B.train_inventory(edited)[1][0][1]
    result=B._json_replace_tag(xml,match,patched,attribute)
    B.validate_xml_document(result,'Train GUI result')
    return result


def gui_copy_donor_level(target,donor):
    # Copy the donor's actual XP triplet, rather than keeping the target XP.
    target_global=B.get_direct_child_block(target,"Global");donor_global=B.get_direct_child_block(donor,"Global")
    values={}
    for name in ('levelup','experience','sexpx'):
        matches=B._level_field_tags(donor_global,name)
        if len(matches)!=1:raise B.SaveToolError('Donor cần đúng một trường '+name+' để sao chép Level/XP.')
        attrs=B.parse_attributes(matches[0].group(0));raw=attrs.get('value',attrs.get('v',''))
        maximum=2_147_483_647 if name=='levelup' else 9223372036854775807
        values[name]=B.parse_int(raw,name,1 if name=='levelup' else 0,maximum)
    result=target_global;changes={}
    for name,value in values.items():
        matches=B._level_field_tags(result,name)
        if len(matches)>1:raise B.SaveToolError('Target có trường '+name+' bị trùng.')
        if matches:
            match=matches[0];attrs=B.parse_attributes(match.group(0));attribute='value' if 'value' in attrs else 'v';changes[name]=(attrs.get(attribute),str(value));tag=B.replace_attribute(match.group(0),attribute,str(value));result=result[:match.start()]+tag+result[match.end():]
        else:
            changes[name]=(None,str(value));result=B._advanced_field(result,name,str(value))
    B.validate_xml_document(b'<root>'+result+b'</root>','Clone Level/XP')
    for name,value in values.items():
        attrs=B.parse_attributes(B._level_field_tags(result,name)[0].group(0))
        if attrs.get('value',attrs.get('v'))!=str(value):raise B.SaveToolError('Xác minh Clone '+name+' thất bại.')
    return B.replace_direct_child_block(target,"Global",result),changes

def gui_sync_local_level(local, game):
    level=B.read_township_level(game)
    if len(re.findall(rb'<PushNotifDeviceInfo\b',local))!=1:
        raise B.SaveToolError('Cần đúng một PushNotifDeviceInfo trong LocalInfo để đồng bộ LV; tải lại cặp save qua ADB.')
    updated=B._clone_patch_opening(local,'PushNotifDeviceInfo',{'lvl':str(level)})
    B.validate_xml_document(updated,'Clone: LocalInfo đồng bộ LV')
    if B._clone_tag_attrs(updated,'PushNotifDeviceInfo').get('lvl')!=str(level):
        raise B.SaveToolError('LocalInfo chưa đồng bộ LV; không áp dụng clone.')
    return updated

def gui_preserve_v3_device(target, game, old_local, local):
    fields=('deviceId','advId','Device','OS','GeoIp','Country','DeviceLang','userId','user_id','accountId')
    restored=[]
    for name in fields:
        before=B._level_field_tags(target,name);after=B._level_field_tags(game,name)
        if len(before)>1 or len(after)>1:raise B.SaveToolError('Trường định danh trùng: '+name+'; không áp dụng V3.')
        if before:
            tag=before[0].group(0)
            if after:
                match=after[0];game=game[:match.start()]+tag+game[match.end():]
            else:
                endings=list(re.finditer(rb'</Global\s*>',game,re.I))
                if len(endings)!=1:raise B.SaveToolError('Không xác định Global để giữ '+name)
                pos=endings[0].start();game=game[:pos]+tag+game[pos:]
            restored.append(name)
        elif after:
            match=after[0];game=game[:match.start()]+game[match.end():]
    old_push=B._clone_tag_attrs(old_local,'PushNotifDeviceInfo')
    keys=('advId','deviceToken','deviceType','model','osver','platform','geoip','lang','location','tz')
    local=B._clone_patch_opening(local,'PushNotifDeviceInfo',{key:old_push.get(key,'') for key in keys})
    for name in fields:
        before=B._level_field_tags(target,name);after=B._level_field_tags(game,name)
        if before and (not after or B.parse_attributes(before[0].group(0))!=B.parse_attributes(after[0].group(0))):
            raise B.SaveToolError('V3 làm thay đổi định danh '+name+'; không áp dụng.')
    for name in ('cityId','gameId'):
        expected=B._clone_tag_attrs(old_local,'AWS' if name=='cityId' else 'Version').get(name,'')
        if not expected or B._clone_field_value(game,name)!=expected:raise B.SaveToolError('V3 không giữ đúng '+name)
    B.validate_xml_document(game,'V3 giữ định danh thiết bị');B.validate_xml_document(local,'V3 LocalInfo thiết bị hiện tại')
    B.print('V3 giữ định danh tài khoản và thiết bị hiện tại:',restored)
    return game,local

def gui_check_v3_versions(target, donor):
    current=B._clone_field_value(target,'Version','')
    source=B._clone_field_value(donor,'Version','')
    B.print(f'Phiên bản save V3: hiện tại={current or "thiếu"}; donor={source or "thiếu"}')
    def parts(value):
        if not re.fullmatch(r'\d+(?:\.\d+){1,3}',value):return None
        numbers=tuple(int(part) for part in value.split('.'))
        return numbers+(0,)*(4-len(numbers))
    old,new=parts(current),parts(source)
    if old is None or new is None:
        B.print('Cảnh báo: không xác định được phiên bản save; vẫn tiếp tục V3 với các kiểm tra XML và cặp save.')
        return
    if new>old:
        try:
            result=B.adb('shell','dumpsys','package',B.PACKAGE_NAME,timeout=30)
            versions=re.findall(r'(?m)^\s*versionName=([^\s]+)',result.stdout)
            installed=versions[0] if versions else ''
            app_version=parts(installed)
        except Exception as exc:
            B.print('Cảnh báo: chưa đọc được phiên bản game qua ADB:',str(exc))
            B.print(f'Donor {source} mới hơn save hiện tại {current}; vẫn tiếp tục Clone V3. Game có thể không chấp nhận save này.')
            return
        if app_version is None:
            B.print(f'Cảnh báo: chưa xác định được phiên bản game đang cài; donor {source} mới hơn save hiện tại {current}. Vẫn tiếp tục Clone V3.')
            return
        B.print('Phiên bản Township đang cài trên thiết bị:',installed)
        if new>app_version:
            B.print(f'Cảnh báo: donor V3 dùng {source}, mới hơn game đang cài {installed}. Vẫn tiếp tục clone; game có thể không chấp nhận save này.')
        else:
            B.print('Game đang cài không cũ hơn donor; cho phép V3 dù XML gốc còn ghi phiên bản cũ. Không sửa nhãn phiên bản XML.')

def gui_pair_level_report(game, local, label):
    level=B.read_township_level(game)
    raw=B._clone_tag_attrs(local,'PushNotifDeviceInfo').get('lvl','')
    B.print(f'{label}: mGameInfo.levelup={level}; LocalInfo.PushNotifDeviceInfo.lvl={raw or "thiếu"}')
    if raw!=str(level):raise B.SaveToolError('Level giữa mGameInfo và LocalInfo không khớp; giữ game đóng để kiểm tra.')
    return level

def gui_stage_clone_pair(game, local):
    session=B.SESSION
    templates=session.pending_pair_templates or (session.original_container,session.localinfo_container)
    if any(template is None for template in templates):raise B.SaveToolError('Clone đổi LV cần tải cả mGameInfo và LocalInfo qua ADB.')
    encoded_game=B.encode_save(game,templates[0]);encoded_local=B.encode_save(local,templates[1])
    B.stage_account_pair(encoded_game,encoded_local)

GUI_LV3_TEMPLATE_DATA = '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'

# Automatic new-account workflow: bounded polling, no guessed account IDs.
def gui_newtown_identity(game, local):
    B.validate_xml_document(game,'New Town mGameInfo');B.validate_xml_document(local,'New Town LocalInfo')
    aws=B._clone_tag_attrs(local,'AWS');version=B._clone_tag_attrs(local,'Version')
    city=aws.get('cityId','');gid=version.get('gameId','');token=aws.get('token','')
    if not city or not gid or not token:raise B.SaveToolError('Chưa có đủ City ID, Game ID và token.')
    if B._clone_field_value(game,'cityId')!=city or B._clone_field_value(game,'gameId')!=gid:
        raise B.SaveToolError('Định danh giữa hai file chưa khớp.')
    return city,gid,token

def gui_commit_device_pair(game_raw,local_raw):
    game=B.decode_save(game_raw);local=B.decode_save(local_raw)
    B.validate_xml_document(game,'mGameInfo thiết bị');B.validate_xml_document(local,'LocalInfo thiết bị')
    metadata,friends=B.parse_localinfo_metadata(local)
    for path,data in [(B.SOURCE_FILE,game_raw),(B.LOCALINFO_SOURCE_FILE,local_raw),(B.DECODED_FILE,game),(B.LOCALINFO_DECODED_FILE,local)]:B.atomic_write(path,data)
    s=B.SESSION;s.original_container=game_raw;s.original_xml=game;s.current_xml=game
    s.localinfo_container=local_raw;s.localinfo_xml=local;s.localinfo_meta=metadata;s.friends=friends
    s.pending_localinfo_xml=None;s.pending_pair_templates=None;s.selected_friend=None;s.donor_xml=None;s.donor_path=None
    return game,local

def gui_prepare_lv3_pair(game_raw,local_raw,donor):
    target=B.decode_save(game_raw);old_local=B.decode_save(local_raw)
    identity=gui_newtown_identity(target,old_local)
    if not 1<=B.read_township_level(target)<=3:raise B.SaveToolError('Tài khoản mới không còn ở LV1–3; chưa áp dụng mẫu.')
    if B.read_township_level(donor)!=3:raise B.SaveToolError('Mẫu phải ở LV3.')
    for key in ('Version','FVer'):
        if B._clone_field_value(target,key)!=B._clone_field_value(donor,key):
            raise B.SaveToolError('Mẫu LV3 khác phiên bản tài khoản mới; chọn mẫu cùng phiên bản. Chưa ghi LV3.')
    game,local,report=B.clone_city_v3(target,donor,old_local,True,True)
    game,local=gui_preserve_v3_device(target,game,old_local,local);local=gui_sync_local_level(local,game)
    if gui_newtown_identity(game,local)!=identity:raise B.SaveToolError('Ghép mẫu làm thay đổi định danh.')
    gui_pair_level_report(game,local,'Cặp save LV3 chuẩn bị')
    encoded_game=B.encode_save(game,game_raw);encoded_local=B.encode_save(local,local_raw)
    if B.decode_save(encoded_game)!=B.canonical_xml(game) or B.decode_save(encoded_local)!=B.canonical_xml(local):
        raise B.SaveToolError('Encode/decode mẫu LV3 không khớp.')
    return encoded_game,encoded_local

def gui_agree_point(hierarchy,package):
    """Only return a visible, enabled Agree control belonging to Township."""
    root=B.ET.fromstring(hierarchy)
    labels={'agree','i agree','đồng ý','tôi đồng ý'}
    parents={child:node for node in root.iter() for child in node}
    for node in root.iter('node'):
        text=(node.get('text','') or node.get('content-desc','')).strip().casefold()
        if text not in labels or node.get('package')!=package or node.get('enabled')!='true':continue
        button=node
        while button.get('clickable')!='true' and button in parents:button=parents[button]
        if button.get('package')!=package or button.get('enabled')!='true' or button.get('clickable')!='true':continue
        match=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',button.get('bounds',''))
        if match:
            x1,y1,x2,y2=map(int,match.groups())
            if x2>x1 and y2>y1:return ((x1+x2)//2,(y1+y2)//2)
    return None

def gui_try_agree():
    path='/sdcard/ts_studio_agree.xml'
    try:
        B.adb('shell','rm','-f',path,timeout=10)
        B.adb('shell','uiautomator','dump',path,timeout=15)
        result=B.adb('shell','cat',path,timeout=10)
        start=result.stdout.find('<?xml')
        if start<0:start=result.stdout.find('<hierarchy')
        if start<0:return False
        point=gui_agree_point(result.stdout[start:],B.PACKAGE_NAME)
        if point is None:return False
        B.adb('shell','input','tap',str(point[0]),str(point[1]),timeout=10)
        return True
    except Exception:return False
    finally:
        try:B.adb('shell','rm','-f',path,timeout=10,check=False)
        except Exception:pass

def gui_wait_newtown_identity(excluded,timeout,cancelled,try_agree=True,agree_xy=None):
    deadline=B.time.monotonic()+timeout;previous=None;last_ui=0;ui_attempts=0;coordinate_used=False;last_progress=-30;last_error='chưa có save mới'
    while B.time.monotonic()<deadline:
        if cancelled():raise Cancelled()
        try:
            g=B._clone_read_remote(B.REMOTE_SAVE,'newtown_poll_game');l=B._clone_read_remote(B.REMOTE_LOCALINFO,'newtown_poll_local')
            gx=B.decode_save(g);lx=B.decode_save(l);identity=gui_newtown_identity(gx,lx)
            if identity[0] not in excluded and 1<=B.read_township_level(gx)<=3:
                if identity==previous:return identity,g,l
                previous=identity
            else:previous=None;last_error='game vẫn ghi định danh cũ hoặc mẫu reset'
        except Cancelled:raise
        except Exception:previous=None;last_error='đang chờ cặp save hợp lệ'
        now=B.time.monotonic()
        if try_agree and ui_attempts<2 and now-last_ui>=10:
            if gui_try_agree():ui_attempts+=1;B.print('Đã nhận diện và bấm Agree của Township.')
            elif agree_xy is not None and not coordinate_used:
                # Coordinate is supplied explicitly by the user, never guessed.
                foreground=B.adb('shell','dumpsys','window','windows',timeout=15,check=False).stdout
                if re.search(r'm(?:CurrentFocus|FocusedApp)[^\n]*'+re.escape(B.PACKAGE_NAME)+r'/',foreground):
                    B.adb('shell','input','tap',str(agree_xy[0]),str(agree_xy[1]),timeout=10);coordinate_used=True
                    B.print('Đã bấm vị trí Agree do bạn cấu hình.')
            last_ui=now
        remaining=max(0,int(deadline-B.time.monotonic()))
        if last_progress-remaining>=15 or last_progress<0:
            B.print(f'Chờ định danh mới: còn khoảng {remaining} giây. Nếu Agree không nhận diện được, bấm Agree trong giả lập; chương trình sẽ tự tiếp tục.');last_progress=remaining
        # Frequent cancellation checks, without a long blocking wait.
        for _ in range(10):
            if cancelled():raise Cancelled()
            B.time.sleep(0.2)
    raise B.SaveToolError(f'Hết thời gian chờ định danh mới ({last_error}). Chưa ghép LV3. Mở game, bấm Agree nếu cần rồi dùng chế độ tiếp tục; không reset lần nữa.')


# Native source preview and selective Clone V1 (v1.39).
DESIGN_GROUPS = {
    '🏙 Bố cục thành phố': ['city', 'IslandsInfo', 'decor'],
    '🦁 Sở thú / Bảo tàng': ['zoo', 'ArtInfo'],
    '🎨 Trang trí / Hồ sơ': ['skins', 'stickers', 'badges', 'titles', 'frames', 'styles', 'avatars'],
    '📊 Thống kê / Tùy chọn': ['stats', 'airscore', 'ccsecrets'],
}
DESIGN_LABELS = {
    'city': 'Đất và công trình thành phố', 'IslandsInfo': 'Đảo / IslandsInfo',
    'decor': 'Kho Decoration', 'zoo': 'Zoo / ZooInfo / ZooQuests',
    'ArtInfo': 'Bảo tàng / ArtInfo', 'skins': 'Skin', 'stickers': 'Stickers',
    'badges': 'Huy hiệu', 'titles': 'Danh hiệu', 'frames': 'Khung', 'styles': 'Phong cách',
    'avatars': 'Avatar', 'stats': 'Stats / Level / kho / M3',
    'airscore': 'AirScore / AirInfo (kèm Stats)', 'ccsecrets': 'Xóa CCSecret',
}
DESIGN_BLOCKS = {'IslandsInfo': 'IslandsInfo', 'ArtInfo': 'ArtInfo',
                 'skins': 'Skins', 'decor': 'BuildingsStash', 'stickers': 'FragmentedBeautyManager'}
DESIGN_PROFILE = {'badges': 'UnlockedBadges', 'titles': 'UnlockedExpRanks',
                  'frames': 'UnlockedFrames', 'styles': 'UnlockedStyles'}

def gui_design_metadata(xml):
    root = B.validate_xml_document(xml, 'Nguồn Clone V1')
    if root.tag != 'root': raise B.SaveToolError('Nguồn Clone V1 cần có phần tử root.')
    return {'name': B._clone_field_value(xml, 'townName', 'Chưa có tên'),
            'city_id': B._clone_field_value(xml, 'cityId', ''),
            'level': B._clone_field_value(xml, 'levelup', ''),
            'version': B._clone_field_value(xml, 'Version', '')}

from functools import lru_cache

@lru_cache(maxsize=4)
def gui_design_spans(xml):
    spans = {}
    for span in B.direct_child_spans(xml):spans.setdefault(span.tag,[]).append(span)
    return spans

def gui_design_block(xml, name):
    matches = gui_design_spans(xml).get(name,[])
    if len(matches)>1:raise B.SaveToolError('Khối root bị trùng: '+name)
    span = matches[0] if matches else None
    return xml[span.start:span.end] if span else None

def gui_design_availability(donor, target):
    root = B.validate_xml_document(donor, 'Nguồn bố cục')
    B.validate_xml_document(target, 'Save hiện tại')
    available = {}; reasons = {}
    ground = gui_design_block(donor, 'TownGround')
    buildings = gui_design_block(donor, 'Buildings')
    city_ok = ground is not None and (buildings is not None or B.ET.fromstring(ground).find('Buildings') is not None)
    available['city'] = city_ok
    reasons['city'] = 'Có đất + công trình' if city_ok else 'Nguồn thiếu TownGround hoặc Buildings'
    for key, name in DESIGN_BLOCKS.items():
        available[key] = gui_design_block(donor, name) is not None
        reasons[key] = 'Có '+name if available[key] else 'Nguồn chưa có '+name
    zoo = gui_design_block(donor, 'Zoo')
    zoo_info = gui_design_block(donor, 'ZooInfo')
    available['zoo'] = zoo is not None and (gui_design_block(target, 'ZooInfo') is None or zoo_info is not None)
    reasons['zoo'] = ' + '.join(n for n in ('Zoo','ZooInfo','ZooQuests') if gui_design_block(donor,n) is not None) if available['zoo'] else 'Nguồn thiếu Zoo hoặc ZooInfo cần thiết'
    for key, name in DESIGN_PROFILE.items():
        source = [m for m in B._level_field_tags(donor,name) if m.group(0).startswith(b'<DataElem')]
        existing = [m for m in B._level_field_tags(target,name) if m.group(0).startswith(b'<DataElem')]
        anchors = [m for m in B._level_field_tags(target,'UnlockedAvatars') if m.group(0).startswith(b'<DataElem')]
        if len(source)>1 or len(existing)>1:raise B.SaveToolError('Trường hồ sơ bị trùng: '+name)
        available[key] = len(source)==1 and (len(existing)==1 or len(anchors)==1)
        reasons[key] = 'Có '+name if available[key] else 'Thiếu dữ liệu nguồn hoặc vị trí hồ sơ đích'
    level_fields=all(len(B._level_field_tags(gui_design_block(donor,'Global') or b'',k))==1 for k in ('levelup','experience','sexpx'))
    available['stats']=gui_design_block(donor,'Global') is not None and level_fields
    reasons['stats']='Có Global và bộ Level/XP' if available['stats'] else 'Nguồn thiếu Global hoặc Level/XP'
    available['airscore']=available['stats'] and (gui_design_block(donor,'AirInfo') is not None or bool(B._level_field_tags(donor,'AirScore')))
    reasons['airscore']='Dùng cùng Stats theo xử lý V1 hiện tại' if available['airscore'] else 'Nguồn thiếu dữ liệu AirScore / AirInfo'
    available['avatars']=bool(re.search(rb'name=["\']Unlocked_ava\d+["\']',donor))
    reasons['avatars']='Có cờ Avatar' if available['avatars'] else 'Nguồn chưa có cờ Avatar'
    available['ccsecrets']=True;reasons['ccsecrets']='Xóa CCSecret trong tài khoản hiện tại'
    return available, reasons

def gui_design_version_check(target, donor):
    current = gui_design_metadata(target)['version']; source = gui_design_metadata(donor)['version']
    if current != source or not current:
        return f'Phiên bản nguồn: {source or "chưa xác định"}; hiện tại: {current or "chưa xác định"}. Cần kiểm tra kết quả trong game.'
    return ''

def gui_clone_v1(target,donor,selection,copy_level):
    selection=list(dict.fromkeys(selection))
    if not selection or set(selection)-set(DESIGN_LABELS):raise B.SaveToolError('Chọn ít nhất một mục Clone V1 hợp lệ.')
    available,_=gui_design_availability(donor,target)
    missing=[DESIGN_LABELS[k] for k in selection if not available[k]]
    if missing:raise B.SaveToolError('Nguồn không đủ dữ liệu: '+', '.join(missing))
    if 'airscore' in selection and 'stats' not in selection:raise B.SaveToolError('AirScore / AirInfo hiện dùng cùng Stats trong V1. Chọn thêm Stats hoặc bỏ chọn AirScore.')
    extra={'IslandsInfo','ArtInfo'};base=[k for k in selection if k not in extra]
    result,report=B.clone_city_v1(target,donor,base) if base else (target,[])
    donor_id=B._clone_field_value(donor,'cityId');target_id=B._clone_field_value(target,'cityId')
    if not target_id:raise B.SaveToolError('Save hiện tại thiếu City ID; chưa áp dụng Clone V1.')
    for key in selection:
        if key not in extra:continue
        block=gui_design_block(donor,key)
        if donor_id and donor_id!=target_id:
            block=re.sub(rb'<[A-Za-z_][\w:.-]*\b[^>]*>',lambda m:B.replace_attribute(m.group(0),'user',target_id)
                         if B.html.unescape(B.parse_attributes(m.group(0)).get('user',''))==donor_id else m.group(0),block)
        result=B._clone_upsert_root_block(result,key,block);report.append(key)
    sync_level=bool(copy_level or 'stats' in selection)
    if sync_level:
        result,changes=gui_copy_donor_level(result,donor);report.append('Level/XP từ donor: '+str(changes))
    protected=['cityId','gameId','userId','user_id','accountId','PromoCode','token','deviceId','advId','Version','FVer']
    if not sync_level:protected+=['levelup','experience','sexpx']
    if 'stats' not in selection:protected+=['money','moneyCash','GHash']
    for name in protected:
        if [m.group(0) for m in B._level_field_tags(target,name)]!=[m.group(0) for m in B._level_field_tags(result,name)]:
            raise B.SaveToolError('Clone V1 làm thay đổi trường cần giữ: '+name+'; chưa áp dụng.')
    B.validate_xml_document(result,'Clone V1 sau khi ghép')
    return result,report,sync_level

def gui_read_design_source(path):
    path = Path(path)
    if path.suffix.lower()=='.zip':
        game,_,_,_ = B.read_account_backup(path);return B.decode_save(game)
    if path.stat().st_size>B.MAX_XML_SIZE:raise B.SaveToolError('File mẫu vượt giới hạn 32 MB.')
    raw = path.read_bytes()
    xml = B.decode_save(raw)
    gui_design_metadata(xml)
    return xml

class CloneV1Dialog(NativeDialog):
    def __init__(self, owner, donor=None):
        super().__init__('🏙 Clone City V1',owner,'Tải nguồn để xem các phần có thể sao chép, rồi chọn những phần muốn áp dụng.')
        self.owner = owner;self.target = B.SESSION.current_xml;self.donor = None;self.worker = None;self.picker = None;self.load_error = '';self.fixed_source = donor is not None
        self.source = DonorSource();self.body.addWidget(self.source)
        self.load_button = QPushButton('📥 Tải nguồn và xem danh sách');self.load_button.clicked.connect(self.load_source);self.body.addWidget(self.load_button)
        self.source_toggle=QPushButton('Đổi nguồn / tải lại…');self.source_toggle.clicked.connect(self.toggle_source);self.source_toggle.hide();self.body.addWidget(self.source_toggle)
        self.info = QLabel('Chưa tải nguồn.');self.info.setWordWrap(True);self.body.addWidget(self.info)
        self.preview = QStackedWidget();self.preview.addWidget(QLabel('Danh sách các phần sẽ xuất hiện sau khi tải nguồn.'));self.body.addWidget(self.preview,1)
        self.copy_level=QCheckBox('Lấy Level + XP từ donor và đồng bộ LocalInfo (cho phép giảm LV)');self.copy_level.setChecked(True);self.body.addWidget(self.copy_level)
        self.footer.setText('Giữ City ID và thông tin tài khoản hiện tại. Muốn giữ LV/XP: bỏ chọn lấy Level và không chọn Stats. Stats vẫn lấy LV/XP như V1 trước đây.')
        self.buttons.button(QDialogButtonBox.Apply).setEnabled(False);self.validator = self.validate_selection
        decorate(self)
        self.source.kind.currentIndexChanged.connect(self.invalidate)
        for edit in (self.source.path,self.source.city,self.source.bver,self.source.fver):edit.textChanged.connect(self.invalidate)
        self.source.friend.currentIndexChanged.connect(self.invalidate)
        if donor is not None:
            self.source.hide();self.load_button.hide();self.show_donor(donor)
        elif B.SESSION.donor_xml is None and not B.DONOR_FILE.is_file():self.source.kind.setCurrentIndex(self.source.kind.findData('file'))
    def toggle_source(self):
        visible=not self.source.isVisible();self.source.setVisible(visible);self.load_button.setVisible(visible)
        self.source_toggle.setText('Thu gọn nguồn' if visible else 'Đổi nguồn / tải lại…')
    def invalidate(self,*_):
        self.donor=None;self.buttons.button(QDialogButtonBox.Apply).setEnabled(False);self.preview.setCurrentIndex(0);self.info.setText('Nguồn đã đổi. Nhấn Tải nguồn để cập nhật danh sách.')
    def load_source(self):
        if self.worker is not None:return
        try:data = self.source.data()
        except (OSError,B.SaveToolError) as exc:QMessageBox.warning(self,'Nguồn bố cục',str(exc));return
        self.invalidate();self.load_error='';self.source.setEnabled(False);self.load_button.setEnabled(False);self.info.setText('Đang tải nguồn…');result={}
        def load():
            if data[0] in ('file','zip'):result['xml']=gui_read_design_source(data[1])
            else:result['xml']=DonorSource.load(data)
        self.worker = Worker(load);self.worker.output.connect(self.owner.append)
        def done(status,error):
            if status=='ok':
                try:self.show_donor(result['xml'])
                except Exception as exc:self.load_error=str(exc)
            else:self.load_error=error or 'Đã hủy tải nguồn.'
        self.worker.done.connect(done);self.worker.finished.connect(self.loaded);self.worker.start()
    def loaded(self):
        worker=self.worker;self.worker=None;worker.deleteLater();self.source.setEnabled(True);self.load_button.setEnabled(True)
        if self.load_error:self.info.setText(self.load_error);QMessageBox.warning(self,'Không tải được nguồn',self.load_error)
        elif self.donor is not None:
            B.SESSION.donor_xml=self.donor
            if self.source.kind.currentData() in ('file','zip'):B.SESSION.donor_path=Path(self.source.path.text())
    def show_donor(self,donor):
        available,reasons=gui_design_availability(donor,self.target)
        source=gui_design_metadata(donor);target=gui_design_metadata(self.target)
        version_note='';compatible=True
        try:version_note=gui_design_version_check(self.target,donor)
        except B.SaveToolError as exc:version_note=str(exc);compatible=False
        self.info.setText(f'Nguồn: {source["name"]} · City ID: {source["city_id"] or "—"} · LV {source["level"] or "—"} · {source["version"] or "—"}\nHiện tại: {target["name"]} · City ID: {target["city_id"] or "—"} · LV {target["level"] or "—"}'+('\n'+version_note if version_note else ''))
        picker=ItemPicker(DESIGN_GROUPS,labels=DESIGN_LABELS,current=reasons,disabled=[k for k,v in available.items() if not v])
        while self.preview.count()>1:
            widget=self.preview.widget(1);self.preview.removeWidget(widget);widget.deleteLater()
        picker.tree.headerItem().setText(2,'Dữ liệu nguồn')
        for group,item in picker.groups.items():
            symbol,title=split_icon(group)
            if symbol:item.setText(0,f'{title} ({item.childCount()})');item.setIcon(0,native_icon(symbol))
        for (_,key),item in picker.rows.items():item.setToolTip(0,reasons[key])
        self.preview.addWidget(picker);self.preview.setCurrentWidget(picker);self.picker=picker;self.donor=donor
        self.buttons.button(QDialogButtonBox.Apply).setEnabled(compatible and any(available.values()))
        level_ok=all(len(B._level_field_tags(gui_design_block(donor,'Global') or b'',k))==1 for k in ('levelup','experience','sexpx'))
        self.copy_level.setEnabled(level_ok)
        if not level_ok:self.copy_level.setChecked(False)
        if not self.fixed_source:
            self.source.hide();self.load_button.hide();self.source_toggle.show();self.source_toggle.setText('Đổi nguồn / tải lại…')
    def validate_selection(self):
        if self.worker is not None:raise B.SaveToolError('Đợi tải nguồn hoàn tất.')
        if self.donor is None:raise B.SaveToolError('Tải nguồn trước khi áp dụng.')
        self.picker.require()
        if 'airscore' in self.picker.ids() and 'stats' not in self.picker.ids():raise B.SaveToolError('Chọn Stats cùng AirScore / AirInfo, hoặc bỏ chọn AirScore.')
        if self.copy_level.isChecked() or 'stats' in self.picker.ids():gui_copy_donor_level(self.target,self.donor)
    def reject(self):
        if self.worker is not None:
            QMessageBox.information(self,'Đang tải nguồn','Đợi yêu cầu tải nguồn hoàn tất trước khi đóng.');return
        super().reject()
    def closeEvent(self,event):
        if self.worker is not None:event.ignore();self.reject()
        else:super().closeEvent(event)

class NativeWindow(Window):
    def __init__(self):
        super().__init__();self.setWindowTitle('TS Studio • v1.39')
        self.stop_scan=QPushButton('Dừng quét');self.stop_scan.clicked.connect(self.stop_network);self.centralWidget().layout().addWidget(self.stop_scan);self.stop_scan.hide()
        for button in self.controls.findChildren(QPushButton):
            if 'Mở LocalInfo' in button.text():button.clicked.disconnect();button.clicked.connect(self.open_localinfo)
            elif 'Ghi vào game' in button.text():button.clicked.disconnect();button.clicked.connect(self.write_game)
            elif 'Hoàn tác' in button.text():button.clicked.disconnect();button.clicked.connect(self.undo_native)
        self.update_connection_controls()
    def start(self,action,name):
        super().start(action,name)
        if hasattr(self,'stop_scan'):
            self.stop_scan.setText('Dừng quét');self.stop_scan.setEnabled(True);self.stop_scan.setText('Dừng tạo mới' if name=='New TownCity · tự động LV3' else 'Dừng quét');self.stop_scan.setVisible(name in ('Friend Network','New TownCity · tự động LV3'))
    def stop_network(self):
        if self.worker is not None and self.current_action in ('Friend Network','New TownCity · tự động LV3'):
            self.worker.cancelled=True;self.stop_scan.setEnabled(False);self.stop_scan.setText('Đang đợi request hiện tại kết thúc…')
    def thread_finished(self):
        super().thread_finished()
        if hasattr(self,'stop_scan'):self.stop_scan.hide()
    def make_cards(self,entries):
        widget=super().make_cards(entries)
        direct={'museum_prompt':B.unlock_museum,'all_cards':lambda xml:B.update_owned_cards(xml,True),
                'my_cards':lambda xml:B.update_owned_cards(xml,False),'golden_pass_prompt':B.unlock_golden_pass,
                'land_prompt':B.unlock_land}
        for button,entry in zip(self.action_buttons[-len(entries):],entries):
            button.clicked.disconnect()
            function,name=entry[3],entry[1]
            if function in direct:
                button.setText('Apply '+name+'  ✓');button.setObjectName('primary')
                button.clicked.connect(lambda _,fn=direct[function],n=name:self.apply_direct(fn,n))
            else:button.clicked.connect(lambda _,fn=function,n=name:self.open_editor(fn,n))
        return widget
    def apply_direct(self,fn,name):
        if self.worker is not None:return
        if not B.SESSION.loaded:
            QMessageBox.information(self,name,'Mở save hoặc kết nối ADB trước khi Apply.');return
        self.run_edit(lambda:fn(B.SESSION.current_xml),name)
    def run_edit(self,fn,name):self.start(lambda:apply_result(fn()),name)
    def open_editor(self,function,name):
        if self.worker is not None:return
        try:
            if function not in ('backup_prompt','history_prompt','encode_file_prompt','decode_file_prompt'):B.SESSION.require_loaded()
            handlers={
                'decoration_prompt':self.decorations,'unlock_all_avatars_prompt':self.avatars,
                'skin':lambda:self.catalog('skin'),'stickers':lambda:self.catalog('stickers'),
                'profile':lambda:self.catalog('profile'),'achievements':lambda:self.catalog('achievements'),
                'barn_prompt':self.barn,'academy_prompt':self.academy,'zoo_cards_prompt':self.zoo,
                'advantages_prompt':self.advantages,'quantities_prompt':self.quantities,
                'market_prompt':self.market,'golden_pass_editor_prompt':self.pass_editor,
                'train_prompt':self.trains,'regatta_tasks_prompt':self.regatta,
                'encode_file_prompt':lambda:self.file_codec(True),'decode_file_prompt':lambda:self.file_codec(False),
                'tutorial_fix_prompt':self.tutorial,'clone_city_v1_prompt':lambda:self.clone(1),
                'clone_city_v3_prompt':lambda:self.clone(3),'send_card_prompt':self.send_card,
                'backup_prompt':self.backup,'history_prompt':self.history,'new_towncity_prompt':self.new_town,
                'land_prompt':lambda:self.simple('Land','Mở đất; xóa các đối tượng expandBuy theo logic bản gốc.',B.unlock_land),
                'museum_prompt':lambda:self.simple('Museum','Hoàn thành các cổ vật theo danh sách trong file gốc.',B.unlock_museum),
                'golden_pass_prompt':lambda:self.simple('Golden Pass','Mở Golden Pass trong save đang chỉnh sửa.',B.unlock_golden_pass),
                'all_cards':lambda:self.simple('All Cards','Cập nhật toàn bộ thẻ theo logic gốc.',lambda xml:B.update_owned_cards(xml,True)),
                'my_cards':lambda:self.simple('My Cards','Chỉ cập nhật những thẻ đang sở hữu.',lambda xml:B.update_owned_cards(xml,False))}
            handlers[function]()
        except Exception as exc:QMessageBox.warning(self,name,str(exc))
    def simple(self,title,desc,fn):
        dialog=NativeDialog(title,self,desc);dialog.resize(600,260);dialog.body.addWidget(QLabel('Nhấn Áp dụng để thực hiện chức năng này.'))
        if dialog.exec_()==QDialog.Accepted:self.run_edit(lambda:fn(B.SESSION.current_xml),title)
    def decorations(self):
        inventory=B.decoration_inventory(B.SESSION.current_xml)
        inventory={item:inventory.get(item,0) for items in B.DECORATION_GROUPS.values() for item in items}
        names={'normal':'Đồ trang trí thường','special':'Merge / Expedition','sign':'Biển tên thành phố'}
        groups={names[k]:v for k,v in B.DECORATION_GROUPS.items()}
        dialog=NativeDialog('Decorations',self,'Chỉnh Current cho từng Decor. Mục đã chọn chưa sửa riêng dùng Số lượng mỗi món khi Áp dụng.');picker=DecorationPicker(groups,inventory);dialog.body.addWidget(picker,1)
        form=dialog.form();count=number(1,1,20);form.addRow('Số lượng mỗi món',count)
        bulk=QPushButton('Đặt số lượng cho mục đã chọn');bulk.clicked.connect(lambda:picker.set_selected_quantity(count.value()));dialog.body.addWidget(bulk)
        detail=QLabel('Số lượng riêng: 0–20 (0 xóa số lượng trong kho). Biển tên luôn là 1. Merge / Expedition được hoàn thành theo logic gốc. Các dòng không chọn giữ nguyên.');detail.setWordWrap(True);detail.setObjectName('muted');dialog.body.addWidget(detail)
        dialog.validator=lambda:picker.quantities(count.value())
        if dialog.exec_()==QDialog.Accepted:
            quantities=picker.quantities(count.value());self.run_edit(lambda:gui_set_decoration_quantities(B.SESSION.current_xml,quantities),'Decorations · '+str(len(quantities))+' món')
    def avatars(self):
        states=B.avatar_states(B.SESSION.current_xml)
        initial={('Avatar',key):value['state'] is True for key,value in states.items()}
        unsupported={key for key,value in states.items() if value['state'] is not None and type(value['state']) is not bool}
        dialog=NativeDialog('Avatar',self,'Tick để mở, bỏ tick để khóa. Checkbox thể hiện trạng thái hiện tại; chỉ các mục thay đổi được áp dụng khi bấm Apply.')
        picker=UnlockStatePicker({'Avatar':list(states)},initial,labels={key:'Avatar '+key for key in states},disabled=unsupported);dialog.body.addWidget(picker,1);bind_unlock_apply(dialog,picker)
        for key in unsupported:picker.rows[('Avatar',key)].setToolTip(0,'Unsupported avatar flag value; this item cannot be changed.')
        if dialog.exec_()==QDialog.Accepted:
            changes={key:value for (_,key),value in picker.changes().items()}
            if changes:self.run_edit(lambda:gui_set_avatar_states(B.SESSION.current_xml,changes),'Avatar')
    def catalog(self,kind):
        catalogs={'skin':B.TSVIP_SKINS,'stickers':B.TSVIP_STICKERS,'profile':B.TSVIP_PROFILE,'achievements':{'Achievements':tuple(B.TSVIP_ACHIEVEMENTS)}}
        original=catalogs[kind];groups={B.PROFILE_GROUP_LABELS.get(key,key):value for key,value in original.items()};reverse={B.PROFILE_GROUP_LABELS.get(key,key):key for key in original}
        initial={};labels={}
        for group,ids in original.items():
            display=B.PROFILE_GROUP_LABELS.get(group,group);states=B.unlock_catalog_states(B.SESSION.current_xml,kind,group,ids)
            for index,item in enumerate(ids):
                initial[(display,str(item))]=states[item]
                if kind=='stickers' and str(item) in STICKER_VI_LABELS:labels[(display,str(item))]=STICKER_VI_LABELS[str(item)]
                names=B.PROFILE_ITEM_LABELS.get(group,()) if kind=='profile' else ()
                if index<len(names):labels[(display,str(item))]=names[index]
        desc='Tick để mở, bỏ tick để khóa. Checkbox thể hiện trạng thái hiện tại; chỉ các mục thay đổi được áp dụng khi bấm Apply.'
        if kind=='achievements':desc+=' Bỏ tick Achievement chỉ gỡ cờ mở/nhận thưởng, giữ bộ đếm tiến độ.'
        dialog=NativeDialog({'skin':'Skin','stickers':'Stickers','profile':'Profiles','achievements':'Achievements'}[kind],self,desc)
        picker=UnlockStatePicker(groups,initial,labels=labels);dialog.body.addWidget(picker,1);bind_unlock_apply(dialog,picker)
        if dialog.exec_()==QDialog.Accepted:
            changes={}
            for (group,key),value in picker.changes().items():changes.setdefault(reverse[group],{})[key]=value
            if changes:self.run_edit(lambda:gui_set_catalog_states(B.SESSION.current_xml,kind,changes),dialog.windowTitle())
    def bulk_value_row(self,dialog,picker,label='Giá trị cho các mục đã chọn',minimum=0,maximum=2147483647,default=0):
        row=QHBoxLayout();row.addWidget(QLabel(label));spin=number(default,minimum,maximum);row.addWidget(spin);button=QPushButton('Đặt cho mục đã chọn');button.clicked.connect(lambda:picker.set_all_values(spin.value()));row.addWidget(button);dialog.body.addLayout(row)
    def bulk_value_row_for_layout(self,layout,picker,label,minimum,maximum,default):
        row=QHBoxLayout();row.addWidget(QLabel(label));spin=number(default,minimum,maximum);row.addWidget(spin);button=QPushButton('Đặt cho mục đã chọn');button.clicked.connect(lambda:picker.set_all_values(spin.value()));row.addWidget(button);layout.addLayout(row)
    def barn(self):
        xml=B.SESSION.current_xml;dialog=NativeDialog('Barn',self,'Sửa cấp kho hoặc sản phẩm. Tab Sản phẩm chỉ áp dụng các dòng đã chọn có số lượng mới khác hiện tại.');tabs=QTabWidget();dialog.body.addWidget(tabs,1)
        levelpage=QWidget();form=QFormLayout(levelpage);level=number(int(B._advanced_read(xml,'WareHouseCashUpgrade') or 0));form.addRow('Cấp kho',level);capacity=QLabel();form.addRow('Sức chứa cơ bản',capacity);level.valueChanged.connect(lambda v:capacity.setText(str(B.barn_capacity(v))));capacity.setText(str(B.barn_capacity(level.value())));tabs.addTab(levelpage,'Cấp kho')
        products=B.TSVIP_BARN_PRODUCTS;current={k:B._advanced_read(xml,B.barn_product_field(k)) or '0' for k in products}
        picker=BarnPicker(barn_groups(products),current={k:int(v) for k,v in current.items()});tabs.addTab(picker,'Sản phẩm')
        self.bulk_value_row(dialog,picker,'Số lượng cho các dòng đã chọn')
        dialog.validator=lambda:picker.require_changes() if tabs.currentIndex()==1 else None
        if dialog.exec_()==QDialog.Accepted:
            if tabs.currentIndex()==0:
                value=level.value();self.run_edit(lambda:B.set_barn_level(B.SESSION.current_xml,value),'Barn · cấp kho')
            else:
                values=picker.changed_values()
                def patch():
                    result=B.SESSION.current_xml;buckets={}
                    for k,v in values.items():buckets.setdefault(v,[]).append(k)
                    for v,ids in buckets.items():result=B.set_barn_products(result,ids,v)
                    return result
                self.run_edit(patch,'Barn · sản phẩm')
    def academy(self):
        xml=B.SESSION.current_xml;dialog=NativeDialog('Academi',self,'Chỉnh từng dòng trong Industries, Trains hoặc Islands. Apply dùng mức nâng cấp của mẫu TSVIP và các bonus trong bảng.');dialog.resize(1060,820)
        tabs=QTabWidget();dialog.body.addWidget(tabs,1);upgrades=AcademyUpgradePage(xml);tabs.addTab(upgrades,'Cấp / Bonus')
        slots=gui_factory_slots_page(xml);tabs.addTab(slots,'Ô sản xuất nhà máy');self.bulk_value_row_for_layout(slots.layout(),slots,'Số ô cho nhà máy đã chọn',2,7,7)
        dialog.validator=lambda:upgrades.require() if tabs.currentIndex()==0 else slots.require_slot_changes()
        if dialog.exec_()==QDialog.Accepted:
            if tabs.currentIndex()==1:
                changes=slots.slot_changes();self.run_edit(lambda:gui_set_factory_slots(B.SESSION.current_xml,changes),'Academi · ô sản xuất nhà máy');return
            selection=upgrades.selected_rows();self.run_edit(lambda:gui_set_academy_rows(B.SESSION.current_xml,selection),'Academi · Cấp / Bonus')
    def zoo(self):
        _,data=B.zoo_card_inventory(B.SESSION.current_xml);present={v['type']:v for v in data['list'] if isinstance(v,dict) and 'type' in v};current={}
        for key in B.TSVIP_ZOO_ANIMALS:
            current[key]=', '.join(f'{v.get("piecesCount",0)}/30 · trạng thái {v.get("status",0)}' for v in present.get(key,{}).get('members',[]) if isinstance(v,dict)) if key in present else 'Chưa có chuồng'
        dialog=NativeDialog('Zoo Card',self,'Hoàn thành thẻ của các loài được chọn (30 mảnh, status=3). Chuồng chưa có trong save sẽ bị vô hiệu hóa.');picker=ItemPicker({'Động vật':list(B.TSVIP_ZOO_ANIMALS)},labels=B.TSVIP_ZOO_ANIMALS,current=current,disabled=set(B.TSVIP_ZOO_ANIMALS)-set(present));dialog.body.addWidget(picker,1);dialog.validator=picker.require
        if dialog.exec_()==QDialog.Accepted:
            ids=picker.ids();self.run_edit(lambda:B.set_zoo_cards(B.SESSION.current_xml,ids),'Zoo Card')
    def advantages(self):
        xml=B.SESSION.current_xml;season=B._advanced_block(xml,'SeasonTicket');current={}
        for key in B.TSVIP_ADVANTAGES:
            tags=B._level_field_tags(season,key);current[key]=B.parse_attributes(tags[0].group(0)).get('v','0') if len(tags)==1 else '0'
            if key=='SP_BoostMineRocket':current[key]=B._advanced_read(xml,'DiggingPremiumLevel') or '0'
        dialog=NativeDialog('Advantages',self,'Đánh dấu bonus cần sửa; giá trị 0 tắt bonus. Các giá trị đề xuất lấy từ TSVIP.');picker=ItemPicker({'Bonus Golden Pass':list(B.TSVIP_ADVANTAGES)},current=current,values=True,defaults=B.TSVIP_ADVANTAGES);dialog.body.addWidget(picker,1);form=dialog.form();minecheck,days=optional_field(form,'Mine x2 · số ngày',number(0,0,36500));self.bulk_value_row(dialog,picker)
        def validate():
            if not picker.ids() and not minecheck.isChecked():raise B.SaveToolError('Chọn bonus hoặc bật sửa Mine x2.')
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            values=picker.values();mine=days.value() if minecheck.isChecked() else None;self.run_edit(lambda:B.set_advantages(B.SESSION.current_xml,values,mine),'Advantages')
    def quantities(self):
        xml=B.SESSION.current_xml;groups={'Booster / Lab / Mỏ / Quặng':list(B.TSVIP_QUANTITIES),'Coupons':B.TSVIP_COUPONS,'Thời gian boost':['lives_inf_days','booster2x_days'],'Token / Star / M3 moves':['currency_provider_amount','train_journey_amount','star','match3_moves']};current={}
        for key in B.TSVIP_QUANTITIES:current[key]=B._advanced_read(xml,B.TSVIP_QUANTITIES[key][0]) or '0'
        dialog=NativeDialog('Quantities',self,'Sửa số lượng từng mục trong cột Giá trị mới, hoặc đặt cùng một giá trị cho các mục đã chọn.');picker=ItemPicker(groups,labels=B.TSVIP_QUANTITY_LABELS,current=current,values=True,defaults={k:int(v) for k,v in current.items()});dialog.body.addWidget(picker,1)
        for key,spin in picker.spinboxes.items():
            if key[1].endswith('_days'):spin.setMaximum(36500)
        self.bulk_value_row(dialog,picker);dialog.validator=picker.require
        if dialog.exec_()==QDialog.Accepted:
            values=picker.values();self.run_edit(lambda:B.set_quantities(B.SESSION.current_xml,values),'Quantities')
    def market(self):
        rows=[d for _,d in B._json_attribute_rows(B.SESSION.current_xml) if d.get('storeId')=='citymarket' and 'slotsCount' in d]
        if len(rows)!=1:raise B.SaveToolError('Cần một Object citymarket có slotsCount.')
        dialog=NativeDialog('Market',self,'Chỉnh số ô chợ: 1–9999.');dialog.resize(600,280);form=dialog.form();count=number(rows[0]['slotsCount'],1,9999);form.addRow('Số ô chợ',count)
        if dialog.exec_()==QDialog.Accepted:
            value=count.value();self.run_edit(lambda:B.set_market_slots(B.SESSION.current_xml,value),'Market')
    def pass_editor(self):
        xml=B.SESSION.current_xml;season=B._advanced_block(xml,'SeasonTicket');attrs=B.parse_attributes(season.split(b'>',1)[0]+b'>')
        dialog=NativeDialog('Golden Pass Editor',self,'Edit each Stage: Claim, reward product and quantity. Chest products are configured separately for each Stage. Claim changes the saved flag; it does not directly add products to inventory.')
        dialog.resize(1100,800);form=dialog.form();fields={}
        fields['premium']=optional_field(form,'Premium (0/1)',number(int(attrs.get('premium',0)),0,1));fields['score']=optional_field(form,'Score',number(int(attrs.get('score',0))))
        tabs=QTabWidget();dialog.body.addWidget(tabs,1);pages={}
        for road,title in (('FreeRoad','Free'),('PremiumRoad','Premium')):
            if not re.search(('<'+road+r'\b').encode(),season):continue
            page=PassStagePage(xml,road);pages[road]=page;tabs.addTab(page,title)
        def validate():
            if not any(page.changes() for page in pages.values()) and not any(check.isChecked() for check,widget in fields.values()):raise B.SaveToolError('Make at least one change before applying.')
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            changes={road:page.changes() for road,page in pages.items()};opening={key:str(widget.value()) for key,(check,widget) in fields.items() if check.isChecked()}
            def patch():
                if B.SESSION.current_xml!=xml:raise B.SaveToolError('The save changed while this editor was open. Reopen the editor.')
                result=pass_apply_rows(xml,changes)
                if opening:
                    season=B._advanced_block(result,'SeasonTicket');end=season.index(b'>')+1;tag=season[:end]
                    for key,value in opening.items():tag=B.replace_attribute(tag,key,value)
                    result=B._decor_replace_block(result,'SeasonTicket',tag+season[end:])
                return result
            self.run_edit(patch,'Golden Pass Editor')
    def trains(self):
        try:
            scopes,_=gui_train_groups(B.SESSION.current_xml)
            if not scopes:raise B.SaveToolError('Save đang mở chưa có dữ liệu toa tàu theo định dạng editor hỗ trợ.')
        except B.SaveToolError as exc:
            self.train_help(str(exc));return
        scope=1
        if len(scopes)>1:
            chooser=NativeDialog('Chọn khối Trains',self,'Save chứa nhiều nhóm dữ liệu tàu. Chọn nhóm thuộc thành phố đang chỉnh sửa; chương trình chỉ cập nhật nhóm được chọn.',apply_text='Mở nhóm đã chọn')
            table=QTreeWidget();table.setHeaderLabels(['Nhóm / đường dẫn XML','Số dòng tàu','Dữ liệu toa hiện có']);table.header().setSectionResizeMode(0,QHeaderView.Stretch);chooser.body.addWidget(table,1)
            for index,group in enumerate(scopes,1):
                overview=[]
                for _,data,_,_ in group['rows']:
                    overview.append(', '.join(f'{data.get("productId_"+str(n),"?")} × {data.get("productCount_"+str(n),0)}' for n in range(1,6) if 'productId_'+str(n) in data or 'productCount_'+str(n) in data))
                item=QTreeWidgetItem(table,[f'{index}. '+group['path'],str(len(group['rows'])),' | '.join(overview)])
                item.setData(0,Qt.UserRole,index);item.setToolTip(2,item.text(2))
            def validate_scope():
                if table.currentItem() is None:raise B.SaveToolError('Chọn một nhóm trong bảng.')
            chooser.validator=validate_scope
            chooser.footer.setText('Nếu chưa xác định được nhóm cần sửa, dùng Lưu chẩn đoán Train để gửi đường dẫn XML cho người hỗ trợ.')
            diagnostics=QPushButton('Lưu chẩn đoán Train');diagnostics.clicked.connect(lambda:self.train_help('Có nhiều khối Trains; cần xác định nhóm đang dùng.'));chooser.body.addWidget(diagnostics)
            if chooser.exec_()!=QDialog.Accepted:return
            scope=table.currentItem().data(0,Qt.UserRole)
        rows=gui_train_inventory(B.SESSION.current_xml,scope)
        groups={};current={};trainmap={}
        for n,(_,data,_,_) in enumerate(rows,1):
            group='Tàu '+str(n);trainmap[group]=n;groups[group]=[str(w) for w in range(1,6) if f'productId_{w}' in data or f'productCount_{w}' in data]
            for w in groups[group]:current[(group,w)]=f'{data.get("productId_"+w,"—")} × {data.get("productCount_"+w,0)} · done={data.get("productDone_"+w,0)}'
        dialog=NativeDialog('Train',self,f'Khối {scope}: {scopes[scope-1]["path"]}. Chọn toa ở một hoặc nhiều tàu. Các ô không bật Sửa được giữ nguyên; productDone=0 đặt lại trạng thái toa theo TSVIP.');picker=ItemPicker(groups,labels={key:'Toa '+key[1] for key in current},current=current);dialog.body.addWidget(picker,1);form=dialog.form();fields={}
        for key in ('productId','productCount','orderBlue','orderBlueTime','cardPack','productDone'):
            widget=text_field() if key in ('productId','cardPack') else number(0,-2147483648 if key=='productCount' else 0);fields[key]=optional_field(form,key,widget)
        def validate():
            picker.require()
            if not any(c.isChecked() for c,w in fields.values()):raise B.SaveToolError('Bật Sửa ít nhất một thông số toa tàu.')
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            selection=selected_mapping(picker);values={k:(w.text().strip() if isinstance(w,QLineEdit) else w.value()) for k,(c,w) in fields.items() if c.isChecked()}
            def patch():
                result=B.SESSION.current_xml
                for group,ids in selection.items():result=gui_edit_train_wagons(result,trainmap[group],[int(v) for v in ids],values,scope=scope)
                return result
            self.run_edit(patch,'Train')
    def train_help(self,reason):
        dialog=NativeDialog('Train · chưa có dữ liệu toa tàu',self,reason)
        dialog.resize(740,440);dialog.buttons.button(QDialogButtonBox.Apply).hide()
        instructions=QLabel('Để chỉnh toa tàu:\n\n'
            '1. Mở Township của đúng tài khoản và kiểm tra nhà ga đã được mở.\n'
            '2. Nếu tàu đang đi, chờ ít nhất một tàu về thành phố và còn đơn hàng/toa hiện trên màn hình.\n'
            '3. Thoát game để lưu, rồi Kết nối ADB để tải lại mGameInfo mới nhất. Nếu mở file trên máy, lấy lại save mới.\n\n'
            'Nếu tàu đã về nhưng vẫn gặp thông báo này, save có thể dùng cấu trúc khác. Lưu chẩn đoán Train để kiểm tra; editor sẽ không tự thêm tàu/toa mới.')
        instructions.setWordWrap(True);dialog.body.addWidget(instructions)
        row=QHBoxLayout();reload=QPushButton('Tải lại save qua ADB');diagnose=QPushButton('Lưu chẩn đoán Train');row.addWidget(reload);row.addWidget(diagnose);dialog.body.addLayout(row)
        def reload_save():dialog.reject();self.connect_device()
        def save_diagnostics():
            try:
                try:rows,blocks=gui_train_scan(B.SESSION.current_xml,allow_multiple=True);scan_error=''
                except B.SaveToolError as exc:rows=[];blocks=[];scan_error=str(exc)
                report={'source':B.SESSION.source_label,'package':B.PACKAGE_NAME,'reason':reason,'scan_error':scan_error,
                        'train_blocks':blocks,'supported_rows':len(rows),
                        'train_groups':[{'index':i,'path':group['path'],'rows':len(group['rows'])} for i,group in enumerate(gui_train_groups(B.SESSION.current_xml)[0],1)] if not scan_error else [],
                        'indexed_wagon_keys':sorted(set(v.decode() for v in re.findall(rb'(?:productId|productCount|productDone|orderBlue|orderBlueTime)_[0-9]+',B.SESSION.current_xml))),
                        'note':'Structure and field names only; no token, AES key or full save.'}
                path,_=QFileDialog.getSaveFileName(dialog,'Lưu chẩn đoán Train','train_diagnostic.json','JSON (*.json)')
                if path:B.atomic_write(Path(path),json.dumps(report,ensure_ascii=False,indent=2).encode());QMessageBox.information(dialog,'Train','Đã lưu chẩn đoán: '+path)
            except Exception as exc:QMessageBox.warning(dialog,'Chẩn đoán Train',str(exc))
        reload.clicked.connect(reload_save);diagnose.clicked.connect(save_diagnostics)
        dialog.footer.setText('Train chỉnh toa tàu hiện có. Nâng cấp cấp tàu dùng Tool → Academi → Tàu hỏa.')
        dialog.exec_()
    def regatta(self):
        _,_,tasks,old=B.regatta_task_inventory(B.SESSION.current_xml);dialog=NativeDialog('Regatta Tasks',self,'Đặt lại danh sách nhiệm vụ đã hoàn thành; 150 điểm/mục, ưu tiên Match3 theo TSVIP.');form=dialog.form();count=number(old,0,10000);form.addRow('Số MyOldTask hiện tại',QLabel(str(old)));form.addRow('Số nhiệm vụ mới',count)
        table=QTreeWidget();table.setHeaderLabels(['Task ID','Mục tiêu','Số lượng','Phiên bản']);table.header().setSectionResizeMode(0,QHeaderView.Stretch)
        for task in tasks:QTreeWidgetItem(table,[str(task.get(k,'')) for k in ('id','target','num','ver')])
        dialog.body.addWidget(table,1)
        if dialog.exec_()==QDialog.Accepted:
            value=count.value();self.run_edit(lambda:B.set_regatta_tasks(B.SESSION.current_xml,value),'Regatta Tasks')
    def tutorial(self):
        labels={k:re.sub(r'^\d+\.\s*','',v['label']) for k,v in B.TSVIP_TUTORIAL_FIXES.items()};current={k:str(len(v['fields']))+' cờ cần sửa' for k,v in B.TSVIP_TUTORIAL_FIXES.items()}
        dialog=NativeDialog('Fix Tutorial Bug',self,'Chọn một hoặc nhiều nhóm hướng dẫn cần sửa.');picker=ItemPicker({'Nhóm tutorial':list(labels)},labels=labels,current=current);dialog.body.addWidget(picker,1);dialog.validator=picker.require
        if dialog.exec_()==QDialog.Accepted:
            ids=picker.ids();self.run_edit(lambda:B.fix_tutorial_categories(B.SESSION.current_xml,ids),'Fix Tutorial Bug')
    def clone_v1(self):
        B.SESSION.require_loaded();dialog=CloneV1Dialog(self)
        if dialog.exec_()!=QDialog.Accepted:return
        donor=dialog.donor;selection=dialog.picker.ids();copy_level=dialog.copy_level.isChecked();expected=dialog.target
        def action():
            import uuid
            session=B.SESSION
            if session.current_xml!=expected:raise B.SaveToolError('Phiên save đã thay đổi; mở lại Clone V1 để tải đúng dữ liệu.')
            B.print(f'Clone V1: LV trước={B.read_township_level(expected)}; LV nguồn={B._clone_field_value(donor,"levelup","chưa có")}')
            note=gui_design_version_check(expected,donor)
            if note:B.print(note)
            result,report,sync_level=gui_clone_v1(expected,donor,selection,copy_level)
            current_local=session.pending_localinfo_xml or session.localinfo_xml;local=None
            if sync_level:
                if current_local is None:raise B.SaveToolError('Clone đổi LV cần LocalInfo; kết nối ADB tải lại cả hai file.')
                local=gui_sync_local_level(current_local,result)
            if result==expected and (local is None or local==current_local):B.print('Không có thay đổi.');B.print('Chi tiết:',report);return
            templates=session.pending_pair_templates or (session.original_container,session.localinfo_container)
            if templates[0] is None or (local is not None and templates[1] is None):raise B.SaveToolError('Thiếu container gốc để kiểm tra Clone V1; kết nối ADB lại.')
            game_container=B.encode_save(result,templates[0])
            if B.decode_save(game_container)!=B.canonical_xml(result):raise B.SaveToolError('Clone V1 encode/decode mGameInfo không khớp; chưa áp dụng.')
            local_container=None
            if local is not None:
                local_container=B.encode_save(local,templates[1])
                if B.decode_save(local_container)!=B.canonical_xml(local):raise B.SaveToolError('Clone V1 encode/decode LocalInfo không khớp; chưa áp dụng.')
            if session.localinfo_container is not None and session.localinfo_xml is not None:
                backup=B.create_account_backup(*B.current_account_containers(True),label='before Clone V1')
                B.print('Backup phiên trước Clone V1:',backup)
            else:
                backup=B.BACKUP_DIR/('before_clone_v1_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:8]+'.xml')
                B.atomic_write(backup,expected);B.print('Backup XML trước Clone V1:',backup)
            # Keep session state intact if writing either working file fails.
            writes=[(B.MODIFIED_FILE,result)]+([(B.CLONE_LOCAL_MODIFIED,local)] if local is not None else [])
            previous={path:path.read_bytes() if path.exists() else None for path,_ in writes};written=[]
            try:
                for path,xml in writes:B.atomic_write(path,xml);written.append(path)
            except Exception:
                for path in reversed(written):
                    try:
                        if previous[path] is None:path.unlink(missing_ok=True)
                        else:B.atomic_write(path,previous[path])
                    except OSError as exc:B.print('Không khôi phục được file làm việc:',path,str(exc))
                raise
            session.current_xml=result
            if local is not None:
                session.pending_localinfo_xml=local;session.pending_pair_templates=(game_container,local_container)
                B.print('Đã chuẩn bị cả mGameInfo và LocalInfo; khi ghi sẽ ghi cặp save.')
            else:B.print('Đã áp dụng vào XML làm việc. LocalInfo giữ nguyên.')
            B.print('LV kết quả:',B.read_township_level(result));B.print('Chi tiết:',report);B.print('Chưa ghi vào game.')
        self.start(action,'Clone City V1')

    def clone(self,version):
        if version==1:return self.clone_v1()
        if B.SESSION.localinfo_xml is None:raise B.SaveToolError('Clone V3 cần LocalInfo của tài khoản hiện tại.')
        dialog=NativeDialog('Clone City V3',self,'Chọn nguồn donor. FetchCity chạy khi áp dụng nếu chọn City ID hoặc bạn bè.');source=DonorSource();dialog.body.addWidget(source)
        remove=QCheckBox('Xóa CCSecret của donor');remove.setChecked(True);keep=QCheckBox('Giữ AirScore / AirInfo của donor');dialog.body.addWidget(remove);dialog.body.addWidget(keep);info=QLabel('V3 thay toàn bộ donor mGameInfo và dựng lại LocalInfo; giữ cityId/gameId/token/thiết bị hiện tại, reset clan/bạn bè/regatta. Phải xuất hoặc ghi cả hai file cùng nhau.');info.setWordWrap(True);dialog.body.addWidget(info)
        dialog.validator=source.data
        if dialog.exec_()==QDialog.Accepted:
            data=source.data();rem=remove.isChecked();air=keep.isChecked()
            def action():
                donor=DonorSource.load(data);before_level=B.read_township_level(B.SESSION.current_xml);donor_level=B.read_township_level(donor)
                B.print(f'Clone V3: LV trước={before_level}; LV nguồn={donor_level}')
                gui_check_v3_versions(B.SESSION.current_xml,donor)
                game,local,report=B.clone_city_v3(B.SESSION.current_xml,donor,B.SESSION.localinfo_xml,rem,air)
                game,local=gui_preserve_v3_device(B.SESSION.current_xml,game,B.SESSION.localinfo_xml,local);local=gui_sync_local_level(local,game)
                if B.read_township_level(game)!=donor_level:raise B.SaveToolError('Clone V3 chưa lấy đúng LV nguồn; không áp dụng.')
                gui_pair_level_report(game,local,'Cặp save V3 chuẩn bị');B.apply_clone_v3_session(game,local);B.print('LV kết quả:',B.read_township_level(game));B.print('Đã chuẩn bị cặp mGameInfo + LocalInfo:',report)
            self.start(action,'Clone City V3')
    def backup(self):
        dialog=NativeDialog('Backup',self,'Tạo ZIP chứa mGameInfo.xml + LocalInfo.xml + thông tin tài khoản.',apply_text='Tạo backup');dialog.footer.setText('Backup từ thiết bị sẽ đóng game trước khi đọc để hai file nhất quán.');dialog.resize(720,330);form=dialog.form();source=QComboBox();source.addItem('Hai file hiện tại trên thiết bị','device');source.addItem('Hai file gốc đã tải','original');source.addItem('Hai file đã chỉnh sửa (encode + verify)','edited');form.addRow('Nguồn backup',source);folder=path_field(form,'Thư mục lưu',str(B.ACCOUNT_BACKUP_DIR),True)
        cloud=QCheckBox('Tải bản ZIP lên Google Drive sau khi lưu trên máy');cloud.setChecked(GoogleDriveBackup.auto_upload());dialog.body.addWidget(cloud)
        cloud_config=QPushButton('Cấu hình Google Drive…');cloud_config.clicked.connect(lambda:GoogleDriveSettingsDialog(dialog).exec_());dialog.body.addWidget(cloud_config)
        def validate():
            if not folder.text().strip():raise B.SaveToolError('Chọn thư mục lưu.')
            if cloud.isChecked():GoogleDriveBackup().client_config()
            if source.currentData()!='device':B.current_account_containers()
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            kind=source.currentData();directory=Path(folder.text());upload_cloud=cloud.isChecked()
            def action():
                if kind=='device':
                    B.check_device();B.adb_shell(f'am force-stop {B.shell_quote(B.PACKAGE_NAME)}');game=B._clone_read_remote(B.REMOTE_SAVE,'backup_game');local=B._clone_read_remote(B.REMOTE_LOCALINFO,'backup_local')
                else:game,local=B.current_account_containers(kind=='edited')
                path=B.create_account_backup(game,local,directory,label=kind);B.print('Đã backup và kiểm tra ZIP:',path)
                if upload_cloud:
                    B.print('Đang tải backup lên Google Drive…')
                    try:result=drive_operation(lambda c:c.upload(path))
                    except Exception as exc:
                        B.print('Tải lên cloud chưa hoàn tất. ZIP trên máy vẫn được giữ:',path)
                        if isinstance(exc,B.SaveToolError):raise
                        raise CloudError('Tải lên Drive chưa hoàn tất; kiểm tra mạng và cấu hình rồi thử lại từ History.') from None
                    B.print('Đã tải và kiểm tra backup Google Drive:',result['name'])
            self.start(action,'Backup')
    def preserve_pair(self,label):
        originals=B.current_account_containers()
        if B.SESSION.changed:B.print('Backup thay đổi chưa lưu:',B.create_account_backup(*B.current_account_containers(True),label=label+' edited'))
        B.print('Backup file gốc:',B.create_account_backup(*originals,label=label+' original'))
    def restore_history_pair(self, game, local):
        # Preserve the user's working session before refreshing the device baseline.
        self.preserve_pair('pre-restore')
        B.check_device();B.adb_shell('am force-stop '+B.shell_quote(B.PACKAGE_NAME))
        current_game=B._clone_read_remote(B.REMOTE_SAVE,'history_game')
        current_local=B._clone_read_remote(B.REMOTE_LOCALINFO,'history_local')
        game_xml=B.decode_save(current_game);local_xml=B.decode_save(current_local)
        B.validate_xml_document(game_xml,'History: mGameInfo hiện tại')
        B.validate_xml_document(local_xml,'History: LocalInfo hiện tại')
        metadata,friends=B.parse_localinfo_metadata(local_xml)
        backup=B.create_account_backup(current_game,current_local,label='pre-restore device')
        B.print('Backup cặp save hiện tại trên thiết bị:',backup)
        B.atomic_write(B.SOURCE_FILE,current_game);B.atomic_write(B.LOCALINFO_SOURCE_FILE,current_local)
        B.atomic_write(B.DECODED_FILE,game_xml);B.atomic_write(B.LOCALINFO_DECODED_FILE,local_xml)
        session=B.SESSION
        session.original_container=current_game;session.original_xml=game_xml;session.current_xml=game_xml
        session.localinfo_container=current_local;session.localinfo_xml=local_xml
        session.localinfo_meta=metadata;session.friends=friends;session.selected_friend=None
        session.pending_localinfo_xml=None;session.pending_pair_templates=None
        B.stage_account_pair(game,local)
        # Pair writer still compares both remote files against this fresh baseline,
        # verifies readback and rolls back on write failure.
        self.write_game_action()

    def file_codec(self,encode):
        title='Encode' if encode else 'Decode'
        description='Select a plain Township XML to encode. A new container is generated using TSVIP-style encoding and verified by decoding again before saving.' if encode else 'Select a Township save (mGameInfo.xml or LocalInfo.xml) to decode into readable XML.'
        dialog=NativeDialog(title,self,description,apply_text='Encode file' if encode else 'Decode file');dialog.resize(820,420)
        input_folder=B.WORK_DIR/'inputxml';output_folder=B.WORK_DIR/'output'
        input_folder.mkdir(parents=True,exist_ok=True);output_folder.mkdir(parents=True,exist_ok=True)
        source_key='codec/inputxml' if encode else 'codec/inputsave';output_key='codec/encode_output' if encode else 'codec/decode_output'
        form=dialog.form();source=path_field(form,'Input XML' if encode else 'Input save',str(input_folder),remember_key=source_key)
        default_output=output_folder/('mGameInfo_encoded.xml' if encode else 'mGameInfo_decoded.xml')
        output=path_field(form,'Output file',str(default_output),remember_key=output_key,save=True)
        output.textEdited.connect(lambda _:output.setProperty('codecManualOutput',True))
        def suggest(path):
            file=Path(path)
            if path and not file.is_dir() and not output.property('codecManualOutput'):
                settings=QSettings('TownshipStudio','PyQt5');directory=Path(str(settings.value(output_key+'/browse_dir',str(output_folder))))
                output.setText(str(directory/(file.stem+('_encoded' if encode else '_decoded')+'.xml')))
        source.textChanged.connect(suggest)
        dialog.footer.setText('Files are processed separately. Apply does not change the loaded session or write to the game.')
        def validate():
            if not source.text().strip() or not Path(source.text()).is_file():raise B.SaveToolError('Select an existing input file.')
            if not output.text().strip():raise B.SaveToolError('Choose an output file.')
            destination=Path(output.text()).resolve()
            protected=[Path(source.text()).resolve()]
            if destination in protected:raise B.SaveToolError('Output must be different from the input file.')
            if not destination.parent.is_dir():raise B.SaveToolError('The output folder does not exist.')
            if destination.exists() and QMessageBox.question(dialog,'Replace output file','Replace the existing output file?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:raise B.SaveToolError('Choose another output file or confirm replacement.')
        dialog.validator=validate
        if dialog.exec_()!=QDialog.Accepted:return
        filename=source.text();destination=output.text()
        remember_browse_path(source_key,filename);remember_browse_path(output_key,destination)
        def action():
            result=gui_convert_save_file(filename,destination,encode)
            B.print('Encoded file saved:' if encode else 'Decoded XML saved:',str(result))
        self.start(action,title)

    def history(self):
        dialog=NativeDialog('History',self,'Chọn nhiều ZIP để tải lên Drive (Ctrl / Shift). Mở hoặc khôi phục vào game cần chọn đúng một ZIP.');dialog.resize(1180,900);dialog.setMinimumSize(1020,720);dialog.buttons.button(QDialogButtonBox.Apply).hide();dialog.footer.setText('Mở/khôi phục sẽ tạo backup phiên hiện tại trước khi thay thế hai file.');form=dialog.form();folder=path_field(form,'Thư mục backup',str(B.ACCOUNT_BACKUP_DIR),True)
        search=text_field();search.setPlaceholderText('Lọc tên file / tên tài khoản / City ID / level…');dialog.body.addWidget(search)
        tree=QTreeWidget();tree.setSelectionMode(QAbstractItemView.ExtendedSelection);tree.setHeaderLabels(['Tên backup','Thư mục tài khoản','Sửa đổi','Trạng thái']);tree.header().setStretchLastSection(False);tree.header().setSectionResizeMode(0,QHeaderView.Stretch);tree.header().setSectionResizeMode(1,QHeaderView.ResizeToContents);tree.header().setSectionResizeMode(2,QHeaderView.ResizeToContents);tree.header().setSectionResizeMode(3,QHeaderView.ResizeToContents);tree.setMinimumHeight(260);info=QPlainTextEdit();info.setReadOnly(True);info.setMinimumHeight(70);splitter=QSplitter(Qt.Vertical);splitter.setObjectName('historyBackupSplitter');splitter.addWidget(tree);splitter.addWidget(info);splitter.setStretchFactor(0,4);splitter.setStretchFactor(1,1);splitter.setSizes([420,110]);splitter.setChildrenCollapsible(False);dialog.body.addWidget(splitter,1)
        row=QGridLayout();buttons={}
        for index,label in enumerate(['Làm mới','Chọn ZIP','Xem thông tin','Mở để chỉnh sửa','Khôi phục vào game','Xóa ZIP']):
            button=QPushButton(label);buttons[label]=button;row.addWidget(button,index//3,index%3)
        dialog.body.addLayout(row)
        cloud_row=QHBoxLayout();drive_button=QPushButton('Google Drive…');drive_button.setIcon(native_icon('☁'));upload_button=QPushButton('Tải ZIP đã chọn lên Drive');cloud_row.addWidget(drive_button);cloud_row.addWidget(upload_button);select_all=QPushButton('Chọn tất cả đang hiện');select_all.clicked.connect(lambda:cloud_select_visible(tree));cloud_row.addWidget(select_all);clear_selection=QPushButton('Bỏ chọn');clear_selection.clicked.connect(tree.clearSelection);cloud_row.addWidget(clear_selection);cloud_row.addStretch();dialog.body.addLayout(cloud_row)
        def add_path(path):
            path=Path(path)
            for i in range(tree.topLevelItemCount()):
                existing=tree.topLevelItem(i)
                if Path(existing.data(0,Qt.UserRole)).resolve()==path.resolve():return existing
            item=QTreeWidgetItem(tree,[path.name,path.parent.name,datetime.fromtimestamp(path.stat().st_mtime).strftime('%d/%m/%Y %H:%M'),'Chưa kiểm tra']);item.setData(0,Qt.UserRole,str(path));return item
        def refresh():
            tree.clear();root=Path(folder.text());files=sorted(root.rglob('*.zip'),key=lambda p:p.stat().st_mtime,reverse=True) if root.is_dir() else []
            for path in files:add_path(path)
            filter_rows()
        def filter_rows():
            word=search.text().strip().casefold()
            for i in range(tree.topLevelItemCount()):
                item=tree.topLevelItem(i);item.setHidden(bool(word and word not in ' '.join(item.text(j) for j in range(4)).casefold()))
        def selected():
            items=cloud_selected_items(tree)
            if len(items)!=1:raise B.SaveToolError('Chọn đúng một ZIP để xem, mở, khôi phục hoặc xóa. Nhiều ZIP chỉ dùng để tải lên Drive.')
            item=items[0]
            return item,Path(item.data(0,Qt.UserRole))
        def view():
            try:
                item,path=selected();_,_,meta,doc=B.read_account_backup(path);item.setText(3,'Hợp lệ · LV '+meta['level']);info.setPlainText(json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n'+doc);filter_rows()
            except Exception as exc:QMessageBox.warning(dialog,'Backup',str(exc))
        def open_zip():
            paths,_=QFileDialog.getOpenFileNames(dialog,'Chọn các backup ZIP',folder.text(),'Backup (*.zip)')
            if paths:
                search.clear();tree.clearSelection()
                for path in paths:add_path(Path(path)).setSelected(True)
                if len(paths)==1:view()
                else:info.setPlainText(f'Đã chọn {len(paths)} ZIP. Bấm Tải ZIP đã chọn lên Drive để tải cả đợt.')
        def apply(restore=False):
            try:
                _,path=selected();B.current_account_containers();B.read_account_backup(path)
            except Exception as exc:QMessageBox.warning(dialog,'History',str(exc));return
            if QMessageBox.question(dialog,'Thay cặp save','Backup phiên hiện tại rồi thay toàn bộ hai file bằng ZIP đã chọn'+(' và ghi vào game?' if restore else '?'),QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:return
            dialog.reject()
            def action():
                game,local,meta,_=B.read_account_backup(path)
                if restore:self.restore_history_pair(game,local)
                else:self.preserve_pair('pre-restore');B.stage_account_pair(game,local)
                B.print('Đã khôi phục backup:' if restore else 'Đã mở backup:',meta)
            self.start(action,'History · '+('khôi phục' if restore else 'mở backup'))
        def delete():
            try:item,path=selected()
            except Exception as exc:QMessageBox.warning(dialog,'History',str(exc));return
            if QMessageBox.question(dialog,'Xóa ZIP','Xóa '+path.name+'?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
                try:path.unlink();tree.takeTopLevelItem(tree.indexOfTopLevelItem(item));info.clear()
                except OSError as exc:QMessageBox.warning(dialog,'Không xóa được',str(exc))
        buttons['Xóa ZIP'].setToolTip('Chỉ xóa ZIP trên máy; không xóa backup trên Google Drive.')
        buttons['Làm mới'].clicked.connect(refresh);buttons['Chọn ZIP'].clicked.connect(open_zip);buttons['Xem thông tin'].clicked.connect(view);buttons['Mở để chỉnh sửa'].clicked.connect(lambda:apply(False));buttons['Khôi phục vào game'].clicked.connect(lambda:apply(True));buttons['Xóa ZIP'].clicked.connect(delete);tree.itemDoubleClicked.connect(lambda *_:view());search.textChanged.connect(filter_rows)
        def from_cloud():
            cloud_dialog=GoogleDriveHistoryDialog(dialog,folder.text() or str(B.ACCOUNT_BACKUP_DIR))
            cloud_dialog.exec_()
            if cloud_dialog.downloaded_paths:
                search.clear();tree.clearSelection()
                for path in cloud_dialog.downloaded_paths:add_path(path).setSelected(True)
                if len(cloud_dialog.downloaded_paths)==1:view()
                else:info.setPlainText(f'Đã tải và kiểm tra {len(cloud_dialog.downloaded_paths)} ZIP. Chọn một ZIP để xem thông tin hoặc khôi phục.')
        def to_cloud():
            items=cloud_selected_items(tree)
            if not items:QMessageBox.information(dialog,'Google Drive','Chọn một hoặc nhiều ZIP để tải lên.');return
            CloudBatchDialog.perform(dialog,'upload',[Path(item.data(0,Qt.UserRole)) for item in items])
        drive_button.clicked.connect(from_cloud);upload_button.clicked.connect(to_cloud)
        refresh();dialog.exec_()
    def auto_new_town(self,donor,timeout,do_reset,try_agree,agree_xy):
        worker=self.worker
        def cancelled():return worker.cancelled
        B.check_device()
        if cancelled():raise Cancelled()
        self.preserve_pair('pre-auto-new-town')
        B.adb_shell('am force-stop '+B.shell_quote(B.PACKAGE_NAME))
        current_game=B._clone_read_remote(B.REMOTE_SAVE,'newtown_initial_game');current_local=B._clone_read_remote(B.REMOTE_LOCALINFO,'newtown_initial_local')
        live_game=B.decode_save(current_game);live_local=B.decode_save(current_local)
        if do_reset and B.SESSION.loaded and B._clone_field_value(B.SESSION.current_xml,'cityId')!=B._clone_field_value(live_game,'cityId'):
            raise B.SaveToolError('Tài khoản trên thiết bị khác phiên đã tải; kết nối lại ADB trước khi tạo mới.')
        if do_reset:
            for field in ('Version','FVer'):
                if B._clone_field_value(live_game,field)!=B._clone_field_value(donor,field):
                    raise B.SaveToolError('Mẫu LV3 khác phiên bản save hiện tại. Chọn ZIP cùng phiên bản trước khi reset.')
        backup=B.create_account_backup(current_game,current_local,label='before auto new town');B.print('Backup tài khoản trước thao tác:',backup)
        gui_commit_device_pair(current_game,current_local)
        reset_game,reset_local,_=B.new_towncity_payload();reset_id=B._clone_field_value(B.decode_save(reset_game),'cityId')
        excluded={reset_id}
        if do_reset:
            excluded.add(B._clone_field_value(live_game,'cityId'))
            if cancelled():raise Cancelled()
            B.print('Bước 1/4: ghi mẫu reset New TownCity. Game sẽ tạo định danh mới khi khởi động.')
            folder,details=B.write_clone_pair_to_device(reset_game,reset_local)
            gui_commit_device_pair(reset_game,reset_local)
            B.print('Đã ghi mẫu reset; backup:',folder)
        else:B.print('Tiếp tục từ tài khoản đã reset; không ghi mẫu reset lần nữa.')
        if cancelled():raise Cancelled()
        B.print('Bước 2/4: mở Township và chờ City ID mới.');self.launch_township()
        identity,_,_=gui_wait_newtown_identity(excluded,timeout,cancelled,try_agree,agree_xy)
        B.adb_shell('am force-stop '+B.shell_quote(B.PACKAGE_NAME))
        g=B._clone_read_remote(B.REMOTE_SAVE,'newtown_ready_game');l=B._clone_read_remote(B.REMOTE_LOCALINFO,'newtown_ready_local')
        if gui_newtown_identity(B.decode_save(g),B.decode_save(l))!=identity:raise B.SaveToolError('Định danh đổi khi đóng game; chưa ghép mẫu. Kết nối lại ADB rồi tiếp tục.')
        gui_commit_device_pair(g,l)
        backup=B.create_account_backup(g,l,label='new identity before LV3');B.print('Backup định danh mới trước LV3:',backup)
        B.print('Đã có City ID mới:',identity[0]);B.print('Bước 3/4: ghép mẫu LV3, giữ City ID / Game ID / token / thiết bị.')
        eg,el=gui_prepare_lv3_pair(g,l,donor)
        export=B.create_account_backup(eg,el,label='auto new town LV3 prepared');B.print('ZIP LV3 đã chuẩn bị:',export)
        if cancelled():raise Cancelled()
        folder,details=B.write_clone_pair_to_device(eg,el)
        gui_commit_device_pair(eg,el)
        B.print('Đã ghi và xác minh cặp save LV3. Backup ghi:',folder)
        B.print('Bước 4/4: mở Township để kiểm tra LV3 và tutorial.');self.launch_township()
        B.print('Hoàn tất chuẩn bị tài khoản LV3. City ID:',identity[0]);B.print('Kiểm tra kết quả trong game; bản ghi đã xác minh trước khi mở game.')

    def new_town(self):
        B.current_account_containers()
        dialog=NativeDialog('New TownCity',self,'Tạo mới LV3: backup → reset → mở game / Agree → đợi định danh mới → ghép mẫu LV3 → ghi và mở game. Thao tác này ghi trực tiếp vào game.');dialog.resize(850,620)
        form=dialog.form();mode=QComboBox();mode.addItem('🌱 Tự tạo tài khoản mới LV3','auto');mode.addItem('▶ Tiếp tục LV3 sau reset / chờ Agree','resume');mode.addItem('Mẫu TSVIP có sẵn (chuẩn bị như trước)','builtin');mode.addItem('ZIP thành phố của bạn (chuẩn bị như trước)','file');form.addRow('Chế độ',mode)
        path=path_field(form,'ZIP mẫu LV3 / ZIP thành phố',str(self.settings.value('lv3_template_zip','')))
        hint=QLabel('Để trống ZIP ở chế độ LV3 sẽ dùng mẫu 39.0.2 đã thử thành công. Có thể chọn mẫu LV3 khác cùng phiên bản. Không dùng ID của mẫu làm ID tài khoản mới.');hint.setWordWrap(True);dialog.body.addWidget(hint)
        timeout=QSpinBox();timeout.setRange(60,600);timeout.setValue(int(self.settings.value('lv3_wait_seconds',180)));timeout.setSuffix(' giây');form.addRow('Thời gian chờ định danh',timeout)
        agree=QCheckBox('Tự nhận diện và bấm Agree bằng ADB');agree.setChecked(True);dialog.body.addWidget(agree)
        coords=QCheckBox('Dùng tọa độ Agree đã xác định nếu không đọc được chữ (tùy chọn)');dialog.body.addWidget(coords)
        x=QSpinBox();y=QSpinBox()
        for field in (x,y):field.setRange(0,4096)
        x.setValue(int(self.settings.value('lv3_agree_x',0)));y.setValue(int(self.settings.value('lv3_agree_y',0)))
        row=QHBoxLayout();row.addWidget(QLabel('X'));row.addWidget(x);row.addWidget(QLabel('Y'));row.addWidget(y);dialog.body.addLayout(row)
        def update():
            automatic=mode.currentData() in ('auto','resume');dialog.buttons.button(QDialogButtonBox.Apply).setText('Tạo mới và ghi vào game' if mode.currentData()=='auto' else 'Tiếp tục và ghi LV3' if mode.currentData()=='resume' else 'Áp dụng vào phiên');path.setEnabled(mode.currentData()!='builtin');timeout.setEnabled(automatic);agree.setEnabled(automatic);coords.setEnabled(automatic and agree.isChecked());x.setEnabled(automatic and agree.isChecked() and coords.isChecked());y.setEnabled(x.isEnabled())
        mode.currentIndexChanged.connect(update);agree.toggled.connect(update);coords.toggled.connect(update);update()
        dialog.footer.setText('Tạo mới sẽ thay tài khoản hiện tại; backup được lưu trước khi reset. Hết thời gian chờ: dùng chế độ Tiếp tục để tránh reset lại. Với các chế độ chuẩn bị, vẫn cần bấm Ghi vào game như trước.')
        prepared={}
        def validate():
            kind=mode.currentData();filename=path.text().strip()
            if kind in ('auto','resume'):
                if filename:
                    g,_,_,_=B.read_account_backup(Path(filename));donor=B.decode_save(g)
                else:
                    g,_,_,_=B.read_account_backup_bytes(base64.b64decode(GUI_LV3_TEMPLATE_DATA));donor=B.decode_save(g)
                if B.read_township_level(donor)!=3:raise B.SaveToolError('Chọn mẫu LV3.')
                prepared['donor']=donor
            elif kind=='file' and not Path(filename).is_file():raise B.SaveToolError('Chọn ZIP thành phố.')
        dialog.validator=validate
        if dialog.exec_()!=QDialog.Accepted:return
        kind=mode.currentData();filename=path.text().strip()
        if kind in ('auto','resume'):
            self.settings.setValue('lv3_template_zip',filename);self.settings.setValue('lv3_wait_seconds',timeout.value());self.settings.setValue('lv3_agree_x',x.value());self.settings.setValue('lv3_agree_y',y.value())
            xy=(x.value(),y.value()) if agree.isChecked() and coords.isChecked() else None
            wait_seconds=timeout.value();auto_agree=agree.isChecked()
            self.start(lambda:self.auto_new_town(prepared['donor'],wait_seconds,kind=='auto',auto_agree,xy),'New TownCity · tự động LV3')
        else:
            def action():
                if kind=='builtin':game,local,meta=B.new_towncity_payload()
                else:game,local,meta,_=B.read_account_backup(Path(filename))
                self.preserve_pair('pre-new-town');B.stage_account_pair(game,local);B.print('Đã chuẩn bị New TownCity:',meta)
            self.start(action,'New TownCity')

    def send_card(self):
        defaults=B.send_card_defaults(B.SESSION.current_xml,B.SESSION.localinfo_xml);dialog=NativeDialog('Send Card',self,'Chọn người nhận và card; các request được gửi qua SendBox API. Master AES key cần lấy từ phiên TSVIP hợp lệ.',apply_text='Gửi card qua API');dialog.resize(1100,860);dialog.footer.setText('Không tự gửi lại khi timeout; kiểm tra hộp thư trong game trước khi thao tác lại. Token và master key không được lưu vào báo cáo.')
        # Five rows per column keep the recipient/card lists tall.
        columns=QHBoxLayout();columns.setSpacing(24);dialog.body.addLayout(columns)
        left=QFormLayout();right=QFormLayout()
        for form in (left,right):
            form.setContentsMargins(0,0,0,0);form.setVerticalSpacing(8)
            form.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
            columns.addLayout(form,1)
        fields={}
        for label,key in [('Sender City ID','sender'),('col_id','collection'),('col_et · Unix seconds','end_time'),('Tên sender','name'),('pic','pic')]:
            fields[key]=text_field(defaults.get(key,''));left.addRow(label,fields[key])
        for label,key in [('bver','bver'),('fver','fver')]:
            fields[key]=text_field(defaults.get(key,''));right.addRow(label,fields[key])
        counter=number(1);right.addRow('sendCounter bắt đầu',counter)
        token=text_field(defaults.get('token',''),True);master=text_field('',True)
        right.addRow('ts-token',token);right.addRow('Master AES key · hex',master)
        tabs=QTabWidget();tabs.setMinimumHeight(300);friends=sorted((B.SESSION.friends or {}).values(),key=B.friend_sort_key);recipients=ItemPicker({'Bạn bè':[f.city_id for f in friends]},labels={f.city_id:f.city_name for f in friends},current={f.city_id:'LV '+str(f.level) for f in friends});tabs.addTab(recipients,'Người nhận');cards=ItemPicker({'Set '+str(n):[str(v) for v in range((n-1)*10+1,n*10+1)] for n in range(1,17)},labels={str(n):f'Card {n:02d}' for n in range(1,161)});tabs.addTab(cards,'Card 1–160');dialog.body.addWidget(tabs,1);extra=text_field();extra.setPlaceholderText('City ID bổ sung, phân cách bằng dấu phẩy');dialog.body.addWidget(extra)
        def payload():
            ids=list(dict.fromkeys(recipients.ids()+[v for v in re.split(r'[,;\s]+',extra.text().strip()) if v]));cards.require()
            if not ids:raise B.SaveToolError('Chọn ít nhất một người nhận.')
            try:key=bytes.fromhex(master.text().strip())
            except ValueError:raise B.SaveToolError('Master AES key phải là hex hợp lệ.')
            if len(key) not in (16,24,32):raise B.SaveToolError('Master AES key phải dài 16, 24 hoặc 32 byte.')
            data={k:w.text().strip() for k,w in fields.items()};end=B.parse_int(data['end_time'],'col_et',1,9223372036854775807);first=counter.value()
            requests=[]
            for recipient in ids:
                for card in cards.ids():
                    requests.append(B.prepare_send_card(data['sender'],recipient,int(card),data['collection'],end,first,token.text().strip(),data['name'],data['pic'],data['bver'],data['fver'],key));first+=1
            return requests,key
        dialog.validator=lambda:payload()
        if dialog.exec_()==QDialog.Accepted:
            prepared,key=payload()
            if QMessageBox.question(self,'Gửi card',f'Gửi {len(prepared)} card request qua API?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:return
            def action():
                records=[];failure=None
                for request in prepared:
                    box=json.loads(json.loads(request.plaintext_json)['box'])
                    try:result=B.send_card_live(request,key);records.append({'card':box['card_id'],'recipient':box['to'],'result':result});B.print(box['card_id'],'→',box['to'],result['status'])
                    except Exception as exc:
                        failure=exc;records.append({'card':box['card_id'],'recipient':box['to'],'error':str(exc)});break
                path=B.WORK_DIR/('send_card_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+B.uuid.uuid4().hex[:8]+'.json');B.atomic_write(path,json.dumps(records,ensure_ascii=False,indent=2).encode());B.print('Báo cáo:',path)
                if failure:raise B.SaveToolError('Dừng gửi: '+str(failure))
            self.start(action,'Send Card')
    def open_localinfo(self):
        if self.worker is not None:return
        if B.SESSION.pending_localinfo_xml is not None:QMessageBox.warning(self,'LocalInfo','Đang có cặp save chưa lưu. Xuất/ghi hoặc hoàn tác trước.');return
        path,_=QFileDialog.getOpenFileName(self,'Mở LocalInfo','','Save (*.xml);;Tất cả (*)')
        if not path:return
        def action():
            raw=Path(path).read_bytes();xml=B.decode_save(raw);meta,friends=B.parse_localinfo_metadata(xml);B.atomic_write(B.LOCALINFO_SOURCE_FILE,raw);B.atomic_write(B.LOCALINFO_DECODED_FILE,xml);s=B.SESSION;s.localinfo_container=raw;s.localinfo_xml=xml;s.localinfo_meta=meta;s.friends=friends;s.selected_friend=None;B.print('Đã đọc LocalInfo:',len(friends),'bạn bè')
        self.start(action,'Mở LocalInfo')
    def launch_township(self):
        package=B.PACKAGE_NAME
        result=B.adb('shell','cmd','package','resolve-activity','--brief','-a','android.intent.action.MAIN','-c','android.intent.category.LAUNCHER',package,timeout=30)
        components=[line.strip() for line in result.stdout.splitlines() if re.fullmatch(re.escape(package)+r'/[A-Za-z0-9_.$]+',line.strip())]
        if not components:raise B.SaveToolError('Không tìm thấy màn hình khởi động cho '+package)
        result=B.adb('shell','am','start','-W','-n',components[-1],timeout=45)
        response=(result.stdout or '')+'\n'+(result.stderr or '')
        if re.search(r'(?im)^\s*(?:Error|Exception|Failure)\b',response):
            raise B.SaveToolError(response.strip())
        B.print('Đã gửi lệnh mở Township trên giả lập:',package)

    def refresh_pair_write_baseline(self):
        session=B.SESSION
        if session.localinfo_container is None or session.localinfo_xml is None:
            raise B.SaveToolError('Thiếu LocalInfo gốc; kết nối ADB tải lại cặp save.')
        B.check_device();B.adb_shell('am force-stop '+B.shell_quote(B.PACKAGE_NAME))
        current_game=B._clone_read_remote(B.REMOTE_SAVE,'write_baseline_game')
        current_local=B._clone_read_remote(B.REMOTE_LOCALINFO,'write_baseline_local')
        if (current_game,current_local)==(session.original_container,session.localinfo_container):return
        game_xml=B.decode_save(current_game);local_xml=B.decode_save(current_local)
        B.validate_xml_document(game_xml,'Save hiện tại trước ghi')
        B.validate_xml_document(local_xml,'LocalInfo hiện tại trước ghi')
        def identity(xml):
            aws=B._clone_tag_attrs(xml,'AWS');version=B._clone_tag_attrs(xml,'Version')
            return aws.get('cityId',''),version.get('gameId','')
        before=identity(session.localinfo_xml);now=identity(local_xml)
        if not all(before) or before!=now:
            raise B.SaveToolError('Tài khoản trên thiết bị đã đổi hoặc thiếu cityId/gameId. Không ghi kết quả clone; kết nối lại ADB trên đúng tài khoản.')
        metadata,friends=B.parse_localinfo_metadata(local_xml)
        backup=B.create_account_backup(current_game,current_local,label='pre-write refreshed device')
        B.print('Save đã thay đổi từ lúc kết nối; đã backup cặp save mới:',backup)
        # Keep the prepared clone and its codec templates while updating only the baseline.
        templates=session.pending_pair_templates or (session.original_container,session.localinfo_container)
        B.atomic_write(B.SOURCE_FILE,current_game);B.atomic_write(B.LOCALINFO_SOURCE_FILE,current_local)
        B.atomic_write(B.DECODED_FILE,game_xml);B.atomic_write(B.LOCALINFO_DECODED_FILE,local_xml)
        session.original_container=current_game;session.original_xml=game_xml
        session.localinfo_container=current_local;session.localinfo_xml=local_xml
        session.localinfo_meta=metadata;session.friends=friends;session.selected_friend=None
        session.pending_pair_templates=templates
        B.print('Đã cập nhật bản gốc để đối chiếu; giữ nguyên cặp save clone đang chờ ghi.')

    def write_game_action(self):
        s=B.SESSION;s.require_loaded()
        if not s.changed:B.print('Không có thay đổi để ghi.');return
        if s.pending_localinfo_xml is not None:
            self.refresh_pair_write_baseline()
            game=s.encode_verify();local=B.encode_pending_localinfo()
            gui_pair_level_report(B.decode_save(game),B.decode_save(local),'Cặp save encode trước ghi')
            backup,details=B.write_clone_pair_to_device(game,local);B.print('Đã ghi cặp save:',backup);B.print('\n'.join(details))
            verified_game=B._clone_read_remote(B.REMOTE_SAVE,'level_verify_game');verified_local=B._clone_read_remote(B.REMOTE_LOCALINFO,'level_verify_local')
            if verified_game!=game or verified_local!=local:raise B.SaveToolError('Save thay đổi ngay sau ghi; chưa mở game. Kiểm tra backup và kết nối lại ADB.')
            gui_pair_level_report(B.decode_save(verified_game),B.decode_save(verified_local),'Đọc lại từ thiết bị trước mở game')
            # Preserve the same session commit semantics as the original pair writer.
            s.original_container=game;s.original_xml=s.current_xml;s.localinfo_container=local;s.localinfo_xml=s.pending_localinfo_xml;s.localinfo_meta,s.friends=B.parse_localinfo_metadata(s.localinfo_xml);s.pending_localinfo_xml=None;s.pending_pair_templates=None;s.selected_friend=None
            B.atomic_write(B.SOURCE_FILE,game);B.atomic_write(B.LOCALINFO_SOURCE_FILE,local);B.atomic_write(B.DECODED_FILE,s.current_xml);B.atomic_write(B.LOCALINFO_DECODED_FILE,s.localinfo_xml)
        else:
            encoded=s.encode_verify();backup,remote=B.write_save_to_device(encoded,s.original_container);s.original_container=encoded;s.original_xml=s.current_xml;B.atomic_write(B.SOURCE_FILE,encoded);B.atomic_write(B.DECODED_FILE,s.current_xml);B.print('Ghi thành công. Backup:',backup,'Backup thiết bị:',remote)
        if self.auto_launch_game:
            try:self.launch_township()
            except Exception as exc:B.print('Save đã ghi thành công, nhưng không mở được Township:',str(exc))
    def write_game(self):
        if self.worker is not None:return
        if not B.SESSION.loaded:QMessageBox.information(self,'Ghi vào game','Mở save trước.');return
        if not B.SESSION.changed:QMessageBox.information(self,'Ghi vào game','Không có thay đổi chưa lưu.');return
        if QMessageBox.question(self,'Ghi vào game','Encode + verify, tạo backup rồi ghi '+('cả mGameInfo và LocalInfo' if B.SESSION.pending_localinfo_xml is not None else 'mGameInfo')+' vào thiết bị đã cấu hình?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:self.start(self.write_game_action,'Ghi vào game')
    def undo_native(self):
        if self.worker is not None:return
        if not B.SESSION.loaded:return
        if B.SESSION.changed and QMessageBox.question(self,'Hoàn tác','Bỏ toàn bộ thay đổi chưa lưu?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:return
        def action():
            s=B.SESSION;s.pending_localinfo_xml=None;s.pending_pair_templates=None;s.apply_xml(s.original_xml);B.print('Đã hoàn tác phiên về save gốc.')
        self.start(action,'Hoàn tác')
    def help(self):
        QMessageBox.information(self,'Hướng dẫn TS Studio v1.39','Mở save / LocalInfo hoặc kết nối ADB trước.\n\nDecorations và các danh mục: đánh dấu từng mục, chọn cả nhóm hoặc tất cả, tìm theo tên/ID.\nCác bảng số lượng: chỉnh từng dòng hoặc đặt chung cho mục đã chọn.\nÔ Sửa chỉ bật những thông số cần thay đổi.\nÁp dụng giữ thay đổi trong phiên; Xuất file hoặc Ghi vào game để lưu.\n\nTên ID lấy từ file gốc; chưa có ảnh hay tên dịch cho toàn bộ danh mục. Clone V3 / New TownCity / History dùng cả hai file. New TownCity tự động LV3: backup, reset, mở game, chờ ID mới và ghi mẫu; không cần bấm Ghi vào game lần nữa. Nếu chờ Agree quá lâu, bấm Agree trên giả lập hoặc cấu hình vị trí Agree. Chế độ Tiếp tục không reset lại. Encode kiểm tra không đảm bảo server chấp nhận nội dung.\nCông cụ XML chuyên sâu dùng biểu mẫu; điều kiện tìm tag vẫn nhập theo cú pháp key=value.')
    def extra(self):
        if self.worker is not None:return
        dialog=NativeDialog('FetchCity & công cụ bổ sung',self,'Các công cụ bổ sung cũng sử dụng bảng danh sách và biểu mẫu.');dialog.buttons.button(QDialogButtonBox.Apply).hide();dialog.footer.hide();grid=QGridLayout();dialog.body.addLayout(grid)
        entries=[('Bạn bè / FetchCity',self.friends_dialog),('Manual City ID → FetchCity',self.fetch_dialog),('Xem donor hiện tại',self.donor_info),('Clone City / Zoo / Stash / All',self.layout_clone),('Quét City ID trong XML',self.scan_ids),('Friend Network',self.network_dialog),('Sửa Var bất kỳ',self.var_editor),('Sửa thuộc tính tag',self.tag_editor),('Khôi phục backup local',self.restore_single)]
        def dispatch(fn):
            dialog.reject()
            try:fn()
            except Exception as exc:QMessageBox.warning(self,'Công cụ',str(exc))
        for i,(label,fn) in enumerate(entries):
            button=QPushButton(label);button.clicked.connect(lambda _,f=fn:dispatch(f));grid.addWidget(button,i//2,i%2)
        dialog.exec_()
    def friends_dialog(self):
        friends=sorted((B.SESSION.friends or {}).values(),key=B.friend_sort_key)
        if not friends:raise B.SaveToolError('Mở LocalInfo trước để có danh sách bạn bè.')
        dialog=NativeDialog('Bạn bè / FetchCity',self,'Tìm và chọn bạn bè; chọn tải donor hoặc chỉ lưu lựa chọn.',apply_text='FetchCity người đã chọn');dialog.footer.setText('FetchCity lưu donor, chưa thay đổi save tài khoản hiện tại.');search=text_field();search.setPlaceholderText('Tìm tên hoặc City ID');dialog.body.addWidget(search)
        tree=QTreeWidget();tree.setHeaderLabels(['Tên','City ID','Level','Nhóm']);tree.header().setSectionResizeMode(0,QHeaderView.Stretch);dialog.body.addWidget(tree,1)
        for friend in friends:
            item=QTreeWidgetItem(tree,[friend.city_name,friend.city_id,str(friend.level),', '.join(friend.groups or [])]);item.setData(0,Qt.UserRole,friend.city_id)
        def filtered():
            word=search.text().casefold()
            for i in range(tree.topLevelItemCount()):
                item=tree.topLevelItem(i);item.setHidden(word not in (item.text(0)+' '+item.text(1)).casefold())
        search.textChanged.connect(filtered);select=QPushButton('Chọn bạn bè, chưa Fetch');dialog.body.addWidget(select)
        def get_friend():
            item=tree.currentItem()
            if item is None:raise B.SaveToolError('Chọn một người trong bảng.')
            return B.SESSION.friends[item.data(0,Qt.UserRole)]
        def select_friend():
            try:B.SESSION.selected_friend=get_friend();dialog.reject();self.append('Đã chọn bạn bè: '+B.SESSION.selected_friend.city_id)
            except Exception as exc:QMessageBox.warning(dialog,'Bạn bè',str(exc))
        select.clicked.connect(select_friend);dialog.validator=get_friend
        if dialog.exec_()==QDialog.Accepted:
            friend=get_friend();B.SESSION.selected_friend=friend;meta=B.SESSION.localinfo_meta or {};bver=meta.get('version');fver=meta.get('fver')
            if not bver or not fver:raise B.SaveToolError('LocalInfo thiếu bver/fver.')
            def action():
                donor,_,version=B.fetch_city_live(friend.city_id,bver,fver,friend.fetched_city_ver);B.SESSION.donor_xml=donor;B.SESSION.donor_path=B.FRIENDS_DIR/friend.city_id/'friend_city.xml';B.atomic_write(B.DONOR_FILE,donor);B.print('FetchCity thành công:',friend.city_id,'cityVer:',version)
            self.start(action,'FetchCity bạn bè')
    def fetch_dialog(self):
        dialog=NativeDialog('Manual City ID → FetchCity',self,'Nhập City ID để tải donor; có thể clone layout ngay vào save đã mở.',apply_text='FetchCity');dialog.resize(700,440);form=dialog.form();city=text_field();meta=B.SESSION.localinfo_meta or {};bver=text_field(meta.get('version') or '');fver=text_field(meta.get('fver') or '');form.addRow('City ID',city);form.addRow('bver',bver);form.addRow('fver',fver);mode=QComboBox();mode.addItem('Chỉ tải donor',None)
        for label,value in [('City layout','city'),('Zoo layout','zoo'),('BuildingsStash','stash'),('All: City + Zoo + Stash','all')]:mode.addItem(label,value)
        form.addRow('Sau khi tải',mode)
        copy_level=QCheckBox('Lấy Level + XP từ donor (cho phép giảm LV)');form.addRow('',copy_level)
        copy_level.setEnabled(False);mode.currentIndexChanged.connect(lambda _:copy_level.setEnabled(mode.currentData() is not None))
        def validate():
            if not re.fullmatch(r'[A-Za-z0-9_-]{3,64}',city.text().strip()):raise B.SaveToolError('City ID phải có 3–64 ký tự chữ, số, _ hoặc -.')
            if not bver.text().strip() or not fver.text().strip():raise B.SaveToolError('Điền bver và fver.')
            if mode.currentData():B.SESSION.require_loaded()
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            cid=city.text().strip();bv=bver.text().strip();fv=fver.text().strip();clone_mode=mode.currentData();sync_level=copy_level.isChecked()
            def action():
                donor,_,ver=B.fetch_city_live(cid,bv,fv,0);B.SESSION.donor_xml=donor;B.SESSION.donor_path=B.FRIENDS_DIR/cid/'friend_city.xml';B.atomic_write(B.DONOR_FILE,donor);level,_,_=B.extract_city_level(donor);B.SESSION.selected_friend=B.FriendProfile(city_id=cid,city_name='Manual:'+cid,level=level,fver=fv,fetched_city_ver=ver,groups=['ManualCityId']);B.print('Đã tải donor:',cid,'Level:',level)
                if clone_mode:
                    result,blocks,stats=B.clone_friend_layout(B.SESSION.current_xml,donor,clone_mode)
                    if sync_level:result,stats['level_xp_changes']=gui_copy_donor_level(result,donor)
                    apply_result((result,{'blocks':blocks,'stats':stats}))
            self.start(action,'Manual FetchCity')
    def donor_info(self):
        donor=B.SESSION.donor_xml or (B.load_friend_donor(B.DONOR_FILE) if B.DONOR_FILE.is_file() else None)
        if donor is None:raise B.SaveToolError('Chưa có donor.')
        dialog=NativeDialog('Donor hiện tại',self);dialog.buttons.button(QDialogButtonBox.Apply).hide();form=dialog.form()
        form.addRow('File',QLabel(str(B.SESSION.donor_path or B.DONOR_FILE)))
        for name in ('city','zoo','stash'):form.addRow(name,QLabel(json.dumps(B.count_layout_objects(donor,name),ensure_ascii=False)))
        sha=text_field(B.sha256_bytes(donor));sha.setReadOnly(True);form.addRow('SHA-256',sha);dialog.exec_()
    def layout_clone(self):
        B.SESSION.require_loaded();dialog=NativeDialog('Clone layout',self,'Chọn nguồn donor và phần layout cần sao chép.');source=DonorSource();dialog.body.addWidget(source);form=dialog.form();mode=QComboBox()
        for label,value in [('City: TownGround + Buildings','city'),('Zoo layout','zoo'),('BuildingsStash','stash'),('All: City + Zoo + Stash','all')]:mode.addItem(label,value)
        form.addRow('Nội dung',mode);copy_level=QCheckBox('Lấy Level + XP từ donor (cho phép giảm LV)');form.addRow('',copy_level);dialog.validator=source.data
        if dialog.exec_()==QDialog.Accepted:
            data=source.data();kind=mode.currentData();sync_level=copy_level.isChecked()
            def patch():
                donor=DonorSource.load(data);result,blocks,stats=B.clone_friend_layout(B.SESSION.current_xml,donor,kind)
                if sync_level:result,stats['level_xp_changes']=gui_copy_donor_level(result,donor)
                return result,{'blocks':blocks,'stats':stats}
            self.run_edit(patch,'Clone layout')
    def scan_ids(self):
        path,_=QFileDialog.getOpenFileName(self,'Chọn friend_city / friend_honor XML','','XML (*.xml);;Tất cả (*)')
        if not path:return
        xml=B.canonical_xml(Path(path).read_bytes().rstrip(b'\x00'));B.validate_xml_document(xml,'XML');rows=B.extract_related_city_ids(xml);dialog=NativeDialog('City ID liên quan',self,f'Tìm thấy {len(rows)} dấu vết City ID.');dialog.buttons.button(QDialogButtonBox.Apply).hide();tree=QTreeWidget();tree.setHeaderLabels(['City ID','Quan hệ','Bằng chứng']);tree.header().setSectionResizeMode(2,QHeaderView.Stretch)
        for row in rows:QTreeWidgetItem(tree,list(row))
        dialog.body.addWidget(tree);dialog.exec_()
    def network_dialog(self):
        if not B.SESSION.friends:raise B.SaveToolError('Mở LocalInfo có bạn bè trước.')
        dialog=NativeDialog('Friend Network',self,'Quét mạng bạn bè, lọc trùng City ID và tìm tài khoản theo level.',apply_text='Bắt đầu quét');dialog.resize(720,520);form=dialog.form();mode=QComboBox();mode.addItem('Sequential · theo thứ tự','1');mode.addItem('Random · xáo trộn','2');depth=number(2,1,10);target=number(100,1,100000);limit=number(5000,1,100000);level=text_field('>100');delay=QDoubleSpinBox();delay.setRange(0,60);delay.setValue(.5);delay.setDecimals(2)
        for label,w in [('Kiểu quét',mode),('Độ sâu',depth),('Số tài khoản mục tiêu',target),('Giới hạn FetchCity',limit),('Điều kiện level (>100, >=150, 100-200)',level),('Nghỉ giữa request (giây)',delay)]:form.addRow(label,w)
        dialog.footer.setText('Kết quả được lưu theo từng bước trong workspace_simple/friend_network. Bấm Dừng quét để dừng sau request đang chạy.')
        def validate():
            B._parse_level_filter(level.text())
            if limit.value()<target.value():raise B.SaveToolError('Giới hạn FetchCity phải ≥ số tài khoản mục tiêu.')
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            answers=iter([mode.currentData(),str(depth.value()),str(target.value()),str(limit.value()),level.text(),str(delay.value()),'y'])
            def action():
                original=B.input
                def configured_input(prompt=''):
                    try:return next(answers)
                    except StopIteration:raise B.SaveToolError('Friend Network yêu cầu tham số ngoài cấu hình GUI.')
                B.input=configured_input
                try:B.crawl_friend_network_prompt()
                finally:B.input=original
            self.start(action,'Friend Network')
    def attribute_table(self,title,description):
        dialog=NativeDialog(title,self,description);tree=QTreeWidget();tree.setHeaderLabels(['Thuộc tính','Giá trị']);tree.header().setSectionResizeMode(1,QHeaderView.Stretch);dialog.body.addWidget(tree,1);row=QHBoxLayout();add=QPushButton('+ Thuộc tính');remove=QPushButton('Xóa dòng');row.addWidget(add);row.addWidget(remove);dialog.body.addLayout(row)
        def new_row(key='',value=''):
            item=QTreeWidgetItem(tree,[key,value]);item.setFlags(item.flags()|Qt.ItemIsEditable);return item
        add.clicked.connect(lambda:new_row());remove.clicked.connect(lambda:tree.takeTopLevelItem(tree.indexOfTopLevelItem(tree.currentItem())) if tree.currentItem() else None)
        def values():
            result={}
            for i in range(tree.topLevelItemCount()):
                item=tree.topLevelItem(i);key=item.text(0).strip()
                if not re.fullmatch(r'[A-Za-z_][\w:.-]*',key):raise B.SaveToolError('Tên thuộc tính không hợp lệ.')
                if key in result:raise B.SaveToolError('Thuộc tính bị trùng: '+key)
                result[key]=item.text(1)
            if not result:raise B.SaveToolError('Thêm ít nhất một thuộc tính.')
            return result
        return dialog,tree,new_row,values
    def var_editor(self):
        B.SESSION.require_loaded();dialog,tree,new_row,values=self.attribute_table('Sửa Var','Chọn Var, tải thuộc tính rồi sửa trực tiếp từng dòng. Không cho thay name của Var.');form=dialog.form();names=list(dict.fromkeys(B.parse_attributes(m.group(0)).get('name','') for m in re.finditer(rb'<Var\b[^>]*>',B.SESSION.current_xml)));var=QComboBox();var.setEditable(True);var.addItems([n for n in names if n]);form.addRow('Tên Var',var);load=QPushButton('Tải thuộc tính');dialog.body.addWidget(load)
        def load_attrs():
            try:
                attrs=B.read_var(B.SESSION.current_xml,var.currentText());tree.clear()
                for k,v in attrs.items():
                    if k!='name':new_row(k,v)
            except Exception as exc:QMessageBox.warning(dialog,'Var',str(exc))
        load.clicked.connect(load_attrs)
        def validate():
            updates=values()
            if 'name' in updates:raise B.SaveToolError('Không được đổi name của Var.')
            B.read_var(B.SESSION.current_xml,var.currentText())
        dialog.validator=validate
        if names:load_attrs()
        if dialog.exec_()==QDialog.Accepted:
            name=var.currentText().strip();updates=values();self.run_edit(lambda:B.patch_var(B.SESSION.current_xml,name,updates),'Sửa Var')
    def tag_editor(self):
        B.SESSION.require_loaded();dialog,tree,new_row,values=self.attribute_table('Sửa thuộc tính tag','Công cụ XML chuyên sâu: điều kiện tìm tag dùng key=value, phân cách dấu phẩy. Thuộc tính cập nhật sửa trực tiếp trong bảng.');form=dialog.form();tag=text_field();selector=text_field();selector.setPlaceholderText('set1=abc,a1=1982');form.addRow('Tên tag',tag);form.addRow('Điều kiện tìm',selector);new_row('value','')
        def validate():
            if not re.fullmatch(r'[A-Za-z_][\w:.-]*',tag.text().strip()):raise B.SaveToolError('Tên tag không hợp lệ.')
            filters=B.parse_key_value_pairs(selector.text());updates=values()
            if not filters:raise B.SaveToolError('Cần ít nhất một thuộc tính tìm tag.')
            if set(filters)&set(updates):raise B.SaveToolError('Không sửa thuộc tính đang dùng để tìm tag.')
            B.read_tag_attributes(B.SESSION.current_xml,tag.text().strip(),filters)
        dialog.validator=validate
        if dialog.exec_()==QDialog.Accepted:
            name=tag.text().strip();filters=B.parse_key_value_pairs(selector.text());updates=values();self.run_edit(lambda:B.patch_tag_attributes(B.SESSION.current_xml,name,filters,updates),'Sửa tag')
    def restore_single(self):
        files=sorted(B.BACKUP_DIR.glob('*.mGameInfo'),reverse=True)
        if not files:raise B.SaveToolError('Chưa có backup local *.mGameInfo. Backup cặp ZIP nằm trong tab VIP → History.')
        dialog=NativeDialog('Khôi phục backup local',self,'Chọn backup mGameInfo cần ghi vào thiết bị.',apply_text='Khôi phục vào game');combo=QComboBox()
        for path in files:combo.addItem(path.name,str(path))
        dialog.body.addWidget(combo)
        if dialog.exec_()==QDialog.Accepted:
            path=Path(combo.currentData())
            if QMessageBox.question(self,'Khôi phục','Ghi backup '+path.name+' vào thiết bị?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)!=QMessageBox.Yes:return
            def action():
                if not B.SOURCE_FILE.exists():B.atomic_write(B.SOURCE_FILE,B.pull_save_from_device())
                B.restore_local_backup(path);B.print('Đã khôi phục. Kết nối/tải save lại trước khi chỉnh sửa tiếp.')
            self.start(action,'Khôi phục backup local')


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app=QApplication(sys.argv); app.setApplicationName('Township Studio'); app.setStyle('Fusion');apply_theme(load_theme()[1]);app.interface_language=InterfaceLanguage(app)
    window=NativeWindow();apply_theme(ACTIVE_THEME);window.show();app.interface_language.translate_all();return app.exec_()

if __name__=='__main__': raise SystemExit(main())

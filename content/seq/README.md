The following is a rough guide to the construction of the ids of the sequences:

```
=       3d_equals
>       3c_greater_than
@       40_at

^       5e_hat
`       60_backtick

{       7b_left_brace
|       7c_pipe
}       7d_right_brace
~       7e_tilde

c0-a                    a_c0_{a-z}

ESC 6                   a_esc_a{0-9} (numeric)
                        a_esc_c{a-z} (CAPS)
                        a_esc_s{a-z} (lower)
                        a_esc_x40_at

ESC # 3                 a_esc_zhash_a{0-9} (numeric)

ESC % @                 a_esc_zpercent__at__
                        a_esc_zpercent_c{a-z} (CAPS)

ESC ␣ F                 a_esc_zspace_c{a-z} (CAPS)

ESC [ Ⓝ A              csi_ca

ESC ? Ⓝ A              csi_ca__p

ESC > Ⓝ A              csi_ca__q

ESC = Ⓝ A              csi_ca__r

ESC Ⓝ ! A              csi_ca_t_bang

ESC [ Ⓝ $ A            csi_ca_t_dollar

ESC [ Ⓝ # A            csi_ca_t_hash

ESC [ Ⓝ + A            csi_ca_t_plus

ESC [ Ⓝ " A            csi_ca_t_quote

ESC [ Ⓝ ␣ A            csi_ca_t_space

ESC [ Ⓝ * A            csi_ca_t_star

ESC [ Ⓝ ' A            csi_ca_t_tick



ESC [ Ⓝ ^              csi_x5e_hat


ESC P ...               dcs

ESC ]                   osc
```

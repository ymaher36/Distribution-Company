PGDMP         /                 {         
   first_test    15.0    15.0     p           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            q           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            r           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            s           1262    79854 
   first_test    DATABASE     �   CREATE DATABASE first_test WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE first_test;
                postgres    false            �            1259    80001    locations_governorate    TABLE     m   CREATE TABLE public.locations_governorate (
    id uuid NOT NULL,
    name character varying(30) NOT NULL
);
 )   DROP TABLE public.locations_governorate;
       public         heap    postgres    false            m          0    80001    locations_governorate 
   TABLE DATA           9   COPY public.locations_governorate (id, name) FROM stdin;
    public          postgres    false    232   �       �           2606    80005 )   locations_governorate locations_city_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public.locations_governorate
    ADD CONSTRAINT locations_city_pkey PRIMARY KEY (id);
 S   ALTER TABLE ONLY public.locations_governorate DROP CONSTRAINT locations_city_pkey;
       public            postgres    false    232            m   a  x�MT[n#7�֜b/���|�%?|4�ag-�E�v��Ifn�Iy|H`X�U�UMz+�PhmP/��,2(�½q�b�>o_�{�?������1%O����Q�]��V�R����Y_���w ���,�"�I��Q�3R�F�W�/����v\��;�ߖ��Z��T����I�cjż8v��tE����<wː���'��R��f����E������_n�߶��}��k�Դ0�@ۂ��=�ل�_0�햤�y�"���$	u�Lɫ���z��n{�N�âlǄk���̉z2%��sH���u�_��r�U��QN�7=�*q
�z1��r��+l|X��?o���Z�'�fa�YR��C�|������r�bMh����$��4�$7n�?����p���qwF��#�6)E��!$9�[�vf��,��FX�0�:@M��Ms&�+�U��麲��q=/3z��g�V�-�&��+���\�K��k�bش�=k.KC�хvC���-	T"����4?���Iv��]�/�!b��%^��r%A���h�⏻���n�ѻ9(�	�\�0��#�}Lŏw�	���nw�%�z�1R����G�d\�w�+ vƆ��Q�dT�\;clwV��.�jcƫU����e;�Q��u�Q�n����x��G	_��/_.1�gT��1��53�ޣ�A\N����n���?�ļߖ�G�e�جRo����Hr)N���;�ַ�s.�P�Qub�dFaL�)��,߮\c���r���Ρxa]D�=[�;���C�2�e�кݱ�)(�MV|��?��m_������tR� �fv��@���?�����˲�>��     
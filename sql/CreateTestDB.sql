CREATE TABLE test (
    `list_va` NUMERIC(7, 2),
    `list_iodid` NUMERIC(7, 4),
    `list_vc` NUMERIC(9, 3),
    `list_ve` NUMERIC(7, 2),
    `list_calcium` NUMERIC(6, 3),
    `list_kohlenhydrate` NUMERIC(8, 2),
    `list_linolsaeure` NUMERIC(8, 3),
    `list_fat` NUMERIC(5, 2),
    `list_kalium` NUMERIC(6, 2),
    `list_linolensaeure` NUMERIC(7, 3),
    `list_vb2` NUMERIC(6, 2),
    `list_vb1` NUMERIC(7, 3),
    `list_eisen` NUMERIC(7, 2),
    `list_vb6` NUMERIC(7, 3),
    `list_magnesium` NUMERIC(5, 2),
    `list_recipe_href` VARCHAR(69) CHARACTER SET utf8,
    `list_ballaststoffe` NUMERIC(8, 3),
    `list_eiwei` NUMERIC(8, 2),
    `list_kcal` NUMERIC(6, 2),
    `list_zink` NUMERIC(7, 3),
    `list_vb12` NUMERIC(3, 2)
);
INSERT INTO test VALUES (621.76,164.625,38200.0,3194.5,593.45,11432.25,2679.93,68.37,1311.09,766.98,1578.35,2601.75,6029.25,1643.75,139.6,'/rezept/501707/Gefuellte-Zucchini-und-Paprika.html',3637.4,88105.5,1018.47,7639.2,4.8);
INSERT INTO test VALUES (1313.81,40.04,14030.0,13965.9,488.65,24891.7,11063.42,111.55,2857.59,1453.79,1903.5,1107.25,14869.85,3250.2,238.3,'/rezept/501195/Haehnchensteaks-mit-Austernpilz-Frischkaese-Sosse.html',20895.8,147085.4,1684.27,9383.75,3.6);
INSERT INTO test VALUES (1547.91,82.47,251550.0,6342.8,477.3,29586.8,8056.52,136.65,2937.09,1855.34,1949.6,773.1,7592.4,2363.7,172.3,'/rezept/501146/Mistkratzerli-aus-der-Schweiz-Heidelbeerdessert.html',15230.3,79752.5,1731.62,5681.6,2.35);
INSERT INTO test VALUES (4723.14,26.9875,120496.225,3595.65,442.025,33815.7,1990.655,64.27,2132.79,629.605,700.4,501.875,3271.5,871.075,136.4,'/rezept/500992/Moehren-Paprika-Suppe.html',13965.525,30551.2,839.27,2071.125,1.0);
INSERT INTO test VALUES (1438.99,39.1,113646.25,7723.0,576.4,23933.6,2939.68,68.65,1109.64,527.43,1191.8,575.2,4979.2,492.2,96.65,'/rezept/500793/Gesundes-Abendessen.html',7076.3,45042.0,898.5,5016.15,3.49);
INSERT INTO test VALUES (487.43,18.29,227226.56,1411.16,306.94,31543.8,425.378,1.82,1678.72,468.17,409.02,435.6,4398.46,1037.32,114.48,'/rezept/500551/Blumenkohl-Sueppchen.html',13928.08,13222.7,203.46,2301.6,0.0);
INSERT INTO test VALUES (434.84,3.695,26930.0,7725.65,195.25,15012.8,3511.53,9.74,545.34,565.73,259.15,383.6,4601.4,490.2,75.4,'/rezept/498803/Musik-spezial-Zwiebelsalat.html',4414.45,7394.25,183.5,1528.45,0.0);
INSERT INTO test VALUES (169.49,25.013,50506.0,13550.5,275.47,147397.5,21651.71,54.95,1846.96,4468.05,555.6,1127.8,11810.4,1126.3,261.11,'/rezept/498621/Champignon-Gemuese-Spaghetti.html',18810.8,45877.0,1274.22,5589.85,0.0);
INSERT INTO test VALUES (15418.28,48.55,621140.0,15439.0,562.5,102243.0,1858.57,4.36,5220.04,578.84,866.6,1766.3,10259.4,3848.8,278.7,'/rezept/497810/Gemuesesuppe.html',46521.4,25247.0,566.69,4638.1,0.0);
INSERT INTO test VALUES (247.14,11.14,63520.0,1647.1,126.5,24609.7,715.23,20.67,449.14,359.33,186.95,87.95,1026.4,149.05,53.55,'/rezept/496245/Karotten-Selleriesalat-selber-machen.html',2600.0,4082.0,321.35,548.6,0.45);


select list_recipe_href,list_kcal,list_va,list_iodid,list_vc,list_ve,list_calcium,list_kohlenhydrate,list_linolsaeure,list_fat,list_kalium,
 list_linolensaeure,list_vb2, list_vb1, list_eisen, list_vb6, list_magnesium, list_ballaststoffe, list_eiwei, list_zink, list_vb12 from test;

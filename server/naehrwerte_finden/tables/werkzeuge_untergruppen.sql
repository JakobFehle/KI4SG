-- phpMyAdmin SQL Dump
-- version 3.3.2deb1ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 17. Dezember 2012 um 14:22
-- Server Version: 5.1.66
-- PHP-Version: 5.3.2-1ubuntu4.18

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `vamos`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `werkzeuge_untergruppen`
--

CREATE TABLE IF NOT EXISTS `werkzeuge_untergruppen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bezeichnung` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `obergruppen_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=198 ;

--
-- Daten für Tabelle `werkzeuge_untergruppen`
--

INSERT INTO `werkzeuge_untergruppen` (`id`, `bezeichnung`, `obergruppen_id`) VALUES
(1, 'Pfanne', 1),
(2, 'Topf', 2),
(3, 'Backofen', 3),
(4, 'Backpapier', 4),
(5, 'Form', 5),
(6, 'Kühlschrank', 6),
(7, 'Backblech', 9),
(8, 'Auflaufform', 5),
(9, 'Springform', 5),
(10, 'Umluft', 7),
(11, 'Deckel', 2),
(12, 'Sieb', 8),
(13, 'Blech', 9),
(14, 'Teller', 10),
(15, 'Herd', 3),
(16, 'Gabel', 10),
(17, 'Schiene', 3),
(18, 'Wok', 11),
(19, 'Alufolie', 12),
(20, 'Mixer', 13),
(21, 'Tellern', 10),
(22, 'Glas', 10),
(23, 'Schneebesen', 14),
(24, 'Löffel', 10),
(25, 'Esslöffel', 10),
(26, 'Folie', 15),
(27, 'Bräter', 16),
(28, 'Unterhitze', 3),
(29, 'Tortenring', 17),
(30, 'Waffeleisen', 18),
(31, 'Gläser', 10),
(32, 'Tasse', 10),
(33, 'Tuch', 19),
(34, 'Spritzbeutel', 20),
(35, 'Teelöffel', 10),
(36, 'Küchenmaschine', 21),
(37, 'Küchenpapier', 22),
(38, 'Heißluft', 7),
(39, 'Handrührgerät', 23),
(40, 'Grill', 24),
(41, 'Knethaken', 23),
(42, 'Rührschüssel', 25),
(43, 'Pürierstab', 26),
(44, 'Kastenform', 5),
(45, 'Frischhaltefolie', 15),
(46, 'Kuchengitter', 27),
(47, 'Förmchen', 5),
(48, 'Mikrowelle', 28),
(49, 'Gefäß', 5),
(50, 'Backrohr', 3),
(51, 'Backform', 5),
(52, 'Küchenkrepp', 22),
(53, 'Gefrierbeutel', 29),
(54, 'Formen', 5),
(55, 'Rost', 31),
(56, 'Küchentuch', 22),
(57, 'Klarsichtfolie', 15),
(58, 'Springformrand', 5),
(59, 'Tassen', 10),
(60, 'Tortenplatte', 30),
(61, 'Herdplatte', 3),
(62, 'Bleche', 9),
(63, 'Schälchen', 5),
(64, 'Gitter', 31),
(65, 'Fettpfanne', 9),
(66, 'Nudelholz', 32),
(67, 'Brett', 33),
(68, 'Stabmixer', 13),
(69, 'Schaumlöffel', 34),
(70, 'Handrührgerätes', 23),
(71, 'Presse', 35),
(72, 'Bratpfanne', 1),
(73, 'Backbleche', 9),
(74, 'Zahnstocher', 36),
(75, 'Beutel', 29),
(76, 'Teelöffeln', 10),
(77, 'Kuchenrost', 27),
(78, 'Holzlöffel', 37),
(79, 'Schnellkochtopf', 38),
(80, 'Zauberstab', 26),
(81, 'Kelle', 39),
(82, 'Salatschüssel', 25),
(83, 'Backofens', 3),
(84, 'Arbeitsplatte', 33),
(85, 'Rührgerät', 23),
(86, 'Schmortopf', 16),
(87, 'Küchengarn', 40),
(88, 'Esslöffeln', 10),
(89, 'Oberhitze', 3),
(90, 'Mixstab', 13),
(91, 'Kuchenform', 5),
(92, 'Sterntülle', 41),
(93, 'Geschirrtuch', 19),
(94, 'Schaumkelle', 34),
(95, 'Fleischwolf', 42),
(96, 'Sparschäler', 43),
(97, 'Zahnstochern', 36),
(98, 'Handmixer', 13),
(99, 'Muffinform', 44),
(100, 'Pinsel', 45),
(101, 'Römertopf', 46),
(102, 'Gasherd', 3),
(103, 'Topfboden', 2),
(104, 'Schere', 47),
(105, 'Kochlöffel', 37),
(106, 'Tarteform', 5),
(107, 'Haarsieb', 8),
(108, 'Pergamentpapier', 4),
(109, 'Backrahmen', 48),
(110, 'Schüsseln', 25),
(111, 'Gugelhupfform', 5),
(112, 'Springformboden', 5),
(113, 'Ausstecher', 49),
(114, 'Tüte', 29),
(115, 'Eismaschine', 50),
(116, 'Schöpfkelle', 39),
(117, 'Rührbesen', 14),
(118, 'Lochtülle', 41),
(119, 'Muffinblech', 44),
(120, 'Schöpflöffel', 39),
(121, 'Suppentassen', 10),
(122, 'Tülle', 41),
(123, 'Suppenteller', 10),
(124, 'Holzspieße', 36),
(125, 'Servierplatte', 51),
(126, 'Nudelmaschine', 52),
(127, 'Schüsselchen', 25),
(128, 'Holzspießchen', 36),
(129, 'Backofengrill', 3),
(130, 'Holzstäbchen', 36),
(131, 'Grillpfanne', 53),
(132, 'Quicheform', 5),
(133, 'Bratentopf', 2),
(134, 'Formrand', 5),
(135, 'Rührbecher', 54),
(136, 'Gefrierschrank', 6),
(137, 'Messbecher', 54),
(138, 'Tiefkühler', 6),
(139, 'Kochplatte', 3),
(140, 'Grillrost', 31),
(141, 'Schraubglas', 55),
(142, 'Plastikbeutel', 29),
(143, 'Dessertgläser', 56),
(144, 'Umluftherd', 7),
(145, 'Mixtopf', 54),
(146, 'Ringform', 5),
(147, 'Portionstellern', 57),
(148, 'Kuchenblech', 9),
(149, 'Toaster', 58),
(150, 'Pfännchen', 1),
(151, 'Handrührer', 23),
(152, 'Kartoffelstampfer', 59),
(153, 'Backtrennpapier', 4),
(154, 'Elektroherd', 3),
(155, 'Schneidstab', 26),
(156, 'Kaffeetasse', 10),
(157, 'Terrinenform', 5),
(158, 'Fettfangschale', 9),
(159, 'Moulinette', 21),
(160, 'Tüten', 29),
(161, 'Tiefkühlfach', 6),
(162, 'Dessertteller', 10),
(163, 'Cocktailglas', 60),
(164, 'Spritztülle', 41),
(165, 'Löffels', 10),
(166, 'Eisfach', 6),
(167, 'Mixers', 13),
(168, 'Gläschen', 10),
(169, 'Haushaltspapier', 22),
(170, 'Töpfchen', 2),
(171, 'Marmeladengläser', 55),
(172, 'Kochlöffelstiel', 37),
(173, 'Metallschüssel', 25),
(174, 'Tablett', 51),
(175, 'Dessertschalen', 56),
(176, 'Topfdeckel', 2),
(177, 'Küchenschere', 47),
(178, 'Hobel', 61),
(179, 'Servierteller', 10),
(180, 'Mixbecher', 54),
(181, 'Backförmchen', 5),
(182, 'Lasagneform', 5),
(183, 'Kugelausstecher', 62),
(184, 'Schaschlikspieße', 36),
(185, 'Backfolie', 4),
(186, 'Zestenreißer', 63),
(187, 'Suppenkelle', 39),
(188, 'Salatschleuder', 64),
(189, 'Brettchen', 33),
(190, 'Kaffeemühle', 65),
(191, 'Töpfe', 2),
(192, 'Wasserkocher', 66),
(193, 'Küchenreibe', 61),
(194, 'Schüssel', 25),
(195, 'Schale', 25),
(196, 'Ofen', 3),
(197, 'Friteuse', 67);

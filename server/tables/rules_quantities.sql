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
-- Tabellenstruktur für Tabelle `rules_quantities`
--

CREATE TABLE IF NOT EXISTS `rules_quantities` (
  `unit` text COLLATE utf8_unicode_ci NOT NULL,
  `grams` float NOT NULL,
  `ingredient` text COLLATE utf8_unicode_ci NOT NULL,
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `constamount` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=286 ;

--
-- Daten für Tabelle `rules_quantities`
--

INSERT INTO `rules_quantities` (`unit`, `grams`, `ingredient`, `ID`, `constamount`) VALUES
('ml', 1, '', 1, 0),
('g', 1, '', 2, 0),
('gramm', 1, '', 3, 0),
('liter', 1000, '', 4, 0),
('kilo', 1000, '', 5, 0),
('kg', 1000, '', 6, 0),
('kilogramm', 1000, '', 7, 0),
('', 30, 'lauchzwiebel', 112, 0),
('', 1, 'salz', 9, 1),
('prise', 1, 'salz', 10, 1),
('n.B.', 1, 'salz', 11, 1),
('prise', 1, '', 12, 0),
('', 50, 'bratwurst', 110, 0),
('', 50, 'cabanossi', 270, 0),
('glas', 240, 'tomaten', 22, 0),
('dose', 240, 'tomaten', 23, 0),
('cl', 10, '', 113, 0),
('pck.', 10, '', 109, 0),
('pck.', 150, 'feta', 35, 0),
('dosen', 400, '', 108, 0),
('dose', 400, 'kichererbsen', 31, 0),
('zehe', 2, 'knoblauch', 37, 0),
('tasse', 120, 'reis', 38, 0),
('el', 15, 'reis', 39, 0),
('el', 15, '', 40, 0),
('tl', 5, '', 41, 0),
('tasse', 125, '', 42, 0),
('', 190, 'aal', 43, 0),
('', 1000, 'ananas', 44, 0),
('', 115, 'apfel', 46, 0),
('', 140, 'apfelsine', 47, 0),
('', 45, 'aprikose', 48, 0),
('', 400, 'aubergine', 51, 0),
('', 120, 'artischocke', 50, 0),
('', 225, 'avocado', 52, 0),
('', 100, 'banane', 53, 0),
('', 500, 'bier', 54, 0),
('', 130, 'birne', 55, 0),
('', 500, 'blumenkohl', 56, 0),
('', 60, 'brötchen', 57, 0),
('messerspitze', 3, 'butter', 58, 0),
('tl', 4, 'butter', 59, 0),
('el', 10, 'butter', 60, 0),
('packung', 250, 'butter', 61, 0),
('packung', 150, 'camembert', 62, 0),
('', 10, 'champignons', 63, 0),
('', 50, 'hühnerei', 96, 0),
('', 20, 'eigelb', 65, 0),
('', 35, 'eiweiß', 66, 0),
('', 300, 'salat', 73, 0),
('', 400, 'grapefruit', 68, 0),
('', 600, 'melone', 69, 0),
('', 100, 'kartoffel', 70, 0),
('', 2, 'knoblauchzehe', 71, 0),
('', 5, 'knoblauch', 72, 0),
('ml', 0.008, 'fleischbrühe', 267, 0),
('', 200, 'maiskolben', 75, 0),
('tl', 5, 'mehl', 78, 0),
('el', 12, 'mehl', 77, 0),
('', 10, 'mirabelle', 79, 0),
('', 60, 'karotte', 80, 0),
('', 115, 'nektarine', 81, 0),
('', 150, 'orange', 82, 0),
('', 140, 'paprika', 83, 0),
('', 120, 'pfirsich', 84, 0),
('', 35, 'pflaume', 85, 0),
('', 800, 'rotkohl', 86, 0),
('', 500, 'gurke', 87, 0),
('', 500, 'salatgurke', 88, 0),
('', 60, 'tomate', 89, 0),
('', 720, 'wirsing', 90, 0),
('', 60, 'zitrone', 91, 0),
('', 175, 'zucchini', 92, 0),
('', 100, 'zwiebel', 93, 0),
('', 15, 'sonnenblumenöl', 268, 1),
('', 1, 'pfeffer', 95, 1),
('', 1, 'speisesalz', 97, 1),
('glas', 200, '', 102, 0),
('dose', 400, '', 101, 0),
('gläser', 200, '', 107, 0),
('kl. glas', 80, '', 103, 0),
('becher', 200, '', 104, 0),
('', 100, 'zwiebeln', 105, 0),
('scheibe', 80, 'ananas', 106, 0),
('', 80, 'bleichsellerie', 114, 0),
('', 140, 'paprikaschoten', 115, 0),
('tropfen', 0.3, '', 116, 0),
('blätter', 10, '', 117, 0),
('blatt', 10, '', 118, 0),
('bund', 15, '', 119, 0),
('', 5, 'essig', 120, 1),
('schuss', 5, '', 121, 0),
('', 5, 'petersilienblatt', 127, 0),
('', 5, 'petersilie', 125, 0),
('', 5, 'oregano', 126, 0),
('', 1, 'chili', 128, 0),
('', 1, 'kräutersalz', 129, 1),
('', 1, 'kräuter', 130, 0),
('', 2, 'chilisoße', 131, 0),
('', 5, 'olivenöl', 132, 0),
('', 5, 'ingwerknolle', 133, 0),
('', 1, 'koriander', 134, 0),
('', 2, 'sojasoße', 135, 0),
('msp.', 0.2, '', 136, 0),
('', 720, 'wirsingkohl', 137, 0),
('pkt.', 8, 'vanillezucker', 138, 0),
('', 30, 'schalotte', 139, 0),
('', 1, 'thymian', 140, 0),
('', 1, 'rosmarin', 141, 0),
('prise', 0.2, 'muskatnuss', 144, 0),
('', 0.2, 'muskatnuss', 143, 0),
('', 100, 'kartoffeln', 145, 0),
('', 900, 'knollensellerie', 146, 0),
('tüte', 8, 'vanillezucker', 147, 0),
('', 60, 'tomaten', 148, 0),
('', 60, 'zitronen', 149, 0),
('etwas', 5, '', 150, 0),
('', 60, 'mozzarella', 151, 0),
('', 15, 'garnele', 152, 0),
('cm', 1, 'tomatenmark', 153, 0),
('', 0.2, 'lorbeerblatt', 154, 0),
('stange', 0.6, 'zimt', 155, 0),
('', 0.1, 'gewürznelken', 156, 0),
('', 0.1, 'anis', 157, 0),
('', 2, 'basilikum', 158, 0),
('', 1, 'salbei', 159, 0),
('', 2, 'schnittlauch', 160, 0),
('', 0.5, 'currypulver', 161, 0),
('', 400, 'rüben', 162, 0),
('', 70, 'granatapfel', 163, 0),
('', 5, 'bratfett', 164, 0),
('würfel', 30, 'hefe', 165, 0),
('', 5, 'vanilleschote', 166, 0),
('zweig', 4, '', 172, 0),
('pkt.', 300, 'spinat', 170, 0),
('pkt.', 300, 'blattspinat', 171, 0),
('', 80, 'tortenboden', 175, 0),
('pkt.', 15, 'backpulver', 174, 0),
('', 10, 'waffeln', 176, 0),
('', 40, 'tortilla', 177, 0),
('scheibe', 20, 'weißbrot', 178, 0),
('', 30, 'kiwi', 179, 0),
('pkt.', 450, 'blätterteig', 180, 0),
('', 10, 'champignon', 181, 0),
('', 130, 'fenchel', 182, 0),
('', 130, 'chicoree', 183, 0),
('', 40, 'limette', 184, 0),
('flasche', 500, '', 185, 0),
('', 1000, 'chinakohl', 186, 0),
('', 500, 'eisbergsalat', 187, 0),
('dl', 100, '', 188, 0),
('gr. dose', 425, '', 189, 0),
('', 1, 'majoran', 190, 0),
('platte', 20, 'blätterteig', 191, 0),
('', 800, 'broccoli', 192, 0),
('', 200, 'fische', 195, 1),
('', 200, 'kalb', 196, 1),
('scheibe', 4, 'parmaschinken', 197, 0),
('scheiben', 4, 'parmaschinken', 198, 0),
('scheiben', 4, 'schinken', 199, 0),
('scheibe', 4, 'schinken', 200, 0),
('paket', 300, 'blattspinat', 201, 0),
('paket', 300, 'spinat', 202, 0),
('', 200, 'wildkaninchen', 203, 1),
('', 200, 'hauskaninchen', 204, 1),
('', 200, 'brathähnchen', 205, 1),
('', 200, 'lamm', 206, 1),
('', 100, 'mandarine ', 207, 0),
('scheiben', 3, 'salami', 208, 0),
('scheibe', 3, 'salami', 209, 0),
('', 200, 'pute', 210, 1),
('', 200, 'hähnchenbrustfilet', 211, 1),
('', 3, 'sardellenfilet', 212, 0),
('tüte', 10, 'kokosnuss', 213, 0),
('', 200, 'schwein', 214, 1),
('', 200, 'ente', 215, 1),
('', 200, 'rind', 216, 1),
('', 5, 'löffelbiskuit', 217, 0),
('l', 8, 'fleischbrühe', 273, 0),
('', 800, 'weißkohl', 219, 0),
('liter', 8, 'gemüsebrühe', 238, 0),
('liter', 8, 'fleischbrühe', 272, 0),
('', 110, 'porree', 233, 0),
('stück', 150, 'brathähnchen', 266, 0),
('port.', 125, 'eierteigwaren', 263, 0),
('l', 8, 'gemüsebrühe', 239, 0),
('l', 8, 'brühe', 240, 0),
('liter', 8, 'brühe', 241, 0),
('ml', 0.008, 'brühe', 242, 0),
('ml', 0.008, 'gemüsebrühe', 243, 0),
('pck', 450, 'blätterteig', 274, 0),
('pck.', 450, 'blätterteig', 275, 0),
('tüte', 250, 'parmesan', 276, 0),
('l', 8, 'hühnerbrühe/-bouillon', 280, 0),
('ml', 0.008, 'hühnerbrühe/-bouillon', 279, 0),
('liter', 8, 'hühnerbrühe/-bouillon', 281, 0),
('paket', 450, 'blätterteig', 284, 0),
('scheibe', 20, 'blätterteig', 283, 0),
('', 1, 'paprika edelsüß', 285, 0);

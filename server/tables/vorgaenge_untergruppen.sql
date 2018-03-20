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
-- Tabellenstruktur für Tabelle `vorgaenge_untergruppen`
--

CREATE TABLE IF NOT EXISTS `vorgaenge_untergruppen` (
  `obergruppen_id` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bezeichnung` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=129 ;

--
-- Daten für Tabelle `vorgaenge_untergruppen`
--

INSERT INTO `vorgaenge_untergruppen` (`obergruppen_id`, `id`, `bezeichnung`) VALUES
(1, 1, 'backe'),
(1, 2, 'backt'),
(1, 3, 'heizen'),
(1, 4, 'toasten'),
(1, 5, 'erhitz'),
(1, 6, 'wärmen'),
(1, 7, 'erwärmt'),
(1, 8, 'gratinieren'),
(1, 9, 'heizt'),
(2, 10, 'kochen'),
(2, 11, 'garen'),
(2, 12, 'durchziehen'),
(2, 13, 'kocht'),
(2, 14, 'köcheln'),
(2, 15, 'köchelt'),
(2, 16, 'ziehen'),
(2, 17, 'durchgezogen'),
(2, 18, 'dünsten'),
(2, 19, 'pochier'),
(3, 20, 'abbinden'),
(3, 21, 'reduzieren'),
(3, 22, 'reduziert'),
(3, 23, 'andick'),
(3, 24, 'eindick'),
(3, 25, 'eingedickt'),
(4, 26, 'frittier'),
(5, 27, 'quellen'),
(5, 28, 'aufgegangen'),
(5, 29, 'gehen'),
(6, 30, 'gelieren'),
(7, 31, 'braten'),
(7, 32, 'schwitzen'),
(7, 33, 'zerlassen'),
(7, 34, 'auslassen'),
(7, 35, 'bräunen'),
(7, 36, 'schmelzen'),
(7, 37, 'geschmolzen'),
(7, 38, 'zerlaufen'),
(7, 39, 'brät'),
(8, 40, 'rösten'),
(8, 41, 'geröstet'),
(9, 42, 'blanchieren'),
(10, 43, 'schmoren'),
(11, 44, 'häuten'),
(12, 45, 'zupfen'),
(12, 46, 'zerkleiner'),
(12, 47, 'schneide'),
(12, 48, 'hacken'),
(12, 49, 'geschnitten'),
(12, 50, 'hobeln'),
(12, 51, 'mahlen'),
(12, 52, 'brechen'),
(12, 53, 'pflücken'),
(12, 54, 'stoßen'),
(12, 55, 'krümeln'),
(12, 56, 'auslösen'),
(12, 57, 'zerstampfen'),
(12, 58, 'aushöhlen'),
(12, 59, 'gewürfelt'),
(12, 60, 'würfeln'),
(12, 61, 'halbieren'),
(12, 62, 'teilen'),
(12, 63, 'entkernen'),
(12, 64, 'reiben'),
(12, 65, 'gerieben'),
(12, 66, 'bröckeln'),
(12, 67, 'schaben'),
(12, 68, 'bröseln'),
(12, 69, 'gehackt'),
(12, 70, 'zerhacken'),
(12, 71, 'entstielen'),
(12, 72, 'herauslösen'),
(12, 73, 'stifteln'),
(12, 74, 'rupfen'),
(12, 75, 'reißen'),
(12, 76, 'raspel'),
(13, 77, 'wäscht'),
(13, 78, 'waschen'),
(13, 79, 'putzen'),
(13, 80, 'abbrausen'),
(13, 81, 'säubern'),
(13, 82, 'ausspülen'),
(14, 83, 'schlagen'),
(14, 84, 'verquirlen'),
(15, 85, 'pürieren'),
(15, 86, 'passieren'),
(15, 87, 'passiert'),
(15, 88, 'durchpressen'),
(15, 89, 'dazupressen'),
(15, 90, 'stampfen'),
(15, 91, 'durchsieben'),
(15, 92, 'aufmixen'),
(16, 93, 'rühre'),
(16, 94, 'rührt'),
(17, 95, 'karamellisieren'),
(18, 96, 'abziehen'),
(18, 97, 'pellen'),
(18, 98, 'schälen'),
(18, 99, 'geschält'),
(18, 100, 'entrinden'),
(19, 101, 'einlegen'),
(20, 102, 'frieren'),
(21, 103, 'auswellen'),
(21, 104, 'ausrollen'),
(21, 105, 'auswallen'),
(22, 106, 'entkernen'),
(23, 107, 'abschrecken'),
(24, 108, 'auftauen'),
(24, 109, 'aufgetaut'),
(25, 110, 'marinieren'),
(26, 111, 'bestreichen'),
(26, 112, 'einstreichen'),
(26, 113, 'pinseln'),
(26, 114, 'streichen'),
(26, 115, 'glasieren'),
(27, 116, 'filetieren'),
(28, 117, 'einfetten'),
(28, 118, 'ausfetten'),
(28, 119, 'gefettet'),
(28, 120, 'buttern'),
(29, 121, 'aufschäumen'),
(30, 122, 'abseihen'),
(30, 123, 'absieben'),
(31, 124, 'klopfen'),
(32, 125, 'panieren'),
(32, 126, 'bemehlen'),
(32, 127, 'farinieren'),
(32, 128, 'mehlieren');

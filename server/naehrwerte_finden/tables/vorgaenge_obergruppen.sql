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
-- Tabellenstruktur für Tabelle `vorgaenge_obergruppen`
--

CREATE TABLE IF NOT EXISTS `vorgaenge_obergruppen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bezeichnung` text COLLATE utf8_unicode_ci NOT NULL,
  `typ` int(11) NOT NULL,
  `zeitverbrauchinminuten` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=33 ;

--
-- Daten für Tabelle `vorgaenge_obergruppen`
--

INSERT INTO `vorgaenge_obergruppen` (`id`, `bezeichnung`, `typ`, `zeitverbrauchinminuten`) VALUES
(1, 'backen', 1, 10),
(2, 'feuchtes garen', 1, 5),
(3, 'eindicken', 1, 5),
(4, 'frittieren', 1, 5),
(5, 'quellen', 1, 5),
(6, 'gelieren', 0, 3),
(7, 'braten', 1, 5),
(8, 'rösten', 0, 5),
(9, 'blanchieren', 0, 5),
(10, 'schmoren', 1, 5),
(11, 'häuten', 0, 5),
(12, 'zerkleinern', 0, 5),
(13, 'waschen', 0, 1),
(14, 'schlagen', 0, 2),
(15, 'pürieren', 0, 1),
(16, 'rühren', 0, 0),
(17, 'karamellisieren', 0, 3),
(18, 'abziehen', 0, 2),
(19, 'einlegen', 0, 1),
(20, 'frieren', 0, 0),
(21, 'ausrollen', 0, 10),
(22, 'entkernen', 0, 4),
(23, 'abschrecken', 0, 0),
(24, 'auftauen', 0, 0),
(25, 'marinieren', 0, 0),
(26, 'bestreichen', 0, 3),
(27, 'filetieren', 0, 10),
(28, 'einfetten', 0, 1),
(29, 'aufschäumen', 0, 5),
(30, 'abseihen', 0, 0),
(31, 'klopfen', 0, 0),
(32, 'panieren', 0, 0);

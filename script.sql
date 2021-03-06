USE [master]
GO
/****** Object:  Database [Sprint-1]    Script Date: 07/09/2017 13:27:03 ******/
CREATE DATABASE [Sprint-1]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Sprint-1', FILENAME = N'F:\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\Sprint-1.mdf' , SIZE = 2039808KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Sprint-1_log', FILENAME = N'F:\Microsoft SQL Server\MSSQL13.MSSQLSERVER\MSSQL\DATA\Sprint-1_log.ldf' , SIZE = 1122304KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [Sprint-1] SET COMPATIBILITY_LEVEL = 130
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Sprint-1].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Sprint-1] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Sprint-1] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Sprint-1] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Sprint-1] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Sprint-1] SET ARITHABORT OFF 
GO
ALTER DATABASE [Sprint-1] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Sprint-1] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Sprint-1] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Sprint-1] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Sprint-1] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Sprint-1] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Sprint-1] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Sprint-1] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Sprint-1] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Sprint-1] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Sprint-1] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Sprint-1] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Sprint-1] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Sprint-1] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Sprint-1] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Sprint-1] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Sprint-1] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Sprint-1] SET RECOVERY FULL 
GO
ALTER DATABASE [Sprint-1] SET  MULTI_USER 
GO
ALTER DATABASE [Sprint-1] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Sprint-1] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Sprint-1] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Sprint-1] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Sprint-1] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Sprint-1] SET QUERY_STORE = OFF
GO
USE [Sprint-1]
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO
USE [Sprint-1]
GO
/****** Object:  Table [dbo].[Address]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Address](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[line1] [nvarchar](max) NULL,
	[line2] [nvarchar](max) NULL,
	[postcode] [nvarchar](max) NULL,
	[county] [nvarchar](max) NULL,
	[country] [nvarchar](max) NOT NULL,
	[locationId] [int] NOT NULL,
	[city] [nvarchar](max) NULL,
 CONSTRAINT [PK_Address] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Agent]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Agent](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[agentType] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_Agent] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[GeoBoundingBox]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[GeoBoundingBox](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[locationArea] [geography] NOT NULL,
	[locationId] [int] NOT NULL,
 CONSTRAINT [PK_GeoBoundingBox] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[GeoPoint]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[GeoPoint](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[locationId] [int] NULL,
	[longitude] [float] NOT NULL,
	[latitude] [float] NOT NULL,
 CONSTRAINT [PK_GeoPoint] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Location]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Location](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[locationType] [nvarchar](max) NULL,
	[displayString] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_Location] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Mention]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Mention](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[postEntityId] [nvarchar](400) NOT NULL,
	[userAccountId] [int] NOT NULL,
 CONSTRAINT [PK_Mention] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Organisation]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Organisation](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](max) NOT NULL,
	[website] [nvarchar](max) NOT NULL,
	[agentId] [int] NOT NULL,
	[locationId] [int] NOT NULL,
 CONSTRAINT [PK_Organisation] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Person]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Person](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](max) NOT NULL,
	[agentId] [int] NOT NULL,
	[locationId] [int] NOT NULL,
 CONSTRAINT [PK_Person] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Platform]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Platform](
	[Id] [int] NOT NULL,
	[forumType] [nvarchar](max) NOT NULL,
	[forumName] [nvarchar](max) NOT NULL,
	[forumSiteUrl] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_Platform] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Post]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Post](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[postType] [nvarchar](max) NOT NULL,
	[title] [nvarchar](max) NULL,
	[body] [nvarchar](max) NOT NULL,
	[createdAt] [datetime2](7) NOT NULL,
	[importedAt] [datetime2](7) NOT NULL,
	[hasCreator] [int] NOT NULL,
	[platformPostID] [nvarchar](max) NULL,
	[SearchId] [int] NULL,
	[locationId] [int] NULL,
 CONSTRAINT [PK_Post] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PostEntity]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PostEntity](
	[Id] [nvarchar](400) NOT NULL,
	[value] [nvarchar](max) NOT NULL,
	[postId] [int] NOT NULL,
 CONSTRAINT [PK_PostEntity] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Premises]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Premises](
	[Id] [nvarchar](400) NOT NULL,
	[businessName] [nvarchar](max) NOT NULL,
	[belongToAgent] [int] NOT NULL,
	[locationId] [int] NOT NULL,
	[businessType] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_Premisses] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Rating]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Rating](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[premisesId] [nvarchar](400) NOT NULL,
	[schemeType] [nvarchar](400) NOT NULL,
	[ratingKey] [nvarchar](400) NOT NULL,
	[ratingValue] [nvarchar](400) NOT NULL,
	[ratingDate] [date] NOT NULL,
	[newRatingPending] [bit] NOT NULL,
 CONSTRAINT [PK_Rating] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Review]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Review](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[postId] [int] NOT NULL,
	[premisesId] [nvarchar](400) NOT NULL,
 CONSTRAINT [PK_Review] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Search]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Search](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[StartOfSearch] [datetime2](7) NULL,
	[EndOfSearch] [datetime2](7) NULL,
	[LocationId] [int] NULL,
	[Radius] [float] NOT NULL,
	[Note] [nvarchar](max) NOT NULL,
	[Keywords] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_Search] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UserAccount]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserAccount](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[platformAccountId] [nvarchar](max) NULL,
	[accountURL] [nvarchar](max) NULL,
	[displayName] [nvarchar](max) NULL,
	[accountCreatedAt] [datetime2](7) NULL,
	[profileDescription] [nvarchar](max) NULL,
	[verified] [bit] NULL,
	[platformId] [int] NOT NULL,
	[agentId] [int] NOT NULL,
	[lastCheckedDate] [datetime2](7) NOT NULL,
 CONSTRAINT [PK_UserAccount] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UserAccountPremisesMapping]    Script Date: 07/09/2017 13:27:03 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserAccountPremisesMapping](
	[UserAccount_Id] [int] NOT NULL,
	[Premises_Id] [nvarchar](400) NOT NULL,
 CONSTRAINT [PK_UserAccountPremissesMapping] PRIMARY KEY CLUSTERED 
(
	[UserAccount_Id] ASC,
	[Premises_Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_LocationAddress]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_LocationAddress] ON [dbo].[Address]
(
	[locationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_LocationGeoBoundingBox]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_LocationGeoBoundingBox] ON [dbo].[GeoBoundingBox]
(
	[locationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_LocationGeoPoint]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_LocationGeoPoint] ON [dbo].[GeoPoint]
(
	[locationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [IX_FK_PostEntityMention]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_PostEntityMention] ON [dbo].[Mention]
(
	[postEntityId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_UserAccountMention]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_UserAccountMention] ON [dbo].[Mention]
(
	[userAccountId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_AgentOrganisation]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_AgentOrganisation] ON [dbo].[Organisation]
(
	[agentId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_LocationOrganisation]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_LocationOrganisation] ON [dbo].[Organisation]
(
	[locationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_AgentPerson]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_AgentPerson] ON [dbo].[Person]
(
	[agentId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_LocationPerson]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_LocationPerson] ON [dbo].[Person]
(
	[locationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_UserAccountPost]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_UserAccountPost] ON [dbo].[Post]
(
	[hasCreator] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_PostPostEntity]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_PostPostEntity] ON [dbo].[PostEntity]
(
	[postId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_AgentPremisses]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_AgentPremisses] ON [dbo].[Premises]
(
	[belongToAgent] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_LocationPremisses]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_LocationPremisses] ON [dbo].[Premises]
(
	[locationId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_PostReview]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_PostReview] ON [dbo].[Review]
(
	[postId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [IX_FK_PremissesReview]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_PremissesReview] ON [dbo].[Review]
(
	[premisesId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_AgentUserAccount]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_AgentUserAccount] ON [dbo].[UserAccount]
(
	[agentId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
/****** Object:  Index [IX_FK_PlatformUserAccount]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_PlatformUserAccount] ON [dbo].[UserAccount]
(
	[platformId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [IX_FK_UserAccountPremisses_Premisses]    Script Date: 07/09/2017 13:27:03 ******/
CREATE NONCLUSTERED INDEX [IX_FK_UserAccountPremisses_Premisses] ON [dbo].[UserAccountPremisesMapping]
(
	[Premises_Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Address]  WITH CHECK ADD  CONSTRAINT [FK_LocationAddress] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[Address] CHECK CONSTRAINT [FK_LocationAddress]
GO
ALTER TABLE [dbo].[GeoBoundingBox]  WITH CHECK ADD  CONSTRAINT [FK_LocationGeoBoundingBox] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[GeoBoundingBox] CHECK CONSTRAINT [FK_LocationGeoBoundingBox]
GO
ALTER TABLE [dbo].[GeoPoint]  WITH CHECK ADD  CONSTRAINT [FK_LocationGeoPoint] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[GeoPoint] CHECK CONSTRAINT [FK_LocationGeoPoint]
GO
ALTER TABLE [dbo].[Mention]  WITH CHECK ADD  CONSTRAINT [FK_PostEntityMention] FOREIGN KEY([postEntityId])
REFERENCES [dbo].[PostEntity] ([Id])
GO
ALTER TABLE [dbo].[Mention] CHECK CONSTRAINT [FK_PostEntityMention]
GO
ALTER TABLE [dbo].[Mention]  WITH CHECK ADD  CONSTRAINT [FK_UserAccountMention] FOREIGN KEY([userAccountId])
REFERENCES [dbo].[UserAccount] ([Id])
GO
ALTER TABLE [dbo].[Mention] CHECK CONSTRAINT [FK_UserAccountMention]
GO
ALTER TABLE [dbo].[Organisation]  WITH CHECK ADD  CONSTRAINT [FK_AgentOrganisation] FOREIGN KEY([agentId])
REFERENCES [dbo].[Agent] ([Id])
GO
ALTER TABLE [dbo].[Organisation] CHECK CONSTRAINT [FK_AgentOrganisation]
GO
ALTER TABLE [dbo].[Organisation]  WITH CHECK ADD  CONSTRAINT [FK_LocationOrganisation] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[Organisation] CHECK CONSTRAINT [FK_LocationOrganisation]
GO
ALTER TABLE [dbo].[Person]  WITH CHECK ADD  CONSTRAINT [FK_AgentPerson] FOREIGN KEY([agentId])
REFERENCES [dbo].[Agent] ([Id])
GO
ALTER TABLE [dbo].[Person] CHECK CONSTRAINT [FK_AgentPerson]
GO
ALTER TABLE [dbo].[Person]  WITH CHECK ADD  CONSTRAINT [FK_LocationPerson] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[Person] CHECK CONSTRAINT [FK_LocationPerson]
GO
ALTER TABLE [dbo].[Post]  WITH CHECK ADD  CONSTRAINT [FK_Post_Location] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[Post] CHECK CONSTRAINT [FK_Post_Location]
GO
ALTER TABLE [dbo].[Post]  WITH CHECK ADD  CONSTRAINT [FK_Post_Search] FOREIGN KEY([SearchId])
REFERENCES [dbo].[Search] ([Id])
GO
ALTER TABLE [dbo].[Post] CHECK CONSTRAINT [FK_Post_Search]
GO
ALTER TABLE [dbo].[Post]  WITH CHECK ADD  CONSTRAINT [FK_UserAccountPost] FOREIGN KEY([hasCreator])
REFERENCES [dbo].[UserAccount] ([Id])
GO
ALTER TABLE [dbo].[Post] CHECK CONSTRAINT [FK_UserAccountPost]
GO
ALTER TABLE [dbo].[PostEntity]  WITH CHECK ADD  CONSTRAINT [FK_PostPostEntity] FOREIGN KEY([postId])
REFERENCES [dbo].[Post] ([Id])
GO
ALTER TABLE [dbo].[PostEntity] CHECK CONSTRAINT [FK_PostPostEntity]
GO
ALTER TABLE [dbo].[Premises]  WITH CHECK ADD  CONSTRAINT [FK_AgentPremisses] FOREIGN KEY([belongToAgent])
REFERENCES [dbo].[Agent] ([Id])
GO
ALTER TABLE [dbo].[Premises] CHECK CONSTRAINT [FK_AgentPremisses]
GO
ALTER TABLE [dbo].[Premises]  WITH CHECK ADD  CONSTRAINT [FK_LocationPremisses] FOREIGN KEY([locationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[Premises] CHECK CONSTRAINT [FK_LocationPremisses]
GO
ALTER TABLE [dbo].[Rating]  WITH CHECK ADD  CONSTRAINT [FK_Rating_Premises] FOREIGN KEY([premisesId])
REFERENCES [dbo].[Premises] ([Id])
GO
ALTER TABLE [dbo].[Rating] CHECK CONSTRAINT [FK_Rating_Premises]
GO
ALTER TABLE [dbo].[Review]  WITH CHECK ADD  CONSTRAINT [FK_PostReview] FOREIGN KEY([postId])
REFERENCES [dbo].[Post] ([Id])
GO
ALTER TABLE [dbo].[Review] CHECK CONSTRAINT [FK_PostReview]
GO
ALTER TABLE [dbo].[Review]  WITH CHECK ADD  CONSTRAINT [FK_PremissesReview] FOREIGN KEY([premisesId])
REFERENCES [dbo].[Premises] ([Id])
GO
ALTER TABLE [dbo].[Review] CHECK CONSTRAINT [FK_PremissesReview]
GO
ALTER TABLE [dbo].[Search]  WITH CHECK ADD  CONSTRAINT [FK_Search_Location] FOREIGN KEY([LocationId])
REFERENCES [dbo].[Location] ([Id])
GO
ALTER TABLE [dbo].[Search] CHECK CONSTRAINT [FK_Search_Location]
GO
ALTER TABLE [dbo].[UserAccount]  WITH CHECK ADD  CONSTRAINT [FK_AgentUserAccount] FOREIGN KEY([agentId])
REFERENCES [dbo].[Agent] ([Id])
GO
ALTER TABLE [dbo].[UserAccount] CHECK CONSTRAINT [FK_AgentUserAccount]
GO
ALTER TABLE [dbo].[UserAccount]  WITH CHECK ADD  CONSTRAINT [FK_PlatformUserAccount] FOREIGN KEY([platformId])
REFERENCES [dbo].[Platform] ([Id])
GO
ALTER TABLE [dbo].[UserAccount] CHECK CONSTRAINT [FK_PlatformUserAccount]
GO
ALTER TABLE [dbo].[UserAccountPremisesMapping]  WITH CHECK ADD  CONSTRAINT [FK_UserAccountPremisses_Premisses] FOREIGN KEY([Premises_Id])
REFERENCES [dbo].[Premises] ([Id])
GO
ALTER TABLE [dbo].[UserAccountPremisesMapping] CHECK CONSTRAINT [FK_UserAccountPremisses_Premisses]
GO
ALTER TABLE [dbo].[UserAccountPremisesMapping]  WITH CHECK ADD  CONSTRAINT [FK_UserAccountPremisses_UserAccount] FOREIGN KEY([UserAccount_Id])
REFERENCES [dbo].[UserAccount] ([Id])
GO
ALTER TABLE [dbo].[UserAccountPremisesMapping] CHECK CONSTRAINT [FK_UserAccountPremisses_UserAccount]
GO
USE [master]
GO
ALTER DATABASE [Sprint-1] SET  READ_WRITE 
GO
